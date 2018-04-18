#!/usr/bin/python3
def multiple_returns(sentence):
    empty = ""
    length = len(sentence)
    if sentence is empty:
        return(length, None)
    else:
        return(length, sentence[0]) 
