#importing modules
import pygame
from pygame.locals import *
from sys import exit
  
  
#initializing variables
pygame.init()
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Key Press Test")
f1=pygame.font.SysFont("comicsansms",24)
  
#main loop which displays the pressed keys on the screen
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
      print i
      name=pygame.key.name(i) 
      text=f1.render(name,True,(0,0,0))
      screen.blit(text,(100,a))
      a=a+100
   pygame.display.update()


   rt  ctrl 305
   winodws 311
   menu 319
   home 278
   page up 280
   oage down 281
   end 279

   scoll 302
   pause 19
   insert 277
   del 127
