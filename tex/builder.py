from datetime import datetime
from .template import TEX_TEMPLATE
from .escape import escape_tex

def tikz_circle(letter, size="0.4"):
    return (
        r"\begin{tikzpicture}[baseline=-0.8ex]"
        rf"\draw (0,0) circle ({size}cm);"
        rf"\node at (0,0) {{\large\textbf{{{letter}}}}};"
        r"\end{tikzpicture}"
    )

def make_questions_latex(questions):
    out = []
    for q in questions:
        qid = q.get("id", "")
        enunciado = escape_tex(q.get("enunciado", ""))
        alternativas = q.get("alternativas", {})
        alt_lines = []
        for letra in sorted(alternativas.keys()):
            alt = escape_tex(str(alternativas[letra]))
            alt_lines.append(
                f"{tikz_circle(letra)}~{alt} \\\\"
            )
        alternatives_latex = "\n".join(alt_lines)
        q_latex = (
            f"\\noindent\\textbf{{Question {qid}}}: {enunciado} \\\\[0.5em]\n"
            "\\begin{tabular}{@{}l@{}}\n"
            f"{alternatives_latex}\n"
            "\\end{tabular}\n"
            "\\vspace{1.5em}\n"
        )
        out.append(q_latex)
    return "\n".join(out)

def make_gabarito_latex(questions):
    out = [r"\noindent"]
    out.append(r"\begin{tabular}{rl}")
    for q in questions:
        qid = q.get("id", "")
        alternativas = q.get("alternativas", {})
        letras = sorted(alternativas.keys())
        circles = " ".join(
            tikz_circle(letra, size="0.5") for letra in letras
        )
        out.append(f"\\textbf{{{qid}.}} & {circles} \\\\ [1em]")
    out.append(r"\end{tabular}")
    return "\n".join(out)

def make_tex(yaml_data):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    creator = yaml_data.get("Creator", "Unknown")
    id_ = yaml_data.get("ID", "N/A")
    title = yaml_data.get("title", "Document Title")
    subtitle = yaml_data.get("subtitle", "")
    # O título e subtítulo devem ser escapados para evitar erros de alinhamento (&)
    title = escape_tex(title)
    subtitle = escape_tex(subtitle)
    questions = yaml_data.get("questions", [])
    questions_latex = make_questions_latex(questions)
    gabarito_latex = make_gabarito_latex(questions)
    return TEX_TEMPLATE.format(
        created_at=now,
        creator=creator,
        id=id_,
        title=title,
        subtitle=subtitle,
        questions_latex=questions_latex,
        gabarito_latex=gabarito_latex
    )