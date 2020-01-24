class Item:
	def __init__(self, name, weight, worth):
		self.name = name
		self.weight = weight
		self.worth = worth

class Potion(Item):
	def __init__(self):
		Item.__init__(self,name, weight,worth)

class StaminaPotion(Potion):
	def __init__(self, health = 10):
		Item.__init__(self, "Stamina_Potion",2,3)
		self.health = health

