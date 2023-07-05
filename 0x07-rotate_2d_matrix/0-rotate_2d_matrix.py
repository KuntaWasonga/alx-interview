#!/usr/bin/python3
""" This module is Task 7 of the alx interview
"""


def rotate_2d_matrix(matrix):
    """ This function rotates a 2D matrix 90 degrees clockwise
    """
    n = len(matrix)

    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse rows in matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
