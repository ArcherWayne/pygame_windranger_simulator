import pygame

class TREE(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)

		# type
		self.type = 'tree'

		self.image = pygame.image.load('assets/graphics/map/tree.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)