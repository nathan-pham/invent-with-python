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

