import pygame

#Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Color Setting
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialize pygame
pygame.init()

#Window title
pygame.display.set_caption("Ball")

#Set Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock();

ball_x = int(SCREEN_WIDTH / 2)
ball_y = int(SCREEN_HEIGHT / 2)
ball_dx = 4
ball_dy = 4
ball_size = 40

#Ongoing game
done = False

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True


    #Game Logic
    ball_x += ball_dx
    ball_y += ball_dy

    if(ball_x + ball_size) > SCREEN_WIDTH or (ball_x - ball_size) < 0:
        ball_dx = ball_dx*-1
    if (ball_y + ball_size) > SCREEN_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy = ball_dy * -1

    #Delete Screen

    #Fill the Screen
    screen.fill(WHITE)

    #draw the screen
    pygame.draw.circle(screen, BLUE, [ball_x, ball_y], ball_size, 0)


    #Update the screen
    pygame.display.flip()

    #초당 60프레임
    clock.tick(60)

pygame.quit()
