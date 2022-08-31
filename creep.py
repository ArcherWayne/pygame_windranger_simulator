import pygame
from setting import *

class CREEP(pygame.sprite.Sprite):
	def __init__(self, *groups) -> None:
		super().__init__(*groups)

		# position
		self.pos = pygame.math.Vector2()
		self.pos.x = window_size[0]/2 
		self.pos.y = window_size[1]/2 

		# graphics
		self.image = pygame.transform.scale(pygame.image.load("assets/graphics/windranger/windranger_idle_animation1.png").convert_alpha(), (HERO_WIDTH, HERO_HEIGHT))
		self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))

		# movement
		self.direction = pygame.math.Vector2()
		self.movement_speed = 150

	def update(self):
		pass