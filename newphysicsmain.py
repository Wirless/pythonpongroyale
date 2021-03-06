#####################################
#!/usr/bin/env python               #
# authors are constantly updated     #
# authors: Wirless / hnrkcode / ... #
# Title: Paddle Royale              #
#####################################
from sounds import SoundEffect
from random import randint

# required libraries
import pygame

import settings
from ball import Ball
from goal import Goal
from paddle import Paddle


def restart():
    main()
def main():
    # pygame initialize
    pygame.init()
    # BOTS turn True to turn on all bots. ---01Variables
    winner = ""
    loser = ""
    time_elapsed = 0
    dt = pygame.time.get_ticks()
    if settings.AUDIO == True:
        sfxc = SoundEffect(settings.CJ, 1.0)
        sfxc.play()
    # Players health
    scoreA = 3
    scoreB = 3
    scoreC = 3
    scoreD = 3
    # window size and initialization + Title "Title is not showing because FPS is on"
    size = (700, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Paddle Royale")

    # Paddle Initialization
    paddleA = Paddle(settings.RED, (10, 80), (20, 200))
    paddleB = Paddle(settings.BLUE, (10, 80), (670, 200))
    paddleC = Paddle(settings.YELLOW, (80, 10), (200, 15))
    paddleD = Paddle(settings.GREEN, (80, 10), (250, 680))

    # Goal initialization "sprite"
    goalA = Goal(settings.RED, (5, 800), (0, 0))
    goalB = Goal(settings.BLUE, (5, 735), (695, 1))
    goalC = Goal(settings.YELLOW, (700, 5), (0, 0))
    goalD = Goal(settings.GREEN, (700, 5), (0, 695))

    ball = Ball(settings.WHITE, (10, 10), (randint(300,400), randint(300,400)))

    # group sprites
    all_sprites_list = pygame.sprite.Group()

    # add all the sprites to the window
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(paddleC)
    all_sprites_list.add(paddleD)
    all_sprites_list.add(goalA)
    all_sprites_list.add(ball)
    all_sprites_list.add(goalB)
    all_sprites_list.add(goalC)
    all_sprites_list.add(goalD)

    # looping if it breaks out we could have restart or switch between screens
    carryOn = True

    # initialize clock for frame counting
    clock = pygame.time.Clock()

    # START
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                # exit game with p
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    carryOn = False
                #might just make variable or something.
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("space up")
                    ball.bounce
        # Controls
        ball.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            ball.bouncedouble3()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)
        if keys[pygame.K_a]:
            paddleC.moveLeft(5)
        if keys[pygame.K_d]:
            paddleC.moveRight(5)
        if keys[pygame.K_LEFT]:
            paddleD.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            paddleD.moveRight(5)
        if settings.BOTS == True:
            # Blue Paddle AI
            if paddleB.rect.y+40 > ball.rect.y:
                paddleB.moveUp(randint(1,3))
            if paddleB.rect.y+40 < ball.rect.y:
                paddleB.moveDown(randint(1,3))
            # Paddle red AI
            if paddleA.rect.y+40 > ball.rect.y:
                paddleA.moveUp(randint(1,3))
            if paddleA.rect.y+40 < ball.rect.y:
                paddleA.moveDown(randint(1,3))
            # Paddle Yellow AI
            if paddleC.rect.x+40 < ball.rect.x:
                paddleC.moveRight(randint(1,3))
            if paddleC.rect.x+40 > ball.rect.x:
                paddleC.moveLeft(randint(1,3))
            # Paddle Green AI
            if paddleD.rect.x+40 < ball.rect.x:
                paddleD.moveRight(randint(1,3))
            if paddleD.rect.x+40 > ball.rect.x:
                paddleD.moveLeft(randint(1,3))
        # update sprites in real time while the game plays.
        all_sprites_list.update()
        # Ball bounce of walls (not yet goals) score point
        
        if ball.rect.x >= settings.RIGHT_WALL:
            scoreB -= 1
            ball.bounce()
            if scoreB > -1:
                ball.sound_effect()
        if ball.rect.x <= settings.LEFT_WALL:
            scoreA -= 1
            ball.bounce()
            if scoreA > -1:
                ball.sound_effect()
        if ball.rect.y > settings.BOTTOM_WALL:
            scoreD -= 1
            ball.bounce2()
            if scoreD > -1:
                ball.sound_effect()
        if ball.rect.y < settings.TOP_WALL:
            scoreC -= 1
            ball.bounce2()
            if scoreC > -1:
                ball.sound_effect()

        if ball.rect.y < -10:
            all_sprites_list.remove(ball)
            ball = Ball(settings.WHITE, (10, 10), (randint(300,400), randint(300,400)))
            all_sprites_list.add(ball)
        if ball.rect.y > 710:
            all_sprites_list.remove(ball)
            ball = Ball(settings.WHITE, (10, 10), (randint(300,400), randint(300,400)))
            all_sprites_list.add(ball)
        if ball.rect.x < -10:
            all_sprites_list.remove(ball)
            ball = Ball(settings.WHITE, (10, 10), (randint(300,400), randint(300,400)))
            all_sprites_list.add(ball)
        if ball.rect.y > 710:
            all_sprites_list.remove(ball)
            ball = Ball(settings.WHITE, (10, 10), (randint(300,400), randint(300,400)))
            all_sprites_list.add(ball)
        # ball physics to push ball away if it gets behind the paddle
        if (
            pygame.sprite.collide_mask(ball, paddleB)
            and scoreB >= 1
        ):
            ball.bounce()
            ball.rect.x = 660
            ball.sound_effect2()
        if (
            pygame.sprite.collide_mask(ball, paddleA)
            and scoreA >= 1
        ):
            ball.bounce()
            ball.rect.x = 30
            ball.sound_effect2()
        if (
            pygame.sprite.collide_mask(ball, paddleD)
            and scoreD >= 1
        ):
            ball.bounce2()
            ball.rect.y = 670
            ball.sound_effect2()
        if (
            pygame.sprite.collide_mask(ball, paddleC)
            and scoreC >= 1
        ):
            ball.bounce2()
            ball.rect.y = 25
            ball.sound_effect2()
        #
        #
        #
        #
        #Ball velocity in straight line #OOGBERROR
        #if (
        #    ball.velocity[1] < 1.0
        #    and ball.velocity[1] > -1.0
        #):
        #    ball.bounce()
        #if (
        #    ball.velocity[0] < 1.0 
        #    and ball.velocity[0] > -1.0
        #):
        #    ball.bounce() 
        #    
        # ball physics to bounce on collision with paddles checks for score to disable bouncing as paddle object stays in game its just sprite that stops rendering.
        ######
        #Issue 1
        #if ball.rect.right == paddleB.rect.left:
        #    ball.bounce()
        #
        # What happens when ball hits Paddle
        #if pygame.sprite.collide_mask(ball, paddleA) and scoreA >= 1:
        #    ball.bounce()
        #if ball.rect.right == paddleB.rect.left:
        #    if ball.velocity[0] == +ball.velocity[0] and ball.velocity[1] == -ball.velocity[1]:
        #        ball.velocity[0] = -ball.velocity[0]
        #        ball.velocity[1] = -ball.velocity[1]
        #
        #        
        # BEGIN removing the sprite of each paddle once player dies.
        if scoreA == 0:
            paddleA.sound_effect()
            scoreA-= 1
        if scoreB == 0:
            paddleB.sound_effect()
            scoreB-= 1
        if scoreC == 0:
            paddleC.sound_effect()
            scoreC-= 1
        if scoreD == 0:
            paddleD.sound_effect()
            scoreD-= 1
        if scoreA <= 0:
            all_sprites_list.remove(paddleA)
        if scoreB <= 0:
            all_sprites_list.remove(paddleB)
        if scoreC <= 0:
            all_sprites_list.remove(paddleC)
        if scoreD <= 0:
            all_sprites_list.remove(paddleD)
        # screen color or backdrop
        screen.fill(settings.BLACK)
        # draw the sprites from the group onto the scene
        all_sprites_list.draw(screen)
        # update me please anytime i move
        # scoring logic
        font = pygame.font.Font(None, 50)
        if settings.DEBUG == True:
            text = font.render(str(ball.direction), 1, settings.RED)
            screen.blit(text, (200, 250))
            text = font.render(str(ball.speed), 1, settings.RED)
            screen.blit(text, (200, 450))
            text = font.render(str(ball.rect.x), 1, settings.WHITE)
            screen.blit(text, (200, 350))
            text = font.render(str(ball.rect.y), 1, settings.WHITE) 
            screen.blit(text, (200, 550))
            text = font.render(str('X:'), 1, settings.WHITE)
            screen.blit(text, (160, 350))
            text = font.render(str('Y:'), 1, settings.WHITE) 
            screen.blit(text, (160, 550))
            text = font.render(str('bounce count'), 1, settings.PURPLE)
            screen.blit(text, (400,500))
            text = font.render(str(ball.bouncecount), 1, settings.PURPLE)
            screen.blit(text, (400, 540))
        if scoreA >= 1 and winner != "red":
            text = font.render(str(scoreA), 1, settings.RED)
            screen.blit(text, (25, 10))
        elif scoreA <= 0 and winner != "red":
            text = font.render(str(loser), 1, settings.RED)
            screen.blit(text, (25, 10))
        if scoreB >= 1 and winner != "blue":
            text = font.render(str(scoreB), 1, settings.BLUE)
            screen.blit(text, (640, 620))
        elif scoreB <= 0 and winner != "blue":
            text = font.render(str(loser), 1, settings.BLUE)
            screen.blit(text, (640, 620))
        if scoreC >= 1 and winner != "yellow":
            text = font.render(str(scoreC), 1, settings.YELLOW)
            screen.blit(text, (640, 10))
        elif scoreC <= 0 and winner != "yellow":
            text = font.render(str(loser), 1, settings.YELLOW)
            screen.blit(text, (640, 10))
        if scoreD >= 1 and winner != "green":
            text = font.render(str(scoreD), 1, settings.GREEN)
            screen.blit(text, (25, 620))
        elif scoreD <= 0 and winner != "green":
            text = font.render(str(loser), 1, settings.GREEN)
            screen.blit(text, (25, 620))
        if scoreA >= 1 and scoreB <= 0 and scoreC <= 0 and scoreD <= 0:
            winner = "red"
            scoreA += 100
        elif scoreB >= 1 and scoreA <= 0 and scoreC <= 0 and scoreD <= 0:
            winner = "blue"
            scoreB += 100
        elif scoreC >= 1 and scoreA <= 0 and scoreB <= 0 and scoreD <= 0:
            winner = "yellow"
            scoreC += 100
        elif scoreD >= 1 and scoreA <= 0 and scoreB <= 0 and scoreC <= 0:
            winner = "green"
            scoreD += 100

        if winner == "red":
            text = font.render(str("winner"), 1, settings.RED)
            screen.blit(text, (250, 250))
        # carryOn = False
        elif winner == "blue":
            text = font.render(str("winner"), 1, settings.BLUE)
            screen.blit(text, (250, 250))
        elif winner == "yellow":
            text = font.render(str("winner"), 1, settings.YELLOW)
            screen.blit(text, (250, 250))
        elif winner == "green":
            text = font.render(str("winner"), 1, settings.GREEN)
            screen.blit(text, (250, 250))
        pygame.display.flip()
        # framers per /s
        clock.tick(60)
        # display FPS instead of title
        # pygame.display.set_caption("fps: " + str(clock.get_fps()))
        if winner != '':
            restart()
            
    # goodybe
    pygame.quit()


if __name__ == "__main__":
    main()
