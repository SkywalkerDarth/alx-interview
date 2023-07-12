#!/usr/bin/python3


""" A minimum_operations Interview """


def minOperations(n) -> int:
    """ a function called minOperations
    Args:
        int n: given number

    Return:
        Integer, if successful, 0 if not
    """
    if (n < 2):
        return 0

    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1
    return operations
