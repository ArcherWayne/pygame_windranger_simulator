import pygame
from PIL import Image


window_size = (1400, 800)
WIN_WIDTH = window_size[0]
WIN_HEIGHT = window_size[1]
screen = pygame.display.set_mode(window_size)

FPS = 120

map = Image.open('assets/graphics/map/map.png')
MAP_WIDTH = map.width       #图片的宽
MAP_HEIGHT = map.height      #图片的高
map_size = (MAP_WIDTH, MAP_HEIGHT)


# game setting 
show_collision_area = 1
show_absolute_vector = 1

# game stats
CURSOR_WIDTH = 32
CURSOR_HEIGHT = 32

# hero stats
# __init__(self, name, health, movement_speed, damage, forswing, backswing, flag_moving)
HERO_WIDTH = 60
HERO_HEIGHT = 60
HERO_COLLISION_WIDTH = 20
HERO_COLLISION_HEIGHT = 20
HERO_HEALTH = 550
HERO_MOVEMENT_SPEED = 200
HERO_ATTACK_INTERVAL = FPS/3

# ARROW stats 
ARROW_WIDTH = 10
ARROW_HEIGHT = 10
ARROW_COLLISION_WIDTH = 10
ARROW_COLLISION_HEIGHT = 10
ARROW_SPEED = 600
ARROW_DAMAGE = 10


# creep stats
# __init__(self, health, movement_speed, damage, forswing, backswing)
CREEP_WIDTH = 60
CREEP_HEIGHT = 60
CREEP_COLLISION_WIDTH = 40
CREEP_COLLISION_HEIGHT = 40
CREEP_HEALTH = 20
CREEP_MOVEMENT_SPEED = 120
CREEP_DAMAGE = 20
CREEP_ATTACK_INTERVAL = FPS/10



# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
COLOR_TRANSPARENT = (0, 0, 0, 0) # alpha = 0, total transparency

