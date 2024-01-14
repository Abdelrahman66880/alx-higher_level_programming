#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
