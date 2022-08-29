import pygame
from setting import *
from debug import debug

class HERO(pygame.sprite.Sprite):
	def __init__(self, *groups) -> None:
		super().__init__(*groups)
		
		# position
		self.pos = pygame.math.Vector2()
		self.pos.x = window_size[0]/2 
		self.pos.y = window_size[1]/2 
		# self.pos = (window_size[0]/2, window_size[1]/2)

		# graphics
		self.image = pygame.transform.scale(pygame.image.load("assets/graphics/windranger/windranger_idle_animation1.png").convert_alpha(), (HERO_WIDTH, HERO_HEIGHT))
		self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))

		# movement
		self.direction = pygame.math.Vector2()
		self.movement_speed = 100

	def keyboard_movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.moving_state = 0
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.moving_state = 0
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_a]:
			self.moving_state = 0
			self.direction.x = -1
		elif keys[pygame.K_d]:
			self.moving_state = 0
			self.direction.x = 1
		else:
			self.direction.x = 0

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.pos.x += self.direction.x * self.movement_speed * self.dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.movement_speed * self.dt
		self.rect.y = round(self.pos.y)

	def update(self, dt):
		self.dt = dt

		self.keyboard_movement()