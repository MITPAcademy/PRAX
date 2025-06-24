from PRAX.tex.builder import make_gabarito_latex

def test_make_gabarito_latex_renders_all_questions():
    questions = [
        {"id": 1, "alternativas": {"A": "x", "B": "y"}},
        {"id": 2, "alternativas": {"A": "p", "B": "q", "C": "r"}}
    ]
    latex = make_gabarito_latex(questions)
    assert "\\textbf{1.}" in latex
    assert "\\textbf{2.}" in latex
    assert "tikzpicture" in latex