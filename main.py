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
        self.objects = {"Player": Player(self.screen)}
        self.Map = Map()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.objects["Player"])

    def main(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.KEYDOWN:
                    self.objects["Player"].Action(event.key, 1)
                elif event.type == pygame.KEYUP:
                    self.objects["Player"].Action(event.key, 0)
            
            for i in self.objects.values():
                i.Tick()
                    
            self.sprites.update()
            self.screen.fill(BLACK)
            self.sprites.draw(self.screen)
            self.Map.drawMap(self.screen)
            pygame.display.flip()


game = Game()
game.main()
