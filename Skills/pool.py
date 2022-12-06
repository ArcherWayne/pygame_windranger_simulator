from Skills.base import Base_Skill

# 技能池
class Skill_Pool():
    def __init__(self) -> None:
        self.pool = []
        self.key = 0

    def append(self, skill, unit):
        if isinstance(skill, Base_Skill):
            self.pool.append({'skill': skill, 'unit': unit, 'key': self.key})
            self.key += 1
    
    def update(self):
        for skill in self.pool:
            skill.update()