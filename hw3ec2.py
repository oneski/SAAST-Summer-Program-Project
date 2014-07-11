'''
input a list, return with a list of all the permutations of the list
'''
from random import shuffle
from math import factorial
#x = [1,2,3]
#shuffle(x)
#print x

def contains(output, l):
	for ls in output:
		if(l == ls):
			return
		else:
			output.append(l)

"""def permutations(listt):
	# list -> list of lists
	output = [listt]
	x = listt
	while (len(output) < factorial(len(listt))):
		shuffle(x)
		print x
		contains(output,x)
	print output
"""
#permutations([1,2])


def safe_permutations(listt):
	
	def contains(op, l):
		i = 0
		for ls in op:
			if(l == ls):
				factorial(3)
			else:
				i+=1
		if(i == len(op)):
			op += [l]
		return op

	output = [listt]

	#print output
	while len(output) < factorial(len(listt)):
		x = [s for s in listt]
		shuffle(x)
		#print x
		output = contains(output,x)
		#print output
	return output
	

print safe_permutations(["t","s"])

"""
listx = [1,2,3]
newList = [listx[randint(0,len(listx) - 1)]]


def """




"""print x
		i = 0
		while i < (len(output)-1):
			if(output[i] == x):
				break
			i += 1
		if(i == (len(output)-1)):
			output.append(x)
			
		if(len(output)>= factorial(len(listt))):
			break"""