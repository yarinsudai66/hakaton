# checking if solider on a mine
def is_on_mine(soldier_rect, mines):
    left_leg = get_soldier_feet_index(soldier_rect)
    right_leg = [left_leg[0] + 1, left_leg[1]]
    if left_leg in mines and right_leg in mines:
        return True
    return False