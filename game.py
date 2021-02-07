import pygame
from constants import *
import window_resizing as ws
from tiles import *
from pieces import *
from generate_board import gen_board

WINDOW_ASPECT_RATIO = (1, 1)


def game(screen, window):

    # mouse sprite is relative to the window
    # as an offsett is applied
    mouse_sprite = MousePointer()
    mouse_sprite_group = pygame.sprite.Group()
    mouse_sprite_group.add(mouse_sprite)
    mouse_cycle_counter = 0

    tiles, pieces_group = gen_board(window)
    selected_piece = None

    # push a screen resize to adjust all the sizing
    pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, w=screen.get_width(), h=screen.get_height()))

    clock = pygame.time.Clock()
    done = False
    while not done:

        # -- reset color of window and screen --
        screen.fill(BLUE)
        window.fill(BLACK)

        # -- event handler --
        for event in pygame.event.get():

            # -- on quit --
            if event.type == pygame.QUIT:
                ## TODO ##
                ## functionality to quit the whole program ##
                done = True
                pass

            #   --- SELECTION AND DESELECTION ---
            #     -- MOUSE INPUT --
            #     works on a two click cycle
            #
            #   mouse_cycle_counter = 0
            #       mouse down: select piece
            #       mouse up: pass
            #
            #   (player waves piece around board)
            #
            #   mouse_cycle_counter = 1
            #       mouse down: if piece selected inc counter
            #       mouse up: place piece, inc counter

            # -- when mouse pressed --
            if event.type == pygame.MOUSEBUTTONDOWN:

                if mouse_cycle_counter == 0:

                    # find all peices colliding with mouse (should only be one)
                    selected_list = pygame.sprite.spritecollide(mouse_sprite, pieces_group, False)

                    # set clicked piece to selected
                    if len(selected_list) != 0:
                        selected_piece = selected_list[0]

                elif mouse_cycle_counter == 1:
                    pass

            # -- when mouse released --
            if event.type == pygame.MOUSEBUTTONUP:

                if mouse_cycle_counter == 0:
                    if len(selected_list) != 0:
                        # ready to move on to next cycle
                        mouse_cycle_counter = 1

                elif mouse_cycle_counter == 1:

                    # check peice has been selected
                    if selected_piece != None:

                        # check a  tile has been selected
                        tiles_collided = pygame.sprite.spritecollide(mouse_sprite, tiles, False)
                        if len(tiles_collided) != 0:

                            # check tile is legal move
                            if tiles_collided[0].is_legal:

                                # move the peice to that tile
                                selected_piece.tile = tiles_collided[0]
                                selected_piece = None

                                # ready to move on to next cycle
                                mouse_cycle_counter = 0

            #   --- END OF SELECTION AND DESELECTION ---

            # -- on resize --
            if event.type == pygame.VIDEORESIZE:
                # resize screen
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                current_screen_size = screen.get_size()

                # resize the window
                window = ws.scale_up_to_ratio(window, screen, WINDOW_ASPECT_RATIO)
                centered_pos = ws.center_surfaces(window, screen)

        # update sprite groups
        tiles.update(window, mouse_sprite)
        pieces_group.update(window, mouse_sprite)
        # pass the offset of the window from the screen
        mouse_sprite_group.update(centered_pos[0])

        # re-update the selected piecce
        if selected_piece != None:
            legal_moves = selected_piece.selected(window, mouse_sprite, tiles)
        else:
            legal_moves = []

        # highlight legal moves
        for i in legal_moves:
            tiles.sprites()[i].legal_move()

        # -- draw sprite groups --
        tiles.draw(window)
        pieces_group.draw(window)
        mouse_sprite_group.draw(window)

        # -- display window and screen --
        screen.blit(window, centered_pos)
        pygame.display.update()

        clock.tick(FPS)


if __name__ == '__main__':

    pygame.display.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Pygame boilerplate")
    window = pygame.Surface((SCREEN_SIZE))
    game(screen, window)
