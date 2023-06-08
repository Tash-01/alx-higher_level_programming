#!/usr/bin/python3
if __name__ = " __main__":
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print("Usage:./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        ops = {
                '+': add,
                '-': sub,
                '*': mul,
                '/': div
                }

        if argv[2] in ops:
            num1
