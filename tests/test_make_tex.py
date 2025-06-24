from PRAX.tex.builder import make_tex

def test_make_tex_renders_metadata_and_questions():
    yaml_data = {
        "Creator": "Alice",
        "ID": "exam-001",
        "title": "Math Test",
        "subtitle": "Algebra",
        "questions": [
            {"id": 1, "enunciado": "1+1=?", "alternativas": {"A": "1", "B": "2"}}
        ]
    }
    tex = make_tex(yaml_data)
    assert "Alice" in tex
    assert "exam-001" in tex
    assert "Math Test" in tex
    assert "Algebra" in tex
    assert "\\textbf{Question 1}:" in tex