#!/usr/bin/python3
def multiple_returns(sentence):
    empty = ""
    length = len(sentence)
    if sentence == empty:
        return(None)
    else:
        return(length, sentence[0]) 
