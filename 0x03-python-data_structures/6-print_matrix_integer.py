#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            length = len(i)
            for n in range(length):
                if n < length - 1:
                    print("{:d}".format(i[n]), end=" ")
                else:
                    print("{:d}".format(i[n]), end="")

            print()
