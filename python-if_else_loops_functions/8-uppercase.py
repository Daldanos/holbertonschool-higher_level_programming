#!/usr/bin/python3
def uppercase(str):
    g = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            x = ord(ch) - 32
            y = chr(x)
            g = g + y
        else:
            g = g + ch
    print(g)
