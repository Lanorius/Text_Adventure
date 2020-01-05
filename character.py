class Character:
	def __init__(self, name, hp, mana, capacity, strength, armor, inteligence, damage, healing):#,inventory):
		self.name = name
		self.hp = hp
		self.mana = mana
		self.capacity = capacity
		self.strength = strength
		self.armor = armor
		self.inteligence = inteligence 
		self.damage = damage
		self.healing = healing
		#self.inventory = []

	def attack(self,):
		pass

	def get_hit(self,hp,damage):
		self.hp = self.hp - max(0,(damage-self.armor))
		if self.hp <= 0:
			self.die()

	def die(self):
		exit("Everything turns dark. The magic Kitan, takes your soul.")




class Player(Character):
	def __init__(self,name, player_class, hp, mana, capacity, strength, armor, inteligence, damage, healing):
		Character.__init__(self, name, hp, mana, capacity, strength, armor, inteligence, damage, healing)
		self.name = name
		self.player_class = player_class
		self.max_hp = hp
		self.max_mana = mana

	def rest(self):
		self.hp = self.max_hp
		self.mana = self.max_mana
