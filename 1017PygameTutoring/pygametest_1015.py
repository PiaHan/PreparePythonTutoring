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
pygame.display.set_caption("pygame")

#Set Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock();

#Ongoing game
done = False

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True


    #Game Logic

    #Delete Screen

    #Fill the Screen
    screen.fill(WHITE)

    #draw the screen

    #Update the screen
    pygame.display.flip()

    #초당 60프레임
    clock.tick(60)