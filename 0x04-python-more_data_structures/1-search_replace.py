#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(replace if n == search else n, my_list)
    return (new_list)
