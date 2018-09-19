import pygame
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")



carryOn = True

clock = pygame.time.Clock()


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False



    screen.fill(WHITE)


    pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)


    pygame.display.flip()


    clock.tick(60)


pygame.quit()


