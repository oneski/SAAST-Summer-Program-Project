import sys
import time
from drawingpanel import *

class WordGenerator:
	def __init__(self, files):
		self.lastAccess = 0
		self.in_quotes = False
		with open(files) as f:
			temp = []
			for line in f.readlines():
				temp.extend(line.split())
			self.words = temp
		
	def next_word(self):
		if not self.is_empty():
			output = self.words[self.lastAccess]
			self.lastAccess += 1
			if '"' in output:
				if(self.in_quotes):
					self.in_quotes = False
					return (output, True)
				else:
					self.in_quotes = True
					return (output, True)
			else:
				return (output, self.in_quotes)
		else:
			raise ValueError("End of File")

	def is_empty(self):
		return self.lastAccess >= len(self.words)

def main(args):
	if len(args) == 6:
		arg2, arg3, arg4 = int(args[2]), int(args[3]), int(args[4])
		arg1 = WordGenerator(args[1])	
		arg5 = 60 * 1000 / int(args[5])
		animate(arg1, arg2, arg3, arg4, arg5)

	else:
		print "fuck off"

def animate(generator, height=500,width=500,fontt=16,timeout=200):
	def create_textt(canvas,fontr,textt,colorr="#000"):
		canvas.create_text(height/2,width/2,text=textt,font=fontr,fill=colorr)

	def sleep(obj,timee):
		obj.update()
		time.sleep(timee / 1000.0)
		obj.update()

	fonter = ("Courier", fontt)
	panal = DrawingPanel(height,width)
	canvas = panal.canvas

	while True:
		try:
			canvas.create_rectangle(0, 0, height, width, fill = "white")
			word = generator.next_word()
			if(word[1]):
				if(word[0][len(word[0])-1] == "." or word[0][len(word[0])-1] == "," or word[0][len(word[0])-1] == ":" or word[0][len(word[0])-1] == ";" or word[0][len(word[0])-1] == "!" or word[0][len(word[0])-1] == "?"):
					create_textt(canvas,fonter,word[0],"#00b")
					sleep(canvas,timeout*1.3)
				else:
					create_textt(canvas,fonter,word[0],"#00b")
					sleep(canvas,timeout)
			else:
				if(word[0][len(word[0])-1] == "." or word[0][len(word[0])-1] == "," or word[0][len(word[0])-1] == ":" or word[0][len(word[0])-1] == ";" or word[0][len(word[0])-1] == "!" or word[0][len(word[0])-1] == "?"):
					create_textt(canvas,fonter,word[0])
					sleep(canvas,timeout*1.3)
				else:
					create_textt(canvas,fonter,word[0])
					sleep(canvas,timeout)
		except ValueError:
			print "End of File"
			break

if __name__ == "__main__":
	main(sys.argv)