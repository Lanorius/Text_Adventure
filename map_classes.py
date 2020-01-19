import random
import random
import monsters
import items

class Field:
	def __init__(self,enemies,items):
		self.enemies = enemies
		self.items = items

	def print_state(self):
		if len(self.enemies) == len(self.items) == 0:
			print("\nYou raise your light, but the candle does not show anything close by.")
		elif len(self.items) != 0:
			print("\nYou spot an item laying on the ground:")
			for i in self.items:
				print(i.name)
		else:
			print("\nYou raise your light and the light of the candle falls on:")
			for i in self.enemies:
				print(i.name)


	@staticmethod
	def gen_random():
		rand = random.randint(0,100)
		if rand % 5 == 0:
			return Field([monsters.Cursed_Kitan()],[])
		if rand % 4 == 0:
			return Field([monsters.Enchanted_Kitan()],[])
		if rand % 7 == 0:
			return Field([monsters.Cursed_Kitan(), monsters.Enchanted_Kitan()],[])
		if rand % 3 == 0:
			return Field([],[items.StaminaPotion()])
		else:
			#return Field([],[])
			return Field([], [items.StaminaPotion()])

class Map:
	def __init__(self,width, height):
		self.state = []
		self.x = 0
		self.y = 0
		boss_cords = (random.randint(0,width-1),random.randint(0,height-1))
		for i in range(width):
			fields = []
			for j in range(height):
				if (i,j) == boss_cords:
					fields.append(Field([monsters.Evil_Magic_Lizard()],[]))
				else:
					fields.append(Field.gen_random())
			self.state.append(fields)



	def print_state(self):
		self.state[self.x][self.y].print_state()

	def get_enemies(self):
		return self.state[self.x][self.y].enemies

	def get_items(self):
		return self.state[self.x][self.y].items

	def forward(self):
		if self.x == len(self.state[self.x]) - 1:
			print("The Evil Magic Lizard prevents you from leaving the plane.")
		else:
			self.x = self.x + 1

	def backward(self):
		if self.x == 0:
			print("The Evil Magic Lizard prevents you from leaving the plane.")
		else:
			self.x = self.x - 1

	def right(self):
		if self.y == len(self.state[self.x]) - 1:
			print("The Evil Magic Lizard prevents you from leaving the plane.")
		else:
			self.y = self.y + 1

	def left(self):
		if self.y == 0:
			print("The Evil Magic Lizard prevents you from leaving the plane.")
		else:
			self.y = self.y - 1