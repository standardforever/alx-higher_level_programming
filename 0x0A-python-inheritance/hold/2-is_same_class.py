#!/usr/bin/python3

"""def is_same_class"""

def is_same_class(obj, a_class):
    """
    it returns True if the object is exactly an instance
    of the specified class; other wise False
    """
    return (type(obj) == a_class)
    