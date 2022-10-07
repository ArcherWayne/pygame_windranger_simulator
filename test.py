
import pygame, sys
from test2 import HERO
from tree import TREE
from setting import *

pygame.init()
screen = pygame.display.set_mode(window_size)
display_surf = pygame.display.get_surface()

camera_group = pygame.sprite.Group()
hero = HERO(camera_group, camera_group)

camera_group.add(TREE((1,1),camera_group))

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
			pygame.quit()
			sys.exit()

	# test area ----------------------------------------------------------------------------------------------------- #
	print(camera_group)
	print(hero.camera_group)




	# test area ----------------------------------------------------------------------------------------------------- #






	pygame.display.update()
