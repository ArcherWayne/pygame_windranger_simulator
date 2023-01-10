print("game start!")

# module importing
import pygame, sys, time
from Config.setting import *

# function importing
from debug import debug
from Camera.me_camera_base_camera import CameraGroup
from UI.UIgroup import UIGroup
from random import randint


# entity importing
from Units.hero import HERO
from Units.tree import TREE
from Units.creep import CREEP
from Units.cursor import CURSOR

# skill pool
from Skills.pool import skill_pool

class MAINGAME:
	def __init__(self):
		## pygame setup

		self.stats_manager = STAT_MANAGER()

		pygame.init()
		print("pygame initialized!")
		self.screen = pygame.display.set_mode(WINDOW_SIZE)
		pygame.display.set_caption('windranger_simulator')
		pygame.display.set_icon(pygame.image.load('assets/dota2.png'))
		pygame.mouse.set_visible(False)
		self.clock = pygame.time.Clock()

# group setup ----------------------------------------------------------------------------------------------- #
		self.camera_group = CameraGroup(self.stats_manager)
		self.hero_group = pygame.sprite.GroupSingle()
		self.creep_group = pygame.sprite.Group()
		self.tree_group = pygame.sprite.Group()
		self.arrow_group = pygame.sprite.Group()
		self.attri_item_group = pygame.sprite.Group()
		self.cursor = CURSOR()


# class setup
		self.hero = HERO([self.camera_group, self.hero_group], self.creep_group, self.camera_group, self.arrow_group, self.stats_manager)
		self.ui_group = UIGroup(self.hero_group, self.camera_group, self.arrow_group, self.stats_manager)
		self.hero.install_skills()


# user event setting
		self.creep_enemy_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.creep_enemy_timer, 1000)


# attribute setup
		self.mouse_pos = (0, 0)
		self.last_time = time.time()
		self.start_time = time.time()
		self.frames = 0
		self.game_active = True


	# init finish ---------------------------------------------------------------------------------------- # 

	def generate_trees(self):
		for i in range(30):
			random_x = randint(500,5000)
			random_y = randint(500,5000)
			TREE((random_x,random_y),self.camera_group)


	def game_loop(self):
		while True:
			self.clock.tick(FPS)
			# delta time    ------------------------------------------------------------------------------------- #
			dt = time.time() - self.last_time
			self.last_time = time.time()
			self.frames += 1

			# event loop    ------------------------------------------------------------------------------------- #
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
					pygame.quit()
					sys.exit()

				if event.type == self.creep_enemy_timer:
					self.camera_group.add(CREEP([self.camera_group, self.creep_group], self.creep_group, \
						self.hero, self.hero.arrow_group, self.camera_group, self.attri_item_group,self.stats_manager))

				# mouse action ------------------------------------------------------------------ #
				if event.type == pygame.MOUSEMOTION:
					self.mouse_pos = event.pos

				if event.type == pygame.MOUSEBUTTONDOWN:
					# 这个只管down的一瞬间
					self.mouse_down_pos = event.pos
					self.mouse_down_button = event.button

					if self.mouse_down_button == 1:
						pass

					if self.mouse_down_button == 2:
						pass

					if self.mouse_down_button == 3:
						pass

				if event.type == pygame.MOUSEBUTTONUP:
					self.mouse_up_pos = event.pos
					self.mouse_up_button = event.button

					if self.mouse_up_button == 1:
						pass

					if self.mouse_up_button == 2:
						pass

					if self.mouse_up_button == 3:
						pass

				# keyboard action --------------------------------------------------------------------------- #
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					# use skill ----------------------------------------------- #
					if event.key == pygame.K_1:
						# self.hero.use_skill_shackleshot()
						self.hero.use_skill('Shackle Shot')

					if event.key == pygame.K_2:
						self.hero.use_skill_powershot(self.mouse_pos)

					if event.key == pygame.K_3:
						self.hero.use_skill_windrun()

					if event.key == pygame.K_4:
						self.hero.use_skill('Gale Force')

					if event.key == pygame.K_5:
						self.hero.use_skill_focusfire()

					if event.key == pygame.K_k:	# debug key
						
						for sprite in self.creep_group.sprites():
							sprite.health = -1
					# use skill end ------------------------------------------- #


			# game loop    ---------------------------------------------------------------------------------- #
			if self.game_active:

				self.active_time = time.time() - self.start_time

				# 按键长按管理部分 ----------------------------- #
				mouse_pressed_list = pygame.mouse.get_pressed(num_buttons=3)
				if mouse_pressed_list[2]:
					self.hero.shoot_arrow(self.mouse_pos)

				self.stats_manager.update()
				skill_pool.update()
				self.screen.fill(BLACK)
				self.camera_group.update(dt)
				self.camera_group.custom_draw(self.hero)
				self.camera_group.show_absolute_vector(self.hero)
				self.camera_group.show_collision_area()
				self.ui_group.update()
				self.ui_group.ui_draw()

				self.cursor.update(self.mouse_pos)
				self.cursor.draw()

				# debug space
				debug(self.active_time)
				pygame.display.update()


if __name__ == "__main__":
	main_game = MAINGAME()

	# init functions
	main_game.generate_trees()

	# game loop
	main_game.game_loop()

