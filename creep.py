import pygame
from setting import *

class CREEP(pygame.sprite.Sprite):
	def __init__(self, *groups, hero) -> None:
		super().__init__(*groups)

		# init stat
		self.hero = hero

		# position
		self.pos = pygame.math.Vector2()
		# FIXME: 添加随机位置生成: 在屏幕外面

		# graphics
		self.surf = pygame.Surface((CREEP_WIDTH, CREEP_HEIGHT)).convert_alpha()
		self.surf.fill(RED)
		self.rect = self.surf.get_rect(topleft=self.pos)
		self.old_rect = self.rect.copy()

		# movement
		self.direction = pygame.math.Vector2()
		self.movement_speed = 150

	def move_to_hero(self):
		pass
		# FIXME: 从剑圣模拟器粘贴过来


	def update(self, dt):
		self.dt = dt
		self.old_rect = self.rect.copy()
		pass