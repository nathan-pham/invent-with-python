# Import packages
import pygame, random, sys
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

# Register font
FONT = pygame.font.Font("assets/SF-Pro.ttf", 32)
text_surface = FONT.render("Hello World", True, colors["blue"], colors["green"])
text_rect = text_surface.get_rect()
text_rect.center = (200, 150)

# Game loop
while True:
    display.fill(colors["white"])
    display.blit(text_surface, text_rect)

    # Loop through events
    for event in pygame.event.get():
        # Close window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)