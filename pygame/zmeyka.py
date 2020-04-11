import pygame 
import random

pygame.init()
screen=pygame.display.set_mode((800,600))


background = pygame.Surface(screen.get_size()) 
ballsurface= pygame.Surface(screen.get_size())    
x=20
y=20
a=random.randint(10,790)
b=random.randint(10,590)

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                pygame.draw.circle(screen,(120,120,120),(a,b),10,5)    
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
            y=y-1
        if event.key==pygame.K_DOWN:
            y=y+1
        if event.key==pygame.K_RIGHT:
            x=x+1
        if event.key==pygame.K_LEFT:
            x=x-1
        if x<20:
            x=780 
        if x>780:
            x=20       
        if y<20:
            y=580 
        if y>580:
            y=20 

    screen.fill((0,0,0))        
    pygame.draw.circle(screen,(50,0,255),(x,y),20,5)                 
    pygame.display.flip()        
                    
