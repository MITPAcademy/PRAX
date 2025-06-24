from tex.builder import make_questions_latex

def test_make_questions_latex_basic():
    questions = [
        {"id": 1, "enunciado": "What is 2+2?", "alternativas": {"A": "3", "B": "4", "C": "5"}},
        {"id": 2, "enunciado": "Capital of France?", "alternativas": {"A": "Paris", "B": "London"}}
    ]
    latex = make_questions_latex(questions)
    assert "\\textbf{Question 1}:" in latex
    assert "\\textbf{Question 2}:" in latex
    assert "What is 2\\+2?" not in latex  # Should NOT escape '+'
    assert "Paris" in latex