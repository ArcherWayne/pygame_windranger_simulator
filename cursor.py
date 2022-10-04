import pygame
from setting import *

class CURSOR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/graphics/UI/cursor.png').convert_alpha(), (CURSOR_WIDTH, CURSOR_HEIGHT))
        self.rect = self.image.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

    def get_pos(self, mouse_pos):
        self.rect.topleft = mouse_pos

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self, mouse_pos):
        self.get_pos(mouse_pos)
