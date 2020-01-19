import fight
#import inventory
import items



def illuminate(p,m,i):
	m.print_state()

def forward(p,m,i):
	m.forward()
	m.print_state()
	#clear()

def backward(p,m,i):
	m.backward()
	m.print_state()
	#clear()

def right(p,m,i):
	m.right()
	m.print_state()
	#clear()

def left(p,m,i):
	m.left()
	m.print_state()
	#clear()

def save():
	pass

def load():
	pass

def quit_game(p,m,i):
	print("The magic Lizard appears and takes you away.")
	exit(0)


def print_help(p,m,i):
	print("The commands of this game are: ")
	print(*(list(Commands.keys())), sep =', ')

def inventory(p,m,i):
	i.show_items()

def pick_up(p,m,i):
	found_items = m.get_items()
	for j in range((len(found_items)-1),-1,-1):
		if p.capacity >= found_items[j].weight:
			print("You pick up the "+str(found_items[j].name)+".")
			p.capacity -= found_items[j].weight
			i.items.append(found_items[j])
			found_items.remove(found_items[j])
		else:
			print("The items are to heavy.")

def rest(p,m,i):
	p.rest()


Commands = {
	'help': print_help,
	'illuminate': illuminate,
	'forward': forward,
	'backward': backward,
	'right': right,
	'left': left,
	'fight': fight.fight,
	'pick_up': pick_up,
	'inventory': inventory,
	'quit': quit_game,
	#'save': save,
	#'load': load,
	#'rest': rest,
	#'run': run_away
}