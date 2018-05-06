#!/usr/bin/python3
def text_indentation(text):
    delim = {'.', '?', ':'}
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    doc = text.strip()
    for page, letters in enumerate(doc):
        if letters in delim:
            print("{:s}\n".format(letters))
        else:
            if (doc[page - 1] in delim or (doc[page] is " " and doc[page -1] is " ")):
                continue
            print("{:s}".format(letters), end="")
