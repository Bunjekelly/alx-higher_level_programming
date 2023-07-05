#!/usr/bin/python3
"""a function that multiplies matrices using th NumPy module"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """defining the function"""
    result = numpy.matmul(m_a, m_b)

    return result
