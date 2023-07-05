#!usr/bin/python3

"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Args: matrix, div
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns a new matrix
    """

    if matrix == [] or not (isinstance(matrix, list)) or\
            not all(isinstance(row, list) for row in matrix) or\
            not all(isinstance(ele, (int, float))
                    for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix
                    (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(ele / div, 2) for ele in row] for row in matrix]

    return new_matrix
