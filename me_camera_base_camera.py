
import pygame, sys
# from random import randint
# from debug import debug

# active = 0

# class Tree(pygame.sprite.Sprite):
# 	def __init__(self,pos,group):
# 		super().__init__(group)
# 		self.image = pygame.image.load('assets/graphics/map/tree.png').convert_alpha()
# 		self.rect = self.image.get_rect(topleft = pos)

# class Player(pygame.sprite.Sprite):
# 	def __init__(self,pos,group):
# 		super().__init__(group)
# 		self.image = pygame.image.load('assets/graphics/windranger/windranger_idle_animation1.png').convert_alpha()
# 		self.rect = self.image.get_rect(center = pos)
# 		self.direction = pygame.math.Vector2()
# 		self.speed = 5

# 	def input(self):
# 		keys = pygame.key.get_pressed()

# 		if keys[pygame.K_UP]:
# 			self.direction.y = -1
# 		elif keys[pygame.K_DOWN]:
# 			self.direction.y = 1
# 		else:
# 			self.direction.y = 0

# 		if keys[pygame.K_RIGHT]:
# 			self.direction.x = 1
# 		elif keys[pygame.K_LEFT]:
# 			self.direction.x = -1
# 		else:
# 			self.direction.x = 0

# 	def update(self):
# 		self.input()
# 		self.rect.center += self.direction * self.speed

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surf = pygame.display.get_surface()

		# camera offset
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surf.get_size()[0] // 2
		self.half_h = self.display_surf.get_size()[1] // 2

		# ground
		self.ground_surf = pygame.image.load('assets/graphics/map/map.png').convert_alpha()
		self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

	def center_target_camera(self, target):
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y = target.rect.centery - self.half_h

	def custom_draw(self, player):

		self.center_target_camera(player)

		# ground
		ground_offset = self.ground_rect.topleft - self.offset # move everything in the opposite direction of the target, so thats a negative sign
		self.display_surf.blit(self.ground_surf, ground_offset)

		# tree elements
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surf.blit(sprite.image, offset_pos)


# if active:
# 	pygame.init()
# 	screen = pygame.display.set_mode((1280,720))
# 	clock = pygame.time.Clock()
# 	pygame.event.set_grab(True)

# 	# setup 
# 	camera_group = CameraGroup()
# 	player = Player((640,360),camera_group)

# 	for i in range(20):
# 		random_x = randint(1000,2000)
# 		random_y = randint(1000,2000)
# 		Tree((random_x,random_y),camera_group)

# 	while True:
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()
# 			if event.type == pygame.KEYDOWN:
# 				if event.key == pygame.K_ESCAPE:
# 					pygame.quit()
# 					sys.exit()

# 			if event.type == pygame.MOUSEWHEEL:
# 				camera_group.zoom_scale += event.y * 0.03

# 		screen.fill('#71ddee')

# 		camera_group.update()
# 		camera_group.custom_draw(player)
# 		debug(player.direction)
# 		# camera_group.custom_draw()

# 		pygame.display.update()
# 		clock.tick(60)
