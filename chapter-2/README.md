# (2) Pygame Basics
pygame: Python framework for building games  

## Initializing Pygame Window
```py
# Import packages
import pygame, sys
from pygame.locals import * 

# Initialize Pygame
pygame.init()

# Config
WINDOW_SIZE = (400, 300)
WINDOW_NAME = "Hello World!"
FPS = 60
display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()

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
```

## Pixels
a surface is composed of pixels   
intially black but color can be changed  
in pygame, the origin is in the top left
cartesian coordinates follow (x, y) format  
![cartesian coordinates on pygame](https://inventwithpython.com/pygame/chapter2_files/image004.png)

## Surfaces & Window
surface objects: rectangular 2D image  
* contain pixels which can be altered with drawing images

window border, title bar, and buttons are part of the window, not surfaces  
`pygame.display.set_mode` returns the main rendering surface  

### Colors
primary colors of light: red, green, blue (RGB)
* computers use light and not the generic primary colors
* each value represented 0 - 255 (minimum - maximum)
* 255 x 255 x 255 color combinations

RGB colors represented with tuples  
ex) `(255, 255, 255)`  
mixing RGB values will result in different colors

| color     | RGB value       |
|-----------|-----------------|  
| Aqua      | (0, 255, 255)   |
| Black     | (0, 0, 0)       |
| Blue      | (0, 0, 255)     |
| Fuchsia   | (255, 0, 255)   |
| Gray      | (128, 128, 128) |
| Green     | (0, 128, 0)     |
| Lime      | (0, 255, 0)     |
| Maroon    | (128, 0, 0)     |
| Navy Blue | (0, 0, 128)     |
| Olive     | (128, 128, 0)   |
| Purple    | (128, 0, 128)   |
| Red       | (255, 0, 0)     |
| Silver    | (192, 192, 192) |
| Teal      | (0, 128, 128)   |
| White     | (255, 255, 255) |
| Yellow    | (255, 255, 0)   |

### Introducting Transparency
add a fourth value (0 - 255) representing opacity, or alpha  
must draw colors on a converted surface
```py
surface = display.convert_alpha()
```

### Rect Objects
accepts 4 arguments  
- x coordinate of top left corner
- y coordinate of top left corner
- width (px)
- height (px)

```py
import pygame
rect = pygame.Rect(10, 20, 200, 300)
print(rect.right) # => 210
```

the `Rect` object contains automatically computed attributes  
| attribute | description |
|-----------|-------------|
| rect.left | x coordinate of left |
| rect.right | x coordinate of the right |
| rect.top | y coordinate of the top |
| rect.bottom | y coordinate of the bottom |
| rect.centerx | x coordinate of center |
| rect.centery | y coordinate of center |
| rect.width | width of rectangle|
| rect.height | height of rectangle |
| rect.size | tuple (width, height) |
| rect.topleft | tuple (left, top) |
| rect.topright | tuple (right, top) |
| rect.bottomleft | tuple (left, bottom) |
| rect.bottomright | tuple (right, bottom) |
| rect.midleft | tuple (left, centery) |
| rect.midright | tuple (right, centery) |
| rect.midtop | tuple (centerx, top) |
| rect.midbottom | tuple (centerx, bottom) |

### Primitive Drawing Functions 
create rectangles, circles, lines, pixels, and other basic geometry  
`surface.fill(color)`: fills entire surface with a specified color  
`pygame.draw.polygon(surface, color, points, width)`: connects a set of points together with a certain line width & color  
`pygame.draw.line(surface, color, (x1, y1), (x2, y2), width)`: connect two points together with a certain line width & color  
`pygame.draw.lines(surface, color, closed, points, width)`: similar to polygon but `closed` determines if the lines form a closed figure  
`pygame.draw.circle(surface, color, center_point, radius, width)`: creates a circle with a center (remember radius is 0.5 * diameter)  
`pygame.draw.ellipse(surface, color, bounding_rectangle, width)`: specify a square & pygame will draw an ellipse inside the square  
`pygame.draw.rect(surface, color, rect_tuple, width)`: rect_tuple is the (x, y, width, height)  
```py
display.fill(colors["white"])

pygame.draw.line(display, colors["blue"], (60, 60), (120, 60), 4)
pygame.draw.circle(display, colors["red"], (300, 50), 20, 0)
pygame.draw.rect(display, colors["green"], (200, 150, 100, 50))
```

## pygame.display.update
renders surface to the computer  
add images to surfaces with "blit"  

### Animation
draw a slightly different picture every frame to give the illusion of movement  
`pygame.image.load(sprite_path)`: loads a sprite  
`image.get_rect()`: returns bounds of an image   
```py
# Import packages
import pygame, random, sys
from pygame.locals import * 

# Initialize Pygame
pygame.init()

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
    display.fill((255, 255, 255))
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
```

### Fonts
`pygame.font.Font(path, size)`: registers a new font at a certain size in pixels  
`FONT.render(text, _, text_color, background_color)`: creates a text surface  
```py
# Register font
FONT = pygame.font.Font("assets/SF-Pro.ttf", 32)
text_surface = FONT.render("Hello World", True, colors["blue"], colors["green"])
text_rect = text_surface.get_rect()
text_rect.center = (200, 150)

# Game loop
while True:
    display.fill(colors["white"])
    display.blit(text_surface, text_rect)
```