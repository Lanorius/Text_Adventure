import random

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
				print(self.name +" looks exhausted.")
			else:
				print(self.name +" is very exhaused.")
		if self.hp <= 0:
			self.die()

	def healing(self):
		if (random.randint(1,101) >= self.hp/self.max_hp*100):
			print("You removed the curse!")
			self.hp = 0
			if self.name == "Evil Magic Lizard":
				exit("You have defeated the Evil Magic Lizard, and all Kitans are free!\n Thank you for playing!")
		else:
			print("The curse resisted the healing.")


	def is_dead(self):
		return self.hp <= 0

	def die(self):
		if self.name == "Evil Magic Lizard":
			exit("You have defeated the Evil Magic Lizard, and all Kitans are free!\n Thank you for playing!")
		else:
			print(self.name +" was so exhaused from playing that it rolled on the ground and purs very happily.")

class Cursed_Kitan(Monster):
	def __init__(self):
		Monster.__init__(self,"Cursed Kitan",20,0,2,4)

class Enchanted_Kitan(Monster):
	def __init__(self):
		Monster.__init__(self,"Enchanted Kitan",10,10,0,6)

class Evil_Magic_Lizard(Monster):
	def __init__(self):
		Monster.__init__(self,"Evil Magic Lizard",200,100,3,15)
