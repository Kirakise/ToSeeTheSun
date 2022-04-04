import pygame
import Objects.Player as PL
import Objects.Item as Item
from Objects.Enemy import Enemy
from Map.Room.ShoppingRoomController import ShoppingRoomController
import ScreenAndObjs as SO


class Game:
    def __init__(self):
        # Инициализация окна
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("To see the sun")
        self.clock = pygame.time.Clock()
        self.Map = ShoppingRoomController()
        self.gameMap = self.Map.generate_room()
        SO.objects["Player"] = PL.Player()
        SO.sprites.add(SO.objects["Player"])
        Enemy(0, SO.WIDTH /2 - 40, SO.HEIGHT / 2 - 40)
        Enemy(1)
        Item.SpeedArt(30, 33);
        Item.SpeedArt(50, 33);
        Item.SpeedArt(70, 33);
        Item.SpeedArt(90, 33);
        Item.SpeedArt(110, 33);
        Item.TreasureChest(150, 33);

    def main(self):
        while True:
            self.clock.tick(SO.FPS)

            for event in pygame.event.get():
                # Ввод
                if event.type == pygame.QUIT:
                    return

                elif event.type == pygame.KEYDOWN:
                    SO.objects["Player"].Action(event.key, 1)
                elif event.type == pygame.KEYUP:
                    SO.objects["Player"].Action(event.key, 0)
            
            for i in SO.objects.copy().values():
                i.Tick()
            SO.sprites.update()
            SO.screen.fill(SO.BLACK)
            self.Map.draw_room(SO.screen, self.gameMap)
            SO.sprites.draw(SO.screen)
            pygame.display.flip()

game = Game()
game.main()
