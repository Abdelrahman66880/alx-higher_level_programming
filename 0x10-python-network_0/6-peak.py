#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(arr):
    """Finds a peak in list_of_integers"""
    if len(arr) == 0:
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[-1]
