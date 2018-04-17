#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for number in range(len(matrix)):
        for pos in range(len(matrix[number])):
            if pos == len(matrix[number]) - 1:
                print("{:d}".format(matrix[number][pos]), end="")
            else:
                print("{:d}".format(matrix[number][pos]), end=" ")
        print()
