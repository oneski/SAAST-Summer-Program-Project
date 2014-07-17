'''
def monsterDiction(filename):
	monsterNames = []
	monsterLevels = []
	monsterTypes = []
	treasures = []
	monsterDict = {}
	f = open(filename).readlines()
	f = [x.replace("\n", "") for x in f]
	f.remove("Class,Type,Level,TreasureClass")
	g = [item.split(",") for item in f]
	for i in range(0, len(g)):
		monsterNames.append(g[i][0])
		monsterLevels.append(g[i][2])
		monsterTypes.append(g[i][1])
		treasures.append(g[i][3])
	for i in range(0, len(g)):
		monsterDict[monsterNames[i]] = [monsterLevels[i], monsterTypes[i], treasures[i]]
	return monsterDict

print monsterDiction("monstats_copy.txt")
'''

import random

def monster(filename):
	f = open(filename).readlines()
	f = [x.replace("\n", "") for x in f]
	f.remove("Class,Type,Level,TreasureClass")
	g = [item.split(",") for item in f]
	tc = g[random.randint(0,len(g)-1)][3]
	return tc

print monster("monstats.txt")

'''
def armor(argument_from_previous):
	armorDict = {}
	armorNames = []
	armorStats = []
	f = open(filename).readlines()
	f = [item.replace("\n", "") for item in f]
	f.remove("name,minac,maxac")
	g = [item.split(",") for item in f]
	for i in range(0, len(g)):
		armorNames.append(g[i][0])
	for i in range(0, len(g)):
		armorStats.append(g[i][0])
	return diction
'''

def armor(item, filename):
	with open(filename) as f:
		lines = [n.replace("\n", "").split(",") for n in f.readlines()[1:]]
	
	"""for i in range(0, len(g)):
		if g[i][0] == item:
			x = random.randint(int(g[i][1]), int(g[i][2]+1))
			return x
	"""
	for i in lines:
		if i[0] == item:
			a = int(i[1])
			b = int(i[2])
			rand =  random.randint(a, b)
			return rand



print armor("Leather Armor", "armor.txt")





