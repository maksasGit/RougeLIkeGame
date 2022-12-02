import pygame, sys
from sys import exit
from level import Level
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(((SCREEN_WIDTH,SCREEN_HEIGHT)))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pygame.display.set_caption("kek")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
