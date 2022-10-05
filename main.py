# module importing
import pygame, sys, time
from setting import *

# function importing
from debug import debug
from me_camera_base_camera import CameraGroup
from random import randint

# entity importing
from hero import HERO
from tree import TREE
from creep import CREEP
from cursor import CURSOR
from arrow import ARROW
# from hero import PLAYER # debug use

class MAINGAME:
	def __init__(self):
		## pygame setup

		pygame.init()
		self.screen = pygame.display.set_mode(window_size)
		pygame.display.set_caption('windranger_simulator')
		pygame.display.set_icon(pygame.image.load('assets/dota2.png'))
		pygame.mouse.set_visible(False)
		# background_surface = pygame.transform.scale(
		#     pygame.image.load('assets/background/ground.png').convert(), (setting.WIN_WIDTH, setting.WIN_HEIGTH))
		# background_rect = background_surface.get_rect(center=(setting.WIN_WIDTH / 2, setting.WIN_HEIGTH / 2))
		self.clock = pygame.time.Clock()
		# font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

# group setup ----------------------------------------------------------------------------------------------- #
		self.camera_group = CameraGroup()

		self.hero_group = pygame.sprite.GroupSingle()
		self.creep_group = pygame.sprite.Group()
		self.tree_group = pygame.sprite.Group()

		self.arrow_group = pygame.sprite.Group()

# class setup
		# class = Class()
		self.hero = HERO(self.camera_group)
		# self.hero = PLAYER((window_size[0]/2, window_size[1]/2), CameraGroup) # debug use

# user event setting
		self.creep_enemy_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.creep_enemy_timer, 1000)

		# self.shoot_arrow = pygame.USEREVENT + 1

# attribute setup
		self.cursor = CURSOR()
		self.mouse_pos = (0, 0)
		self.last_time = time.time()
		self.start_time = time.time()
		self.frames = 0
		self.game_active = True

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
					self.camera_group.add(CREEP([self.camera_group, self.creep_group], self.creep_group, self.hero))

				if event.type == pygame.MOUSEMOTION:
					self.mouse_pos = event.pos

				if event.type == pygame.MOUSEBUTTONDOWN:
					self.mouse_click_pos = event.pos
					self.mouse_click_button = event.button
					# mouse_action(self.mouse_pos, self.mouse_click_pos, self.mouse_click_button)
					if self.mouse_click_button == 1:
						aim_direction = pygame.math.Vector2()
						aim_direction.x = self.mouse_click_pos[0] - WIN_WIDTH/2
						aim_direction.y = self.mouse_click_pos[1] - WIN_HEIGHT/2
						ARROW([self.camera_group, self.arrow_group], aim_direction, ARROW_SPEED, ARROW_DAMAGE, self.hero.pos, self.creep_group)

					# FIXME : 方向计算有问题

					if self.mouse_click_button == 2:
						pass

					if self.mouse_click_button == 3:
						pass
			
			# game loop    ---------------------------------------------------------------------------------- #
			if self.game_active:
				self.screen.fill(BLACK)
				# screen.blit(background_surface, background_rect)
				# self.all_sprites.update()
				# self.all_sprites.draw(self.screen)
				# self.hero.update(dt)
				self.camera_group.update(dt)
				self.camera_group.custom_draw(self.hero)
				self.camera_group.show_absolute_vector(self.hero)
				self.camera_group.show_collision_area()

				self.cursor.update(self.mouse_pos)
				self.cursor.draw()

				# debug space
				# debug(self.hero.pos, info_name="self.hero.pos")
				# debug(self.camera_group.ground_rect.topleft, y = 30, info_name="self.camera_group.ground_rect.topleft")
				# debug(self.camera_group.offset, y = 50, info_name="self.camera_group.offset")
				# debug(self.creep_group.Sprites.rect)
				debug(self.creep_group.sprites())
				debug(self.camera_group.sprites(), y = 30, info_name='camera_group')
				debug(len(self.arrow_group.sprites()), y = 50, info_name='len(arrow_group)')
				debug(str(time.time()-self.start_time), y = 70)
				self.frames += 1
				debug(str(self.frames), y = 90)
				# debug(self.hero.rect.topleft, x=self.hero.rect.topleft[0], y=self.hero.rect.topleft[1])
				pygame.display.update()


class GAMEMANAGER:
	def __init__(self):
		pass

	def update(self):
		pass


if __name__ == "__main__":
	main_game = MAINGAME()
	game_manager = GAMEMANAGER()

	# init functions
	main_game.generate_trees()

	# game loop
	main_game.game_loop()

