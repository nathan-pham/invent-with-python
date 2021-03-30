import pygame, sys
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