import random

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

print TC("Cow (H)")