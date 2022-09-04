import pygame
from random import randint
from setting import *

class CREEP(pygame.sprite.Sprite):
	def __init__(self, *groups, hero) -> None:
		super().__init__(*groups)

		# init stat
		self.hero = hero

		# position
		self.pos = pygame.math.Vector2()
		self.pos.x = 
		self.pos.y = 
		self.pos_relto_hero = pygame.math.Vector2()
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

		# dt and old_rect -------------------------------------------------------------------- #
		self.dt = dt
		self.old_rect = self.rect.copy()

		# update the pos relative to self.hero ----------------------------------------------- #
		self.pos_relto_hero.x = self.pos.x - self.hero.pos.x
		self.pos_relto_hero.y = self.pos.y - self.hero.pos.y

		pass