import pygame
from constants import *
from grid import create_grid, check_matches, remove_matches
from animations import animate_swap
from graphics import draw_grid
from utils import get_grid_position

def main():
    clock = pygame.time.Clock()
    grid = create_grid()
    selected = None
    new_case_count = 0
    running = True

    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = get_grid_position(pos, SQUARE_SIZE)
                
                if selected:
                    if selected == (col, row):
                        selected = None
                    else:
                        selected_col, selected_row = selected
                        if abs(selected_row - row) + abs(selected_col - col) == 1:
                            animate_swap(grid, (selected_row, selected_col), (row, col))
                            grid[selected_row][selected_col], grid[row][col] = grid[row][col], grid[selected_row][selected_col]
                            matches = check_matches(grid)
                            if matches:
                                new_case_count = remove_matches(grid, matches, new_case_count)
                            selected = None
                        else:
                            selected = (col, row)
                else:
                    selected = (col, row)
        
        WIN.fill((255, 255, 255))
        draw_grid(grid, selected=selected)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
