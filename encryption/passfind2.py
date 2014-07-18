def main(stringg,wordList):
	output = []
	current = []
	def iterator(stringgg,wordListt):
		invent = create_inventory(stringg)
		for key in WordList.getKeys():
			if(is_in(WordList[key],invent)):
				current += [str(key)]
				if to_str(subtract(wordList[key],invent)) == "":
					output += [current]
					current = []
				else:
					iterator(to_str(subtract(wordList[key],invent)),wordListt)
	
	iterator(stringg,wordList)
	return output
	

			
