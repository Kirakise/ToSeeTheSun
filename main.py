import pygame
from Objects.Player import Player
from Objects.Item import Item
from Objects.Enemy import Enemy
# from Map.MapController import MapController
from Map.Room.RoomController import RoomController
from Map.Room.MonsterRoomController import MonsterRoomController


WIDTH = 1366
HEIGHT = 768
FPS = 30
BLACK = (0, 0, 0)


class Game:

    def __init__(self):
        # Инициализация окна
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("To See The Sun")
        self.clock = pygame.time.Clock()
        self.objects = {"Player": Player(self.screen)}

        # temporary (Room as Map)
        # Генерация комнаты
        self.Map = RoomController()
        self.gameMap = self.Map.generate_start_room()

        # Группировка спрайтов
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.objects["Player"])

    def main(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                # Ввод
                if event.type == pygame.QUIT:
                    break
                # Реакция на управление персонажем
                elif event.type == pygame.KEYDOWN:
                    self.objects["Player"].Action(event.key, 1)
                elif event.type == pygame.KEYUP:
                    self.objects["Player"].Action(event.key, 0)
            
            for i in self.objects.values():
                i.Tick()

            # Отрисовка
            self.sprites.update()
            self.screen.fill(BLACK)
            self.Map.draw_room(self.screen, self.gameMap)
            self.sprites.draw(self.screen)
            pygame.display.flip()

game = Game()
game.main()
