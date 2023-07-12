#!/usr/bin/python3


""" A minimum_operations Interview """


def minOperations(n)->int:
    """ a function called minOperations
    Args:
        int n: given number

    Return:
        Integer, if successful, 0 if not
    """
    if n <= 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))

    if operations[n] == float('inf'):
        return 0
    else:
        return operations[n]
