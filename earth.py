import consts
import random
import pygame
import screen

earth = []


# creating an empty matrix
def empty_screen():
    row_to_append = []
    for row in range(consts.SCREEN_ROWS):
        for col in range(consts.SCREEN_COLS):
            row_to_append.append(consts.EMPTY)
        earth.append(row_to_append)
        row_to_append = []


def put_garbage():
    garbage_count = 0
    while garbage_count < consts.GARBAGE_COUNT:
        row = random.randint(0, consts.SCREEN_ROWS - 1)
        col = random.randint(0, consts.SCREEN_COLS - consts.GARBAGE_WIDTH - 1)
        if earth[row][col] == consts.EMPTY:
            garbage_count += 1
            for i in range(consts.GARBAGE_WIDTH):
                earth[row][col + i] = consts.GARBAGE


def garbage_indexes():
    garbage_index = []
    for row in range(consts.SCREEN_ROWS):
        for col in range(consts.SCREEN_COLS):
            if earth[row][col] == consts.GARBAGE:
                garbage_index.append([col, row])
    return garbage_index


def unite_screen():
    empty_screen()
    put_garbage()


unite_screen()
for m in range(consts.SCREEN_ROWS):
    for n in range(consts.SCREEN_COLS):
        print(earth[m][n], end=" ")
    print(" ")

print(garbage_indexes())
print(len(garbage_indexes()))
