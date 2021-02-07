import pygame
from constants import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, row, column, color, window, key):
        super().__init__()

        # number in master list of tiles
        self.key = key
        
        # counting from top left, indexed from 1 to 8
        self.pos = [row, column]
        self.color = color  

        # instanciate dummy surface and fill with color
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()

    def update(self, window, mouse_sprite):

        self.is_legal = False
        self.image.fill(self.color)
        self.x = (window.get_width() / 8) * (self.pos[0] - 1)
        self.y = (window.get_height() / 8) * (self.pos[1] - 1)
        self.rect = pygame.Rect((self.x, self.y), (window.get_size()[0] // 8, window.get_size()[1] // 8))
        self.image = pygame.transform.scale(self.image, (self.rect.size))

    def legal_move(self):
        self.image.fill(RED)
        self.is_legal = True