from drawingpanel import *

def animate(files="text.txt", height=500,width=500,fontt=16,timeout=200):
	
	def create_textt(canvas,fontr,textt):
		canvas.create_text(height/2,width/2,text=textt,font=fontr)


	def sleep(obj,timee):
		obj.update()
		time.sleep(timee / 1000.0)
		obj.update()

	fonter = ("Helvetica", fontt)
	panal = DrawingPanel(height,width)
	canvas = panal.canvas
	

	while True:
		try:
			 word = gen.next_word()
			 create_textt(canvas,fonter,word)
			 sleep(canvas,timeout)
		except ValueError:
			print "End of File"
			break


animate()