#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for my_list in matrix:
        for num in my_list:
            print(num, end=' ' if num != my_list[-1] else "")
            print()
