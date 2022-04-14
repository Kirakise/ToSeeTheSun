from Map.Room.MonsterRoomService import MonsterRoomService


class MonsterRoomController:
    def __init__(self):
        self.MonsterRoomService = MonsterRoomService()

    def generate_room(self):
        file = open('./Assets/RoomCollection/MonsterRooms/monsterRoom_1.txt', 'r')
        return self.MonsterRoomService.generate_room(file)

    def draw_room(self, screen, room):
        self.MonsterRoomService.draw_room(screen, room)
