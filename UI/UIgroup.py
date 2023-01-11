import pygame
from Config.setting import *
from PIL import Image
from Skills.pool import skill_pool


class UIGroup(pygame.sprite.Group):
	def __init__(self, hero_group, creep_group, arrow_group, stats_manager):
		super().__init__()

		self.display_surf = pygame.display.get_surface()

		self.hero = hero_group.sprite
		self.creep_group = creep_group
		self.arrow_group = arrow_group

		self.skill_number = 5

		self.windows_size = WINDOW_SIZE

		self.stats_manager = stats_manager

		# health_mana_bar_size
		self.hp_mn_bar_size = (self.windows_size[0]*3/14, self.windows_size[1]*6/80)
		self.hp_mn_bar_midtop = (self.windows_size[0]/2, self.windows_size[1]*73/80)

		# self.health_percentage = 100
		# self.mana_percentage = 100

		self.hp_mn_bar_background_surf = pygame.Surface(self.hp_mn_bar_size)
		self.hp_mn_bar_background_surf.fill(BLACK)
		self.hp_mn_bar_background_rect = self.hp_mn_bar_background_surf.get_rect(midtop = self.hp_mn_bar_midtop)

		self.hp_bar_size = (self.hp_mn_bar_size[0] - 4, 0.5*self.hp_mn_bar_size[1] - 4)

		# skills
		self.update_skill_number(self.skill_number)

		self.skill_shackleshot_icon_image = pygame.transform.scale(pygame.image.load('assets/graphics/icons/skills/skill_shackleshot.png').convert_alpha(), \
			(self.skill_slot_length, self.skill_slot_length))
		self.skill_powershot_icon_image = pygame.transform.scale(pygame.image.load('assets/graphics/icons/skills/skill_powershot.png').convert_alpha(), \
			(self.skill_slot_length, self.skill_slot_length))
		self.skill_windrun_icon_image = pygame.transform.scale(pygame.image.load('assets/graphics/icons/skills/skill_windrun.png').convert_alpha(), \
			(self.skill_slot_length, self.skill_slot_length))
		self.skill_galeforce_icon_image = pygame.transform.scale(pygame.image.load('assets/graphics/icons/skills/skill_galeforce.png').convert_alpha(), \
			(self.skill_slot_length, self.skill_slot_length))
		self.skill_focusfire_icon_image = pygame.transform.scale(pygame.image.load('assets/graphics/icons/skills/skill_focusfire.png').convert_alpha(), \
			(self.skill_slot_length, self.skill_slot_length))

		self.skill_icon_list = [self.skill_shackleshot_icon_image, self.skill_powershot_icon_image, self.skill_windrun_icon_image, self.skill_galeforce_icon_image, self.skill_focusfire_icon_image]

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

		self.hp_bar_surf = pygame.Surface((round(self.hp_bar_size[0]*self.stats_manager.hero_current_health_percentage), self.hp_bar_size[1]))
		self.hp_bar_surf.fill(RED)
		self.hp_bar_rect = self.hp_bar_surf.get_rect(topleft = \
			(self.hp_mn_bar_background_rect.topleft[0]+2, self.hp_mn_bar_background_rect.topleft[1]+2))
		self.display_surf.blit(self.hp_bar_surf, self.hp_bar_rect)

		self.mn_bar_surf = pygame.Surface((round(self.hp_bar_size[0]*self.stats_manager.hero_current_mana_percentage), self.hp_bar_size[1]))
		self.mn_bar_surf.fill(BLUE)
		self.mn_bar_rect = self.mn_bar_surf.get_rect(topleft = \
			(self.hp_mn_bar_background_rect.topleft[0]+2, self.hp_mn_bar_background_rect.topleft[1] + 0.5*self.hp_mn_bar_size[1]+2))
		self.display_surf.blit(self.mn_bar_surf, self.mn_bar_rect)


	def draw_health_mana_number(self):
		self.hero_hpnumber_surf = FONT.render(
			str(int(self.stats_manager.hero_current_health))+'/'+str(int(self.stats_manager.hero_max_health)), 
			True, WHITE
			)
		self.hero_hpnumber_rect = self.hero_hpnumber_surf.get_rect(center = \
			(self.hp_mn_bar_background_rect.centerx,self.hp_bar_rect.centery))

		self.display_surf.blit(self.hero_hpnumber_surf, self.hero_hpnumber_rect)

		self.hero_mnnumber_surf = FONT.render(
			str(self.stats_manager.hero_current_mana)+'/'+str(self.stats_manager.hero_max_mana), 
			True, WHITE
			)
		self.hero_mnnumber_rect = self.hero_mnnumber_surf.get_rect(center = \
			(self.hp_mn_bar_background_rect.centerx,self.mn_bar_rect.centery))

		self.display_surf.blit(self.hero_mnnumber_surf, self.hero_mnnumber_rect)


	def draw_health_mana_recover(self):
		font_1 = makesizefont(14)
		hp_recover_str = ("%.2f" % self.stats_manager.hero_health_recover_per_sec)
		self.hero_hprecovernumber_surf = font_1.render(
			# str(int(self.stats_manager.hero_health_recover_per_sec)), True, WHITE
			"+"+hp_recover_str, True, WHITE
		)
		self.hero_hprecovernumber_rect = self.hero_hprecovernumber_surf.get_rect(
			midright = (self.hp_mn_bar_background_rect.right - 4, \
				self.hp_mn_bar_background_rect.topright[1]+0.25*self.hp_mn_bar_background_rect.height)
		)
		self.display_surf.blit(self.hero_hprecovernumber_surf, self.hero_hprecovernumber_rect)

		mn_recover_str = ("%.2f" % self.stats_manager.hero_mana_recover_per_sec)
		self.hero_mnrecovernumber_surf = font_1.render(
			# str(int(self.stats_manager.hero_mana_recover_per_sec)), True, WHITE
			"+"+mn_recover_str, True, WHITE
		)
		self.hero_mnrecovernumber_rect = self.hero_mnrecovernumber_surf.get_rect(
			midright = (self.hp_mn_bar_background_rect.right - 4, \
				self.hp_mn_bar_background_rect.topright[1]+0.75*self.hp_mn_bar_background_rect.height)
			
		)
		self.display_surf.blit(self.hero_mnrecovernumber_surf, self.hero_mnrecovernumber_rect)

	def draw_skills(self):
		for i in range(self.skill_number):
			self.display_surf.blit(self.sklll_background_surf, self.skill_background_rect_list[i])

		# skill icons
		if self.skill_number == 4:
			self.display_surf.blit(self.skill_shackleshot_icon_image, self.skill_background_rect_list[0])
			self.display_surf.blit(self.skill_powershot_icon_image, self.skill_background_rect_list[1])
			self.display_surf.blit(self.skill_windrun_icon_image, self.skill_background_rect_list[2])
			self.display_surf.blit(self.skill_focusfire_icon_image, self.skill_background_rect_list[3])

		elif self.skill_number == 5:
			self.display_surf.blit(self.skill_shackleshot_icon_image, self.skill_background_rect_list[0])
			self.display_surf.blit(self.skill_powershot_icon_image, self.skill_background_rect_list[1])
			self.display_surf.blit(self.skill_windrun_icon_image, self.skill_background_rect_list[2])
			self.display_surf.blit(self.skill_galeforce_icon_image, self.skill_background_rect_list[3])
			self.display_surf.blit(self.skill_focusfire_icon_image, self.skill_background_rect_list[4])


	def draw_skills_cooldown(self):
		if self.stats_manager.skill_powershot_cooldown_frame:
			skill_powershot_cooldwon_size_ratio = (1-self.stats_manager.skill_powershot_cooldown_frame/self.stats_manager.skill_powershot_cd)
			skill_powershot_cooldown_size_width = self.skill_background_length
			skill_powershot_cooldown_size_height = round(skill_powershot_cooldwon_size_ratio*self.skill_background_length)

			self.powershot_cooldown_surface = pygame.Surface((skill_powershot_cooldown_size_width, skill_powershot_cooldown_size_height))
			self.powershot_cooldown_surface.fill(BLACK)
			self.powershot_cooldown_surface.set_alpha(100+155*skill_powershot_cooldwon_size_ratio)
			self.powershot_cooldown_rect = self.powershot_cooldown_surface.get_rect(bottomleft=self.skill_background_rect_list[1].bottomleft)
			self.display_surf.blit(self.powershot_cooldown_surface, self.powershot_cooldown_rect)


		if self.stats_manager.skill_windrun_cooldown_frame:
			skill_windrun_cooldwon_size_ratio = (1-self.stats_manager.skill_windrun_cooldown_frame/self.stats_manager.skill_windrun_cd)
			skill_windrun_cooldown_size_width = self.skill_background_length
			skill_windrun_cooldown_size_height = round(skill_windrun_cooldwon_size_ratio*self.skill_background_length)

			self.windrun_cooldown_surface = pygame.Surface((skill_windrun_cooldown_size_width, skill_windrun_cooldown_size_height))
			self.windrun_cooldown_surface.fill(BLACK)
			self.windrun_cooldown_surface.set_alpha(100+155*skill_windrun_cooldwon_size_ratio)
			self.windrun_cooldown_rect = self.windrun_cooldown_surface.get_rect(bottomleft=self.skill_background_rect_list[2].bottomleft)
			self.display_surf.blit(self.windrun_cooldown_surface, self.windrun_cooldown_rect)

		if self.stats_manager.skill_focusfire_cooldown_frame:
			if self.skill_number == 4:
				skill_focusfire_cooldwon_size_ratio = (1-self.stats_manager.skill_focusfire_cooldown_frame/self.stats_manager.skill_focusfire_cd)
				skill_focusfire_cooldown_size_width = self.skill_background_length
				skill_focusfire_cooldown_size_height = round(skill_focusfire_cooldwon_size_ratio*self.skill_background_length)

				self.focusfire_cooldown_surface = pygame.Surface((skill_focusfire_cooldown_size_width, skill_focusfire_cooldown_size_height))
				self.focusfire_cooldown_surface.fill(BLACK)
				self.focusfire_cooldown_surface.set_alpha(100+155*skill_focusfire_cooldwon_size_ratio)
				self.focusfire_cooldown_rect = self.focusfire_cooldown_surface.get_rect(bottomleft=self.skill_background_rect_list[3].bottomleft)
				self.display_surf.blit(self.focusfire_cooldown_surface, self.focusfire_cooldown_rect)

			elif self.skill_number == 5:
				skill_focusfire_cooldown_size_ratio = (1-self.stats_manager.skill_focusfire_cooldown_frame/self.stats_manager.skill_focusfire_cd)
				skill_focusfire_cooldown_size_width = self.skill_background_length
				skill_focusfire_cooldown_size_height = round(skill_focusfire_cooldown_size_ratio*self.skill_background_length)

				self.focusfire_cooldown_surface = pygame.Surface((skill_focusfire_cooldown_size_width, skill_focusfire_cooldown_size_height))
				self.focusfire_cooldown_surface.fill(BLACK)
				self.focusfire_cooldown_surface.set_alpha(100+155*skill_focusfire_cooldown_size_ratio)
				self.focusfire_cooldown_rect = self.focusfire_cooldown_surface.get_rect(bottomleft=self.skill_background_rect_list[4].bottomleft)
				self.display_surf.blit(self.focusfire_cooldown_surface, self.focusfire_cooldown_rect)
		

		skill_galeforce = skill_pool.get_skill_by_name('Gale Force')
		if skill_galeforce != None:
			if skill_galeforce.cooldown_frame:
				skill_galeforce_cooldown_size_ratio = (1-skill_galeforce.cooldown_frame/(skill_galeforce.cooldown*FPS))
				skill_galeforce_cooldown_size_width = self.skill_background_length
				skill_galeforce_cooldown_size_height = round(skill_galeforce_cooldown_size_ratio*self.skill_background_length)

				self.galeforce_cooldown_surface = pygame.Surface((skill_galeforce_cooldown_size_width, skill_galeforce_cooldown_size_height))
				self.galeforce_cooldown_surface.fill(BLACK)
				self.galeforce_cooldown_surface.set_alpha(100+155*skill_galeforce_cooldown_size_ratio)
				self.galeforce_cooldown_rect = self.galeforce_cooldown_surface.get_rect(bottomleft=self.skill_background_rect_list[3].bottomleft)
				self.display_surf.blit(self.galeforce_cooldown_surface, self.galeforce_cooldown_rect)
				

		skill_shackleshot = skill_pool.get_skill_by_name('Shackle Shot')
		if skill_shackleshot != None:
			if skill_shackleshot.cooldown_frame:
				skill_shackleshot_cooldown_size_ratio = (1-skill_shackleshot.cooldown_frame/(skill_shackleshot.cooldown*FPS))
				skill_shackleshot_cooldown_size_width = self.skill_background_length
				skill_shackleshot_cooldown_size_height = round(skill_shackleshot_cooldown_size_ratio*self.skill_background_length)

				self.shackleshot_cooldown_surface = pygame.Surface((skill_shackleshot_cooldown_size_width, skill_shackleshot_cooldown_size_height))
				self.shackleshot_cooldown_surface.fill(BLACK)
				self.shackleshot_cooldown_surface.set_alpha(100+155*skill_shackleshot_cooldown_size_ratio)
				self.shackleshot_cooldown_rect = self.shackleshot_cooldown_surface.get_rect(bottomleft=self.skill_background_rect_list[0].bottomleft)
				self.display_surf.blit(self.shackleshot_cooldown_surface, self.shackleshot_cooldown_rect)

	def draw_items(self):
		# FIXME: 目前只画了background
		for rect in self.item_background_rect_list:
			self.display_surf.blit(self.item_background_surf, rect)


	def draw_hero_level(self):
		self.hero_level_surf = FONT.render("lvl="+str(self.stats_manager.hero_level), True, WHITE)
		self.hero_level_rect = self.hero_level_surf.get_rect(bottomright = self.wr_mugshot_rect.bottomright)

		self.display_surf.blit(self.hero_level_surf, self.hero_level_rect)


	def draw_hero_attribute(self):
		str_ratio = self.stats_manager.hero_strength/self.stats_manager.hero_total_attri_number
		agi_ratio = self.stats_manager.hero_agility/self.stats_manager.hero_total_attri_number
		int_ratio = self.stats_manager.hero_intelligence/self.stats_manager.hero_total_attri_number

		self.hero_strength_background_surf = pygame.Surface((self.item_background_surf_size[0], int(str_ratio * self.item_background_surf_size[1])))
		self.hero_agility_background_surf = pygame.Surface((self.item_background_surf_size[0], int(agi_ratio * self.item_background_surf_size[1]))) 
		self.hero_intelligence_background_surf = pygame.Surface((self.item_background_surf_size[0], int(int_ratio * self.item_background_surf_size[1])))

		self.hero_strength_background_surf.fill(('#5c0701'))
		self.hero_agility_background_surf.fill(('#0a5c01'))
		self.hero_intelligence_background_surf.fill(('#041361'))

		self.hero_strength_background_rect = self.hero_strength_background_surf.get_rect(bottomleft = self.item_background_rect_list[6].bottomleft)	
		self.hero_agility_background_rect = self.hero_agility_background_surf.get_rect(bottomleft = self.item_background_rect_list[7].bottomleft)	
		self.hero_intelligence_background_rect = self.hero_intelligence_background_surf.get_rect(bottomleft = self.item_background_rect_list[8].bottomleft)	

		self.display_surf.blit(self.hero_strength_background_surf, self.hero_strength_background_rect)
		self.display_surf.blit(self.hero_agility_background_surf, self.hero_agility_background_rect)
		self.display_surf.blit(self.hero_intelligence_background_surf, self.hero_intelligence_background_rect)

		self.hero_strength_surf = FONT.render(str(self.stats_manager.hero_strength), True, RED) 
		self.hero_agility_surf = FONT.render(str(self.stats_manager.hero_agility), True, GREEN) 
		self.hero_intelligence_surf = FONT.render(str(self.stats_manager.hero_intelligence), True, BLUE) 

		self.hero_strength_rect = self.hero_strength_surf.get_rect(center=self.item_background_rect_list[6].center)
		self.hero_agility_rect = self.hero_agility_surf.get_rect(center=self.item_background_rect_list[7].center)
		self.hero_intelligence_rect = self.hero_intelligence_surf.get_rect(center=self.item_background_rect_list[8].center)

		self.display_surf.blit(self.hero_strength_surf, self.hero_strength_rect)
		self.display_surf.blit(self.hero_agility_surf, self.hero_agility_rect)
		self.display_surf.blit(self.hero_intelligence_surf, self.hero_intelligence_rect)

	def draw_mugshot(self):
		self.display_surf.blit(self.wr_mugshot_surf, self.wr_mugshot_rect)
		
	
	def show_active_time(self):
		active_time = "Time Survived = "+str(round(self.stats_manager.active_time))
		active_time_surf = FONT.render((active_time), True, WHITE)
		active_time_rect = active_time_surf.get_rect(midtop = (WIN_WIDTH/2, 30))
		self.display_surf.blit(active_time_surf, active_time_rect)


	def update(self): 
		pass

	def ui_draw(self):
		self.draw_health_mana_bar()
		self.draw_health_mana_number()
		self.draw_health_mana_recover()
		self.draw_skills()
		self.draw_skills_cooldown()
		self.draw_items()
		self.draw_hero_attribute()
		self.draw_mugshot()
		self.draw_hero_level()
		self.show_active_time()