import time
import pygame
from constants import *
from graphics import draw_grid

def animate_swap(grid, pos1, pos2):
    row1, col1 = pos1
    row2, col2 = pos2
    x1, y1 = col1 * SQUARE_SIZE, row1 * SQUARE_SIZE
    x2, y2 = col2 * SQUARE_SIZE, row2 * SQUARE_SIZE

    start_time = time.time()
    while time.time() - start_time < SWAP_ANIMATION_DURATION:
        elapsed_time = time.time() - start_time
        progress = min(1, elapsed_time / SWAP_ANIMATION_DURATION)

        WIN.fill((255, 255, 255))

        current_x1 = x1 + (x2 - x1) * progress
        current_y1 = y1 + (y2 - y1) * progress
        current_x2 = x2 + (x1 - x2) * progress
        current_y2 = y2 + (y1 - y2) * progress

        grid_copy = [row[:] for row in grid]
        grid_copy[row1][col1] = EMPTY_COLOR
        grid_copy[row2][col2] = EMPTY_COLOR
        draw_grid(grid_copy)

        pygame.draw.rect(WIN, grid[row2][col2], (current_x2 + BORDER_WIDTH, current_y2 + BORDER_WIDTH, INNER_SIZE, INNER_SIZE), border_radius=10)
        pygame.draw.rect(WIN, grid[row1][col1], (current_x1 + BORDER_WIDTH, current_y1 + BORDER_WIDTH, INNER_SIZE, INNER_SIZE), border_radius=10)

        pygame.display.update()
        pygame.time.delay(10)

def animate_expand(grid, matches):
    start_time = time.time()
    while time.time() - start_time < EXPAND_ANIMATION_DURATION:
        elapsed_time = time.time() - start_time
        progress = min(1, elapsed_time / EXPAND_ANIMATION_DURATION)
        
        WIN.fill((255, 255, 255))
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in matches:
                    expand_size = INNER_SIZE + int(progress * (SQUARE_SIZE - INNER_SIZE))
                    offset = (SQUARE_SIZE - expand_size) // 2
                    pygame.draw.rect(WIN, grid[row][col], (col * SQUARE_SIZE + offset, row * SQUARE_SIZE + offset, expand_size, expand_size), border_radius=10)
                else:
                    pygame.draw.rect(WIN, BACKGROUND_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(WIN, BORDER_COLOR, (col * SQUARE_SIZE + BORDER_WIDTH, row * SQUARE_SIZE + BORDER_WIDTH, INNER_SIZE, INNER_SIZE))
                    if grid[row][col] is not None:
                        pygame.draw.rect(WIN, grid[row][col], (col * SQUARE_SIZE + BORDER_WIDTH, row * SQUARE_SIZE + BORDER_WIDTH, INNER_SIZE, INNER_SIZE), border_radius=10)

        pygame.display.update()
        pygame.time.delay(10)

def animate_drop(grid, matches):
    drop_positions = {}
    
    # Identifier les colonnes affectées par les suppressions et les lignes maximum affectées
    cols_affected = set(col for row, col in matches)
    max_rows_per_col = {col: max(row for row, c in matches if c == col) for col in cols_affected}
    drop_count = 0  # Initialisation de drop_count

    # Calculer les déplacements des cases qui doivent descendre
    for col in cols_affected:
        drop_count = 0  # Réinitialisation de drop_count pour chaque colonne
        for row in range(ROWS - 1, -1, -1):
            if (row, col) in matches:
                drop_count += 1
            elif drop_count > 0:
                initial_position = (row, col)
                final_position = (row + drop_count, col)
                drop_positions[initial_position] = final_position

    # Vérifier si drop_count est bien défini, sinon utiliser 1 pour éviter l'erreur
    max_drop = max(drop_positions.values(), default=(0, 0))[0] - min(drop_positions.keys(), default=(0, 0))[0]

    # Animer la descente
    start_time = time.time()
    while time.time() - start_time < DROP_ANIMATION_DURATION * max(max_drop, 1):
        elapsed_time = time.time() - start_time
        progress = elapsed_time / (DROP_ANIMATION_DURATION * max(max_drop, 1))

        WIN.fill((255, 255, 255))
        
        # Redessiner toute la grille avant de dessiner les cases en mouvement
        draw_grid(grid)
        
        for (initial_row, initial_col), (final_row, final_col) in drop_positions.items():
            current_y = initial_row * SQUARE_SIZE + (final_row - initial_row) * SQUARE_SIZE * progress
            pygame.draw.rect(WIN, grid[initial_row][initial_col], (initial_col * SQUARE_SIZE + BORDER_WIDTH, current_y + BORDER_WIDTH, INNER_SIZE, INNER_SIZE), border_radius=10)

        pygame.display.update()
        pygame.time.delay(10)

    # Mettre à jour la grille après l'animation
    for (initial_row, initial_col), (final_row, final_col) in drop_positions.items():
        grid[final_row][final_col] = grid[initial_row][initial_col]
        grid[initial_row][initial_col] = None
