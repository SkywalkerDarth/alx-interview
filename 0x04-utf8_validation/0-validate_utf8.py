#!/usr/bin/python3


"""
A method that determines if a given data set represents
a valid UTF-8 encoding
"""


def validUTF8(data) -> bool:
    """
    validUTF8 method
    Args: data(int)
    Return: False, True.
    """
    for byte in data:
        if type(byte) != int or byte < 0 or byte > 0x10ffff:
            return False
        if byte >> 7 == 0:
            continue
        elif byte >> 5 == 0b110:
            continue
        elif byte >> 4 == 0b1110:
            continue
        elif byte >> 3 == 0b11110:
            continue
        else:
            return False
    return True
