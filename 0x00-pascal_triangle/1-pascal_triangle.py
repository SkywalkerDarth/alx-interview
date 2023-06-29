import math
""" another way using n!/((n-k)! * k!) to generate
coefficients but requires importing maths.
"""
def pascal_triangle(n):
    """
    a function that takes in an integer n

    parameters:
        n(int) - input number of rows to generate

    Return:
        triangle - pascals triangle of be generated
    """
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = []
        for j in range(i + 1):
            coefficient = (math.factorial(i) // 
            (math.factorial(j) * math.factorial(i - j)))
            """ 
            n!/((n-k)!*k!) 
            where n is i each iteration, 
            j is k in each iteration

            so if n = 5, i = 0, 1, 2, 3, 4;
            for each i, if i = 4 (4,0) (4,1) (4,2) (4,3) (4,4)
            i is 3, (3,0) (3,1), (3,2) (3,3)
            i is 2, (2,0) (2,1), (2,2)
            i is 1, (1,0) (1,1)
            i is 0, (0,0)

            [0,0] is 0!/(0-0)!0! = 1

            [1,0] is 1!/(1-0)!0! = 1
            [1,1] is 1!/(1-1)!1! = 1

            [2,0] is 2!/(2-0)!0! = 1
            [2,1] is 2!/(2-1)!1! = 2
            [2,2] is 2!/(2-2)!2! = 1

            ....... for 3 

            [4,0] is 4!/(4-0)!0! = 1,
            [4,1] is 4!/(4-1)!1! = 4,
            [4,2] is 4!/(4-2)!2! = 6,
            [4,3] is 4!/(4-3)!3! = 4,
            [4,4] is 4!/(4-4)!4! = 1,
            """
            row.append(coefficient)
            " add coeffient to that row empty array "
        triangle.append(row)
    
    return triangle
