import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, color, rel_size, rel_pos):
        super().__init__()

        self.color = color
        self.rel_size = rel_size
        self.rel_pos = rel_pos

        # instanciate a dummy surface to be transformed
        self.image = pygame.Surface((0, 0))

    def update(self, window):
        
        # scale the dimentions of the button realative to window size
        self.width = int(window.get_width() * self.rel_size[0])
        self.height = int(window.get_height() * self.rel_size[1])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
       
        # set position of rect
        self.rect = self.image.get_rect()
        self.rect.centerx = window.get_width() * self.rel_pos[0]
        self.rect.centery = window.get_height() * self.rel_pos[1]

        self.image.fill(self.color)