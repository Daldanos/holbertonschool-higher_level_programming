#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    infinite = 0

    for i in range(n):
        infinite += int(sys.argv[i + 1])
    print("{}".format(infinite))
