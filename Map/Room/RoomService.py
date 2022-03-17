import pygame
from Map.Room.Tile import Tile

wall = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/wall/brick_brown1.png')
floor = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/floor/cobble_blood3.png')
rock = pygame.image.load('./Assets/Sprites/frames/wall_column_mid.png')

enemy = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/player/base/centaur_brown_f.png')


class RoomService:
    def __init__(self):
        self.Tile = Tile()

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

    def generate_monster_room(self, height, width):
        monster_room = [[0 for x in range(height)] for y in range(width)]

        for i in range(len(monster_room)):
            for j in range(len(monster_room[i])):
                if i == 0 and j == 0:
                    monster_room[i][j] = self.Tile.left_top_corner()
                elif i == width - 1 and j == 0:
                    monster_room[i][j] = self.Tile.right_top_corner()

                elif i == 0 and j == height - 1:
                    monster_room[i][j] = self.Tile.left_bottom_corner()
                elif i == width - 1 and j == height - 1:
                    monster_room[i][j] = self.Tile.right_bottom_corner()

                elif i == 0:
                    monster_room[i][j] = self.Tile.left_wall()
                elif j == 0 or j == height - 1:
                    monster_room[i][j] = self.Tile.middle_wall()
                elif i == width - 1:
                    monster_room[i][j] = self.Tile.right_wall()

                elif i != 0 or i != width - 1 and j != 0 or j != height - 1:
                    monster_room[i][j] = self.Tile.random_monster_type()

        return monster_room

    def generate_treasure_room(self, height, width):
        treasure_room = [[0 for x in range(height)] for y in range(width)]

        for i in range(len(treasure_room)):
            for j in range(len(treasure_room[i])):
                if i == 0 and j == 0:
                    treasure_room[i][j] = self.Tile.left_top_corner()
                elif i == width - 1 and j == 0:
                    treasure_room[i][j] = self.Tile.right_top_corner()

                elif i == 0 and j == height - 1:
                    treasure_room[i][j] = self.Tile.left_bottom_corner()
                elif i == width - 1 and j == height - 1:
                    treasure_room[i][j] = self.Tile.right_bottom_corner()

                elif i == 0:
                    treasure_room[i][j] = self.Tile.left_wall()
                elif j == 0 or j == height - 1:
                    treasure_room[i][j] = self.Tile.middle_wall()
                elif i == width - 1:
                    treasure_room[i][j] = self.Tile.right_wall()

                elif i != 0 or i != width - 1 and j != 0 or j != height - 1:
                    treasure_room[i][j] = self.Tile.room_floor()

        return treasure_room

    def generate_shop_room(self, height, width):
        shop_room = [[0 for x in range(height)] for y in range(width)]

        for i in range(len(shop_room)):
            for j in range(len(shop_room[i])):
                if i == 0 and j == 0:
                    shop_room[i][j] = self.Tile.left_top_corner()
                elif i == width - 1 and j == 0:
                    shop_room[i][j] = self.Tile.right_top_corner()

                elif i == 0 and j == height - 1:
                    shop_room[i][j] = self.Tile.left_bottom_corner()
                elif i == width - 1 and j == height - 1:
                    shop_room[i][j] = self.Tile.right_bottom_corner()

                elif i == 0:
                    shop_room[i][j] = self.Tile.left_wall()
                elif j == 0 or j == height - 1:
                    shop_room[i][j] = self.Tile.middle_wall()
                elif i == width - 1:
                    shop_room[i][j] = self.Tile.right_wall()

                elif i != 0 or i != width - 1 and j != 0 or j != height - 1:
                    shop_room[i][j] = self.Tile.room_floor()

        return shop_room

    def generate_boss_room(self, height, width):
        boss_room = [[0 for x in range(height)] for y in range(width)]

        for i in range(len(boss_room)):
            for j in range(len(boss_room[i])):
                if i == 0 and j == 0:
                    boss_room[i][j] = self.Tile.left_top_corner()
                elif i == width - 1 and j == 0:
                    boss_room[i][j] = self.Tile.right_top_corner()

                elif i == 0 and j == height - 1:
                    boss_room[i][j] = self.Tile.left_bottom_corner()
                elif i == width - 1 and j == height - 1:
                    boss_room[i][j] = self.Tile.right_bottom_corner()

                elif i == 0:
                    boss_room[i][j] = self.Tile.left_wall()
                elif j == 0 or j == height - 1:
                    boss_room[i][j] = self.Tile.middle_wall()
                elif i == width - 1:
                    boss_room[i][j] = self.Tile.right_wall()

                elif i != 0 or i != width - 1 and j != 0 or j != height - 1:
                    boss_room[i][j] = self.Tile.room_floor()

        return boss_room

    def draw_room(self, screen, room):
        for x in range(len(room)):
            for y in range(len(room[x])):
                if room[x][y] == self.Tile.left_top_corner():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_top_corner():
                    self.Tile.draw_tile(screen, wall, x, y)

                if room[x][y] == self.Tile.left_bottom_corner():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_bottom_corner():
                    self.Tile.draw_tile(screen, wall, x, y)

                if room[x][y] == self.Tile.left_wall():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.middle_wall():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_wall():
                    self.Tile.draw_tile(screen, wall, x, y)

                if room[x][y] == self.Tile.room_floor():
                    self.Tile.draw_tile(screen, floor, x, y)

                if room[x][y] == self.Tile.random_monster_type():
                    self.Tile.draw_tile(screen, enemy, x, y)
