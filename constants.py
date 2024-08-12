import pygame

# Paramètres de la grille
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH // COLS
BORDER_WIDTH = 5
INNER_SIZE = SQUARE_SIZE - 2 * BORDER_WIDTH
NEW_CASE_LIMIT = 100
SWAP_ANIMATION_DURATION = 0.25  # Durée de l'animation de l'échange en secondes
EXPAND_ANIMATION_DURATION = 0.2  # Durée de l'animation d'agrandissement en secondes
DROP_ANIMATION_DURATION = 0.1  # Durée de l'animation de la descente des cases par ligne

# Couleurs
BACKGROUND_COLOR = (169, 169, 169)  # Gris pour le fond des cases
BORDER_COLOR = (169, 169, 169)      # Gris foncé pour les bordures
SELECTION_COLOR = (0, 0, 0)         # Noir pour la sélection
EMPTY_COLOR = (169, 169, 169)       # Gris clair pour les anciennes positions lors de l'échange
COLORS = [
    (255, 0, 0),    # Rouge
    (0, 255, 0),    # Vert
    (0, 0, 255),    # Bleu
    (255, 255, 0),  # Jaune
    (255, 165, 0)   # Orange
]

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush Like")
