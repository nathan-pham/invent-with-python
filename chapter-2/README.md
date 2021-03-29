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

## Rect Objects