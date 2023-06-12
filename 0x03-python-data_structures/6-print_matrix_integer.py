#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for c in row:
            print("{:d}".format(c), end=" " if c != row[-1] else "")
            print()
