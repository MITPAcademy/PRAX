import sys
from gui import run_gui
from tex.builder import make_tex
from tex.spinner import Spinner
from util.util import sha256_of_file, add_pdflatex_to_path

import os
import subprocess
import yaml

def process_file(yaml_path, output_format, output_dir):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    base_name = os.path.splitext(os.path.basename(yaml_path))[0]
    tex_code = make_tex(data)

    tex_name = f"{base_name}.tex"
    tex_path = os.path.join(output_dir, tex_name)
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_code)

    if output_format == "tex":
        print(f"LaTeX file saved at: {tex_path}")
        return

    if not os.path.isfile(tex_path):
        print(f"File {tex_path} not created.")
        sys.exit(1)

    spinner = Spinner("Generating PDF")
    spinner.start()
    try:
        compiled = False
        for attempt in range(2):
            try:
                subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", tex_name],
                    cwd=output_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=False
                )
                compiled = True
            except FileNotFoundError:
                ok, pdflatex_dir = add_pdflatex_to_path()
                if ok:
                    os.environ["PATH"] = pdflatex_dir + os.pathsep + os.environ["PATH"]
                    try:
                        subprocess.run(
                            ["pdflatex", "-interaction=nonstopmode", tex_name],
                            cwd=output_dir,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=False
                        )
                        compiled = True
                        continue
                    except Exception:
                        pass
                spinner.stop()
                print("pdflatex not found in PATH and could not be auto-detected.\nPlease install MikTeX and make sure pdflatex is in your system PATH.")
                sys.exit(1)
            except Exception:
                compiled = True
                continue
    finally:
        spinner.stop()

    pdf_path = os.path.join(output_dir, f"{base_name}.pdf")
    if not os.path.exists(pdf_path):
        print("PDF was not generated.")
        sys.exit(1)

    sha256_str = sha256_of_file(pdf_path)
    print(f"PDF generated at: {pdf_path}")
    print(f"SHA-256: {sha256_str}")

def print_help():
    print(
        "Usage:\n"
        "  python app.py                # Open GUI\n"
        "  python app.py --pdf YAML OUTDIR   # Generate PDF(s) from YAML to OUTDIR\n"
        "  python app.py --tex YAML OUTDIR   # Generate .tex file(s) from YAML to OUTDIR\n"
        "  python app.py -help          # Show this help message\n"
        "\n"
        "You can specify multiple YAML files separated by spaces after the command.\n"
        "Examples:\n"
        "  python app.py --pdf exam1.yaml ./output\n"
        "  python app.py --tex exam1.yaml exam2.yaml ./output\n"
    )

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        run_gui()
        sys.exit(0)

    if args[0] in ("-help", "--help", "/?"):
        print_help()
        sys.exit(0)

    # CLI mode
    if args[0] in ("--pdf", "--tex"):
        if len(args) < 3:
            print("Error: You must specify at least one YAML file and an output directory.")
            print_help()
            sys.exit(1)
        output_format = "pdf" if args[0] == "--pdf" else "tex"
        *yaml_files, output_dir = args[1:]
        if not yaml_files:
            print("Error: You must specify at least one YAML file.")
            print_help()
            sys.exit(1)
        if not os.path.isdir(output_dir):
            print(f"Error: Output directory '{output_dir}' does not exist.")
            sys.exit(1)
        for yaml_path in yaml_files:
            if not os.path.isfile(yaml_path):
                print(f"Error: File '{yaml_path}' not found.")
                continue
            process_file(yaml_path, output_format, output_dir)
        sys.exit(0)

    print("Error: Unknown command or arguments.")
    print_help()
    sys.exit(1)