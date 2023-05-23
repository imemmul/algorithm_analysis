def find_longest_drainage_path(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Initialize a 2D memoization table to store the lengths of drainage paths
    memo = [[0] * cols for _ in range(rows)]

    max_length = 0  # Stores the maximum drainage path length

    # Iterate through each grid cell from top-left to bottom-right
    for i in range(rows):
        for j in range(cols):
            # Calculate the length of the longest drainage path starting from grid[i][j]
            length = calculate_drainage_path_length(grid, memo, rows, cols, i, j)
            max_length = max(max_length, length)

    return max_length


def calculate_drainage_path_length(grid, memo, rows, cols, i, j):
    if memo[i][j] != 0:
        return memo[i][j]

    # Initialize the length of the current drainage path to 1
    length = 1

    # Check the four adjacent cells (up, down, left, right) for valid flow
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        ni = i + dx  # Neighbor's row index
        nj = j + dy  # Neighbor's column index

        # Check if the neighbor is within the grid boundaries and has a lower elevation
        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] < grid[i][j]:
            length = max(length, 1 + calculate_drainage_path_length(grid, memo, rows, cols, ni, nj))

    # Memoize the calculated length for the current cell
    memo[i][j] = length

    return length


# Example usage
grid = [
    [66, 78, 41, 3, 77],
    [4, 90, 41, 8, 68],
    [12, 11, 29, 24, 53],
    [0, 51, 58, 9, 28],
    [97, 99, 96, 58, 92]
]

longest_path_length = find_longest_drainage_path(grid)
print("Longest drainage path length:", longest_path_length)
