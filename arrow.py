import pygame
from setting import *
from debug import debug

class ARROW(pygame.sprite.Sprite):
	def __init__(self, groups, direction, hero_pos, creep_group, stats_manager):
		super().__init__(groups)

		self.type = 'arrow'
		self.stats_manager = stats_manager

		# movement 
		self.direction = direction

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		
		# arrow and creep class dont need to change their stats in the stats manager
		# instead they obtain the init stats from the stats manager
		# then manage the stats in itself
		self.movement_speed = self.stats_manager.arrow_speed
		self.damage = self.stats_manager.arrow_damage
		self.knockback = self.stats_manager.arrow_knockback
		self.arrow_penetration = self.stats_manager.arrow_penetration
		
		self.start_pos = hero_pos

		self.pos = pygame.math.Vector2()
		self.pos.x = hero_pos.x
		self.pos.y = hero_pos.y

		self.image = pygame.Surface((self.stats_manager.arrow_width, self.stats_manager.arrow_height)).convert_alpha()
		self.image.fill(RED)
		# self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
		self.rect = pygame.Rect(0, 0, self.stats_manager.arrow_collision_width, self.stats_manager.arrow_collision_height)

		self.old_rect = self.rect.copy()

		# stats
		self.time_10s = 0
		self.creep_group = creep_group

		self.penetrated_creeps = []

	def check_collision(self):
		# 存在两种碰撞: 
		# 1. 检查是否rect之间有碰撞, 这个会检查rect在图像上是否重叠
		# 2. 检查是否pos之间有碰撞, 这个会检查坐标上是否有重叠
		# 在bullet中, 依旧要使用camera_group
		hit_creeps_list = pygame.sprite.spritecollide(self, self.creep_group, False)
		if hit_creeps_list:
			for creep in hit_creeps_list:
				if creep not in self.penetrated_creeps:
					creep.got_hit(self.damage, self)
					self.penetrated_creeps.append(creep)
					self.arrow_penetration -= 1

	def kill_when_more_than_10s(self):
		self.time_10s += 1
		if self.time_10s >= FPS*10:
			self.kill()

	def kill_when_penetrated(self):
		if self.arrow_penetration <= 0:
			self.kill()


	def update(self, dt):
		self.pos.x += self.direction.x * self.movement_speed * dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.movement_speed * dt
		self.rect.y = round(self.pos.y)

		self.kill_when_more_than_10s()
		self.kill_when_penetrated()
		self.check_collision()