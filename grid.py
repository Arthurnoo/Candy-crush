import random
from constants import *
from animations import animate_expand, animate_drop

def create_grid():
    grid = [[random.choice(COLORS) for _ in range(COLS)] for _ in range(ROWS)]
    while check_matches(grid):
        grid = [[random.choice(COLORS) for _ in range(COLS)] for _ in range(ROWS)]
    return grid

def check_matches(grid):
    to_remove = set()

    # Vérification des lignes
    for row in range(ROWS):
        col = 0
        while col < COLS:
            match_start = col
            while col < COLS - 1 and grid[row][col] == grid[row][col + 1]:
                col += 1
            if col - match_start + 1 >= 3:  # Combinaison de 3 ou plus
                for c in range(match_start, col + 1):
                    to_remove.add((row, c))
            col += 1

    # Vérification des colonnes
    for col in range(COLS):
        row = 0
        while row < ROWS:
            match_start = row
            while row < ROWS - 1 and grid[row][col] == grid[row + 1][col]:
                row += 1
            if row - match_start + 1 >= 3:  # Combinaison de 3 ou plus
                for r in range(match_start, row + 1):
                    to_remove.add((r, col))
            row += 1

    return list(to_remove)

def remove_matches(grid, matches, new_case_count):
    animate_expand(grid, matches)  # Animer l'agrandissement avant de supprimer les cases
    
    for row, col in matches:
        grid[row][col] = None

    # Calculer les positions de chute pour chaque case au-dessus des cases supprimées
    drop_positions = {}
    for col in range(COLS):
        drop_count = 0
        for row in range(ROWS-1, -1, -1):
            if grid[row][col] is None:
                drop_count += 1
            elif drop_count > 0:
                drop_positions[(row, col)] = drop_count
                grid[row + drop_count][col] = grid[row][col]
                grid[row][col] = None

    animate_drop(grid, drop_positions)  # Animer la descente des cases

    # Ajouter de nouvelles cases en haut
    for col in range(COLS):
        empty_slots = [row for row in range(ROWS) if grid[row][col] is None]
        for empty_slot in empty_slots:
            if new_case_count < NEW_CASE_LIMIT:
                grid[empty_slot][col] = random.choice(COLORS)
                new_case_count += 1
            else:
                grid[empty_slot][col] = None

    # Vérifier les nouvelles combinaisons après remplissage
    new_matches = check_matches(grid)
    while new_matches:
        new_case_count = remove_matches(grid, new_matches, new_case_count)
        new_matches = check_matches(grid)
    
    return new_case_count
