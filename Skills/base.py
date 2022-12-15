from Config.setting import FPS
# FPS = 120

# 默认技能信息
# 只会录入下表中的技能信息
# 想加入新的技能属性,须要在此添加对应的键值对
default_skill_info = {
	"name": 'Skill Name',
	"desc": 'description',
	"cooldown": 0,
	"duration": 0,
	"damage": 0, # 技能伤害
	"is_active": True, # 主动技能
	"is_charge": False, # 充能技能
	"charge_limit": 0, # 充能上限
	"is_stackable": False, # 可叠加
	"stack_limit": 0 # 叠加上限
}

# 基础技能类
class Base_Skill():
	def __init__(self, skill_info, stats_manager) -> None:
		self.cooldown_frame = 0
		self.duration_frame = 0
		self.actived = False

		self.stats_manager = stats_manager

		# 判断传入技能信息
		# 键值对 -> 录入技能信息
		if isinstance(skill_info, dict):
			for key in default_skill_info: 
				self.__dict__[key] = skill_info.get(key, default_skill_info[key])
		# 数组 -> 录入技能信息
		elif isinstance(skill_info, list):
			for index, key in enumerate(default_skill_info): 
				self.__dict__[key] = skill_info[index] if len(skill_info) > index else default_skill_info[key]
		# 其他 -> 使用默认技能数值
		else:
			for key in default_skill_info: 
				self.__dict__[key] = default_skill_info[key]
		# 当前充能点数
		self.charge_count = self.charge_limit

	# 打印技能信息
	def print_skill_info(self):
		for key in default_skill_info: 
			print("{}:\t{}".format(key, self.__dict__[key]))

	# 更新技能CD
	def update(self):
		# update cooldown
		if self.is_charge:
			if self.cooldown_frame > 0:
				self.cooldown_frame += 1
			if self.cooldown_frame > self.cooldown * FPS:
				if self.charge_count < self.charge_limit:
					self.cooldown_frame = 1
					self.charge_count += 1
				else:
					self.cooldown_frame = 0
		else:
			if self.cooldown_frame > 0:
				self.cooldown_frame += 1
			if self.cooldown_frame > self.cooldown * FPS:
				self.cooldown_frame = 0
		# update duration
		if self.duration_frame > 0:
			self.duration_frame += 1
		if self.duration_frame > self.duration * FPS:
			self.duration_frame = 0
			self.actived = False
			self.destroy()

	def update_skill_cd_duration(self, *new_cd, new_duration):
		self.cooldown = new_cd
		self.duration = new_duration

	# 使用技能
	def use(self):		# 从外部调用的use函数, 释放技能
		if self.is_charge:
			if  self.charge_count > 0 and self.cooldown_frame == 0:
				self.actived = True
				self.cooldown_frame += 1
				self.duration_frame += 1
				self.charge_count -= 1
				self.active()
			else:
				print('skill [{}] is not ready!'.format(self.name))
		elif self.cooldown_frame == 0:
			self.actived = True
			self.cooldown_frame += 1		# cd 
			self.duration_frame += 1		# 持续时间
			self.active()
		else:
			print('skill [{}] is not ready!'.format(self.name))

	# 一般情况下,重写以下两个方法即可,不用重写use()
	# 技能实际效果
	def active(self):
		print('skill {} actived!'.format(self.name))

	# 技能效果结束
	def destroy(self):
		print('skill {} destroyed!'.format(self.name))

# 测试代码
def run1():
	base_skill = Base_Skill([])
	base_skill.print_skill_info()
	base_skill.use()
	pass

# run1()