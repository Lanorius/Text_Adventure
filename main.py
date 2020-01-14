#Magic Kitan 
import random
import os
#import time
#my own files
from os.path import sep

import character
import commands
import map_classes
import items #unused 
#import fight

clear = lambda: os.system('clear') #on Linux System


if __name__ == '__main__':
	#time.sleep(1)
	print("\nWelcome young Kitan.")
	#time.sleep(3)
	s= """\nThis is a dark place. Many Kitans were taken by the Evil Magic Lizard. They were put under a spell, but you can heal them. Before you can do that you need to play with them to make them exhausted."""

	print(s+"\n")
	#time.sleep(5)
	print("You have an everburning candle, that shows you your surroundings after each step.\n")
	#time.sleep(3)

	#def __init__(self,name, player_class, hp, mana, capacity, strength, armor, inteligence, damage, healing)
	name = input("Choose a name young Kitan. ")
	#time.sleep(2)
	while True:
		print("Here is a list of professions you might have: ")
		print(*(list(character.Classes.keys())), sep =", ")
		player_class = input("What class do you chose Kitan?")

		try:
			p = character.Classes[player_class](name,str(player_class))
			break
		except:
			print("Be specific young Kitan. Type the exact name, please.\n")

		'''
		if player_class == "Warrior":
			p = character.Player(name, "Warrior", 200,0,30,5,3,0.3,5,0)
			break
		elif player_class == "Wizard":
			p = character.Player(name, "Wizard", 100,100,15,1,1,0.8,8,5)
			break
		else:
			print("Be specific young Kitan. Type the exact name, please.\n")
		'''

	map = map_classes.Map(5,5)
	print("(type help to list the available commands)\n")
	while True:
		command = input(">").lower().split(" ")
		if command[0] in commands.Commands:
			commands.Commands[command[0]](p, map)
		else:
			print("Use one of the commands.")
		#map.print_state()