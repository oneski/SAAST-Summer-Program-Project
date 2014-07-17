import random
from random import randint

def loot_generator():
	pickedTC = "Cow (H)"
	item = TC(pickedTC)
	# defense = armor(item)
	preSufData = preSuf(randint(0, 3))

	print preSufData[0] + item + preSufData[2]
	#print "Defense: " + defense
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

loot_generator()