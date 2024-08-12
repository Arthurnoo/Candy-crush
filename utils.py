def get_grid_position(mouse_pos, square_size):
    col = mouse_pos[0] // square_size
    row = mouse_pos[1] // square_size
    return col, row

def check_possible_moves(grid):
    for row in range(ROWS):
        for col in range(COLS - 1):
            # Swap horizontal and check for matches
            grid[row][col], grid[row][col + 1] = grid[row][col + 1], grid[row][col]
            if check_matches(grid):
                grid[row][col], grid[row][col + 1] = grid[row][col + 1], grid[row][col]
                return True
            grid[row][col], grid[row][col + 1] = grid[row][col + 1], grid[row][col]

    for col in range(COLS):
        for row in range(ROWS - 1):
            # Swap vertical and check for matches
            grid[row][col], grid[row + 1][col] = grid[row + 1][col], grid[row][col]
            if check_matches(grid):
                grid[row][col], grid[row + 1][col] = grid[row + 1][col]
                return True
            grid[row][col], grid[row + 1][col] = grid[row + 1][col]

    return False
