import sys

def find_longest_path(rows, cols, grid):
    memo = [[0] * cols for _ in range(rows)]
    max_len = 0
    longest_path = []

    for i in range(rows):
        for j in range(cols):
            temp_len, temp_path = calculate_drainage_path_length(grid, memo, rows, cols, i, j)
            if temp_len > max_len:
                max_len = temp_len
                longest_path = temp_path

    return max_len, longest_path


def calculate_drainage_path_length(grid, memo, rows, cols, r, c):
    if memo[r][c] != 0:
        return memo[r][c], [(r, c)]

    curr_len = 1
    curr_path = [(r, c)]

    curr_pos = (r, c)
    moving_directions = {"RIGHT": (1, 0), "LEFT": (-1, 0), "DOWN": (0, -1), "UP": (0, 1)}
    max_len = 0
    max_path = []

    for key, val in moving_directions.items():
        neigh_coord = tuple(map(lambda i, j: i + j, val, curr_pos))
        if 0 <= neigh_coord[0] < rows and 0 <= neigh_coord[1] < cols and grid[neigh_coord[0]][neigh_coord[1]] < grid[r][c]:
            temp_len, temp_path = calculate_drainage_path_length(grid, memo, rows, cols, neigh_coord[0], neigh_coord[1])
            if temp_len + 1 > max_len:
                max_len = temp_len + 1
                max_path = temp_path

    curr_len += max_len
    curr_path += max_path

    memo[r][c] = curr_len

    return curr_len, curr_path

# Example usage
if __name__ == "__main__":
    filename = sys.argv[-1]
    file = open(filename, 'r')
    lines = file.readlines()
    n = int(lines[0].split(' ')[0])  # rows
    m = int(lines[0].split(' ')[1])  # cols
    grid = []
    for i in range(1, len(lines)):
        grid.append([int(x) for x in lines[i].split(' ')])

    longest_path_length, longest_path_coords = find_longest_path(n, m, grid)
    print("Longest drainage path length:", longest_path_length)
    print("Longest drainage path coordinates:", longest_path_coords)
