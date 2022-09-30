import pygame
from setting import *

pygame.init()
screen = pygame.display.set_mode(window_size)
display_surf = pygame.display.get_surface()

pygame.draw.rect(display_surf, (123,132, 53), (10, 10, 10, 10))
