import random
import time

def fight(p,m):
	enemies = m.get_enemies()
	damage_modifier = random.randint(0,len(enemies))
	turn = 0
	while len(enemies) > 0:
		time.sleep(1)
		turn+=1
		while True:
			print("\nTurn: "+ str(turn)+"\n")
			#clear()
			time.sleep(1)
			player_in = input("attack (a) or heal (h)? ")
			time.sleep(1)
			if player_in == "a" or player_in == "attack":
				if len(enemies) > 1:


					###Problem Area
					
					while True:
						player_in = input("Whom do you attack? Please enter the number. ")
						try:
							player_in = int(player_in)
							dmg = random.randint(2,p.damage)
							print("\nYou hit the "+ str(enemies[int(player_in)-1].name +" and deal " + str(max(0,dmg-enemies[int(player_in)-1].armor))+ " damage."))
							enemies[int(player_in)-1].get_hit(enemies[int(player_in)-1].hp,dmg)
							break
						except:
							print("Please give a valid number.")
		
				else:
					dmg = random.randint(2,p.damage)
					print("You hit the "+ str(enemies[0].name +" and deal " + str(max(0,dmg-enemies[0].armor))+ " damage."))
					enemies[0].get_hit(enemies[0].hp,dmg)
				break
			elif player_in == "h" or player_in == "heal":
				print("Healing does not work yet")
			else:
				print("Please choose between attack (a) and heal (h).")
			

		#enemies[0].get_hit(enemies[0].hp,p.damage)
		for i in range((len(enemies))):
			if enemies[i].hp <= 0:
				enemies.remove(enemies[i])
		for i in enemies:
			time.sleep(1)
			dmg = random.randint(1,i.damage)
			p.get_hit(p.hp,dmg)
			print(str(i.name) + " hits you for " + str(max(0,dmg-p.armor)) + " damage.")
		time.sleep(1)
		print("You have " + str(p.hp) + "hp left.")
	#if(p.hp < p.max_hp):
	#	print("You are wounded and have " + str(p.hp) + "hp left.")
	if damage_modifier > 0:
		time.sleep(1)
		print("\nDefeating your enemies made you stronger and increased your damage by " +str(damage_modifier))
		p.damage+=damage_modifier
