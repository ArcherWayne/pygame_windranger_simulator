import pygame, sys
from setting import *



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
		# self.skill_background_length = (self.hp_mn_bar_size[0]/self.skill_number)*0.98
		# self.skill_slot_length = (self.hp_mn_bar_size[0]/self.skill_number)*0.95
		# self.skill_background_topleft_1 = (self.hp_mn_bar_background_rect.topleft[0], self.hp_mn_bar_background_rect.topleft[1] - self.hp_mn_bar_size[0]/self.skill_number)

		# self.sklll_background_surf = pygame.Surface((self.skill_background_length, self.skill_background_length))

		# self.skill_background_rect_list = []

		# for i in range(self.skill_number): # i = 0, 1, 2, ... self.skill_number - 1
		# 	self.skill_background_rect_list.add(self.sklll_background_surf.get_rect(topleft = self.skill_background_topleft_1 + i*(self.hp_mn_bar_size[0]/self.skill_number)))


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

	def update_skill_number(self, skill_number):
		self.skill_number = skill_number

		self.hp_bar_length_dived_by_skill_number = round(self.hp_mn_bar_size[0]/self.skill_number)

		self.skill_background_length = round((self.hp_bar_length_dived_by_skill_number)*0.98)
		self.skill_slot_length = round((self.hp_bar_length_dived_by_skill_number)*0.95)
		self.skill_background_topleft_1 = (self.hp_mn_bar_background_rect.topleft[0], self.hp_mn_bar_background_rect.topleft[1] - self.hp_bar_length_dived_by_skill_number)

		self.sklll_background_surf = pygame.Surface((self.skill_background_length, self.skill_background_length))

		self.skill_background_rect_list = []

		for i in range(self.skill_number): # i = 0, 1, 2, ... self.skill_number - 1
			self.skill_background_rect_list.append(self.sklll_background_surf.get_rect(topleft = \
				(self.skill_background_topleft_1[0] + i*(self.hp_bar_length_dived_by_skill_number), self.skill_background_topleft_1[1])))


	def draw_skills(self):
		for i in range(self.skill_number):
			self.display_surf.blit(self.sklll_background_surf, self.skill_background_rect_list[i])

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