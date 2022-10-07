import pygame
from tree import TREE

class HERO(pygame.sprite.Sprite):
	def __init__(self, groups, camera_group) -> None:
		super().__init__(groups)

		self.camera_group = camera_group
		self.camera_group.add(TREE((1,1),camera_group))