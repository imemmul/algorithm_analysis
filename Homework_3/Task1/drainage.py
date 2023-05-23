import sys

def find_longest_path(rows, cols, grid):
    
    memo = [[0] * cols for _ in range(rows)]

    max_len = 0

    # TODO Did I need to topological sort ? # ANSWER
    # TODO how to keep track of visited cells ? dfs kind of approached can be used for ex go to neighbors until termination
    for i in range(rows):
        for j in range(cols):
            # Calculate the length of the longest drainage path starting from (0, 0)
            temp_len = calculate_drainage_path_length(grid, memo, rows, cols, i, j)
            max_len = max(max_len, temp_len)

    return max_len


def calculate_drainage_path_length(grid, memo, rows, cols, r, c):
    # 
    if memo[r][c] != 0:
        return memo[r][c]

    curr_len = 1 # start with length 1 because already we headed into neighbor cell.
    # FIXME doesn't take the last node visited so that everytime length becomes solution - 1 FIX: init length var with + 1
    # TODO is it possible to backtrack so that code gives the longest path visited nodes ?
        
    # Check the four neighbors cells (up, down, left, right) for valid flow
    curr_pos = (r, c)
    moving_directions = {"RIGHT": (1, 0), "LEFT": (-1, 0), "DOWN":(0, -1), "UP": (0, 1)}
    for key, val in moving_directions.items():
        neigh_coord = tuple(map(lambda i, j: i + j, val, curr_pos))
        # adding constraint on boundraies (handles out of boundary)
        if 0 <= neigh_coord[0] < rows and 0 <= neigh_coord[1] < cols and grid[neigh_coord[0]][neigh_coord[1]] < grid[r][c]:
            temp_len = curr_len
            # a recursive call (for dfs) to check neigh of neighs
            curr_len = max(curr_len, 1 + calculate_drainage_path_length(grid, memo, rows, cols, neigh_coord[0], neigh_coord[1]))
            if temp_len != curr_len:
                # print(f"cell moved to in {key} way and position of {neigh_coord}")
                pass

    # update memoization of r,c with length
    memo[r][c] = curr_len

    return curr_len

# Example usage
if __name__ == "__main__":
    filename = sys.argv[-1]
    file = open(filename, 'r')
    lines = file.readlines()
    n = int(lines[0].split(' ')[0]) # rows
    m = int(lines[0].split(' ')[1]) # cols
    grid = []
    for i in range(1, len(lines)):
        # TODO should keep both floats and integers
        grid.append([int(x) for x in lines[i].split(' ')]) 
    # print(boxes)
    longest_path = find_longest_path(n, m, grid)
    print("Longest drainage path length:", longest_path)
    
