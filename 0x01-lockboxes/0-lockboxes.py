#!/usr/bin/python3


""" a Write a method that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """
    define function can unlock boxes
    Args: boxes
    Return: unlocked
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    for box in range(n):
        if not unlocked[box]:
            continue
        for key in boxes[box]:
            if 0 <= key < n:
                unlocked[key] = True

    return all(unlocked)
