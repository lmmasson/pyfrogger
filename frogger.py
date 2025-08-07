import pygame
from enum import IntEnum


# Const
LINES = 6
COLS = 20
VERSION = "0.5.1"

class D(IntEnum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

road1 = 

# Globals
lh=sh=sw=fw=cw = 0

# Functions

def move_frog(_fx:int, _fy:int, dir:int) -> tuple[int, int]:
    match dir:
        case D.UP:
            if _fy >= lh:
                _fy -= lh
        case D.DOWN:
            if _fy < (sh - lh):
                _fy += lh
        case D.RIGHT:
           if _fx + cw <  (sw - fw):
                    _fx += cw 
        case D.LEFT:
            if _fx >= cw:
                     _fx -= cw
        case _:
            pass
    
    return _fx, _fy

def event_manager() -> tuple[bool, int]:
    # default values
    _running = True
    _dir = D.NONE
    
    # read events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False
        elif event.type == pygame.FINGERDOWN:	
            x = int(event.x * sw)
            y = int(event.y * sh)
            
            debug_print(f"x={x}, y={y}")
            # Compute direction
            if y < lh:
                # up
                _dir = D.UP
            elif y > (sh - lh) and y < sh:
                # down
                _dir = D.DOWN
            elif x < (sw / 2):
                 # left
                 _dir = D.LEFT
            elif x > (sw / 2):
                # right
                _dir = D.RIGHT
        elif event.type == pygame.FINGERUP:
            pass
    return _running, _dir

# init
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# debug
WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 100)

def debug_print(st:str):
    img = font.render(st, True, WHITE)
    screen.blit(img, (0, 0))  

# load images
# background
background = pygame.image.load("./img/Background.png").convert()
background = pygame.transform.smoothscale(background, screen.get_size())
# frog
frog = pygame.image.load("./img/Frog.png").convert_alpha()

# scale frog
sw = screen.get_width()
sh = screen.get_height()

fw = frog.get_width()
fh = frog.get_height()

r = (sh / LINES) / fh
frog = pygame.transform.smoothscale(frog, (fw*r, fh * r))

# get new frog size
fw = frog.get_width()
fh = frog.get_height()

# compute constants that simplify computation
lh = int(sh / LINES)
cw = int(sw / COLS)

# place frog in the middle of bottom area
fy = sh-fh
fx = int(cw * (COLS / 2 - 1))

# Start main loop
running = True
dir = D.NONE


# Main loop
while running:
    # poll for events
    running, dir = event_manager()
    # compute new frog coordinates
    fx, fy = move_frog(fx, fy, dir)
    
    # display background and frog
    screen.blit(background, (0, 0))
    screen.blit(frog, (fx, fy))
    pygame.display.flip()

# End of the main loop
pygame.quit()
exit(0)
