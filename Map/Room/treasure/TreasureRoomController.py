from Map.Room.treasure.TreasureRoomService import TreasureRoomService


class TreasureRoomController:
    def __init__(self):
        self.ShoppingRoomService = TreasureRoomService()

    def generate_room(self):
        file = open('./Assets/RoomCollection/TreasureRoom/treasureRoom_2.txt', 'r')
        return self.ShoppingRoomService.generate_room(file)

    def draw_room(self, screen, room):
        self.ShoppingRoomService.draw_room(screen, room)
