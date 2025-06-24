from util.util import is_pdflatex_in_path, add_pdflatex_to_path

def test_is_pdflatex_in_path_and_add():
    # This test is just to ensure these functions run. We can't guarantee pdflatex is installed on CI.
    found = is_pdflatex_in_path()
    assert isinstance(found, bool)
    ok, path = add_pdflatex_to_path()
    assert isinstance(ok, bool)
    if ok:
        assert path