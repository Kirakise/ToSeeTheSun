import pygame
from Objects.Player import Player
from Objects.Item import Item
from Objects.Enemy import Enemy
from Map import Map

WIDTH = 360
HEIGHT = 480
FPS = 30
BLACK = (0, 0, 0)


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("To see the sun")
        self.clock = pygame.time.Clock()
        self.objects = {"Player": Player()}
        self.Map = Map()

    def main(self):
        while True:
            """ # Считать Ввод """
            self.screen.fill(BLACK)
            """ # Обновить кадр """
            """ # Вывести кадр """
