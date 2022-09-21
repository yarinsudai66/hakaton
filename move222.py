def get_soldier_index(soldier_rect):
    soldier_index = []
    for i in range(consts.SOLDIER_HEIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            soldier_index.append([(soldier_rect.x + j), soldier_rect.y + i])
    return soldier_index