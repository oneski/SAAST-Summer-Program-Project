def main(stringg,wordList):
	output = []
	def iterator(stringgg,wordListt,listBuiltSoFar):
		invent = create_inventory(stringg)
		for key in WordList.getKeys():
			if(is_in(WordList[key],invent)):
				tempListBuiltSo = [x for x in listBuiltSoFar]
				tempListBuiltSo += [str(key)]
				if to_str(subtract(wordList[key],invent)) == "":
					output += [tempListBuiltSo]
				else:
					iterator(to_str(subtract(wordList[key],invent)),wordListt,tempListBuiltSo)
			else:
				pass


	iterator(stringg,wordList)
	return output



	"""def permutate(inputt):
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
	return output"""