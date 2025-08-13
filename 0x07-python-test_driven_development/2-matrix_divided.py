#!/usr/bin/python3
"""Defines a matrix division function.

This module provides functionality for dividing all elements of a matrix
by a given divisor. The division operation creates a new matrix with
results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.
    
    Creates a new matrix where each element is the result of dividing
    the corresponding element in the input matrix by the divisor.
    All results are rounded to 2 decimal places.
    
    Args:
        matrix (list of list of int/float): A matrix represented as a list 
            of lists containing integers or floats. All rows must have the 
            same length and contain only numeric values.
        div (int or float): The divisor to divide each matrix element by.
            Must be a non-zero number.
    
    Returns:
        list of list of float: A new matrix with the same dimensions as the
            input matrix, where each element is the result of dividing the
            corresponding input element by div, rounded to 2 decimal places.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.
    
    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        
        >>> matrix = [[2, 4], [6, 8]]
        >>> matrix_divided(matrix, 2)
        [[1.0, 2.0], [3.0, 4.0]]
    
    Note:
        The original matrix is not modified. A new matrix is returned.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])