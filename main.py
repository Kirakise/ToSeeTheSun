import pygame
# import Objects.Player
from Objects.Item import Item
from Objects.Enemy import Enemy
from Map import Map
import ScreenAndObjs as SO


FPS = 30
BLACK = (0, 0, 0)


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("To see the sun")
        self.clock = pygame.time.Clock()
        self.Map = Map()
        SO.sprites.add(SO.objects["Player"])
        SO.objects[SO.EnemyNum] = Enemy()
        SO.sprites.add(SO.objects[SO.EnemyNum])

    def main(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    SO.objects["Player"].Action(event.key, 1)
                elif event.type == pygame.KEYUP:
                    SO.objects["Player"].Action(event.key, 0)
            
            for i in SO.objects.copy().values():
                i.Tick()

            SO.sprites.update()
            SO.screen.fill(BLACK)
            SO.sprites.draw(SO.screen)
            self.Map.drawMap(SO.screen)
            pygame.display.flip()


game = Game()
game.main()
