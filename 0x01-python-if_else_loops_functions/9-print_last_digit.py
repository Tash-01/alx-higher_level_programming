#!/usr/bin/python3
print_last_digit= __import__('9 - print_last_digit').print_last_digit

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
