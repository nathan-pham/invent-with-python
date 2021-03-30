import pygame, sys
from pygame.locals import *
from config import *
from colors import *
import game

pygame.init()

display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()

mouse_x = 0
mouse_y = 0
mouse_clicked = False
game_board = game.generate_board(WINDOW_SIZE[0], WINDOW_SIZE[1])

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

    for card in game_board:
        card.render(display)

    pygame.draw.circle(display, RED, (mouse_x, mouse_y), 10, 2)

    pygame.display.update()
    clock.tick(FPS)