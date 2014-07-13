from drawingpanel import *
import random

'''
def upTriangle(canvas,x,y,z):
		canvas.create_polygon([x,y+z,x+z/2,y,x+z,y+z],outline="black", fill="white") #fill with rand colors later
		sirP(canvas,x,y,n-1,z)

def sirP(canvas,x,y,n,z):


	if(n==0):
		pass
	elif(n==1):
		upTriangle(canvas,x, y,z)
	else:
		upTriangle(canvas, 3*x/4, y,z/2)
		upTriangle(canvas, x/2, y/2, z/2)
		upTriangle(canvas, x/4, y, z/2)


def main():

	panal = DrawingPanel(500,500)
	canvas = panal.canvas
	sirP(canvas,100,100,3,100)

main()
'''

def downTriangle(canvas,x,y,z,n):
		canvas.create_polygon([x,y+z,x+z/2,y+2*z,x+z,y+z],outline="black", fill="white")
		sirP(canvas, x,y,z,n-1)

def background(canvas,x,y,z):
	canvas.create_polygon([x,y+z,x+z/2,y,x+z,y+z],outline="black", fill="white")

def sirP(canvas, x, y, z, n):
	if n == 0:
		#background(canvas, x, y, z)
		pass
	elif n == 1:
		#downTriangle(canvas, x/2, y, z/2)
		pass
	else:
		downTriangle(canvas,x*1.25, y, z/2,n)
		downTriangle(canvas,x*.75,y*3, z/2,n)
		downTriangle(canvas,x*1.75,y*3,z/2,n)


def main():
	panal = DrawingPanel(500,500)
	canvas = panal.canvas
	background(canvas, 50, 50, 200)
	#downTriangle(canvas, 100, 50, 100,0) #center
	"""downTriangle(canvas, 125, 50, 50) #top triangle
	downTriangle(canvas, 75, 150, 50) #bottom left
	downTriangle(canvas, 175, 150, 50) #bottom right"""
	sirP(canvas,100,50,100,3)

main()
