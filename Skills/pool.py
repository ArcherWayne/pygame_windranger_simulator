from Skills.base import Base_Skill

# 技能池
class Skill_Pool():
    def __init__(self) -> None:
        self.pool = []
        self.key = 0

    def append(self, skill, unit):
        if isinstance(skill, Base_Skill):
            skill.print_skill_info()
            self.pool.append({'skill': skill, 'unit': unit, 'key': self.key})
            self.key += 1
    
    def update(self):
        for item in self.pool:
            skill = item.get('skill')
            skill.update()

    def get_skill_by_name(self, name):
        result = None
        for item in self.pool:
            skill = item.get('skill')
            if skill.name == name:
                result = skill
        return result

skill_pool = Skill_Pool()