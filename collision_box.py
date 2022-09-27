import pygame
from setting import *

class COLLISION_BOX(pygame.sprite.Sprite):
	def __init__(self, *groups, master, collision_size):
		super().__init__(*groups)

		self.master = master
		self.collision_size = collision_size

		self.rect = pygame.Rect()
		self.pos = pygame.math.Vector2()

		self.image = pygame.Surface((self.collision_size[0], self.collision_size[1]))
		self.image.fill(COLOR_TRANSPARENT)
		self.rect = self.image.get_rect(center=self.master.rect.center)
		self.old_rect = self.rect.copy()

	def check_collision(self):
		pass

	def pos_correction(self):
		pass

	def update(self):
		self.pos = self.master.rect.center
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y


