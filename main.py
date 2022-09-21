import pygame
import earth
import screen
import player
import consts
import time


def main():
    pygame.display.set_caption("Cleaning the world")

    earth.unite_screen()
    player_rect = pygame.Rect(0, 0, consts.PLAYER_WIDTH, consts.PLAYER_HEIGHT)

    screen.draw_first_message()
    pygame.time.wait(2000)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit
                run = False
            keys_pressed = pygame.key.get_pressed()
            player.player_movement(keys_pressed, player_rect)


        screen.draw_screen(soldier_rect)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

