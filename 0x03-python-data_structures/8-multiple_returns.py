#!/usr/bin/python3
def multiple_returns(sentence):
    my_typle = ()
    if sentence == "":
        length = 0
        frist  = None
        my_typle = length, frist
        return (my_typle)
    else:
        length = len(sentence)
        frist = sentence[0]
        my_typle = length, frist
    return (my_typle)
