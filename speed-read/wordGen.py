#IMPORTS
import random

#VARIBLE DEFININTIONS
class WordGenerator:
	"""Deck of Cards"""
	def __init__(self, files):
		self.lastAccess = 0
		with open(files) as f:
			temp = []
			for line in f.readlines():
				temp.extend(line.split())
			self.words = temp
		
	def next_word(self):
		if(self.lastAccess<len(self.words)):
			output = self.words[self.lastAccess]
			self.lastAccess += 1
			return output
		else:
			raise ValueError("End of File")

	def is_empty(self):
		return True if self.lastAccess >= len(self.words) else False