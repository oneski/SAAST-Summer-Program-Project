def permutate(inputt):
	output = []
	def iterate(listBuiltSoFar, leftoverInput):
		if len(leftoverInput) == 1:
			listBuiltSoFar.append(leftoverInput[0])
			output.append(listBuiltSoFar)
		else:	
			for i in range(len(leftoverInput)):
				tempLeftover = [x for x in leftoverInput]
				tempLeftover.pop(i)
				tempListBuilt = [x for x in listBuiltSoFar]
				tempListBuilt.append(leftoverInput[i])
				iterate(tempListBuilt, tempLeftover)
	iterate([], inputt)
	return output

def nub(listt):
	output = []
	for i in listt:
		if i not in output:
			output.append(i)
	return output
def intersect(right,down):
	a = ["r" for item in range(0,down-1)]
	b = ["d" for itme in range(0,right-1)]
	a += b
	c = nub(permutate(a))
	print len(c)
	return c 
	#permutate()\


print intersect(3,3)

