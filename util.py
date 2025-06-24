import hashlib
import os
import subprocess

def sha256_of_file(filename):
    sha = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha.update(chunk)
    return sha.hexdigest()

def is_pdflatex_in_path():
    try:
        subprocess.run(['pdflatex', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False

def add_pdflatex_to_path():
    try:
        result = subprocess.run(['where', 'pdflatex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        pdflatex_path = result.stdout.strip().split('\n')[0].strip()
        if not pdflatex_path or not os.path.isfile(pdflatex_path):
            return False, None
        pdflatex_dir = os.path.dirname(pdflatex_path)
        os.environ["PATH"] = pdflatex_dir + os.pathsep + os.environ["PATH"]
        return True, pdflatex_dir
    except Exception:
        return False, None