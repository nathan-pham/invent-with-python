# Import packages
import pygame, sys
from pygame.locals import * 

# Initialize Pygame
pygame.init()

# Colors
colors = {
    "black": (  0,   0,   0),
    "white": (255, 255, 255),
    "red":   (255,   0,   0),
    "green": (  0, 255,   0),
    "blue":  (  0,   0, 255)
}

# Config
WINDOW_SIZE = (400, 300)
WINDOW_NAME = "Hello World!"
FPS = 60
display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()

display.fill(colors["white"])

pygame.draw.line(display, colors["blue"], (60, 60), (120, 60), 4)
pygame.draw.circle(display, colors["red"], (300, 50), 20, 0)
pygame.draw.rect(display, colors["green"], (200, 150, 100, 50))

# Game loop
while True:
    # Loop through events
    for event in pygame.event.get():
        # Close window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)