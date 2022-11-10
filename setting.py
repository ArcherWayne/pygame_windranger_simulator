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
# map = Image.open('assets/graphics/map/dotamap1_25clip.png')
# # map = Image.open('assets/graphics/map/map.png')
# # MAP_WIDTH = map.width       #图片的宽
# # MAP_HEIGHT = map.height      #图片的高
# map.close()

dota2_actual_map_size = (11000, 11000)
MAP_WIDTH = dota2_actual_map_size[0]      #图片的宽
MAP_HEIGHT = dota2_actual_map_size[1]      #图片的高

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

# stats manager -------------------------------------------------------------------------------- #
class STAT_MANAGER:
	def __init__(self) -> None:
		# NOTE: 仔细思考一下, 数值可能还是得赋给类, 然后让类不断获取更新的值
		# hero init stats -------------------------------------- #
		self.hero_width = 60
		self.hero_height = 60
		self.hero_collision_width = 20
		self.hero_collision_height = 20
 
		self.hero_max_health = 524
		self.hero_current_health = 524
		self.hero_current_health_percentage = \
			self.hero_current_health / self.hero_max_health
		self.hero_max_mana = 345
		self.hero_current_mana = 345
		self.hero_current_mana_percentage = \
			self.hero_current_mana / self.hero_max_mana

		self.hero_movement_speed = 290 # FIXME: 修改为公式计算
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
		self.arrow_penetration = 1

		# skill init stats ------------------------------------- #
		## shackleshot
		self.shackleshot_cd = FPS * 3
		
		## powershot
		self.powershot_cd = FPS * 3
		
		## windrun
		self.windrun_cd = FPS * 6
		self.windrun_duration = FPS * 3
		self.windrun_boost = 0.3
		self.windrun_active = 0
		
		## focusfire
		self.focusfire_cd = FPS * 3
		self.focusfire_duration = FPS * 12
		self.focusfire_boost = 2
		self.focusfire_active = 0

		# creep init stats ------------------------------------- #
		self.creep_width = 60
		self.creep_height = 60
		self.creep_collision_width = 40
		self.creep_collision_height = 40

		self.creep_max_health = 550
		self.creep_current_health = 550
		self.creep_current_health_percentage = round(\
			self.creep_current_health / self.creep_max_health)
		# self.creep_max_mana = 345
		# self.creep_current_mana = 345
		# self.creep_current_mana_percentage = round(\
		# 	self.creep_current_mana / self.creep_max_mana)

		self.creep_movement_speed = 315 # 315
		self.creep_damage = 19
		self.creep_attack_interval = FPS

	def update(self):
		# hero stats update ------------------------------------- #
		# health and mana percentage 
		self.hero_current_health_percentage = \
			self.hero_current_health / self.hero_max_health

		self.hero_current_mana_percentage = \
			self.hero_current_mana / self.hero_max_mana

		# hero attack speed 
		self.hero_attack_interval_base = self.hero_attack_interval

		# hero movement speed 
		self.hero_movement_speed_base = hero_movement_speed
		self.hero_movement_speed_boost = (self.windrun_active * self.windrun_boost) 
		self.hero_movement_speed = self.hero_movement_speed_base * (1 + self.hero_movement_speed_boost)


		# old frames go down here
		self.old_hero_max_health = self.hero_max_health


		# creep stats update ------------------------------------- #

		# arrow stats update ------------------------------------- #
