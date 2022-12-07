from Skills.base import Base_Skill

class Skill_Galeforce(Base_Skill):
	def __init__(self, skill_info, creep_group) -> None:
		super().__init__(skill_info)
		self.creep_group = creep_group

	def active(self):
		for sprite in self.creep_group.sprites():
			sprite.set_knockback_wa_acceleration(500)

	def destroy(self):
		return super().destroy()