#!/usr/bin/python3
"""Defines a function to find the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate and return the perimeter of an island in the given grid.

    The grid represents water by 0 and land by 1.

    Args:
        grid : A 2D list where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island defined in the grid.
    """
    # Get the dimensions of the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    land_cells = 0  # To count the number of land cells (1s)
    shared_edges = 0  # To count the shared edges between land cells

    # Iterate through each cell in the grid
    for row in range(num_rows):
        for col in range(num_cols):
            # If the current cell is land (1), process it
            if grid[row][col] == 1:
                land_cells += 1  # Increment the land cell count

                # Check if the left neighbor is also land to count shared edges
                if col > 0 and grid[row][col - 1] == 1:
                    shared_edges += 1

                # Check if the upper neighbor
                # is also land to count shared edges
                if row > 0 and grid[row - 1][col] == 1:
                    shared_edges += 1

    # Each land cell contributes 4 to the perimeter,
    # and each shared edge subtracts 2
    return land_cells * 4 - shared_edges * 2
