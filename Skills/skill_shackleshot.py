from Skills.base import Base_Skill

class Skill_Shackleshot(Base_Skill):
	def __init__(self, skill_info, creep_group, hero) -> None:
		super().__init__(skill_info)
		self.creep_group = creep_group
		self.hero = hero

	def	active(self):
		return super().active()

	def destroy(self):
		return super().destroy()