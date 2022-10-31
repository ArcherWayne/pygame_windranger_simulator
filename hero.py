import pygame
from arrow import ARROW
from setting import *
from debug import debug

class HERO(pygame.sprite.Sprite): # my code
	def __init__(self, groups, creep_group, camera_group, arrow_group, stats_manager) -> None:
		super().__init__(groups)
		# type
		self.type = 'hero'

		# group setting, the imported group is the same reference as the outside group, not the copy of it 

		self.creep_group = creep_group
		self.camera_group = camera_group
		self.arrow_group = arrow_group
		self.stats_manager = stats_manager

		# position
		self.pos = pygame.math.Vector2()
		self.pos.x = WIN_WIDTH/2 
		self.pos.y = WIN_HEIGHT/2 

		# graphics
		# self.image = pygame.transform.scale(pygame.image.load("assets/graphics/windranger/windranger_idle_animation1.png").convert_alpha(), (HERO_WIDTH, HERO_HEIGHT))
		windranger_idle_animation1 = pygame.image.load('assets/graphics/windranger/windranger_idle_animation1.png').convert_alpha()
		self.image = pygame.transform.scale(windranger_idle_animation1\
			, (self.stats_manager.hero_width, self.stats_manager.hero_height))
		# self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
		self.rect = pygame.Rect(0, 0, self.stats_manager.hero_collision_width, self.stats_manager.hero_collision_height)
		self.old_rect = self.rect.copy()

		# movement
		self.direction = pygame.math.Vector2()
		# self.movement_speed = HERO_MOVEMENT_SPEED

		# stat
		# self.max_health = HERO_HEALTH
		# self.current_health = HERO_HEALTH
		# self.max_mana = HERO_MANA
		# self.current_mana = HERO_MANA

		# self.attack_interval = HERO_ATTACK_INTERVAL

		# cooldown frames
		self.hit_cooldown_frame = 0 # 英雄接触到小兵的帧读数
		self.shoot_arrow_cooldown_frame = 0 # attack cd

		self.skill_shackleshot_cooldown_frame = 0 # shackleshot cd
		self.skill_powershot_cooldown_frame = 0 # powershot cd
		self.skill_windrun_cooldown_frame = 0
		self.skill_focusfire_cooldown_frame = 0


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
			ARROW([self.camera_group, self.arrow_group], aim_direction, self.pos, self.creep_group, self.stats_manager)

			self.shoot_arrow_cooldown_frame += 1

	# use skills ---------------------------------------------- # 
	def use_skill_shackleshot(self):
		print("use_skill_shackleshot")


	def use_skill_powershot(self, mouse_pos):
		if self.skill_powershot_cooldown_frame == 0:
			print("use_skill_powershot")

			aim_direction = pygame.math.Vector2()
			aim_direction.x = mouse_pos[0] - WIN_WIDTH/2
			aim_direction.y = mouse_pos[1] - WIN_HEIGHT/2
			SKILL_POWERSHOT([self.camera_group, self.arrow_group], aim_direction, self.stats_manager.arrow_speed, self.stats_manager.arrow_damage, self.pos, self.creep_group)
			
			self.skill_powershot_cooldown_frame += 1

	def use_skill_windrun(self):
		if self.skill_windrun_cooldown_frame == 0:
			print("use_skill_windrun")

			self.movement_speed = self.movement_speed * 3

			self.skill_windrun_cooldown_frame += 1

	def use_skill_focusfire(self):
		if self.skill_focusfire_cooldown_frame == 0:
			print("use_skill_focusfire")

			self.attack_interval = round(self.attack_interval / 3)

			self.skill_focusfire_cooldown_frame += 1

	# use skills end ------------------------------------------ # 

	def check_collision_with_creeps(self):
		creep_sprites = pygame.sprite.spritecollide(self, self.creep_group, False) # dokill = False

		if creep_sprites:
			self.got_hit()

	
	def got_hit(self):
		if self.hit_cooldown_frame == 0:
			# self.current_health -= CREEP_DAMAGE
			self.stats_manager.hero_current_health -= self.stats_manager.creep_damage
			
			self.hit_cooldown_frame += 1


	def check_health(self):
		if self.stats_manager.hero_current_health <= 0:
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
		self.shoot_arrow_cooldown_frame = self.update_cooldowns(self.shoot_arrow_cooldown_frame, self.attack_interval)
		self.hit_cooldown_frame = self.update_cooldowns(self.hit_cooldown_frame, CREEP_ATTACK_INTERVAL)
		self.skill_shackleshot_cooldown_frame = self.update_cooldowns(self.skill_shackleshot_cooldown_frame, SHACKLESHOT_CD)
		self.skill_powershot_cooldown_frame = self.update_cooldowns(self.skill_powershot_cooldown_frame, POWERSHOT_CD)
		self.skill_windrun_cooldown_frame = self.update_cooldowns(self.skill_windrun_cooldown_frame, WINDRUN_CD)
		self.skill_focusfire_cooldown_frame = self.update_cooldowns(self.skill_focusfire_cooldown_frame, FOCUSFIRE_CD)

class SKILL_SHACKLESHOT(pygame.sprite.Sprite):
	def __init__(self, groups):
		super().__init__(groups)

		self.type = 'skill_shackleshot'


class SKILL_POWERSHOT(ARROW):
	def __init__(self, groups, direction, hero_pos, creep_group, stats_manager):
		super().__init__(groups, direction, hero_pos, creep_group, stats_manager)

		self.type = 'arrow'
		self.stats_manager = stats_manager

		# movement 
		self.direction = direction

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.movement_speed = self.stats_manager.arrow_speed * 3
		self.damage = self.stats_manager.arrow_damage * 10
		self.knockback = self.stats_manager.arrow_knockback * 3
		self.penetration = self.stats_manager.arrow_penetration * 10
		self.start_pos = hero_pos

		self.pos = pygame.math.Vector2()
		self.pos.x = hero_pos.x
		self.pos.y = hero_pos.y

		self.image = pygame.Surface((ARROW_WIDTH * 3, ARROW_HEIGHT * 3)).convert_alpha()
		self.image.fill(RED)
		# self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
		self.rect = pygame.Rect(0, 0, ARROW_COLLISION_WIDTH, ARROW_COLLISION_HEIGHT)

		self.old_rect = self.rect.copy()

		# stats
		self.time_10s = 0
		self.creep_group = creep_group



