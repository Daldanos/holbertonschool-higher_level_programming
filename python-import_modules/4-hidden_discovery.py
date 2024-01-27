#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    search = dir(hidden_4)
    dont = "__"
    j = len(search)
    for i in range(0, j):
        if dont not in search[i]:
            print(search[i])
