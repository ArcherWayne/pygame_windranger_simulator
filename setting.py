import pygame
from PIL import Image

pygame.init()

# game manager init -------------------------------------------------------------------------------- #
FONT = pygame.font.Font('assets/font/HuaGuangGangTieZhiHei-KeBianTi-2.ttf', 30)

# map setting ------------------------------------------------- #
WINDOW_SIZE = (1400, 800)
WIN_WIDTH = WINDOW_SIZE[0]
WIN_HEIGHT = WINDOW_SIZE[1]
screen = pygame.display.set_mode(WINDOW_SIZE)
map = Image.open('assets/graphics/map/map.png')
MAP_WIDTH = map.width       #图片的宽
MAP_HEIGHT = map.height      #图片的高
map.close()

dota2_actual_map_size = (11000, 11000)
# MAP_WIDTH = dota2_actual_map_size[0]      #图片的宽
# MAP_HEIGHT = dota2_actual_map_size[1]      #图片的高

MAP_SIZE = (MAP_WIDTH, MAP_HEIGHT)

# camera debug setting  ----------------------------------------------- #
show_collision_area = 0
show_absolute_vector = 0

# game stats -------------------------------------------------- #
FPS = 120
CURSOR_WIDTH = 32
CURSOR_HEIGHT = 32

# colors  ------------------------------------------------------- #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
COLOR_TRANSPARENT = (0, 0, 0, 0) # alpha = 0, total transparency

# stats manager init -------------------------------------------------------------------------------- #

# # hero stats  ------------------------------------------------- #
# # __init__(self, name, health, movement_speed, damage, forswing, backswing, flag_moving)
# HERO_WIDTH = 60
# HERO_HEIGHT = 60
# HERO_COLLISION_WIDTH = 20
# HERO_COLLISION_HEIGHT = 20
# HERO_HEALTH = 524
# HERO_MANA = 345
# HERO_MOVEMENT_SPEED = 290 # 每秒移动的像素
# HERO_ATTACK_INTERVAL = FPS/3

# # ARROW stats  ------------------------------------------------- #
# ARROW_WIDTH = 10
# ARROW_HEIGHT = 10
# ARROW_COLLISION_WIDTH = 10
# ARROW_COLLISION_HEIGHT = 10
# ARROW_SPEED = 600
# ARROW_DAMAGE = 42
# ARROW_KNOCKBACK = 200
# ARROW_PENETRATION = 1

# SHACKLESHOT_CD = FPS * 3
# POWERSHOT_CD = FPS * 3
# WINDRUN_CD = FPS * 3
# FOCUSFIRE_CD = FPS * 3

# # creep stats --------------------------------------------------- #
# # __init__(self, health, movement_speed, damage, forswing, backswing)
# CREEP_WIDTH = 60
# CREEP_HEIGHT = 60
# CREEP_COLLISION_WIDTH = 40
# CREEP_COLLISION_HEIGHT = 40
# CREEP_HEALTH = 550
# CREEP_MOVEMENT_SPEED = 31 # 315
# CREEP_DAMAGE = 19
# CREEP_ATTACK_INTERVAL = FPS


class STAT_MANAGER:
	def __init__(self) -> None:

		# hero init stats -------------------------------------- #
		self.hero_width = 60
		self.hero_height = 60
		self.hero_collision_width = 20
		self.hero_collision_height = 20
		self.hero_health = 524
		self.hero_mana = 345
		self.hero_movement_speed = 290
		self.hero_attack_interval = FPS / 3

		self.hero_strength = 0
		self.hero_agility = 0
		self.hero_intelligence = 0

		# arrow init stats ------------------------------------- #
		self.arrow_width = 10
		self.arrow_height = 10
		self.arrow_collision_width = 10
		self.arrow_collision_height = 10
		self.arrow_speed = 600
		self.arrow_damage = 42
		self.arrow_knockback = 200
		self.penetration = 1

		# skill init stats ------------------------------------- #

		self.shackleshot_cd = FPS * 3
		self.powershot_cd = FPS * 3
		self.windrun_cd = FPS * 3
		self.focusfire_cd = FPS * 3

		# creep init stats ------------------------------------- #
		self.creep_width = 60
		self.creep_height = 60
		self.creep_collision_width = 40
		self.creep_collision_height = 40
		self.creep_health = 550
		self.creep_movement_speed = 31 # 315
		self.creep_damage = 19
		self.creep_attack_interval = FPS
