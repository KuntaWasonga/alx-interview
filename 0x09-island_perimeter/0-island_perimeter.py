#!/usr/bin/python3
""" Module to compute island perimeter.
"""


def island_perimeter(grid):
    """Function that returns perimeter of the island
    described in grid.
    """
    if type(grid) != list:
        return 0

    perimeter = 0
    l = len(grid)

    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == l - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)

    return perimeter
