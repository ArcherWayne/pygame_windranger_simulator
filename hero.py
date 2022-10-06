import pygame
from setting import *
from debug import debug

class HERO(pygame.sprite.Sprite): # my code
	def __init__(self, groups, creep_group) -> None:
		super().__init__(groups)
		# type
		self.type = 'hero'

		self.creep_group = creep_group

		# position
		self.pos = pygame.math.Vector2()
		self.pos.x = WIN_WIDTH/2 
		self.pos.y = WIN_HEIGHT/2 

		# graphics
		# self.image = pygame.transform.scale(pygame.image.load("assets/graphics/windranger/windranger_idle_animation1.png").convert_alpha(), (HERO_WIDTH, HERO_HEIGHT))
		self.image = pygame.Surface((HERO_WIDTH, HERO_HEIGHT)).convert_alpha()
		self.image.fill(GREEN)
		# self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
		self.rect = pygame.Rect(0, 0, HERO_COLLISION_WIDTH, HERO_COLLISION_HEIGHT)
		self.old_rect = self.rect.copy()

		# movement
		self.direction = pygame.math.Vector2()
		self.movement_speed = HERO_MOVEMENT_SPEED

		# stat
		self.health = HERO_HEALTH
		self.hit_frame = CREEP_ATTACK_INTERVAL - 1 # 英雄接触到小兵的帧读数

	def keyboard_movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_a]:
			self.direction.x = -1
		elif keys[pygame.K_d]:
			self.direction.x = 1
		else:
			self.direction.x = 0

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.pos.x += self.direction.x * self.movement_speed * self.dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.movement_speed * self.dt
		self.rect.y = round(self.pos.y)


	def check_collision_with_creeps(self):
		creep_sprites = pygame.sprite.spritecollide(self, self.creep_group, False) # dokill = False

		if creep_sprites:
			self.got_hit()
		
		else: 
			self.hit_frame = CREEP_ATTACK_INTERVAL - 1
			# for creeps in creep_sprites:
				
	
	def got_hit(self):
		print(self.health)
		self.hit_frame += 1
		if self.hit_frame == CREEP_ATTACK_INTERVAL:
			self.health -= CREEP_DAMAGE

			if self.hit_frame > CREEP_ATTACK_INTERVAL:
				self.hit_frame = 0


	def check_health(self):
		if self.health <= 0:
			self.kill()

	def update(self, dt):
		self.dt = dt
		self.old_rect = self.rect.copy()

		self.keyboard_movement()
		self.check_collision_with_creeps()
		self.check_health()

