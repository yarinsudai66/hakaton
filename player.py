def get_soldier_feet_index(soldier_rect):
    feet_x = soldier_rect.x
    feet_y = soldier_rect.y + 1 * (consts.SOLDIER_HEIGHT - 1)
    return [feet_x, feet_y]