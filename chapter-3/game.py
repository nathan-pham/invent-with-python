import pygame, random
from config import *
from colors import *

def scale_coordinates(x, y):
    scaled_x = x * (BOX_SIZE + GAP_SIZE) + X_MARGIN
    scaled_y = y * (BOX_SIZE + GAP_SIZE) + Y_MARGIN
    return (scaled_x, scaled_y)

class Card:
    def __init__(self, icon, x, y):
        self.icon = icon
        self.x = x
        self.y = y

    def hover(self, mouse_x, mouse_y):
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                (scaled_x, scaled_y) = scale_coordinates(x, y)
                rect = pygame.Rect(scaled_x, scaled_y, BOX_SIZE, BOX_SIZE)
                if rect.collidepoint(mouse_x, mouse_y):
                    return (x, y)

        return (None, None)

    def render(self, ctx):
        (shape, color) = self.icon


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
            column.append(Card(possible_icons[0], x, y))
            del possible_icons[0]

        game_board.append(column)

    return game_board

def cleared_game(cards):
    for card in cards:
        if False in card:
            return False

    return True