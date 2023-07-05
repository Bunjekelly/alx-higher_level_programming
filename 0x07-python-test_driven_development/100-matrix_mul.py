#!/usr/bin/python3

"""a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Args: m_a, m_b

    Raises TypeError if any of the args is not a matrix(list of lists)
    or if its elements are not inetegers or floats

    Raises ValueError if any of the lists is empty or
    if the two args can't be multiplied

    Returns new matrix with the multiplication product
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not isinstance(m_a, list) or\
            any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or\
            any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_size = len(m_a[0])
    for row in m_a:
        if len(row) != row_size:
            raise TypeError("each row of m_a must be of the same size")

    row_size = len(m_b[0])
    for rown in m_b:
        if len(row) != row_size:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0] * len(m_b[0]) for e in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
