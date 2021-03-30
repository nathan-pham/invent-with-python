import pygame
import random, sys
from pygame.locals import *
from config import *
from colors import *

pygame.init()

display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()

mouse_x = 0
mouse_y = 0
mouse_clicked = False

while True:
    display.fill(THEME_BG)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            (mouse_x, mouse_y) = event.pos
        elif event.type == MOUSEBUTTONUP:
            (mouse_x, mouse_y) = event.pos
            mouse_clicked = True

    pygame.draw.circle(display, RED, (mouse_x, mouse_y), 10, 2)

    pygame.display.update()
    clock.tick(FPS)
def generate_board(width, height):
    possible_icons = []
    icons_needed = int(BOARD_WIDTH * BOARD_HEIGHT / 2)

    for color in ALL_COLORS:
        for shape in ALL_SHAPES:
            possible_icons.append((shape, color))

    possible_icons = possible_icons[:icons_needed] * 2
    random.shuffle(possible_icons)

    game_board = []
    for x in range(BOARD_WIDTH):
        column = []
        for y in range(BOARD_HEIGHT):
            column.append(possible_icons[0])
            del possible_icons[0]

        game_board.append(column)

    return game_board

def cleared_game(cards):
    for card in cards:
        if False in card:
            return False

    return True