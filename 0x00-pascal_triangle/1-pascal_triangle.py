#!/usr/bin/python3


""" Another way of doing factorial function definition"""


def factorial(n: int) -> int:
    """this function returns a factorial
    Args: n, input integer
    Return: n * factorial(n-1)"""
    if n <= 1:
        return 1
    return n * factorial(n-1)


"""combination function definition"""


def combination(n: int) -> list:
    """this function returns a combination
    Args: n, input integer
    Return: comb_list"""
    comb_list = []
    r = 0
    while n - r >= 0:
        comb = int(factorial(n) / (factorial(n - r) * factorial(r)))
        comb_list.append(comb)
        r += 1
    return comb_list


"""pascal triangle definition"""


def pascal_triangle(n: int):
    """Function returns pascal values
    Args: n, input integer
    Return: pascal"""
    k = 0
    if n <= 0:
        return []
    pascal = []
    while k < n:
        pascal.append(combination(k))
        k += 1
    return pascal
