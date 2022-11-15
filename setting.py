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
		self.skill_shackleshot_cd = FPS * 3
		
		## powershot
		self.skill_powershot_cd = FPS * 3
		
		## windrun
		self.skill_windrun_cd = FPS * 6
		self.skill_windrun_duration = FPS * 3
		self.skill_windrun_boost = 2
		self.skill_windrun_active = 0
		
		## focusfire
		self.skill_focusfire_cd = FPS * 3
		self.skill_focusfire_duration = FPS * 12
		self.skill_focusfire_boost = 10
		self.skill_focusfire_active = 0

		### cooldown frames 冷却时间
		self.hero_hit_cooldown_frame = 0 # 英雄接触到小兵的帧读数
		self.hero_shoot_arrow_cooldown_frame = 0 # attack cd

		self.skill_shackleshot_cooldown_frame = 0 # shackleshot cd
		self.skill_powershot_cooldown_frame = 0 # powershot cd
		self.skill_windrun_cooldown_frame = 0
		self.skill_focusfire_cooldown_frame = 0

		### count down frames 持续时间
		self.skill_windrun_countdown_frame = 0
		self.skill_focusfire_countdown_frame = 0

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

		self.creep_movement_speed = 31 # 315
		self.creep_damage = 19
		self.creep_attack_interval = FPS

	def update_cooldowns(self, cooldown_frame, cooldown_interval):
		if cooldown_frame > 0:
			cooldown_frame += 1
		if cooldown_frame > cooldown_interval:
			cooldown_frame = 0

		return cooldown_frame

	def check_active(self):
		if self.skill_windrun_countdown_frame:
			self.skill_windrun_active = 1
		else: 
			self. skill_windrun_active = 0

		if self.skill_focusfire_countdown_frame:
			self.skill_focusfire_active = 1
		else: 
			self. skill_focusfire_active = 0


	def update(self):
		self.check_active()
		# hero stats update ------------------------------------- #
		# health and mana percentage 
		self.hero_current_health_percentage = \
			self.hero_current_health / self.hero_max_health

		self.hero_current_mana_percentage = \
			self.hero_current_mana / self.hero_max_mana

		# hero attack speed 
		self.hero_attack_interval_base =  2
		self.hero_attack_interval_boost = (self.skill_focusfire_active * self.skill_focusfire_boost)
		self.hero_attack_interval = FPS / round(self.hero_attack_interval_base + self.hero_attack_interval_boost)

		# hero movement speed 
		self.hero_movement_speed_base = 290
		self.hero_movement_speed_boost = (self.skill_windrun_active * self.skill_windrun_boost) 
		self.hero_movement_speed = self.hero_movement_speed_base * (1 + self.hero_movement_speed_boost)


		# update cooldowns
		## 主动攻击间隔
		self.hero_shoot_arrow_cooldown_frame = self.update_cooldowns(self.hero_shoot_arrow_cooldown_frame, self.hero_attack_interval)
		## 被攻击间隔
		self.hero_hit_cooldown_frame = self.update_cooldowns(self.hero_hit_cooldown_frame, self.creep_attack_interval)
		## 技能cd
		self.skill_shackleshot_cooldown_frame = self.update_cooldowns(self.skill_shackleshot_cooldown_frame, self.skill_shackleshot_cd)
		self.skill_powershot_cooldown_frame = self.update_cooldowns(self.skill_powershot_cooldown_frame, self.skill_powershot_cd)
		self.skill_windrun_cooldown_frame = self.update_cooldowns(self.skill_windrun_cooldown_frame, self.skill_windrun_cd)
		self.skill_focusfire_cooldown_frame = self.update_cooldowns(self.skill_focusfire_cooldown_frame, self.skill_focusfire_cd)
		## 技能持续时间
		self.skill_windrun_countdown_frame = self.update_cooldowns(self.skill_windrun_countdown_frame, self.skill_windrun_duration)
		self.skill_focusfire_countdown_frame = self.update_cooldowns(self.skill_focusfire_countdown_frame, self.skill_focusfire_duration)

		# old frames go down here
		self.old_hero_max_health = self.hero_max_health


		# creep stats update ------------------------------------- #

		# arrow stats update ------------------------------------- #
