import random
#import time

def fight(p,m,i):
	enemies = m.get_enemies()
	damage_modifier = random.randint(0,len(enemies))
	turn = 0
	while len(enemies) > 0:
		#time.sleep(1)
		turn+=1
		while True:
			print("\nTurn: "+ str(turn)+"\n")
			#clear()
			#time.sleep(1)
			player_in = input("play (p) or heal (h)? ")
			#time.sleep(1)

			if player_in == "p" or player_in == "play":
				play(p,m,enemies)
				break
			elif player_in == "h" or player_in == "heal":
				heal(p,m,enemies)
				break

			else:
				print("Please choose between play (p) and heal (h).")

		for i in range((len(enemies)-1),-1,-1):
			if enemies[i].hp <= 0:
				enemies.remove(enemies[i])


		for i in enemies:
			#time.sleep(1)
			dmg = random.randint(1,i.damage)
			p.get_hit(p.hp,dmg)
			print(str(i.name) + " plays with you and removes " + str(max(0,dmg-p.armor)) + " points of your stamina.")
		#time.sleep(1)
		print("You have " + str(p.hp) + " stamina left.")
	#if(p.hp < p.max_hp):
	#	print("You are wounded and have " + str(p.hp) + "hp left.")
	if damage_modifier > 0:
		#time.sleep(1)
		print("\nFreeing the Kitan made you even better at playing around!") #+str(damage_modifier))
		p.damage+=damage_modifier



def play(p,m,enemies):
	if len(enemies) > 1:
		while True:
			player_in = input("Whom do you play with? Please enter the number. ")
			try:
				player_in = int(player_in)
				dmg = random.randint(2,p.damage)
				print("\nYou play with the "+ str(enemies[int(player_in)-1].name +" and remove " + str(max(0,dmg-enemies[int(player_in)-1].armor))+ " points of their stamina."))
				enemies[int(player_in)-1].get_hit(enemies[int(player_in)-1].hp,dmg)
				break
			except:
				print("Please give a valid number.")
		
	else:
		dmg = random.randint(2,p.damage)
		print("\nYou play with the "+ str(enemies[0].name + " and remove " + str(max(0,dmg-enemies[0].armor))+ " points of their stamina."))
		enemies[0].get_hit(enemies[0].hp,dmg)
	

def heal(p,m,enemies):
	if len(enemies) > 1:
		while True:
			player_in = input("Whom do you try to heal? Please enter the number. ")
			try:
				player_in = int(player_in)
				enemies[int(player_in)-1].healing()
				break
			except:
				print("Please give a valid number.")	
	else:
		enemies[0].healing()