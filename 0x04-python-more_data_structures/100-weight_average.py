#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return num(a * b for a, b in my_list) / num(b for a, b in my_list)
    return (0)
