import fight



def inventory(p,m):
	pass

def illuminate(p,m):
	m.print_state()

def forward(p,m):
	m.forward()
	m.print_state()
	#clear()

def backward(p,m):
	m.backward()
	m.print_state()
	#clear()

def right(p,m):
	m.right()
	m.print_state()
	#clear()

def left(p,m):
	m.left()
	m.print_state()
	#clear()

def save():
	pass

def load():
	pass

def quit_game(p,m):
	print("The magic Kitan appears and takes you away.")
	exit(0)


def print_help(p,m):
	print("The commands of this game are: ")
	print(*(list(Commands.keys())), sep =', ')

def pickup(p,m):
	pass

def rest(p,m):
	p.rest()


Commands = {
	'help': print_help,
	'illuminate': illuminate,
	'quit': quit_game,
	#'pickup': pickup,
	#'check inventory': inventory,
	'forward': forward,
	'backward': backward,
	'right': right,
	'left': left,
	'fight': fight.fight,
	#'save': save,
	#'load': load,
	#'rest': rest,
	#'run': run_away
}