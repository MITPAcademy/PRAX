import re

def escape_tex(text):
    math_patterns = [
        (r"\$\$(.*?)\$\$", re.DOTALL),    # $$ ... $$
        (r"\\\((.*?)\\\)", re.DOTALL),    # \( ... \)
        (r"\\\[(.*?)\\\]", re.DOTALL),    # \[ ... \]
    ]

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

    tokens = []
    def replacer(match):
        tokens.append(match.group(0))
        return f"__MATH_TOKEN_{len(tokens)-1}__"

    text_ = text
    for pat, flags in math_patterns:
        text_ = re.sub(pat, replacer, text_, flags=flags)

    text_ = escape_chunk(text_)

    for idx, val in enumerate(tokens):
        text_ = text_.replace(f"__MATH_TOKEN_{idx}__", val)

    return text_