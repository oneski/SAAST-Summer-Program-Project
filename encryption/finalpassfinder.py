from string import ascii_lowercase

output = []

def notMain(stringg,filename):
	global output
	class LetterInv:
	    """LetterInv : 
	    attributes:
	    	- content: returns a dictionary that maps each letter of the alphabet to the number of times it appears in the string s
	    methods:
	    	- subtract: returns a dictionary mapping each letter to the number of times it shows up in self minus the number of times it shows up in content of li2
	    	- is_in: returns a boolean if content of obj self is in obj li2 (bigger one is an argument)
	    	- to_str: returns a string of the content of obj self
	    	- prune: GET SHIT WORKING
	    """
	    def __init__(self, s):
	        counts = [s.count(chr(c)) for c in range(ord('a'), ord('z') + 1)]
	        z = zip(list(ascii_lowercase), counts)
	        self.content = {k : v for k, v in z}

	    def subtract(self, li2):
	        diffs = []
	        for i in range(0, len(self.content.values())):
	            diffs.append(abs(self.content[chr(ord('a') + i )] - li2.content[chr(ord('a') + i)]))
	        z = zip(list(ascii_lowercase), diffs)
	      	output = LetterInv("")
	      	output.content = {k : v for k, v in z}
	        return output

	    def is_in(self, li2):
	    	output = True
	    	for key in self.content.keys():
	    		if(self.content[key] <= li2.content[key]):
	    			continue
	    		else:
	    			output = False
	    			break
	    	return output

	    def to_str(self):
	        values = self.content.values()
	        keys = self.content.keys()
	        result = ""
	        for i in range(0, len(keys)):
	            result += values[i] * str(keys[i])
	        return ''.join(sorted(result))

	def compute_inventories(words):
		# returns a dictionary mapping each word in words to a letter inventory object
		output = {}
		for i in range(len(words)):
			output[words[i]] = LetterInv(words[i])
		return output

	def prune_by_inventory(dic, li):
		# returns a dictionary (mapping words to letterinvs) with all of the words that are in the li
		return {key : dic[key] for key in dic.keys() if dic[key].is_in(li)}

	def prune_by_length(dic, n):
		# returns a dictionary (mapping words to letterinvs) with all of the words that are greater than or equal to n letters long
		return {key : dic[key] for key in dic.keys() if len(key) >= n}

	def prune_by_w(dic):
		# returns a dictionary (mapping words to letterinvs) with all of the words that start with "w"
		return {key : dic[key] for key in dic.keys() if key[0] == "w"}

	def iterator(invent,objectDic,listBuiltSoFar):
		print "Calling iterator on " + invent.to_str()
		global output
		if len(objectDic): # if there is still and eligible word (WHEN DO WE CHECK THERE ARE ELIGIBLE WORDS?)
			print "b"
			for key in objectDic.keys(): # for each eligible word:
				print "c", listBuiltSoFar, key
				if(objectDic[key].is_in(invent)): # if the eligible word is in the overall inventory 
					print "d"
					tempListBuiltSo = [x for x in listBuiltSoFar]
					tempListBuiltSo += [str(key)]
					if not sum(objectDic[key].subtract(invent).content.values()): # This checks if the word picked finished off the string, doesn't actually remove the letter counts of the added word
						output += [tempListBuiltSo] # add the list of words to the output
						print "e", output, invent.to_str(), listBuiltSoFar
					else:
						print "e1"
						iterator(invent.subtract(objectDic[key]),objectDic,tempListBuiltSo)
				else:
					print "d1"
					pass
		else:
			print "b1"
			pass

	wordlist = []
	with open(filename) as f:
		wordlist = [x.lower().strip() for x in f.readlines()]
	wordList = compute_inventories(wordlist) # This makes wordList into the dictionary of objects
	#wordList = prune_by_length(prune_by_inventory(prune_by_w(wordList), stringg), 10)
	invent = LetterInv(stringg)

	iterator(invent,wordList,[]) # Args: What is left of the string that we are trying to decode (still the full thing at this), the list of eligible words, and the list of words currently being built
	return output


def main():
	print notMain("doghousefuckoff", "wordlist.txt")

main()