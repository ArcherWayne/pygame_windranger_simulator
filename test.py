from cgi import print_arguments
import pygame, sys
from setting import *

pygame.init()
screen = pygame.display.set_mode(window_size)
display_surf = pygame.display.get_surface()


while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
			pygame.quit()
			sys.exit()





	# test area ----------------------------------------------------------------------------------------------------- #
	# pygame.draw.rect(display_surf, (123,132, 53), (10, 10, 10, 10))
	# rect_1 = pygame.Rect(10, 10, 32, 64)
	# print(rect_1.size)

	image = pygame.Surface((CREEP_WIDTH, CREEP_HEIGHT)).convert_alpha()
	image.fill(RED)

	print(image.get_width())
	# test area ----------------------------------------------------------------------------------------------------- #






	pygame.display.update()
