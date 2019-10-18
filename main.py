#####################################
#!/usr/bin/env python               #
#authors are constantly updated     #
# authors: Wirless / hnrkcode / ... #
# Title: Paddle Royale              #
#####################################

#required libraries
import pygame
from ball import Ball
from goal import Goal
from paddle import Paddle

# Color enumerators
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

def main():
    # Pygame initialize.
    pygame.init()

    # Main variables.
    winner = ""
    loser = "Loser"

    # Players health.
    scoreA = 3
    scoreB = 3
    scoreC = 3
    scoreD = 3

    # Window size and initialization + Title "Title is not showing because FPS is on".
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Paddle Royale")

    # Init the paddles.
    paddleA = Paddle(RED, (1, 80), (20, 200))
    paddleB = Paddle(BLUE, (1, 80), (670, 200))
    paddleC = Paddle(YELLOW, (80, 1), (200, 15))
    paddleD = Paddle(GREEN, (80, 1), (250, 480))

    # Init the goals.
    goalA = Goal(RED, (5, 800), (0, 0))
    goalB = Goal(BLUE, (5, 735), (695, 1))
    goalC = Goal(YELLOW, (700, 5), (0, 0))
    goalD = Goal(GREEN, (700, 5), (0, 495))

    # Init the ball.
    ball = Ball(WHITE, (10, 10), (345, 195))

    # group sprites
    all_sprites_list = pygame.sprite.Group()

    # Add all the sprites to the window.
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(paddleC)
    all_sprites_list.add(paddleD)
    all_sprites_list.add(goalA)
    all_sprites_list.add(ball)
    all_sprites_list.add(goalB)
    all_sprites_list.add(goalC)
    all_sprites_list.add(goalD)

    # Looping if it breaks out we could have restart or switch between screens.
    carryOn = True

    # Initialize clock for frame counting.
    clock = pygame.time.Clock()

    # Start game.
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                #exit game with p
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    carryOn = False

        # Controls
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

        # update sprites in real time while the game plays.
        all_sprites_list.update()
        # Ball bounce of walls (not yet goals) score point
        if ball.rect.x >= 690:
            scoreB -= 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreA -= 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            scoreD -= 1
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            scoreC -= 1
            ball.velocity[1] = -ball.velocity[1]
        # ball physics to push ball away if it gets behind the paddle
        if ball.rect.x >= 660 and pygame.sprite.collide_mask(ball, paddleB) and scoreB >= 1:
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 660
        if ball.rect.x <= 30 and pygame.sprite.collide_mask(ball, paddleA) and scoreA >= 1:
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 30
        if ball.rect.y > 470 and pygame.sprite.collide_mask(ball, paddleD) and scoreD >= 1:
            ball.velocity[1] = -ball.velocity[1]
            ball.rect.y = 470
        if ball.rect.y < 25 and pygame.sprite.collide_mask(ball, paddleC) and scoreC >= 1:
            ball.velocity[1] = -ball.velocity[1]
            ball.rect.y = 25
        # ball physics to bounce on collision with paddles checks for score to disable bouncing as paddle object stays in game its just sprite that stops rendering.
        if pygame.sprite.collide_mask(ball, paddleA) and scoreA >= 1:
            ball.bounce()
        elif pygame.sprite.collide_mask(ball, paddleB) and scoreB >= 1:
            ball.bounce()
        elif pygame.sprite.collide_mask(ball, paddleC) and scoreC >= 1:
            ball.bounce()
        elif pygame.sprite.collide_mask(ball, paddleD) and scoreD >= 1:
            ball.bounce()
        # BEGIN removing the sprite of each paddle once player dies.
        if scoreA <= 0:
            all_sprites_list.remove(paddleA)
        if scoreB <= 0:
            all_sprites_list.remove(paddleB)
        if scoreC <= 0:
            all_sprites_list.remove(paddleC)
        if scoreD <= 0:
            all_sprites_list.remove(paddleD)
        # screen color or backdrop
        screen.fill(BLACK)
        # draw the sprites from the group onto the scene
        all_sprites_list.draw(screen)
        # update me please anytime i move
        # scoring logic
        font = pygame.font.Font(None, 74)
        if scoreA >= 1 and winner != "red":
            text = font.render(str(scoreA), 1, RED)
            screen.blit(text, (250, 10))
        elif scoreA <= 0 and winner != "red":
            text = font.render(str(loser), 1, RED)
            screen.blit(text, (250, 10))
        if scoreB >= 1 and winner != "blue":
            text = font.render(str(scoreB), 1, BLUE)
            screen.blit(text, (420, 10))
        elif scoreB <= 0 and winner != "blue":
            text = font.render(str(loser), 1, BLUE)
            screen.blit(text, (420, 10))
        if scoreC >= 1 and winner != "yellow":
            text = font.render(str(scoreC), 1, YELLOW)
            screen.blit(text, (420, 420))
        elif scoreC <= 0 and winner != "yellow":
            text = font.render(str(loser), 1, YELLOW)
            screen.blit(text, (420, 420))
        if scoreD >= 1 and winner != "green":
            text = font.render(str(scoreD), 1, GREEN)
            screen.blit(text, (250, 420))
        elif scoreD <= 0 and winner != "green":
            text = font.render(str(loser), 1, GREEN)
            screen.blit(text, (250, 420))
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
            text = font.render(str("winner"), 1, RED)
            screen.blit(text, (250, 250))
        elif winner == "blue":
            text = font.render(str("winner"), 1, BLUE)
            screen.blit(text, (250, 250))
        elif winner == "yellow":
            text = font.render(str("winner"), 1, YELLOW)
            screen.blit(text, (250, 250))
        elif winner == "green":
            text = font.render(str("winner"), 1, GREEN)
            screen.blit(text, (250, 250))
        pygame.display.flip()
        # framers per /s
        clock.tick(60)
        # display FPS instead of title
        pygame.display.set_caption("fps: " + str(clock.get_fps()))
    # goodybe
    pygame.quit()

if __name__ == '__main__':
    main()
