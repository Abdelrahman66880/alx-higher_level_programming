#!/usr/bin/python3
"""defines function to scalar divde matrix"""

def matrix_divided(matrix, div):
    """Return the division of mataris on the element"""
    if (type(matrix)) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_size = len(matrix[0])
    tmp = []
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        lst = []
        for element in row:
            lst.append(float(format(element / div, '.2f')))
        tmp.append(lst)
    return (tmp)
