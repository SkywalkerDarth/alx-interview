#!/usr/bin/python3

def pascal_triangle(n):
    """define a function called pascal_triangle that
    takes in an integer variable n"""
    if n <= 0:
        return []
    """if n is less than or equal to 0, return ' '
    edge cases"""
    if n == 1:
        return [[1]]
    " if n == 1 return '[1]' "
    if n == 2:
        return [[1], [1, 1]]
    " if n == 2 return '[1]' then '[1, 1]' next row "
    if n > 2:
        base = [[1], [1, 1]]
        for i in range(n - 2):
            """ loop n-2 times giving last the last row
            giving next 1 """
            last = base[-1]
            next = [1]
            for i in range(len(last) - 1):
                """ nested for loop, looping array of
                last row minus the last 1"""
                next.append(last[i] + last[i + 1])
                """ adds the last 2 numbers in last row
                to each other as it loops consecutively
                joins result to next which is always [1]
                """
            next.append(1)
            " joins the last 1 e.g 1 '3' '3' :1:"
            base.append(next)
            " joins next to base "
    return base
