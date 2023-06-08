#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    def add_arg(sys.agrv)

    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
            prony("{:d}".format(add))
