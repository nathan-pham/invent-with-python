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

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def mult(self, m):
        self.x *= m
        self.y *= m
    
    def repr(self):
        return (self.x, self.y)

class Cat:
    sprite = pygame.image.load("assets/cat.png")
    vel = Vector(random.randint(1, 5), random.randint(1, 5))

    def __init__(self, x=100, y=100):
        rect = self.sprite.get_rect()
        self.width = rect.width
        self.height = rect.height
        self.pos = Vector(x, y)

    def update(self):
        self.pos.add(self.vel)
        if self.pos.x > WINDOW_SIZE[0] - self.width or self.pos.x < 0:
            self.vel.x *= -1
        if self.pos.y > WINDOW_SIZE[1] - self.height or self.pos.y < 0:
            self.vel.y *= -1

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos.repr())

cat = Cat(100, 100)

# Game loop
while True:
    display.fill(colors["white"])
    cat.update()
    cat.render(display)

    # Loop through events
    for event in pygame.event.get():
        # Close window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)