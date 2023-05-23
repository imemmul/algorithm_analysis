import sys
from queue import PriorityQueue

def find_longest_path(rows, cols, grid):
    
    memo = [[0] * cols for _ in range(rows)]

    max_len = 0
    longest_path = []
    # TODO Did I need to topological sort ? # ANSWER
    # TODO how to keep track of visited cells ? dfs kind of approached can be used for ex go to neighbors until termination
    for i in range(rows):
        for j in range(cols):
            # Calculate the length of the longest drainage path starting from (0, 0)
            temp_len, temp_path = calculate_drainage_path_length(grid, memo, rows, cols, i, j)
            if temp_len > max_len:
                max_len = temp_len
                longest_path = temp_path
    # print(longest_path) # only gives the few of coordinates
    return max_len


def calculate_drainage_path_length(grid, memo, rows, cols, r, c):
    # 
    if memo[r][c] != 0:
        return memo[r][c], [(r, c)]

    curr_len = 1 # start with length 1 because already we headed into neighbor cell.
    ## FIXME √ doesn't take the last node visited so that everytime length becomes solution - 1 FIX: init length var with + 1
    # TODO is it possible to backtrack so that code gives the longest path visited nodes ? Might have use Priority Queue for this path,length pairs ?
        
    # Check the four neighbors cells (up, down, left, right) for valid flow
    # START 
    pq = PriorityQueue()
    curr_pos = (r, c)
    curr_path = [(r, c)]
    max_path = []
    moving_directions = {"RIGHT": (1, 0), "LEFT": (-1, 0), "DOWN":(0, -1), "UP": (0, 1)}
    for key, val in moving_directions.items():
        neigh_coord = tuple(map(lambda i, j: i + j, val, curr_pos))
        # adding constraint on boundraies (handles out of boundary)
        if 0 <= neigh_coord[0] < rows and 0 <= neigh_coord[1] < cols and grid[neigh_coord[0]][neigh_coord[1]] < grid[r][c]:
            temp_len, temp_path = calculate_drainage_path_length(grid, memo, rows, cols, neigh_coord[0], neigh_coord[1])
            # if temp_len + 1 > curr_len:
            #     curr_len = temp_len + 1
            #     curr_path = [(r, c)] + temp_path
            #     print(f"curr_path {curr_path}")
            # if temp_len != curr_len:
            #     print(f"cell moved to in {key} way and position of {neigh_coord}")

    # update memoization of r,c with length
    memo[r][c] = curr_len

    return curr_len, curr_path

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
    
