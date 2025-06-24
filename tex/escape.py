import re

def escape_tex(text):
    # Patterns to match: $$...$$, \( ... \), \[ ... \]
    pattern = r"(\$\$.*?\$\$|\\\(.*?\\\)|\\\[.*?\\\])"
    mapping = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
    }
    def escape_chunk(chunk):
        return "".join(mapping.get(char, char) for char in chunk)
    parts = re.split(pattern, text, flags=re.DOTALL)
    for i, part in enumerate(parts):
        if re.fullmatch(pattern, part, flags=re.DOTALL):
            continue
        parts[i] = escape_chunk(part)
    return "".join(parts)