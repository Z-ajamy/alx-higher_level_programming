#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for n in i:
                print("{:d}".format(n), end=" ")
            print()
