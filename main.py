import pygame, sys, time
from setting import *
from debug import debug
from me_camera_base_camera import CameraGroup
from hero import HERO

class MAINGAME:
	def __init__(self):
		## pygame setup

		pygame.init()
		self.screen = pygame.display.set_mode(window_size)
		pygame.display.set_caption('windranger_simulator')
		pygame.display.set_icon(pygame.image.load('assets/dota2.png'))
		# background_surface = pygame.transform.scale(
		#     pygame.image.load('assets/background/ground.png').convert(), (setting.WIN_WIDTH, setting.WIN_HEIGTH))
		# background_rect = background_surface.get_rect(center=(setting.WIN_WIDTH / 2, setting.WIN_HEIGTH / 2))
		self.clock = pygame.time.Clock()
		# font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

# group setup ----------------------------------------------------------------------------------------------- #
		self.camera_group = CameraGroup()
		# self.all_sprites = pygame.sprite.Group()
		# self.collision_sprites = pygame.sprite.Group()

# class setup
		# class = Class()
		self.hero = HERO(self.camera_group)

# attribute setup
		self.last_time = time.time()
		self.game_active = True

	def game_loop(self):
		while True:
			self.clock.tick(FPS)
			# delta time    ------------------------------------------------------------------------------------- #
			last_time = time.time()
			dt = time.time() - last_time

			# event loop    ------------------------------------------------------------------------------------- #
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
					pygame.quit()
					sys.exit()

			if self.game_active:
				self.screen.fill(WHITE)
				# screen.blit(background_surface, background_rect)
				# self.all_sprites.update()
				# self.all_sprites.draw(self.screen)

			self.hero.update(dt)

			self.camera_group.custom_draw(self.hero)
			debug(self.hero.rect)
			debug(self.hero.direction, y = 30)
			pygame.display.update()

	def update(self):
		self.game_loop()

if __name__ == "__main__":
	main_game = MAINGAME()

	# game loop
	main_game.update()

