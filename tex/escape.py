import re

def escape_tex(text):
    # Patterns to match: $$...$$, \( ... \), \[ ... \]
    pattern = r"(\$\$.*?\$\$|\\\(.*?\\\)|\\\[.*?\\\])"
    mapping = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
    }

    def escape_chunk(chunk):
        chunk = "".join(mapping.get(char, char) for char in chunk)
        chunk = re.sub(r'(?<!\\)_', r'\_', chunk)
        return chunk

    parts = re.split(pattern, text, flags=re.DOTALL)
    for i, part in enumerate(parts):
        if re.fullmatch(pattern, part or "", flags=re.DOTALL):
            continue
        parts[i] = escape_chunk(part)
    return "".join(parts)