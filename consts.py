import pygame
import os

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
STEP = 20
GARBAGE_LAND_PIC ="pass"
GARBAGE_SEA_PIC ='DF'
GARBAGE_AIR_PIC = 'DFB'
SCREEN_SEA_PIC = "pass"
SCREEN_LAND_PIC = "PASS"
SCREEN_AIR_PIC ='PASS'

pygame.font.init()
FONT_NAME = "Ariel"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = (0, 0, 0)
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won! " \
              "Thank you for cleaning up the world"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
FIRST_MESSAGE = " Welcome to the cleaning game! " \
                "Let's clean up our world and keep it clean and happy" \
                "Have Fun!"
FIRST_FONT_SIZE = int(15)
FIRST_LOCATION = (500,)

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
GARBAGE_MAN_PIC = pygame.image.load(os.path.join('pics', 'garbage_man.png'))
SCREEN_PIC = pygame.image.load(os.path.join('pics', 'screen.jpeg'))
