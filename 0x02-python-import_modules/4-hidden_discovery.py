#!/usr/bin/python3
if __name__ == "__main__":
    """print all names defined by hidden_4 module."""
    import hidden_4

    ne = dir(hidden_4)
    for names in name:
        if name[:2] != "__":
            print(name)
