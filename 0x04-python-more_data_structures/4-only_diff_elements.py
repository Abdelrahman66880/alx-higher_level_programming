#!/usr/bin/python3
def common_elements(set_1, set_2):
    intersection_1 = set_1.intersection(set_2)
    union_1 = set_1.union(set_2)
    difference = union_1.difference(intersection_1)
    return (difference)
