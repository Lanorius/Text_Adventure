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
		exit("You were defeated. Everything turns dark. The magic Lizard, takes your soul.")




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

class Warrior(Character):
	def __init__(self, name, player_class = "Warrior", hp = 200, mana = 0, capacity = 30, strength = 20, armor = 5, inteligence= 10, damage = 5, healing = 0):
		Character.__init__(self, name, hp, mana, capacity, strength, armor, inteligence, damage, healing)
		self.name = name
		self.player_class = player_class
		self.max_hp = hp
		self.max_mana = mana

class Wizard(Character):
	def __init__(self, name, player_class="Wizard", hp=100, mana=100, capacity=20, strength=10, armor=3, inteligence=20, damage=8, healing=10):
		Character.__init__(self, name, hp, mana, capacity, strength, armor, inteligence, damage, healing)
		self.name = name
		self.player_class = player_class
		self.max_hp = hp
		self.max_mana = mana

class Rogue(Character):
	def __init__(self, name, player_class="Rogue", hp=125, mana=0, capacity=20, strength=10, armor=4, inteligence=10, damage=7, healing=0):
		Character.__init__(self, name, hp, mana, capacity, strength, armor, inteligence, damage, healing)
		self.name = name
		self.player_class = player_class
		self.max_hp = hp
		self.max_mana = mana

class Bunny(Character):
	def __init__(self, name, player_class="Bunny", hp=5000, mana=1000, capacity=200, strength=200, armor=20, inteligence=200, damage=100, healing=100):
		Character.__init__(self, name, hp, mana, capacity, strength, armor, inteligence, damage, healing)
		self.name = name
		self.player_class = player_class
		self.max_hp = hp
		self.max_mana = mana


Classes = {
	'Warrior': Warrior,
	'Wizard': Wizard,
	'Rogue': Rogue,
	'Bunny': Bunny,
	#'Thief': Thief,
	#'Bunny': Bunny,

}
