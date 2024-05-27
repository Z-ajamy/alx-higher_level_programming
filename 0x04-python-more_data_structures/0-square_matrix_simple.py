#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    sq_matrix = []
    for i in matrix:
        s = list(map(lambda x : x ** 2, i))
        sq_matrix.append(s)
    return sq_matrix
