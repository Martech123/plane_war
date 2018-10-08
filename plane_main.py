import pygame
from plane_sprite import *

SCREEN_SIZE = pygame.Rect(0, 0, 480, 700)
FPS = 60
class PlaneGame(object):


    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)
        self.clock = pygame.time.Clock()

        self.__create_sprites()

    def __create_sprites(self):
        pass
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass
    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()
    
    def start_game(self):
        print("游戏开始")
        while True:
            self.clock.tick(FPS)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

if __name__ == "__main__":


    game = PlaneGame()


    game.start_game()
