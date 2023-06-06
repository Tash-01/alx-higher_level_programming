#!/usr/bin/python3
def magic_calculateion(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c
