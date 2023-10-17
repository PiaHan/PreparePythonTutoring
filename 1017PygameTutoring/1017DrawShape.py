import pygame

#Screen Size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

#Color Setting
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialize pygame
pygame.init()

#Window title
pygame.display.set_caption("Drawing")

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
    #This part with shaping

    #Draw line
    pygame.draw.line(screen, RED, [50, 50], [500, 50], 10)
    pygame.draw.line(screen, GREEN, [50, 100], [500, 100], 10)
    pygame.draw.line(screen, BLUE, [50, 150], [500, 150], 10)

    #Rectangular
    pygame.draw.rect(screen, RED, [50, 200, 150, 150], 4)

    #Polygon
    pygame.draw.polygon(screen, GREEN, [[350, 200], [250, 350], [450, 350]], 4)

    #Circle
    pygame.draw.circle(screen, BLUE, [150, 450], 60, 4)

    #Elipse
    pygame.draw.ellipse(screen, BLUE, [250, 400, 200, 100], 0)

    #Font
    font = pygame.font.SysFont('FixedSys', 40, True, False)

    #Espress Test Style
    text = font.render("Hello pygame", True, BLACK)

    #Output Text
    screen.blit(text, [200, 600])

    #Update the screen
    pygame.display.flip()

    #초당 60프레임
    clock.tick(60)