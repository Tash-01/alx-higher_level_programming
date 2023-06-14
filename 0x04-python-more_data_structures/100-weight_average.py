#!/usr/bin/python3
def weight_average(my_list=[]):
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
