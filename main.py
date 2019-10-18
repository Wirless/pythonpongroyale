#!/usr/bin/env python

# some paddle yoke
# Created by some wee man
from paddle import Paddle
from ball import Ball
from goal import Goal
import pygame
pygame.init()

#we got em colours
winner = ''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)
loser = 'Loser'
#application is here
scoreA = 3
scoreB = 3
scoreC = 3
scoreD = 3
size =	(700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paddle Royale")
#initthepaddle
paddleA = Paddle(RED, 1, 80)
paddleA.rect.x = 20
paddleA.rect.y = 200

goalA = Goal(RED, 5, 800)
goalA.rect.x = 0
goalA.rect.y = 0

goalB = Goal(BLUE, 5, 735)
goalB.rect.x = 695
goalB.rect.y = 1

#
goalC = Goal(YELLOW, 700, 5)
goalC.rect.x = 0
goalC.rect.y = 0
#
goalD = Goal(GREEN, 700, 5)
goalD.rect.x = 0
goalD.rect.y = 495
 
paddleB = Paddle(BLUE, 1, 80)
paddleB.rect.x = 670
paddleB.rect.y = 200

paddleC = Paddle(YELLOW, 80, 1)
paddleC.rect.x = 200
paddleC.rect.y = 15

paddleD = Paddle(GREEN, 80, 1)
paddleD.rect.x = 250
paddleD.rect.y = 480

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
#ay
all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(paddleC)
all_sprites_list.add(paddleD)
all_sprites_list.add(goalA)
all_sprites_list.add(ball)
all_sprites_list.add(goalB)
all_sprites_list.add(goalC)
all_sprites_list.add(goalD)
#looping
carryOn = True

#time weeman
clock = pygame.time.Clock()


#START
while carryOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_p:
				carryOn=False
				
	#keying
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddleA.moveUp(10)
	if keys[pygame.K_s]:
		paddleA.moveDown(10)
	if keys[pygame.K_UP]:
		paddleB.moveUp(10)
	if keys[pygame.K_DOWN]:
		paddleB.moveDown(10)
	if keys[pygame.K_a]:
		paddleC.moveLeft(10)
	if keys[pygame.K_d]:
		paddleC.moveRight(10)
	if keys[pygame.K_LEFT]:
		paddleD.moveLeft(10)
	if keys[pygame.K_RIGHT]:
		paddleD.moveRight(10)
				
	#logicke
	all_sprites_list.update()
	#ibeballing
	if ball.rect.x>= 690:
		scoreB-=1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x<=0:
		scoreA-=1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.y>490:
		scoreD-=1
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y<0:
		scoreC-=1
		ball.velocity[1] = -ball.velocity[1]
		

	if ball.rect.x>=670 and pygame.sprite.collide_mask(ball, paddleB) and scoreB>=1:
		ball.velocity[0] = -ball.velocity[0]
		ball.rect.x = 665
	if ball.rect.x<=20 and pygame.sprite.collide_mask(ball, paddleA) and scoreA>=1:
		ball.velocity[0] = -ball.velocity[0]
		ball.rect.x = 25
	if ball.rect.y>480 and pygame.sprite.collide_mask(ball, paddleD) and scoreD>=1:
		ball.velocity[1] = -ball.velocity[1]
		ball.rect.y = 475
	if ball.rect.y<15 and pygame.sprite.collide_mask(ball,paddleC) and scoreC>=1:
		ball.velocity[1] = -ball.velocity[1]
		ball.rect.y = 20
		
	if pygame.sprite.collide_mask(ball, paddleA) and scoreA >= 1:
		ball.bounce()
	elif pygame.sprite.collide_mask(ball, paddleB) and scoreB >= 1:
		ball.bounce()
	elif pygame.sprite.collide_mask(ball, paddleC) and scoreC >= 1:
		ball.bounce()
	elif pygame.sprite.collide_mask(ball, paddleD) and scoreD >=1:
		ball.bounce()
    #BEGIN REMOVING PADDLES sprites remove but object is still there :o
	if scoreA <= 0:
		all_sprites_list.remove(paddleA)
	if scoreB <= 0:
		all_sprites_list.remove(paddleB)
	if scoreC <= 0:
		all_sprites_list.remove(paddleC)
	if scoreD <= 0:
		all_sprites_list.remove(paddleD)
	#screen color or backdrop
	screen.fill(BLACK)

	#remove this line and create 4 coloured offset lines
	
	all_sprites_list.draw(screen)
	# update me please anytime i move
	#scorez
	font = pygame.font.Font(None, 74)
	if scoreA >= 1:
		text = font.render(str(scoreA), 1, RED)
		screen.blit(text, (250,10))
	elif scoreA <= 0:
		text = font.render(str(loser), 1, RED)
		screen.blit(text, (250,10))
	if scoreB >= 1:
		text = font.render(str(scoreB), 1, BLUE)
		screen.blit(text, (420,10))
	elif scoreB <= 0:
		text = font.render(str(loser), 1, BLUE)
		screen.blit(text, (420,10))
	if scoreC >=1:
		text = font.render(str(scoreC), 1, YELLOW)
		screen.blit(text, (420,420))
	elif scoreC <=0:
		text = font.render(str(loser), 1, YELLOW)
		screen.blit(text, (420,420))
	if scoreD >=1:
		text = font.render(str(scoreD), 1, GREEN)
		screen.blit(text, (250,420))
	elif scoreD <=0:
		text = font.render(str(loser), 1, GREEN)
		screen.blit(text, (250,420))
	if scoreA >=1 and scoreB <=0 and scoreC <=0 and scoreD <=0:
		winner = 'red'
	elif scoreB >=1 and scoreA<=0 and scoreC<=0 and scoreD<=0:
		winner = 'blue'

	elif scoreC >=1 and scoreA<=0 and scoreB<=0 and scoreD<=0:
		winner = 'yellow'

	elif scoreD >=1 and scoreA<=0 and scoreB<=0 and scoreC<=0:
		winner = 'green'

	
	if winner == 'red':
		text = font.render(str('winner'), 1, RED)
		screen.blit(text, (250,250))
	elif winner == 'blue':
		text = font.render(str('winner'), 1, BLUE)
		screen.blit(text, (250,250))
	elif winner == 'yellow':
		text = font.render(str('winner'), 1, YELLOW)
		screen.blit(text, (250,250))
	elif winner == 'green':
		text = font.render(str('winner'), 1, GREEN)
		screen.blit(text, (250,250))
	pygame.display.flip()
	#im timer
	clock.tick(60)
	pygame.display.set_caption("fps: " + str(clock.get_fps()))
#goodybe	
pygame.quit()
