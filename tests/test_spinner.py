import time
from PRAX.tex.spinner import Spinner

def test_spinner_start_and_stop(capsys):
    spinner = Spinner("Loading")
    spinner.start()
    time.sleep(0.3)
    spinner.stop()
    out, _ = capsys.readouterr()
    assert "Loading" in out