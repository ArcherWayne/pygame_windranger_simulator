import pygame
import math
from random import random
from setting import *

class DAMAGE_NUMBERS(pygame.sprite.Sprite):

	def __init__(self, groups, number, pos, if_crit):
		super().__init__(groups)

		self.type = 'DAMAGE_NUMBERS'

		self.number = number
		self.pos = pygame.math.Vector2()
		self.pos.x = pos.x
		self.pos.y = pos.y

		self.if_crit = if_crit

		self.existed_frame = 0

		self.font = FONT
		self.image = self.font.render(str(self.number), True, WHITE)
		self.rect = self.image.get_rect(topleft = self.pos)

		self.direction = pygame.math.Vector2()
		self.direction.y = -1
		self.direction.x = -1 + 2*random()

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.movement_speed = 60


	def update(self, dt):
		self.pos.x += self.direction.x * self.movement_speed * dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.movement_speed * dt
		self.rect.y = round(self.pos.y)
		
		# self kill count down
		self.existed_frame += 1

		if self.existed_frame > FPS/2:
			self.kill()



