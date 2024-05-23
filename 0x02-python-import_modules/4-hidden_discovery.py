#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4
    str = dir(hidden_4)
    for i in str:
        if i[:2] != "__":
            print(i)
