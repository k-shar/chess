import pygame
from constants import *
from tiles import *
from pieces import *

def gen_board(window):
    # -- create checkerboard tiles --
    tiles = pygame.sprite.Group()
    i = 0
    for column in range(1, 9):
        for row in range(1, 9):
            # -- decide what color the tile is --
            if row % 2 == 0:
                if column % 2 == 0:
                    tile_color = CHECKER_COL
                else:
                    tile_color = BLACK
            if row % 2 == 1:
                if column % 2 == 0:
                    tile_color = BLACK
                else:
                    tile_color = CHECKER_COL

            # create the tile and add to sprite group
            tiles.add(Tile(row, column, tile_color, window, i))
            i += 1

    # -- create peices --
    pieces_group = pygame.sprite.Group()

    # -- pawns -- 
    for i in range(0, 8):
        pieces_group.add(Pawn("img/pawnB.bmp", tiles.sprites()[8+i]))
        pieces_group.add(Pawn("img/pawnW.bmp", tiles.sprites()[48+i]))

    # -- bishops --
    pieces_group.add(Bishop("img/bishopB.bmp", tiles.sprites()[2]))
    pieces_group.add(Bishop("img/bishopB.bmp", tiles.sprites()[5]))
    pieces_group.add(Bishop("img/bishopW.bmp", tiles.sprites()[58]))
    pieces_group.add(Bishop("img/bishopW.bmp", tiles.sprites()[61]))

    # -- knights --
    pieces_group.add(Knight("img/knightB.bmp", tiles.sprites()[1]))
    pieces_group.add(Knight("img/knightB.bmp", tiles.sprites()[6]))
    pieces_group.add(Knight("img/knightW.bmp", tiles.sprites()[57]))
    pieces_group.add(Knight("img/knightW.bmp", tiles.sprites()[62]))
    #-- rooks --
    pieces_group.add(Rook("img/rookB.bmp", tiles.sprites()[0]))
    pieces_group.add(Rook("img/rookB.bmp", tiles.sprites()[7]))
    pieces_group.add(Rook("img/rookW.bmp", tiles.sprites()[56]))
    pieces_group.add(Rook("img/rookW.bmp", tiles.sprites()[63]))
    # -- Royals --
    pieces_group.add(Queen("img/queenB.bmp", tiles.sprites()[3]))
    pieces_group.add(Queen("img/queenW.bmp", tiles.sprites()[59]))
    pieces_group.add(King("img/kingB.bmp", tiles.sprites()[4]))
    pieces_group.add(King("img/kingW.bmp", tiles.sprites()[60]))

    return tiles, pieces_group 