import pygame
import consts
import random

# coloring window
def draw_window(pic):
    consts.WINDOW.blit(pic, (0, 0))
    pygame.display.update()

def draw_garbage(garbages):
    for gar in range(0, len(garbages)):
        consts.WINDOW.blit(consts.GARBAGE_PIC, (garbages[gar][0] * consts.STEP, garbages[gar][1] * consts.STEP))

def draw_screen():
    draw_window()
    # draw_garbage(garbages= list)

def draw_man():
    consts.WINDOW.blit(consts.GARBAGE_MAN_PIC, [0, 0])
    pygame.display.flip()


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    consts.WINDOW.blit(text_img, location)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE, consts.WIN_COLOR, consts.LOSE_LOCATION)
    pygame.display.update()


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE, consts.WIN_COLOR, consts.WIN_LOCATION)
    pygame.display.update()


def draw_first_message():
    draw_message(consts.FIRST_MESSAGE, consts.FIRST_FONT_SIZE, (0, 0, 0), consts.FIRST_LOCATION)
    pygame.display.update()

def play():
    pygame.init()
    draw_window(consts.SCREEN_PIC)
    draw_man()
    draw_first_message()
    pygame.time.wait(2000)
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
    pygame.quit()
play()