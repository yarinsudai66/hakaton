import consts
import pygame


def get_player_feet_index(player_rect):
    feetl_x = player_rect.x
    feetl_y = player_rect.y + 1 * (consts.PLAYER_HEIGHT - 1)
    feetr_x = feetl_x + 1
    feetr_y = feetl_y
    return [[feetl_x, feetl_y], [feetr_x, feetr_y]]


def get_player_index(player_rect):
    player_index = []
    for i in range(consts.PLAYER_HEIGHT):
        for j in range(consts.PLAYER_WIDTH):
            player_index.append([(player_rect.x + j), player_rect.y + i])
    return player_index


def step_on_trash(get_player_feet_index, trash_list):
    for i in range(0, len(trash_list)):
        for j in range(2):
            if trash_list[i][j] == get_player_feet_index[0] or \
                    trash_list[i][j] == get_player_feet_index[0]:
                return True
    return False


def count_points(trash_list, player_rect):
    count = 0
    if step_on_trash(get_player_feet_index(player_rect), trash_list):
        count += 1
    return count


def step_on_flower(get_player_feet_index, flower_list):
    for i in range(0, len(flower_list)):
        if flower_list[i] == get_player_feet_index[0] or \
                flower_list[i] == get_player_feet_index[0]:
            return True
    return False


def player_movement(keys_pressed, player_rect):
    if keys_pressed[pygame.K_LEFT] \
            and 0 < player_rect.x * consts.STEP < consts.WINDOW_WIDTH:
        player_rect.x -= 1  # left
    if keys_pressed[pygame.K_RIGHT] \
            and 0 < player_rect.x * consts.STEP + consts.STEP * 2 < consts.WINDOW_WIDTH:
        player_rect.x += 1  # right
    if keys_pressed[pygame.K_UP] \
            and 0 < player_rect.y * consts.STEP < consts.WINDOW_HEIGHT:
        player_rect.y -= 1  # up
    if keys_pressed[pygame.K_DOWN] \
            and 0 < player_rect.y * consts.STEP + consts.STEP * 4 < consts.WINDOW_HEIGHT:
        player_rect.y += 1  # down


def draw_player(player_rect):
    consts.WINDOW.blit(consts.SOLDIER_PIC, (player_rect.x * consts.STEP, player_rect.y * consts.STEP))
    pygame.display.update()
