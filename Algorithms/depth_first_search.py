"""
Given a boolean 2D matrix. The task is to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is equal to another (not rotated or reflected).

Examples:

Input: grid[][] =
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
Output: 1
Island 1, 1 in the top left corner is same as island 1, 1 in the bottom right corner
Input: grid[][] =
{1, 1, 0, 1, 1},
{1, 0, 0, 0, 0},
{0, 0, 0, 0, 1},
{1, 1, 0, 1, 1}
Output: 3
Distinct islands in the example above are 1, 1 in the top left corner; 1, 1 in the top right corner and 1 in the bottom right corner. We ignore the island 1, 1 in the bottom left corner since 1, 1 it is identical to the top right corner.

Approach: This problem is an extension of the problem Number of Islands.

The core of the question is to know if 2 islands are equal. The primary criteria is that the number of 1’s should be same in both. But this cannot be the only criteria as we have seen in example 2 above. So how do we know? We could use the position/coordinates of the 1’s.
If we take the first coordinates of any island as a base point and then compute the coordinates of other points from the base point, we can eliminate duplicates to get the distinct count of islands. So, using this approach, the coordinates for the 2 islands in example 1 above can be represented as: [(0, 0), (0, 1), (1, 0), (1, 1)].
"""

# 2D array for the storing the horizontal and vertical
# directions. (Up, left, down, right
dirs = [[0, -1],
        [-1, 0],
        [0, 1],
        [1, 0]]


# Function to perform dfs of the input grid
def dfs(grid, x0, y0, i, j, v):
    rows = len(grid)
    cols = len(grid[0])

    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <= 0:
        return
    # marking the visited element as -1
    grid[i][j] *= -1

    # computing coordinates with x0, y0 as base
    v.append((i - x0, j - y0))

    # repeat dfs for neighbors
    for d in dirs:
        dfs(grid, x0, y0, i + d[0], j + d[1], v)


# Main function that returns distinct count of islands in
# a given boolean 2D matrix
def countDistinctIslands(grid):
    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    if cols == 0:
        return 0

    coordinates = set()

    for i in range(rows):
        for j in range(cols):

            # If a cell is not 1
            # no need to dfs
            if grid[i][j] != 1:
                continue

            # to hold coordinates
            # of this island
            v = []
            dfs(grid, i, j, i, j, v)

            # insert the coordinates for
            # this island to set
            coordinates.add(tuple(v))

    return len(coordinates)


# Driver code
grid = [[1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]]

print("Number of distinct islands is", countDistinctIslands(grid))