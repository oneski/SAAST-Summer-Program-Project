import random
from random import randint

def loot_generator():
	monster = genMonster()
	item = TC(monster[3])
	defense = armor(item)
	preSufData = preSuf(randint(0, 3))

	print "Fighting " + monster[0] + " (Level " + monster[1] + " " + monster[2] + ")..."
	print "You have slain " + monster[0]
	print monster[0] + " dropped:"
	print ""
	print preSufData[0] + item + preSufData[2]
	print "Defense: " + str(defense)
	if preSufData[1] != "": print preSufData[1]
	if preSufData[3] != "": print preSufData[3]

def TC(inputTC):
	def generate(classes, tok):
		if tok not in classes:
			return tok
		else:
			return generate(classes, random.choice(classes[tok].split(",")))

	with open("TreasureClassEx.txt") as f:
		lines = f.readlines()[1:]
	classes = {}
	for line in lines:
		a, b = line.split(",", 1)
		classes[a] = b.strip()
	return generate(classes, inputTC)

def preSuf(a):
	roll = a
	#print roll
	if(roll == 0):
		return ("","","","")
	elif(roll == 1):
		f = open("MagicPrefix.txt").readlines()
		f = [item.replace("\n", "").split(",") for item in f[1:len(f)]]
		selector = randint(0,len(f)-1)
		attibute = str(randint(int(f[selector][2]),int((f[selector][3])))) + " " + str(f[selector][1])

		return (f[selector][0]+ " ", attibute,"","")
	elif(roll == 2):
		f = open("MagicSuffix.txt").readlines()
		f = [item.replace("\n", "").split(",") for item in f[1:len(f)]]
		selector = randint(0,len(f)-1)
		attibute = str(randint(int(f[selector][2]),int((f[selector][3])))) + " " + str(f[selector][1])
		
		return ("",""," "+f[selector][0], attibute)
	else:
		pref = preSuf(1)
		suff = preSuf(2)
		return (pref[0],pref[1],suff[2],suff[3])

def genMonster():
	with open("monstats.txt") as f:
		lines = [x.replace("\n", "") for x in f.readlines()[1:]]
	g = [item.split(",") for item in lines]
	monster = g[random.randint(0,len(g)-1)]
	return monster

def armor(item):
	with open("armor.txt") as f:
		lines = [n.replace("\n", "").split(",") for n in f.readlines()[1:]]

	for i in lines:
		if i[0] == item:
			a = int(i[1])
			b = int(i[2])
			return random.randint(a, b)
print loot_generator()