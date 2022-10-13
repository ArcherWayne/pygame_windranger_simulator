import pygame, sys
from setting import *
from PIL import Image



class UIGroup(pygame.sprite.Group):
	def __init__(self, hero_group, creep_group, arrow_group):
		super().__init__()

		self.display_surf = pygame.display.get_surface()

		self.hero = hero_group.sprite
		self.creep_group = creep_group
		self.arrow_group = arrow_group

		self.skill_number = 4

		self.windows_size = WINDOW_SIZE

		# health_mana_bar_size
		self.hp_mn_bar_size = (self.windows_size[0]*3/14, self.windows_size[1]*6/80)
		self.hp_mn_bar_midtop = (self.windows_size[0]/2, self.windows_size[1]*73/80)

		self.health_percentage = 100
		self.mana_percentage = 100

		self.hp_mn_bar_background_surf = pygame.Surface(self.hp_mn_bar_size)
		self.hp_mn_bar_background_surf.fill(BLACK)
		self.hp_mn_bar_background_rect = self.hp_mn_bar_background_surf.get_rect(midtop = self.hp_mn_bar_midtop)

		self.hp_bar_size = (self.hp_mn_bar_size[0] - 4, 0.5*self.hp_mn_bar_size[1] - 4)

		# skills
		self.update_skill_number(self.skill_number)

		# items
		# 绘制九个放置道具的黑色背景
		self.item_background_ratio = 131/96
		self.item_background_topleft_1 = (self.skill_background_topleft_1[0] + self.hp_mn_bar_size[0] + self.windows_size[0]/100, self.skill_background_topleft_1[1])
		self.item_background_height = round((self.windows_size[1] - self.item_background_topleft_1[1])/3 - (self.windows_size[1] - self.hp_mn_bar_background_rect.bottomleft[1])/3)
		self.item_background_width = round(self.item_background_ratio * self.item_background_height)
		self.item_background_surf_size = (round(0.95*self.item_background_width), round(0.95*self.item_background_height))

		self.item_background_surf = pygame.Surface(self.item_background_surf_size)
		self.item_background_surf.fill(BLACK)

		self.item_background_rect_list = []

		for i in range(3):
			for ii in range(3):
				self.item_background_rect_list.append(self.item_background_surf.get_rect(topleft = \
					(self.item_background_topleft_1[0]+ii*self.item_background_width, self.item_background_topleft_1[1]+i*self.item_background_height)))

		# mugshot
		mugshot = Image.open('assets/graphics/windranger/windranger_mugshot.png')
		# mugshot_width = mugshot.width       #图片的宽
		# mughsot_height = mugshot.height      #图片的高
		mugshot_ratio = mugshot.width/mugshot.height
		mugshot.close()
		mugshot_height = self.windows_size[1] - self.item_background_topleft_1[1]
		mugshot_width = round(mugshot_ratio * mugshot_height)
		self.wr_mugshot_surf = pygame.transform.scale(pygame.image.load('assets/graphics/windranger/windranger_mugshot.png').convert_alpha(), (mugshot_width, mugshot_height))
		self.wr_mugshot_rect = self.wr_mugshot_surf.get_rect(bottomright = \
			(self.hp_mn_bar_background_rect.bottomleft[0] - self.windows_size[0]/100, self.hp_mn_bar_background_rect.bottomleft[1]))



	def update_skill_number(self, skill_number):
		# 每次更新了技能数量， 就会重新计算各个技能的位置
		self.skill_background_rect_list = []
		self.skill_number = skill_number

		self.hp_bar_length_dived_by_skill_number = round(self.hp_mn_bar_size[0]/self.skill_number)

		self.skill_background_length = round((self.hp_bar_length_dived_by_skill_number)*0.98)
		self.skill_slot_length = round((self.hp_bar_length_dived_by_skill_number)*0.95)
		self.skill_background_topleft_1 = (self.hp_mn_bar_background_rect.topleft[0], self.hp_mn_bar_background_rect.topleft[1] - self.hp_bar_length_dived_by_skill_number)

		self.sklll_background_surf = pygame.Surface((self.skill_background_length, self.skill_background_length))

		for i in range(self.skill_number): # i = 0, 1, 2, ... self.skill_number - 1
			self.skill_background_rect_list.append(self.sklll_background_surf.get_rect(topleft = \
				(self.skill_background_topleft_1[0] + i*(self.hp_bar_length_dived_by_skill_number), self.skill_background_topleft_1[1])))



	def draw_health_mana_bar(self):
		self.display_surf.blit(self.hp_mn_bar_background_surf, self.hp_mn_bar_background_rect)

		self.hp_bar_surf = pygame.Surface((round(self.hp_bar_size[0]*self.health_percentage), self.hp_bar_size[1]))
		self.hp_bar_surf.fill(RED)
		self.hp_bar_rect = self.hp_bar_surf.get_rect(topleft = \
			(self.hp_mn_bar_background_rect.topleft[0] - 2, self.hp_mn_bar_background_rect.topleft[1] - 2))
		self.display_surf.blit(self.hp_bar_surf, self.hp_bar_rect)

		self.mn_bar_surf = pygame.Surface((round(self.hp_bar_size[0]*self.mana_percentage), self.hp_bar_size[1]))
		self.mn_bar_surf.fill(BLUE)
		self.mn_bar_rect = self.mn_bar_surf.get_rect(topleft = \
			(self.hp_mn_bar_background_rect.topleft[0] - 2, self.hp_mn_bar_background_rect.topleft[1] + 0.5*self.hp_mn_bar_size[1] - 2))
		self.display_surf.blit(self.mn_bar_surf, self.mn_bar_rect)



	def draw_skills(self):
		# 目前只画了background
		for i in range(self.skill_number):
			self.display_surf.blit(self.sklll_background_surf, self.skill_background_rect_list[i])

	def draw_items(self):
		# 目前只画了background
		for rect in self.item_background_rect_list:
			self.display_surf.blit(self.item_background_surf, rect)

	def draw_mugshot(self):
		self.display_surf.blit(self.wr_mugshot_surf, self.wr_mugshot_rect)


	def update(self): 
		if self.hero.current_health > 0 and self.hero.current_mana > 0:
			self.health_percentage = self.hero.current_health / self.hero.max_health
			self.mana_percentage = self.hero.current_mana / self.hero.max_mana
		else: 
			self.health_percentage = 0
			self.mana_percentage = 0

	def ui_draw(self):
		self.draw_health_mana_bar()
		self.draw_skills()
		self.draw_items()
		self.draw_mugshot()