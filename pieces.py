import pygame
from constants import *


class MousePointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 5, 5)

    def update(self, offset):
        self.rect.x = pygame.mouse.get_pos()[0] - offset
        self.rect.y = pygame.mouse.get_pos()[1]

        self.image = pygame.Surface((5, 5))


class Piece(pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        self.file = file
        if self.file[-5] == "W":
            self.polarity = 1
        if self.file[-5] == "B":
            self.polarity = -1

        self.base_image = pygame.image.load(file)
        self.image = self.base_image
        self.image.set_colorkey(RED)

        self.highlight = pygame.Surface((self.image.get_size()))
        self.highlight.fill(GREEN)

    def update(self, window, mouse_sprite):
        self.image = pygame.transform.scale(self.base_image, (int(self.tile.image.get_width() * 0.9), int(self.tile.image.get_height() * 0.9)))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.tile.rect.centerx
        self.rect.centery = self.tile.rect.centery

    def selected(self, window, mouse_sprite, tiles):
        self.highlight = pygame.transform.scale(self.highlight, (self.image.get_size()))
        temp = self.image
        self.image = self.highlight
        self.image.blit(temp, (0, 0))

        self.rect.centerx, self.rect.centery = mouse_sprite.rect.centerx, mouse_sprite.rect.centery


def diagonals(start, key, tiles, legal):
    i = key
    # top right diagonal
    while i >= 0 and (tiles.sprites()[i].pos[0] != 1 or start == 1):
        legal.append(i)
        i -= 7
    # top left diagonal
    i = key
    while i >= 0 and (tiles.sprites()[i].pos[0] != 8 or start == 8):
        legal.append(i)
        i -= 9
    # bottom right diagonal
    i = key
    while i <= 63 and (tiles.sprites()[i].pos[0] != 1 or start == 1):
        legal.append(i)
        i += 9
    # bottom left diagonal
    i = key
    while i <= 63 and (tiles.sprites()[i].pos[0] != 8 or start == 8):
        legal.append(i)
        i += 7
    return legal


def orthogonal(key, tiles, legal):
    # up
    i = key
    while i >= 0:
        legal.append(i)
        i -= 8
        if tiles.sprites()[i].pos[1] == 1:
            legal.append(i)
            break
    # down
    i = key
    while i <= 55:
        legal.append(i)
        i += 8
        if tiles.sprites()[i].pos[1] == 8:
            legal.append(i)
            break
    # left
    i = key
    while tiles.sprites()[i].pos[0] != 1:
        legal.append(i)
        i -= 1
        if tiles.sprites()[i].pos[0] == 1:
            legal.append(i)
            break
    # right
    i = key
    while tiles.sprites()[i].pos[0] != 8:
        legal.append(i)
        i += 1
        if tiles.sprites()[i].pos[0] == 8:
            legal.append(i)
            break
    return legal


class Pawn(Piece):
    def __init__(self, file, tile):

        self.spawn_tile = tile
        self.tile = tile
        self.move_two = True

        super().__init__(file)

    def selected(self, window, mouse_sprite, tiles):
        super().selected(window, mouse_sprite, tiles)

        if self.spawn_tile == self.tile:
            return [self.tile.key - 16 * self.polarity, self.tile.key - 8 * self.polarity, self.tile.key]
        else:
            return [self.tile.key - 8 * self.polarity, self.tile.key]


class Bishop(Piece):
    def __init__(self, file, tile):

        self.tile = tile
        super().__init__(file)

    def selected(self, window, mouse_sprite, tiles):
        super().selected(window, mouse_sprite, tiles)
        legal = []
        legal = diagonals(self.tile.pos[0], self.tile.key, tiles, legal)
        return legal

class Knight(Piece):
    def __init__(self, file, tile):

        self.tile = tile
        super().__init__(file)

    def selected(self, window, mouse_sprite, tiles):
        super().selected(window, mouse_sprite, tiles)
        legal = [self.tile.key]

        # move to the left top
        if self.tile.pos[0] >= 2 and self.tile.pos[1] >= 3:
            legal.append(self.tile.key - 17)
        # move to the left top middle
        if self.tile.pos[0] >= 3 and self.tile.pos[1] >= 2:
            legal.append(self.tile.key - 10)
        # move to the left bottom middle
        if self.tile.pos[0] >= 3 and self.tile.pos[1] <= 7:
            legal.append(self.tile.key + 6)
        # move to the left bottom
        if self.tile.pos[0] >= 2 and self.tile.pos[1] <= 6:
            legal.append(self.tile.key + 15)

        # move to the right top
        if self.tile.pos[0] <= 7 and self.tile.pos[1] >= 3:
            legal.append(self.tile.key - 15)
        # move to the right top middle
        if self.tile.pos[0] <= 6 and self.tile.pos[1] >= 2:
            legal.append(self.tile.key - 6)
        # move to the right bottom middle
        if self.tile.pos[0] <= 6 and self.tile.pos[1] <= 7:
            legal.append(self.tile.key + 10)
        # move to the right bottom
        if self.tile.pos[0] <= 7 and self.tile.pos[1] <= 6:
            legal.append(self.tile.key + 17)
        return legal

class Rook(Piece):
    def __init__(self, file, tile):

        self.tile = tile
        super().__init__(file)

    def selected(self, window, mouse_sprite, tiles):
        super().selected(window, mouse_sprite, tiles)
        legal = []
        legal = orthogonal(self.tile.key, tiles, legal)
        return legal


class Queen(Piece):
    def __init__(self, file, tile):

        self.tile = tile
        super().__init__(file)

    def selected(self, window, mouse_sprite, tiles):
        super().selected(window, mouse_sprite, tiles)
        legal = []
        legal = diagonals(self.tile.pos[0], self.tile.key, tiles, legal)
        legal = orthogonal(self.tile.key, tiles, legal)
        return legal


class King(Piece):
    def __init__(self, file, tile):

        self.tile = tile
        super().__init__(file)

    def selected(self, window, mouse_sprite, tiles):
        super().selected(window, mouse_sprite, tiles)

        legal = [self.tile.key]
        # variables for diagonals
        # up-left, up-right, down-left, down-right

        ul, ur, dl, dr = True, True, True, True

        # orthogonal directions, and decide if diagonals are legal
        if self.tile.pos[0] != 8:
            legal.append(self.tile.key + 1)  # left
        else: ur, dr = False, False

        if self.tile.pos[0] != 1:
            legal.append(self.tile.key - 1)  # right
        else: ul, dl = False, False

        if self.tile.pos[1] != 1:
            legal.append(self.tile.key - 8)  # up
        else: ul, ur = False, False

        if self.tile.pos[1] != 8:
            legal.append(self.tile.key + 8)  # down
        else: dl, dr = False, False

        # diagonals
        if ul: legal.append(self.tile.key -9)
        if ur: legal.append(self.tile.key -7)
        if dl: legal.append(self.tile.key +7)
        if dr: legal.append(self.tile.key +9)

        return legal
