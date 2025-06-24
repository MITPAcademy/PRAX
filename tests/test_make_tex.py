from tex.builder import make_tex

def test_make_tex_renders_metadata_and_questions():
    yaml_data = {
        "creator": "Alice",
        "id": "exam-001",
        "title": "Math Test",
        "subtitle": "Algebra",
        "questions": [
            {"id": 1, "statement": "1+1=?", "alternatives": {"A": "1", "B": "2"}}
        ]
    }
    tex = make_tex(yaml_data)
    assert "Alice" in tex
    assert "exam-001" in tex
    assert "Math Test" in tex
    assert "Algebra" in tex
    assert "\\textbf{Question 1}:" in tex
    assert r"\begin{tcolorbox}" in tex