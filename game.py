import pygame,sys,math
from classes import*
from process import process
pygame.init()
SCREENWIDTH,SCREENHEIGHT=640,360
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)
#img_bug = pygame.image.load("t1nuvola_apps_bug.png")
clock = pygame.time.Clock()
FPS = 24
total_frames =0
background =pygame.image.load("images/bg3.png")
bug = Bug(0,SCREENHEIGHT-100,"images/xyz.png")
#fly = Fly(40,100,100,100,"images/fly.png")
#fly1 = Fly(40,200,100,100,"images/fly.png")
#fly2 = Fly(40,300,100,100,"images/fly.png")
#fly3 = Fly(40,400,100,100,"images/fly.png")


while True:
	process(bug,FPS,total_frames)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit() 
	bug.motion(SCREENWIDTH,SCREENHEIGHT)
	Fly.update_all(SCREENWIDTH,SCREENHEIGHT)

	BugProjectile.movement()
	total_frames+=1
	#fly.fly(SCREENWIDTH)
	#i+=1
	#if i>255:
	#	i%=255
	#screen.fill((0,0,0))
	screen.blit(background,(0,0))
	BaseClass.allsprites.draw(screen)
	BugProjectile.List.draw(screen)
	#totalframes += 1
	#if totalframes % fivesecondinterval == 0:
	#	pass 
	#pygame.draw.line(screen,clr2, (0,0),(640,360),5)
	#pygame.draw.rect(screen,clr3,(40,40,300,45))
	#pygame.draw.circle(screen,clr1,(350,200),80,1)
	#screen.blit(img_bug,(200,200))
	pygame.display.flip()
	clock.tick(FPS)
