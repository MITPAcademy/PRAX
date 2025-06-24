import tempfile
import os
from util.util import sha256_of_file

def test_sha256_of_file():
    # Create a temp file and calculate hash
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"abc123")
        tmp.flush()
        filename = tmp.name
    try:
        result = sha256_of_file(filename)
        # Precomputed sha256 for "abc123"
        assert result == "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090"
    finally:
        os.remove(filename)