#!/usr/bin/python3
"""progaram that divides all 
    elements of a matrix.
"""

def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix.
    
    Arguments:
        matirx (list): matrix of integers.
        div (int): number divisable against matrix.

    Raises:
        TypeError: if matrix not int/float/list
        TypeError: if matrix[0], matrix[1] not same lenght
        TypeError: if div is not int/float
    Return:
        result of divisable matrix
    """
    if isinstance(matrix, list) is not True:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(matrix[0], list) is not True:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(matrix[1], list) is not True:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) is not len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, int) is not True:
            raise TypeError("div must be a number")
    if div is 0:
            raise ZeroDivisionError("division by zero")
    return[[round(digit / div, 2) for digit in row] for row in matrix]
