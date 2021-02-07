import pygame
from constants import *
import window_resizing as ws
from buttons import *

WINDOW_ASPECT_RATIO = (16, 9)

buttons = pygame.sprite.Group()
enter = Button(RED, [0.3, 0.3], [0.5, 0.5])
buttons.add(enter)

def menu(screen, window):

    clock = pygame.time.Clock()
    done = False
    while not done:

        # -- reset color of window and screen --
        screen.fill(BLUE)
        window.fill(GREEN)

        # -- event handler --
        for event in pygame.event.get():

            # -- on quit --
            if event.type == pygame.QUIT:
                ## TODO ##
                ## functionality to quit the whole program ##
                done = True
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                return screen, window

            # -- on resize --
            if event.type == pygame.VIDEORESIZE:
                # resize screen
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                current_screen_size = screen.get_size()
                
                # resize the window
                window = ws.scale_up_to_ratio(window, screen, WINDOW_ASPECT_RATIO)
                centered_pos = ws.center_surfaces(window, screen)

        # -- update sprite groups --
        buttons.update(window)

        # -- draw sprite groups on window --
        buttons.draw(window)

        # -- display window and screen --
        screen.blit(window, centered_pos)
        pygame.display.update()

        clock.tick(FPS)


if __name__ == '__main__':

    pygame.display.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Pygame boilerplate")
    window = pygame.Surface((SCREEN_SIZE))
    menu(screen, window)
