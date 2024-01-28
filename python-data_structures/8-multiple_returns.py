#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = sentence[0]
    if lenght == 0:
        devol = [0, None]
        return devol
    else:
        devol = [lenght, first]
        return devol
