

import pygame, sys
from setting import *
# from random import randint
# from debug import debug

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surf = pygame.display.get_surface()

		# camera offset
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surf.get_size()[0] // 2
		self.half_h = self.display_surf.get_size()[1] // 2

		# ground
		self.ground_surf = pygame.transform.scale((pygame.image.load('assets/graphics/map/map.png').convert_alpha()), (MAP_SIZE))
		self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

	def center_target_camera(self, target): # 以target作为camera的中心， 求解offset距离
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y = target.rect.centery - self.half_h

	def custom_draw(self, player):

		self.center_target_camera(player)

		# ground
		ground_offset = self.ground_rect.topleft - self.offset # move everything in the opposite direction of the target, so thats a negative sign
		self.display_surf.blit(self.ground_surf, ground_offset)

		# elements
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			if sprite.type == 'hero':
					# hero_offset = self.offset 
					offset_pos = sprite.rect.topleft - self.offset
					self.display_surf.blit(sprite.image, (offset_pos[0]-0.5*(sprite.image.get_width()-sprite.rect.size[0]), \
						offset_pos[1]-0.5*(sprite.image.get_height()-sprite.rect.size[1])))
					# self.display_surf.blit(sprite.image, (offset_pos[0]-sprite.rect.size[0]+0.5*sprite.image.get_width(), \
					# 	offset_pos[1]-sprite.rect.size[1]+0.5*sprite.image.get_height()))


			else:
					offset_pos = sprite.rect.topleft - self.offset
					# self.display_surf.blit(sprite.image, offset_pos)
					self.display_surf.blit(sprite.image, (offset_pos[0]-sprite.rect.size[0]+0.5*sprite.image.get_width(), \
						offset_pos[1]-sprite.rect.size[1]+0.5*sprite.image.get_height()))


	def show_collision_area(self):
		if show_collision_area:
			# draw a rectangle
			# rect(surface, color, rect) -> Rect
			# rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1) -> Rect
			for sprite in self.sprites():
				# FIXME： 这段逻辑一点都不好，还是要去显示实际的creep rect
				if sprite.type == 'creep':
					collision_area_surf = pygame.Surface((CREEP_COLLISION_WIDTH, CREEP_COLLISION_HEIGHT)).convert_alpha()
					collision_area_surf.fill(BLUE)
					collision_area_rect = collision_area_surf.get_rect(topleft = sprite.rect.topleft)
					offset_pos = collision_area_rect.topleft - self.offset
					self.display_surf.blit(collision_area_surf, offset_pos)

				if sprite.type == 'hero':
					collision_area_surf = pygame.Surface((HERO_COLLISION_WIDTH, HERO_COLLISION_HEIGHT)).convert_alpha()
					collision_area_surf.fill(BLUE)
					collision_area_rect = collision_area_surf.get_rect(topleft = sprite.rect.topleft)
					offset_pos = collision_area_rect.topleft - self.offset
					self.display_surf.blit(collision_area_surf, offset_pos)


	def show_absolute_vector(self, player):
		if show_absolute_vector:
			for sprite in self.sprites():
				if sprite.type == 'creep' or sprite.type == 'hero' or sprite.type == 'arrow':
					# pygame.draw.line(屏幕，颜色，起点，终点，宽度)
					pygame.draw.line(self.display_surf, ORANGE, (-player.rect.topleft[0], -player.rect.topleft[1]), sprite.rect.topleft - self.offset, 2)
					# NOTE: 实现方法: 向量起始坐标是绝对位置, 终点坐标是相机的相对位置
					# 指向的是实际的rect的位置, image只是显示图像的, 没有实际逻辑功能
					# 绝对位置和相对位置的转换关系: 相对位置 = 绝对位置 - offset

