#!/usr/bin/python3
"""
Include the inherits_from function
"""


def inherits_from(obj, a_class):
    """Indicates whether 'obj' is a subclass of 'a_class' (True) or not (False)."""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
