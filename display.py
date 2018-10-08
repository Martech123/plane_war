import pygame
from plane_sprite import *

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0, 0))
# pygame.display.update()


hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150, 150))
pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 150, 102, 126)

enermy = GameSprite("./images/enemy1_down1.png", 1)
enermy2 = GameSprite("./images/enemy1_down1.png", 2)
enermy3 = GameSprite("./images/enemy1_down1.png", 3)
enermy_group = pygame.sprite.Group(enermy, enermy2, enermy3)
while True:

    clock.tick(60)
    hero_rect.y -= 1 
    if hero_rect.y < -126:
        hero_rect.y = 700
    screen.blit(bg,(0, 0))
    screen.blit(hero, hero_rect)
    enermy.update()
    enermy2.update()
    enermy3.update()
    enermy_group.draw(screen)
    pygame.display.update()
    

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            print("tuchu")
            pygame.quit()
            exit()

