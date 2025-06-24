import re

def escape_tex(text):
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
        return re.sub(r'(?<!\\)_', r'\_', chunk)
    parts = re.split(pattern, text, flags=re.DOTALL)
    for i, part in enumerate(parts):
        if part and not re.fullmatch(pattern, part, flags=re.DOTALL):
            parts[i] = escape_chunk(part)
    return "".join(parts)