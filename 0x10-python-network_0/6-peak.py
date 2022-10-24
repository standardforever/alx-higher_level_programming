#!/usr/bin/python3

""" find the peak  of a list """
def find_peak(list_of_integers):
    x = len(list_of_integers) - 1 
    y = 0
    if x < 0:
        return (None)
    for i in range(len(list_of_integers) // 2 + 1 ):
        if (list_of_integers[y] > list_of_integers[x]):
            x = x - 1
        else:
            y = y + 1

    if (list_of_integers[x] > list_of_integers[y]):
        return (list_of_integers[x])
    return (list_of_integers[y])
