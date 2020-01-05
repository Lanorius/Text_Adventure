class Monster: 
	def __init__(self, name, hp, mana, armor, damage):
		self.name = name
		self.hp = hp
		self.mana = mana
		self.armor = armor
		self.damage = damage
		self.max_hp = hp

	def get_hit(self,hp,damage):
		self.hp = self.hp - max(0,(damage - self.armor))
		if self.hp <= 0.5*self.max_hp:
			if self.hp >= 0.2*self.max_hp:
				print(self.name +" looks damaged.")
			else:
				print(self.name +" is heavily damaged.")
		if self.hp <= 0:
			self.die()

	def is_dead(self):
		return self.hp <= 0

	def die(self):
		print(self.name +" was defeated.")

class Cursed_Kitan(Monster):
	def __init__(self):
		Monster.__init__(self,"Cursed Kitan",20,0,2,4)

class Enchanted_Kitan(Monster):
	def __init__(self):
		Monster.__init__(self,"Enchanted Kitan",10,10,0,6)