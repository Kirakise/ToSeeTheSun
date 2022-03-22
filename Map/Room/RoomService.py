import pygame
from Map.Room.Tile import Tile

wall = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/wall/brick_brown1.png')
floor = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/floor/cobble_blood3.png')
rock = pygame.image.load('./Assets/Sprites/frames/wall_column_mid.png')

enemy = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/player/base/centaur_brown_f.png')


class RoomService:
    def __init__(self):
        self.Tile = Tile()

    def generate_start_room_fromFile(self):
        file = open('./Assets/MapCollection/startRoom.txt', 'r')
        # Чтение и разделение файла на список строк
        roomMap = file.read().splitlines()

        # Разделение списка на массив списков
        for i in range(0, len(roomMap)):
            roomMap[i] = roomMap[i].split()
            print(roomMap[i])

        file.close()
        return roomMap

    # Генерация массива сетки комнаты.
    # Каждому элементу присваивается тип спрайта
    def generate_start_room(self, height, width):
        room = [[0 for x in range(height)] for y in range(width)]

        for i in range(len(room)):
            for j in range(len(room[i])):
                if i == 0 and j == 0:
                    room[i][j] = self.Tile.left_top_corner()
                elif i == width - 1 and j == 0:
                    room[i][j] = self.Tile.right_top_corner()

                elif i == 0 and j == height - 1:
                    room[i][j] = self.Tile.left_bottom_corner()
                elif i == width - 1 and j == height - 1:
                    room[i][j] = self.Tile.right_bottom_corner()

                elif i == 0:
                    room[i][j] = self.Tile.left_wall()
                elif j == 0 or j == height - 1:
                    room[i][j] = self.Tile.middle_wall()
                elif i == width - 1:
                    room[i][j] = self.Tile.right_wall()

                elif i != 0 or i != width - 1 and j != 0 or j != height - 1:
                    room[i][j] = self.Tile.room_floor()

        return room

    # Отрисовка сетки
    def draw_room(self, screen, room):
        for x in range(len(room)):
            print(len(room[x]))
            for y in range(len(room[x])):
                # Отрисовка верхних угловых тайлов
                if room[x][y] == "ltc" or room[x][y] == "rtc" or room[x][y] == "lbc" or room[x][y] == "rbc" \
                        or room[x][y] == "mw" or room[x][y] == "lw" or room[x][y] == "rw":
                    self.Tile.draw_tile(screen, wall, y, x)

                elif room[x][y] == "fl":
                    self.Tile.draw_tile(screen, floor, y, x)

                # Отрисовка нижних угловых тайлов

                # Отрисовка тайлов левой, вернхней/нижней и правой стены

                # Отрисовка пола

                # Отрисовка монстра

                '''
                # Отрисовка верхних угловых тайлов
                if room[x][y] == self.Tile.left_top_corner():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_top_corner():
                    self.Tile.draw_tile(screen, wall, x, y)

                # Отрисовка нижних угловых тайлов
                if room[x][y] == self.Tile.left_bottom_corner():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_bottom_corner():
                    self.Tile.draw_tile(screen, wall, x, y)

                # Отрисовка тайлов левой, вернхней/нижней и правой стены
                if room[x][y] == self.Tile.left_wall():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.middle_wall():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_wall():
                    self.Tile.draw_tile(screen, wall, x, y)

                # Отрисовка пола
                if room[x][y] == self.Tile.room_floor():
                    self.Tile.draw_tile(screen, floor, x, y)

                # Отрисовка монстра
                if room[x][y] == self.Tile.random_monster_type():
                    self.Tile.draw_tile(screen, enemy, x, y)
                '''