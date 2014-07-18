class LetterInv:
	def __init__(self, string):
		self.letterDict = {}
		for i in range(26):
			self.letterDict[chr(i + 97)] = 0
		for char in string:
			self.letterDict[char] += 1

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