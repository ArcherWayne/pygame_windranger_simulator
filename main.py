# module importing
from ctypes.wintypes import HMODULE
import pygame, sys, time
from setting import *

# function importing
from debug import debug
from me_camera_base_camera import CameraGroup
# from special_effects import DAMAGE_NUMBERS
from UIgroup import UIGroup
from random import randint


# entity importing
from hero import HERO
from tree import TREE
from creep import CREEP
from cursor import CURSOR

# from hero import PLAYER # debug use

class MAINGAME:
	def __init__(self):
		## pygame setup

		pygame.init()
		self.screen = pygame.display.set_mode(WINDOW_SIZE)
		pygame.display.set_caption('windranger_simulator')
		pygame.display.set_icon(pygame.image.load('assets/dota2.png'))
		pygame.mouse.set_visible(False)
		# background_surface = pygame.transform.scale(
		#     pygame.image.load('assets/background/ground.png').convert(), (setting.WIN_WIDTH, setting.WIN_HEIGTH))
		# background_rect = background_surface.get_rect(center=(setting.WIN_WIDTH / 2, setting.WIN_HEIGTH / 2))
		self.clock = pygame.time.Clock()

# group setup ----------------------------------------------------------------------------------------------- #
		self.camera_group = CameraGroup()

		self.hero_group = pygame.sprite.GroupSingle()
		self.creep_group = pygame.sprite.Group()
		self.tree_group = pygame.sprite.Group()

		self.arrow_group = pygame.sprite.Group()

# class setup
		# class = Class()
		self.hero = HERO([self.camera_group, self.hero_group], self.creep_group, self.camera_group, self.arrow_group)


		self.ui_group = UIGroup(self.hero_group, self.camera_group, self.arrow_group)


# user event setting
		self.creep_enemy_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.creep_enemy_timer, 3000)

# attribute setup
		self.cursor = CURSOR()
		self.mouse_pos = (0, 0)
		self.last_time = time.time()
		self.start_time = time.time()
		self.frames = 0
		self.game_active = True

		# hold to shoot mechanics
		# self.isshooting = 0
		# self.holding_frame = HERO_ATTACK_INTERVAL - 1


	# init finish ---------------------------------------------------------------------------------------- # 

	def generate_trees(self):
		for i in range(20):
			random_x = randint(1000,2000)
			random_y = randint(1000,2000)
			TREE((random_x,random_y),self.camera_group)


	def game_loop(self):
		while True:
			self.clock.tick(FPS)
			# delta time    ------------------------------------------------------------------------------------- #
			dt = time.time() - self.last_time
			self.last_time = time.time()
			
			# event loop    ------------------------------------------------------------------------------------- #
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
					pygame.quit()
					sys.exit()

				if event.type == self.creep_enemy_timer:
					self.camera_group.add(CREEP([self.camera_group, self.creep_group], self.creep_group, \
						self.hero, self.hero.arrow_group, self.camera_group))

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
					if event.key == pygame.K_2:
						self.hero.use_skill_powershot(self.mouse_pos)

			# game loop    ---------------------------------------------------------------------------------- #
			if self.game_active:

				# 按键长按管理部分 ----------------------------- #
				mouse_pressed_list = pygame.mouse.get_pressed(num_buttons=3)
				if mouse_pressed_list[2]:
					self.hero.shoot_arrow(self.mouse_pos)


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
				debug(self.creep_group.sprites())
				debug(self.camera_group.sprites(), y = 30, info_name='camera_group')
				debug(len(self.arrow_group.sprites()), y = 50, info_name='len(arrow_group)')
				debug(str(time.time()-self.start_time), y = 70)

				self.frames += 1
				debug(str(self.frames), y = 90)

				pygame.display.update()


if __name__ == "__main__":
	main_game = MAINGAME()


	# init functions
	main_game.generate_trees()

	# game loop
	main_game.game_loop()

