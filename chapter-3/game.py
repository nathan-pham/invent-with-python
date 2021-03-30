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
        (left, top) = scale_coordinates(self.x, self.y)

        QUARTER = int(BOX_SIZE / 4)
        HALF = int(BOX_SIZE / 2)

        if shape == DONUT:
            pygame.draw.circle(ctx, color, (left + HALF, top + HALF), HALF - 5)
            pygame.draw.circle(ctx, THEME_BG, (left + HALF, top + HALF), QUARTER - 5)
        elif shape == SQUARE:
            pygame.draw.rect(ctx, color, (left + QUARTER, top + QUARTER, BOX_SIZE - HALF, BOX_SIZE - HALF))
        elif shape == DIAMOND:
            pygame.draw.polygon(ctx, color, ((left + HALF, top), (left + BOX_SIZE - 1, top + HALF), (left + HALF, top + BOX_SIZE - 1), (left, top + HALF)))
        elif shape == LINES:
            for i in range(0, BOX_SIZE, 4):
                pygame.draw.line(ctx, color, (left, top + i), (left + i, top))
                pygame.draw.line(ctx, color, (left + i, top + BOX_SIZE - 1), (left + BOX_SIZE - 1, top + i))
        elif shape == OVAL:
            pygame.draw.ellipse(ctx, color, (left, top + QUARTER, BOX_SIZE, HALF))


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
        # column = []
        for y in range(BOARD_HEIGHT):
            game_board.append(Card(possible_icons[0], x, y))
            del possible_icons[0]

        # game_board.append(column)

    return game_board

def cleared_game(cards):
    for card in cards:
        if False in card:
            return False

    return True