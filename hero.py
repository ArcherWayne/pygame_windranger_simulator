import pygame
from arrow import ARROW
from setting import *
from debug import debug

class HERO(pygame.sprite.Sprite): # my code
	def __init__(self, groups, creep_group, camera_group, arrow_group) -> None:
		super().__init__(groups)
		# type
		self.type = 'hero'

		# group setting, the imported group is the same reference as the outside group, not the copy of it 

		self.creep_group = creep_group
		self.camera_group = camera_group
		self.arrow_group = arrow_group

		# position
		self.pos = pygame.math.Vector2()
		self.pos.x = WIN_WIDTH/2 
		self.pos.y = WIN_HEIGHT/2 

		# graphics
		# self.image = pygame.transform.scale(pygame.image.load("assets/graphics/windranger/windranger_idle_animation1.png").convert_alpha(), (HERO_WIDTH, HERO_HEIGHT))
		self.image = pygame.Surface((HERO_WIDTH, HERO_HEIGHT)).convert_alpha()
		self.image.fill(GREEN)
		# self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
		self.rect = pygame.Rect(0, 0, HERO_COLLISION_WIDTH, HERO_COLLISION_HEIGHT)
		self.old_rect = self.rect.copy()

		# movement
		self.direction = pygame.math.Vector2()
		self.movement_speed = HERO_MOVEMENT_SPEED

		# stat
		self.max_health = HERO_HEALTH
		self.current_health = HERO_HEALTH
		self.max_mana = HERO_MANA
		self.current_mana = HERO_MANA

		# cooldown frames
		self.hit_cooldown_frame = 0 # 英雄接触到小兵的帧读数
		self.shoot_arrow_cooldown_frame = 0 # attack cd
		self.skill_powershot_cooldown_frame = 0 # powershot cd


	def keyboard_movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_a]:
			self.direction.x = -1
		elif keys[pygame.K_d]:
			self.direction.x = 1
		else:
			self.direction.x = 0

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.pos.x += self.direction.x * self.movement_speed * self.dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.movement_speed * self.dt
		self.rect.y = round(self.pos.y)


	def shoot_arrow(self, mouse_pos):
		if self.shoot_arrow_cooldown_frame == 0:
			aim_direction = pygame.math.Vector2()
			aim_direction.x = mouse_pos[0] - WIN_WIDTH/2
			aim_direction.y = mouse_pos[1] - WIN_HEIGHT/2
			ARROW([self.camera_group, self.arrow_group], aim_direction, ARROW_SPEED, ARROW_DAMAGE, self.pos, self.creep_group)

			self.shoot_arrow_cooldown_frame += 1

	# use skills ---------------------------------------------- # 
	def use_skill_powershot(self, mouse_pos):
		if self.skill_powershot_cooldown_frame == 0:
			aim_direction = pygame.math.Vector2()
			aim_direction.x = mouse_pos[0] - WIN_WIDTH/2
			aim_direction.y = mouse_pos[1] - WIN_HEIGHT/2
			SKILL_POWERSHOT([self.camera_group, self.arrow_group], aim_direction, ARROW_SPEED, ARROW_DAMAGE, self.pos, self.creep_group)
			
			self.skill_powershot_cooldown_frame += 1

	# use skills end ------------------------------------------ # 

	def check_collision_with_creeps(self):
		creep_sprites = pygame.sprite.spritecollide(self, self.creep_group, False) # dokill = False

		if creep_sprites:
			self.got_hit()

	
	def got_hit(self):
		if self.hit_cooldown_frame == 0:
			self.current_health -= CREEP_DAMAGE
			
			self.hit_cooldown_frame += 1


	def check_health(self):
		if self.current_health <= 0:
			self.kill()


	def update_cooldowns(self, cooldown_frame, cooldown_interval):
		if cooldown_frame > 0:
			cooldown_frame += 1
		if cooldown_frame > cooldown_interval:
			cooldown_frame = 0

		return cooldown_frame

	def update(self, dt):
		self.dt = dt
		self.old_rect = self.rect.copy()

		self.keyboard_movement()
		self.check_collision_with_creeps()
		self.check_health()

		# update cooldowns
		self.shoot_arrow_cooldown_frame = self.update_cooldowns(self.shoot_arrow_cooldown_frame, HERO_ATTACK_INTERVAL)
		self.hit_cooldown_frame = self.update_cooldowns(self.hit_cooldown_frame, CREEP_ATTACK_INTERVAL)
		self.skill_powershot_cooldown_frame = self.update_cooldowns(self.skill_powershot_cooldown_frame, POWERSHOT_CD)

class SKILL_SHACKLESHOT(pygame.sprite.Sprite):
	def __init__(self, groups):
		super().__init__(groups)

		self.type = 'skill_shackleshot'


class SKILL_POWERSHOT(ARROW):
	def __init__(self, groups, direction, speed, damage, hero_pos, creep_group):
		super().__init__(groups, direction, speed, damage, hero_pos, creep_group)

		self.type = 'arrow'

		# movement 
		self.direction = direction

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.movement_speed = speed * 3
		self.damage = damage * 3
		self.knockback = ARROW_KNOCKBACK * 3
		self.start_pos = hero_pos

		self.pos = pygame.math.Vector2()
		self.pos.x = hero_pos.x
		self.pos.y = hero_pos.y

		self.image = pygame.Surface((ARROW_WIDTH, ARROW_HEIGHT)).convert_alpha()
		self.image.fill(RED)
		# self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
		self.rect = pygame.Rect(0, 0, ARROW_COLLISION_WIDTH, ARROW_COLLISION_HEIGHT)

		self.old_rect = self.rect.copy()

		# stats
		self.time_10s = 0
		self.creep_group = creep_group


	def check_collision(self):
		hit_creeps_list = pygame.sprite.spritecollide(self, self.creep_group, False)
		if hit_creeps_list:
			for creep in hit_creeps_list:
				creep.got_hit(self.damage, self)

	def update(self, dt):
		self.pos.x += self.direction.x * self.movement_speed * dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.movement_speed * dt
		self.rect.y = round(self.pos.y)

		self.kill_when_more_than_10s()
		self.check_collision()


