#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)
    length_1 = len(matrix)

    for i in range(length_1):
        length_2 = len(matrix[i])
        for n in range(length_2):
            print("{}".format(matrix[i][n]),end=" ")
        print()
