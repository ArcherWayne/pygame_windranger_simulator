import pygame

from Config.setting import *
from Functions.import_folder import import_folder
# from Skills.base import Base_Skill
from Skills.pool import skill_pool
from Skills.skill_galeforce import Skill_Galeforce
from Skills.skill_shackleshot import Skill_Shackleshot
from Units.arrow import ARROW


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
		windranger_idle_animation1 = pygame.image.load('assets/graphics/windranger/windranger_idle_animation1.png').convert_alpha()
		self.image = pygame.transform.scale(windranger_idle_animation1\
			, (self.stats_manager.hero_width, self.stats_manager.hero_height))
		self.rect = pygame.Rect(0, 0, self.stats_manager.hero_collision_width, self.stats_manager.hero_collision_height)
		self.old_rect = self.rect.copy()
		self.hero_animation = HERO_ANIMATION() # animation

		# movement
		self.direction = pygame.math.Vector2()
		self.facing_direction = 'right'
		self.is_moving = False
		


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

		self.pos.x += self.direction.x * self.stats_manager.hero_movement_speed * self.dt
		self.rect.x = round(self.pos.x)
		self.pos.y += self.direction.y * self.stats_manager.hero_movement_speed * self.dt
		self.rect.y = round(self.pos.y)


	def shoot_arrow(self, mouse_pos):
		if self.stats_manager.hero_shoot_arrow_cooldown_frame == 0:
			aim_direction = pygame.math.Vector2()
			aim_direction.x = mouse_pos[0] - WIN_WIDTH/2
			aim_direction.y = mouse_pos[1] - WIN_HEIGHT/2
			ARROW([self.camera_group, self.arrow_group], aim_direction, self.pos, self.creep_group, self.stats_manager)

			self.stats_manager.hero_shoot_arrow_cooldown_frame += 1

	# use skills ---------------------------------------------- # 
	def use_skill_shackleshot(self):
		print("use_skill_shackleshot")


	def use_skill_powershot(self, mouse_pos):
		if self.stats_manager.skill_powershot_cooldown_frame == 0:
			print("use_skill_powershot")

			aim_direction = pygame.math.Vector2()
			aim_direction.x = mouse_pos[0] - WIN_WIDTH/2
			aim_direction.y = mouse_pos[1] - WIN_HEIGHT/2
			SKILL_POWERSHOT([self.camera_group, self.arrow_group], aim_direction, self.pos, self.creep_group, self.stats_manager)
			# groups, direction, hero_pos, creep_group, stats_manager
			self.stats_manager.skill_powershot_cooldown_frame += 1


	def use_skill_windrun(self):
		if self.stats_manager.skill_windrun_cooldown_frame == 0:
			print("use_skill_windrun")

			self.stats_manager.skill_windrun_countdown_frame += 1 
			self.stats_manager.skill_windrun_cooldown_frame += 1


	def use_skill_focusfire(self):
		if self.stats_manager.skill_focusfire_cooldown_frame == 0:
			print("use_skill_focusfire")

			self.stats_manager.skill_focusfire_countdown_frame += 1 
			self.stats_manager.skill_focusfire_cooldown_frame += 1

	# use skills end ------------------------------------------ # 

	def check_collision_with_creeps(self):
		creep_sprites = pygame.sprite.spritecollide(self, self.creep_group, False) # dokill = False

		if creep_sprites:
			self.got_hit()
			for creep in creep_sprites:
				creep.set_knockback_wa_acceleration(500)

	
	def got_hit(self):
		if self.stats_manager.hero_hit_cooldown_frame == 0:
			self.stats_manager.hero_current_health -= self.stats_manager.creep_damage

			# cooldown_frame += 1 就开始倒计时 读cd
			self.stats_manager.hero_hit_cooldown_frame += 1


	def check_health(self):
		if self.stats_manager.hero_current_health <= 0:
			self.kill()


	def check_facing_direction(self):
		# 设计成这样的: 面向方向决定self.facing_direction, 位置改变决定run或者idle
		x_pos_change = self.rect.x - self.old_rect.x
		if x_pos_change < 0: # moved left
			self.facing_direction = 'left'
		elif x_pos_change > 0: # moved right
			self.facing_direction = 'right'

		if self.rect.topleft != self.old_rect.topleft:
			self.is_moving = True
		else:
			self.is_moving = False

	def update(self, dt):
		self.dt = dt
		self.old_rect = self.rect.copy()

		self.keyboard_movement()
		self.check_facing_direction()
		self.check_collision_with_creeps()
		self.check_health()

	def install_skills(self):
		# add skill galeforce
		skill_galeforce = Skill_Galeforce(['Gale Force', '', self.stats_manager.skill_galeforce_cd], self.stats_manager, self.creep_group)
		skill_pool.append(skill_galeforce, self)

		# add skill shackleshot
		skill_shackleshot = Skill_Shackleshot(['Shackle Shot', '', self.stats_manager.skill_shackleshot_cd, self.stats_manager.skill_shackleshot_duration], self.stats_manager, self.creep_group)
		skill_pool.append(skill_shackleshot, self)


	def use_skill(self, name):
		skill = skill_pool.get_skill_by_name(name)
		if skill is not None:
			skill.use()
		pass


class SKILL_SHACKLESHOT(pygame.sprite.Sprite):
	def __init__(self, groups):
		super().__init__(groups)

		self.type = 'skill_shackleshot'


class SKILL_POWERSHOT(ARROW):
	# FIXME: 重写此类
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
		self.arrow_penetration = self.stats_manager.arrow_penetration * 10
		self.start_pos = hero_pos

		self.pos = pygame.math.Vector2()
		self.pos.x = hero_pos.x
		self.pos.y = hero_pos.y

		self.image = pygame.Surface((self.stats_manager.arrow_width * 3, self.stats_manager.arrow_height * 3)).convert_alpha()
		self.image.fill(RED)
		# self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
		self.rect = pygame.Rect(0, 0, self.stats_manager.arrow_collision_width, self.stats_manager.arrow_collision_height)

		self.old_rect = self.rect.copy()

		# stats
		self.time_10s = 0
		self.creep_group = creep_group


class HERO_ANIMATION:
	def __init__(self) -> None:
		pass
		self.import_assets()
		self.animation_status_list = ['idle_right', 'idle_left', 'run_right', 'run_left']
		self.animation_status = self.animation_status_list[0]

		self.frame_index = 0

	def import_assets(self):
		self.animation = {
			'idle_right':[], 'idle_left':[], 'run_right':[], 'run_left':[]
			}

		for animation in self.animation.keys():
			full_path = 'assets/graphics/windranger/' + animation
			self.animation[animation] = import_folder(full_path)

		self.animation_status = 'idle_right'

	def	update(self):
		pass 

	def update_animation_status(self, direction, is_moving):
		direction = direction
		is_moving = is_moving
		# 判断HERO类下面的self.direction.x 和 self.direction.y两个条件, 判断idle和run
		if is_moving == False:
			match direction:
				case 'right': 
					self.animation_status = 'idle_right'
				case 'left':
					self.animation_status = 'idle_left'

		if is_moving == True:
			match direction:
				case 'right': 
					self.animation_status = 'run_right'
				case 'left':
					self.animation_status = 'run_left'



	def get_animation_surf(self):
		animation_surf = self.animation[self.animation_status][self.frame_index]

		return animation_surf