import random
import monsters

class Field:
	def __init__(self,enemies):
		self.enemies = enemies
		self.loot = []

	def print_state(self):
		if len(self.enemies) == 0:
			print ("\nYou raise your light, but the candle does not show Kitans closeby.")
		else:
			print("\nYou raise your light and the light of the candle falls on:")
			for i in self.enemies:
				print(i.name)


	@staticmethod
	def gen_random():
		rand = random.randint(0,3)
		if rand == 0:
			return Field([])
		if rand == 1:
			return Field([monsters.Cursed_Kitan()])
		if rand == 2:
			return Field([monsters.Enchanted_Kitan()])
		if rand == 3:
			return Field([monsters.Cursed_Kitan(),monsters.Enchanted_Kitan()])

class Map:
	def __init__(self,width, height):
		self.state = []
		self.x = 0
		self.y = 0
		for i in range(width):
			fields = []
			for j in range(height):
				fields.append(Field.gen_random())
			self.state.append(fields)


	def print_state(self):
		self.state[self.x][self.y].print_state()

	def get_enemies(self):
		return self.state[self.x][self.y].enemies

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