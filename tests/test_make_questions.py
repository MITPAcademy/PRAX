from tex.builder import make_questions_latex

def test_make_questions_latex_basic():
    questions = [
        {"id": 1, "statement": "What is 2+2?", "alternatives": {"A": "3", "B": "4", "C": "5"}},
        {"id": 2, "statement": "Capital of France?", "alternatives": {"A": "Paris", "B": "London"}}
    ]
    latex = make_questions_latex(questions)
    assert "\\textbf{Question 1}:" in latex
    assert "\\textbf{Question 2}:" in latex
    assert "What is 2\\+2?" not in latex  # Should NOT escape '+'
    assert "Paris" in latex
    assert r"\begin{tcolorbox}" in latex