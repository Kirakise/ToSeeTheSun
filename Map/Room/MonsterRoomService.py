import random
from Map.Room.RoomService import RoomService


class MonsterRoomService(RoomService):
    def __init__(self):
        super().__init__()

    def generate_monster_room(self, height, width):
        random_num = random.randint(1, 5)
        monster_room = self.generate_start_room(height, width)

        if random_num == 1:
            monster_room[20][10] = self.Tile.random_monster_type()
            monster_room[11][5] = self.Tile.random_monster_type()
        elif random_num == 2:
            monster_room[2][10] = self.Tile.random_monster_type()
        elif random_num == 3:
            monster_room[15][3] = self.Tile.random_monster_type()
        elif random_num == 4:
            monster_room[3][30] = self.Tile.random_monster_type()
        elif random_num == 5:
            monster_room[15][3] = self.Tile.random_monster_type()

        return monster_room
