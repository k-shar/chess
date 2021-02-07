import pygame
from constants import *
from menu import * 
from game import *

if __name__ == "__main__":

    # -- initialise the screen -- 
    pygame.display.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Pygame boilerplate")

    # -- initialise window --
    # the content of the current game loop is blit onto the window
    # the window is then enlarged in accordance with the aspect ratio
    # this prevents images being overstreched, and creates a border effect
    window = pygame.Surface((SCREEN_SIZE))

    screen, window = menu(screen, window)
    game(screen, window)
    pygame.quit()