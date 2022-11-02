

class SM:
	def __init__(self) -> None:
		self.stat = 100

	def update(self):
		self.stat += 100


class HERO:
	def __init__(self, sm) -> None:
		self.sm = sm

	def update(self):
		self.sm.stat += 100

sm = SM()
hero_1 = HERO(sm)
hero_2 = HERO(sm)

print(sm.stat)
print(hero_1.sm.stat)
print('\n')

hero_1.update()
print(sm.stat)
print(hero_1.sm.stat)
print(hero_2.sm.stat)
print('\n')

hero_2.update()
print(sm.stat)
print(hero_1.sm.stat)
print(hero_2.sm.stat)

print('\n')
sm.update()
print(sm.stat)
print(hero_1.sm.stat)
print(hero_2.sm.stat)