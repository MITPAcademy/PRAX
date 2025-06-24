from datetime import datetime
from .template import TEX_TEMPLATE

def tikz_circle(letter, size="0.4"):
    return (
        r"\begin{tikzpicture}[baseline=-0.8ex]"
        rf"\draw (0,0) circle ({size}cm);"
        rf"\node at (0,0) {{\large\textbf{{{letter}}}}};"
        r"\end{tikzpicture}"
    )

def needs_latex(text):
    text = text.strip()
    return (
        text.startswith(r'\(') and text.endswith(r'\)')
        or text.startswith('$$') and text.endswith('$$')
    )

def escape_tex(text):
    # Only escape if not LaTeX math expression
    if needs_latex(text):
        return text
    mapping = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
    }
    return "".join(mapping.get(char, char) for char in text)

def make_questions_latex(questions):
    out = []
    for q in questions:
        qid = q.get("id", "")
        statement = q.get("statement", "")
        alternatives = q.get("alternatives", {})
        statement_latex = escape_tex(statement)
        alt_lines = []
        for letter in sorted(alternatives.keys()):
            alt = alternatives[letter]
            alt_latex = escape_tex(str(alt))
            alt_lines.append(f"{tikz_circle(letter)}~{alt_latex} \\\\")
        alternatives_latex = "\n".join(alt_lines)
        q_latex = (
            r"\begin{tcolorbox}[examquestion]" "\n"
            f"\\textbf{{Question {qid}}}: {statement_latex} \\\\[0.5em]\n"
            "\\begin{tabular}{@{}l@{}}\n"
            f"{alternatives_latex}\n"
            "\\end{tabular}\n"
            r"\end{tcolorbox}" "\n"
        )
        out.append(q_latex)
    return "\n".join(out)

def make_answer_sheet_latex(questions):
    out = [r"\noindent"]
    out.append(r"\begin{tabular}{rl}")
    for q in questions:
        qid = q.get("id", "")
        alternatives = q.get("alternatives", {})
        letters = sorted(alternatives.keys())
        circles = " ".join(
            tikz_circle(letter, size="0.5") for letter in letters
        )
        out.append(f"\\textbf{{{qid}.}} & {circles} \\\\ [1em]")
    out.append(r"\end{tabular}")
    return "\n".join(out)

def make_tex(yaml_data):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    creator = yaml_data.get("creator", "Unknown")
    id_ = yaml_data.get("id", "N/A")
    title = yaml_data.get("title", "Document Title")
    subtitle = yaml_data.get("subtitle", "")
    questions = yaml_data.get("questions", [])
    questions_latex = make_questions_latex(questions)
    answer_sheet_latex = make_answer_sheet_latex(questions)
    return TEX_TEMPLATE.format(
        created_at=now,
        creator=creator,
        id=id_,
        title=title,
        subtitle=subtitle,
        questions_latex=questions_latex,
        answer_sheet_latex=answer_sheet_latex
    )