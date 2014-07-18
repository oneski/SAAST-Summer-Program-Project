def compute_inventories(words):
	output = {}
	for i in range(len(words)):
		output[words] = LetterInv(word)
	return output

def prune_by_inventory(dic, li):
	return {key : dic[key] for key in dic.keys() if is_in(dic[key], li)}

def prune_by_length(dic, n):
	return {key : dic[key] for key in dic.keys() if len(key) >= n}

def prune_by_w(dic):
	return {key : dic[key] for key in dic.keys() if key[0] == w}

def notMain(stringg,filename):
	output = []
	def iterator(stringgg,wordListt,listBuiltSoFar):
		invent = create_inventory(stringg)
		WordListt = prune_by_inventory(wordListt,invent)
		if len(WordListt):
			for key in WordList.keys():
				if(is_in(WordList[key],invent)):
					tempListBuiltSo = [x for x in listBuiltSoFar]
					tempListBuiltSo += [str(key)]
					if to_str(subtract(wordList[key],invent)) == "":
						output += [tempListBuiltSo]
					else:
						iterator(to_str(subtract(wordList[key],invent)),wordListt,tempListBuiltSo)
				else:
					pass
		else:
			pass

	wordList = []
	with open(filename) as f:
		wordList = f.readlines()

	iterator(stringg,wordList,[])
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