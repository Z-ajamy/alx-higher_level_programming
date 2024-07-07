#!/usr/bin/python3
"""
Module for matrix division.

This module provides a function to divide all elements of a matrix
by a given divisor.
It ensures that the matrix is a list of lists containing integers
or floats, that all rows
in the matrix have the same size, and that the divisor is a
non-zero number.

Functions:
    matrix_divided(matrix, div): Divides all elements of a matrix
    by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of list of int/float): The matrix to be divided. Must be
        a list of lists of integers or floats.
        div (int/float): The divisor to divide each element of the matrix by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number (int/float).
        ZeroDivisionError: If div is zero.

    Returns:
        list of list of float: A new matrix with each element divided by div,
        rounded to 2 decimal places.

    Examples:
        >>> matrix_divided([[1, 2], [3, 4]], 2)
        [[0.5, 1.0], [1.5, 2.0]]
        >>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 2.0)
        [[0.75, 1.25], [1.75, 2.25]]
    """

    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(i, list) for i in matrix)
        or not all(isinstance(i, (int, float))for j in matrix for i in j)):
        a = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(a)

    if not all(len(matrix[0]) == len(i) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in matrix[i]:
            new_matrix[i].append(round((j/div), 2))

    return(new_matrix)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
