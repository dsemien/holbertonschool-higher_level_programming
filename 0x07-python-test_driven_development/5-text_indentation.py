#!/usr/bin/python3
"""A progaram  that prints a text with 
2 new lines after each of these characters: ., ? and :
"""
def text_indentation(text):
    """A function that prints a text with 
    2 new lines after each of these characters: ., ? and:

    Arguments:
            text (str): String of text to print

        Raises:
            TypeError: if text in not an str.        
    """
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
