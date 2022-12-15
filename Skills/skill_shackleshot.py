from Skills.base import Base_Skill

class Skill_Shackleshot(Base_Skill):
	def __init__(self, skill_info, stats_manager, creep_group) -> None:
		super().__init__(skill_info, stats_manager)
		self.creep_group = creep_group
		# self.hero = hero

	def	active(self):
		# return super().active()
		for sprite in self.creep_group:
			sprite.rooted(self.duration)

	def destroy(self):
		return super().destroy()