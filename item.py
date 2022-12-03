import pygame
from setting import ITEM_SIZE


class ATTRIBUTE_ITEM_SPRITE(pygame.sprite.Sprite):
	def __init__(self, groups, item, drop_pos, hero,stats_manager):
		super().__init__(*groups)

		self.type = 'attri_item'

		self.item = item
		self.stats_manager = stats_manager
		self.hero = hero

		# self.rect = pygame.Rect(1, 1, 1, 1)
		# item images ------------------------- #
		match self.item:
			case 'branch':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/branch.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'all'
				# self.attri_value = 1
			case 'circlet':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/circlet.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'all'
				# self.attri_value = 2
			case 'crown':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/crown.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'all'
				# self.attri_value = 4
			case 'orb':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/orb.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'all'
				# self.attri_value = 10
			case 'apex':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/apex.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'all'
				# self.attri_value = 70

			case 'gauntlets':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/gauntlets.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'str'
				# self.attri_value = 3
			case 'belt':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/belt.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'str'
				# self.attri_value = 6
			case 'axe':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/axe.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'str'
				# self.attri_value = 10
			case 'reaver':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/reaver.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'str'
				# self.attri_value = 25

			case 'slippers':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/slippers.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'agi'
				# self.attri_value = 3
			case 'band':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/band.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'agi'
				# self.attri_value = 6
			case 'blade':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/blade.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'agi'
				# self.attri_value = 10
			case 'eaglesong':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/eaglesong.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'agi'
				# self.attri_value = 25

			case 'mantle':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/mantle.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'int'
				# self.attri_value = 3
			case 'robe':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/robe.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'int'
				# self.attri_value = 6
			case 'staff':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/staff.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'int'
				# self.attri_value = 10
			case 'mystic':
				self.image = pygame.transform.scale(pygame.image.load('assets/graphics/items/attri_items/mystic.png').convert_alpha(), (ITEM_SIZE[0], ITEM_SIZE[1]))
				# self.attri_type = 'int'
				# self.attri_value = 25

		self.rect = self.image.get_rect(topleft=drop_pos)


	def check_collision_with_hero(self):
		col = pygame.sprite.collide_rect(self.rect, self.hero.rect)
		if col == True:
			match self.item:
				case 'branch': self.stats_manager += 1
				case 'circlet': self.stats_manager += 1
				case 'crown': self.stats_manager += 1
				case 'orb': self.stats_manager += 1
				case 'apex': self.stats_manager += 1

				case 'gauntlets': self.stats_manager += 1
				case 'belt': self.stats_manager += 1
				case 'axe': self.stats_manager += 1
				case 'reaver': self.stats_manager += 1

				case 'slippers': self.stats_manager += 1
				case 'band': self.stats_manager += 1
				case 'blade': self.stats_manager += 1
				case 'eaglesong': self.stats_manager += 1

				case 'mantle': self.stats_manager += 1
				case 'robe': self.stats_manager += 1
				case 'staff': self.stats_manager += 1
				case 'mystic': self.stats_manager += 1

			self.kill()


	def update(self, dt):
		# self.check_collision_with_hero()
		pass