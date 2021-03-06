import pygame
from Map.Room.Tile import Tile

wall = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/wall/brick_brown1.png')
floor = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/floor/cobble_blood3.png')
rock = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/item/amulet/cameo_blue.png')
planks = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/item/amulet/eye_cyan.png')
wood = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/item/amulet/eye_cyan.png')
box = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-misc/blood_green.png')
barrel = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-misc/blood_red1.png')
chest = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-misc/blood_red4.png')

enemy = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/player/base/centaur_brown_f.png')
trader = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/player/base/centaur_brown_f.png')


class RoomService:
    def __init__(self):
        self.Tile = Tile()

    def generate_room(self, file):
        # Чтение и разделение файла на список строк
        roomMap = file.read().splitlines()

        # Разделение списка на массив списков
        for i in range(0, len(roomMap)):
            roomMap[i] = roomMap[i].split()

        file.close()

        return roomMap

    # Отрисовка сетки
    def draw_room(self, screen, room):
        for x in range(len(room)):
            for y in range(len(room[x])):
                # Отрисовка верхних угловых тайлов
                if room[x][y] == self.Tile.left_top_corner():
                    self.Tile.draw_tile(screen, wall, y, x)
                if room[x][y] == self.Tile.right_top_corner():
                    self.Tile.draw_tile(screen, wall, y, x)

                # Отрисовка нижних угловых тайлов
                if room[x][y] == self.Tile.left_bottom_corner():
                    self.Tile.draw_tile(screen, wall, y, x)
                if room[x][y] == self.Tile.right_bottom_corner():
                    self.Tile.draw_tile(screen, wall, y, x)

                # Отрисовка тайлов левой, вернхней/нижней и правой стены
                if room[x][y] == self.Tile.left_wall():
                    self.Tile.draw_tile(screen, wall, y, x)

                if room[x][y] == self.Tile.top_middle_wall():
                    self.Tile.draw_tile(screen, wall, y, x)
                if room[x][y] == self.Tile.bot_middle_wall():
                    self.Tile.draw_tile(screen, wall, y, x)

                if room[x][y] == self.Tile.right_wall():
                    self.Tile.draw_tile(screen, wall, y, x)

                # Отрисовка пола
                if room[x][y] == self.Tile.room_floor():
                    self.Tile.draw_tile(screen, floor, y, x)

                # Отрисовка монстра
                if room[x][y] == self.Tile.enemy_spawner():
                    self.Tile.draw_tile(screen, floor, y, x)

                # Rendering obstacles
                if room[x][y] == self.Tile.room_rock():
                    self.Tile.draw_tile(screen, rock, y, x)

                if room[x][y] == self.Tile.room_planks():
                    self.Tile.draw_tile(screen, planks, y, x)

                if room[x][y] == self.Tile.room_wood():
                    self.Tile.draw_tile(screen, wood, y, x)

                if room[x][y] == self.Tile.room_barrel():
                    self.Tile.draw_tile(screen, barrel, y, x)

                if room[x][y] == self.Tile.room_box():
                    self.Tile.draw_tile(screen, box, y, x)

                if room[x][y] == self.Tile.trader():
                    self.Tile.draw_tile(screen, trader, y, x)

                if room[x][y] == self.Tile.room_chest():
                    self.Tile.draw_tile(screen, chest, y, x)
