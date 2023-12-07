#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_items = sorted(a_dictionary.items())
    dict_sorted_items = dict(sorted_items)
    print(dict_sorted_items)
