from tex.builder import make_answer_sheet_latex

def test_make_answer_sheet_latex_renders_all_questions():
    questions = [
        {"id": 1, "alternatives": {"A": "x", "B": "y"}},
        {"id": 2, "alternatives": {"A": "p", "B": "q", "C": "r"}}
    ]
    latex = make_answer_sheet_latex(questions)
    assert "\\textbf{1.}" in latex
    assert "\\textbf{2.}" in latex
    assert "tikzpicture" in latex