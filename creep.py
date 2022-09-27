import pygame, math
from random import random
from setting import *

class CREEP(pygame.sprite.Sprite):
	def __init__(self, groups, hero) -> None:
		super().__init__(groups)

		# init stat
		self.hero = hero

		# position
		init_distance_with_hero = 500
		starting_aug = 2*3.14*random()

		self.pos_relative_to_hero = pygame.math.Vector2()
		self.pos_relative_to_hero.x = init_distance_with_hero * math.cos(starting_aug)
		self.pos_relative_to_hero.y = init_distance_with_hero * math.sin(starting_aug)
		
		self.pos = pygame.math.Vector2()
		self.pos.x = self.hero.pos.x + self.pos_relative_to_hero.x
		self.pos.y = self.hero.pos.y + self.pos_relative_to_hero.y

		# graphics
		self.image = pygame.Surface((CREEP_WIDTH, CREEP_HEIGHT)).convert_alpha()
		self.image.fill(RED)
		self.rect = self.image.get_rect(center=self.pos)
		self.old_rect = self.rect.copy()

		# movement
		# self.vector_to_hero = pygame.math.Vector2()
		self.direction = pygame.math.Vector2()
		self.movement_speed = CREEP_MOVEMENT_SPEED

	def move_to_hero(self):
		self.direction.x = self.hero.pos.x - self.pos.x
		self.direction.y = self.hero.pos.y - self.pos.y

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.pos.x += self.direction.x * self.movement_speed * self.dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.movement_speed * self.dt
		self.rect.y = round(self.pos.y)

		

	def update(self, dt):

		# dt and old_rect -------------------------------------------------------------------- #
		self.dt = dt
		self.old_rect = self.rect.copy()

		# movement --------------------------------------------------------------------------- #
		self.move_to_hero()

		pass