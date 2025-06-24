import pytest
from tex.escape import escape_tex

@pytest.mark.parametrize("text,expected", [
    ("Hello & World", r"Hello \& World"),
    ("100% sure", r"100\% sure"),
    ("$5 #1", r"\$5 \#1"),
    ("under_score_name", r"under\_score_name"),
    ("{braces}", r"\{braces\}"),
    ("~tilde^", r"\textasciitilde{}tilde\^{}"),
    (r"back\slash", r"back\textbackslash{}slash"),
    ("no special chars", "no special chars"),
    (r"\(x+y=2\)", r"\(x+y=2\)"),   # Should NOT escape
    ("$$x+y=2$$", "$$x+y=2$$"),      # Should NOT escape
])
def test_escape_tex(text, expected):
    assert escape_tex(text) == expected