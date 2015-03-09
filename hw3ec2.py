'''
input a list, return with a list of all the permutations of the list
'''
#ORIGINAL VERSION
"""
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
	return debugTests
	

#print safe_permutations([1,2,3,4,5,6],debugTest)
"""
"""
GOAL OF FINAL VERSION:

[1,2,3]  = input

output = []
	
 	1				2			3
 [1,2,3][0]  -> [2,3][0]	-> [3][0] -> None  therefore add combination to the list... and back track

 							<-cant iterate
 	1				3				2
 [1,2,3][0]  -> [2,3][1]	->	[2][0] -> None therefore add combination to the list... and back track

 			<- cant iterate	<- cant iterate
 	2				1				3
 [1,2,3][1]	 -> [1,3][0]	->	[3][0] -> None therefore add combination to the list... and back track

.....

 <-  cant iterate <- cant iterate <- cant iterate     NO1 can iterate therefore return output list

return [[1,2,3],[1,3,2]...[3,2,1]]

"""
#FINAL VERSION  
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
print permutate(range(3))