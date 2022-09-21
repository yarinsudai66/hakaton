import os
import pygame

SCREEN_ROWS = 10
SCREEN_COLS = 10
EMPTY = "EMPTY"
GARBAGE = "GARBAGE"
GARBAGE_WIDTH = 2
PLAYER_HEIGHT = 4
PLAYER_WIDTH = 2
GARBAGE_COUNT = 5
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
FPS = 60
GARBAGE_MAN_PIC = pygame.image.load(os.path.join('pictures', 'garbage_man.png'))
SCREEN_PIC = pygame.image.load(os.path.join('pictures', 'screen.png'))
