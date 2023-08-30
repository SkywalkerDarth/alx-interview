#!/usr/bin/python3


""" island perimeter project """


def island_perimeter(grid):
    """Return the perimiter of an island.
    Grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
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
