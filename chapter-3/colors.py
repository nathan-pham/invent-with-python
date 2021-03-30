from config import *

# Colors
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

# Theme
THEME_BG = NAVYBLUE
THEME_LIGHT_BG = GRAY
THEME_BOX = WHITE
THEME_HIGHLIGHT = BLUE

# Game objects
DONUT = "DONUT"
SQUARE = "SQUARE"
DIAMOND = "DIAMOND"
LINES = "LINES"
OVAL = "OVAL"

# List
ALL_COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALL_SHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

assert len(ALL_COLORS) * len(ALL_SHAPES) * 2 >= BOARD_WIDTH * BOARD_HEIGHT, "the current board it too large for the available shape & color combinations"