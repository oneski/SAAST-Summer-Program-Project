'''
input a list, return with a list of all the permutations of the list
'''
from random import shuffle
from math import factorial
debugTest = 0
def safe_permutations(listt,debugTest):
	
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
		debugTest += 1
		#print x
		output = contains(output,x)
		#print output
	print debugTest
	return output
	return debugTest
	

print safe_permutations([1,2,3,4,5,6],debugTest)
