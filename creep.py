import pygame
import math
from random import random
from setting import *
from debug import debug


class CREEP(pygame.sprite.Sprite):
	def __init__(self, groups, creep_group, hero, arrow_group) -> None:
		super().__init__(groups)
		# type
		self.type = 'creep'

		# group setting
		self.hero = hero
		self.creep_group = creep_group
		self.arrow_group = arrow_group

		# stats
		self.health = CREEP_HEALTH

		# position
		init_distance_with_hero = 500
		starting_aug = 2*3.14*random()

		self.pos_relative_to_hero = pygame.math.Vector2()
		self.pos_relative_to_hero.x = init_distance_with_hero * math.cos(starting_aug)
		self.pos_relative_to_hero.y = init_distance_with_hero * math.sin(starting_aug)

		self.pos = pygame.math.Vector2()
		self.pos.x = self.hero.pos.x + self.pos_relative_to_hero.x
		self.pos.y = self.hero.pos.y + self.pos_relative_to_hero.y


		# movement
		self.direction = pygame.math.Vector2()
		self.movement_speed = CREEP_MOVEMENT_SPEED

		self.knockback_direction = pygame.math.Vector2()
		self.knockback_acceleration = 0

		# graphics
		self.image = pygame.Surface((CREEP_WIDTH, CREEP_HEIGHT)).convert_alpha()
		self.image.fill(RED)
		self.rect = pygame.Rect(0, 0, CREEP_COLLISION_WIDTH, CREEP_COLLISION_HEIGHT)
		self.rect.center = self.pos
		self.old_rect = self.rect.copy()


	def collision(self, direction):
		collision_sprites = pygame.sprite.spritecollide(self, self.creep_group, False) # dokill = False

		# if self.rect.colliderect(self.player.rect):
		#     collision_sprites.append(self.player)

		if collision_sprites:
			if direction == 'horizontal':
				for sprite in collision_sprites:
					# collision on the right
					if self.rect.right >= sprite.rect.left \
							and self.old_rect.right <= sprite.old_rect.left:
						self.rect.right = sprite.rect.left
						self.pos.x = self.rect.x  # rect和pos是相互更新的
						self.direction.x *= -1

					# collision on the left
					if self.rect.left <= sprite.rect.right \
							and self.old_rect.left >= sprite.old_rect.right:
						self.rect.left = sprite.rect.right
						self.pos.x = self.rect.x  # rect和pos是相互更新的
						self.direction.x *= -1

			if direction == 'vertical':
				for sprite in collision_sprites:
					# collsion on the top
					if self.rect.top <= sprite.rect.bottom \
							and self.old_rect.top >= sprite.old_rect.bottom:
						self.rect.top = sprite.rect.bottom
						self.pos.y = self.rect.y  # 这里是更新自己的位置
						self.direction.y *= -1

					# collision on the bottom
					if self.rect.bottom >= sprite.rect.top \
							and self.old_rect.bottom <= sprite.old_rect.top:
						self.rect.bottom = sprite.rect.top
						self.pos.y = self.rect.y
						self.direction.y *= -1

	def got_hit(self, arrow_damage, hit_arrow):
		self.health -= arrow_damage
		self.hit_arrow = hit_arrow

		self.knockback_direction = self.hit_arrow.direction
		self.knockback_acceleration = self.hit_arrow.knockback

	def KNOCKBACK(self):
		if self.knockback_acceleration < 0:
			self.knockback_acceleration = 0

		# KNOCKBACK 的本质就是向子弹攻击的相反的方向移动一定距离
		self.pos.x += self.knockback_direction.x * self.knockback_acceleration * self.dt
		self.pos.y += self.knockback_direction.y * self.knockback_acceleration * self.dt

		self.knockback_acceleration -= 2*self.knockback_acceleration/FPS
		

	def check_health(self):
		if self.health <= 0:
			self.kill()

	def update(self, dt):
		self.check_health()

		# dt and old_rect -------------------------------------------------------------------- #
		self.dt = dt
		self.old_rect = self.rect.copy()

		# movement --------------------------------------------------------------------------- #
		self.direction.x = self.hero.pos.x - self.pos.x
		self.direction.y = self.hero.pos.y - self.pos.y

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.KNOCKBACK()

		self.pos.x += self.direction.x * self.movement_speed * self.dt
		self.rect.x = round(self.pos.x)
		self.collision('horizontal')
		self.pos.y += self.direction.y * self.movement_speed * self.dt
		self.rect.y = round(self.pos.y)
		self.collision('vertical')

