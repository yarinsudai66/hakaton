# solider movement
def solider_movement(keys_pressed, soldier_rect):
    if keys_pressed[pygame.K_LEFT] \
            and 0 < soldier_rect.x * consts.STEP < consts.WINDOW_WIDTH:
        soldier_rect.x -= 1  # left
    if keys_pressed[pygame.K_RIGHT] \
            and 0 < soldier_rect.x * consts.STEP + consts.STEP * 2 < consts.WINDOW_WIDTH:
        soldier_rect.x += 1  # right
    if keys_pressed[pygame.K_UP] \
            and 0 < soldier_rect.y * consts.STEP < consts.WINDOW_HEIGHT:
        soldier_rect.y -= 1  # up
    if keys_pressed[pygame.K_DOWN] \
            and 0 < soldier_rect.y * consts.STEP + consts.STEP * 4 < consts.WINDOW_HEIGHT:
        soldier_rect.y += 1  # down