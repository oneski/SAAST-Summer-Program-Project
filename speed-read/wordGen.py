#IMPORTS
import random

#VARIBLE DEFININTIONS
class WordGenerator:
	"""Deck of Cards"""
	def __init__(self, files):
		self.lastAccess = 0
		with open(files) as f:
			self.words = f.readlines()[0].split().strip()
		
	def hit(self,stack):
		if(self.lastAccess<len(self.words)):
			output =  self.words[lastAccess]
			self.lastAccess += 1
			return output
		else:
			raise ValueError("End of File")
		stack.lastAccess += 1

