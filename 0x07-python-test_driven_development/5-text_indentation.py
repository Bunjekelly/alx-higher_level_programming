#!/usr/bin/python3

"""a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Args: text
    Raises a TypeError if text is not string
    Returns new text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for char in text:
        if char in ['.', '?', ':']:
            new_text += char + '\n\n'
        else:
            new_text += char
    lines = []

    for line in new_text.splitlines():
        lines.append(line.strip())
    new_text = "\n".join(lines)

    print(new_text)
