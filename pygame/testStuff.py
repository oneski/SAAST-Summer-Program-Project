import sys, pygame
pygame.init()

size = width, height = 350, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	if pygame.key.get_focused():
		press=pygame.key.get_pressed()
		if(press[273]):
			if(speed[1]<0):
				speed[1] -= 1
			else:
				speed[1] += 1
		elif(press[274]):
			if(speed[1]<0):
				speed[1] += 1
			else:
				speed[1] -= 1
		elif(press[275]):
			if(speed[0]<0):
				speed[0] += 1
			else:
				speed[0] -= 1




			speed[0] += 1
		elif(press[276]):
			speed[0] -= 1
	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()



"""

while True:
 for i in pygame.event.get():
  if i.type==QUIT:
   exit()
  a=100
  screen.fill((255,255,255))
  if pygame.key.get_focused():
   press=pygame.key.get_pressed()
   for i in xrange(0,len(press)): 
    if press[i]==1:
     name=pygame.key.name(i) 
     text=f1.render(name,True,(0,0,0))
     screen.blit(text,(100,a))
     a=a+100
   pygame.display.update()
  """