import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
import sys
import shutil
import subprocess
import yaml

from tex.builder import make_tex
from tex.spinner import Spinner
from util.util import sha256_of_file, add_pdflatex_to_path

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

def run_gui():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Select YAML", "Select the YAML exam file(s).")
    yaml_paths = filedialog.askopenfilenames(
        title="Select YAML file(s)",
        filetypes=[("YAML files", "*.yaml *.yml")]
    )
    if not yaml_paths:
        messagebox.showerror("No file", "No file was selected.")
        sys.exit(1)

    output_format = simpledialog.askstring(
        "Output format",
        "Type 'tex' to generate .tex or 'pdf' to generate PDF:"
    )
    if not output_format or output_format.lower() not in {"tex", "pdf"}:
        messagebox.showerror("Invalid", "Invalid format option.")
        sys.exit(1)
    output_format = output_format.lower()

    messagebox.showinfo("Select Output Directory", "Select the output directory.")
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        messagebox.showerror("No directory", "No output directory selected.")
        sys.exit(1)

    # Define assets directory as a sibling to the script
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    assets_dir = os.path.join(script_dir, "assets")
    logo_src = os.path.join(assets_dir, "logo.png")
    logo_dst = os.path.join(output_dir, "logo.png")
    if os.path.exists(logo_src):
        try:
            shutil.copy(logo_src, logo_dst)
        except Exception as e:
            messagebox.showwarning("Logo copy failed", f"Could not copy logo.png: {e}")
    else:
        messagebox.showwarning("Logo not found", "assets/logo.png not found, PDF will not have a logo.")

    for yaml_path in yaml_paths:
        process_file(yaml_path, output_format, output_dir)
    messagebox.showinfo("Done", "All files processed.")