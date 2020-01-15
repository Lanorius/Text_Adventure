class Item:
	def __init__self(self, weight, worth):
		self.weight = weight
		self.worth = worth

class Potion(Item):
	def __init__self(self, weight, worth):
		Item.__init__(self,weight,worth)

class StaminaPotion(Potion):
	def __init__self(self, weight, worth, regenerated_health=10):
		Potion.__init__(self, weight, worth)
		self.regenerated_health = regenerated_health