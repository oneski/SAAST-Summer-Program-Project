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

def notMain(stringg,wordList):
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


	iterator(stringg,wordList,[])
	return output

def create_inventory(s):

    letter_list = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    counts = [s.count(chr(c)) for c in range(ord('a'), ord('z') + 1)]
    z = zip(letter_list, counts)
    return {k : v for k, v in z}

def subtract(li1, li2):
    
    result = {}
    diffs = []
    for i in range(0, len(li1.values())):
        diffs.append(abs(li1[chr( ord('a') + i )] - li2[chr( ord('a') + i)]))
    z = zip([chr(c) for c in range(ord('a'), ord('z') + 1)], diffs)
    return {k : v for k,v in z}

def is_in(li1, li2):
    v1 = li1.values()
    v2 = li2.values()
    bools = []

    for i in range(0, len((v1)) - 1):
        if (v1[i] > 0):
            bools.append(v2[i] > 0)

    return False not in bools

def to_str(li):
    values = li.values()
    keys = li.keys()

    result = ""

    for i in range(0, len(keys) - 1):
        result += values[i] * str(keys[i])
    return result







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