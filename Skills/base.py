# from Config.setting import FPS
FPS = 120

# 默认技能信息
# 只会录入下表中的技能信息
# 想加入新的技能属性,须要在此添加对应的键值对
default_skill_info = {
    "name": 'Skill Name',
    "desc": 'description',
    "is_active": True, # 主动技能
    "cooldown": 0,
    "duration": 0,
    "is_charge": False, # 充能技能
    "charge_limit": 0, # 充能上限
    "is_stackable": False, # 可叠加
    "stack_limit": 0 # 叠加上限
}

# 基础技能类
class Base_Skill():
    def __init__(self, skill_info) -> None:
        self.cooldown_frame = 0
        self.duration_frame = 0
        self.actived = False
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
                self.cooldown_frame = 0
                if self.charge_count < self.charge_limit:
                    self.charge_count += 1
                else:
                    self.cooldown = 0
        else:
            if self.cooldown_frame > 0:
                self.cooldown_frame += 1
            if self.cooldown_frame > self.cooldown * FPS:
                self.cooldown_frame = 0
                self.cooldown = 0
        # update duration
        if self.duration_frame > 0:
            self.duration_frame += 1
        if self.duration_frame > self.duration * FPS:
            self.duration_frame = 0
            self.duration = 0
            self.destroy()

    # 使用技能
    def use(self):
        if self.is_charge and self.charge_count > 0:
            if self.cooldown == 0:
                self.active()
                self.charge_count -= 1
        elif self.cooldown == 0:
            self.active()

    # 技能实际效果
    # 一般情况下,重写该方法即可,不用重写use()
    def active(self):
        print('skill {} actived!'.format(self.name))
        self.actived = True
        pass

    def destroy(self):
        print('skill {} destroyed!'.format(self.name))
        self.actived = False
        pass

# 测试代码
def run1():
    base_skill = Base_Skill([])
    base_skill.print_skill_info()
    base_skill.use()
    pass

run1()