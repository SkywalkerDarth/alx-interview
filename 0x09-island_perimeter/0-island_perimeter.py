#!/usr/bin/python3


""" island perimeter module """


def island_perimeter(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4   # 4 sides of a square
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 for adjacent land cells
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 for adjacent land cells

    return perimeter
