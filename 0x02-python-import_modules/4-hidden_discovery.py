#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list1 = dir(hidden_4)
    for i in list1:
        if i[0] != "_":
            print(i)
