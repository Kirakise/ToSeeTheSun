from Map.Room.ShoppingRoomService import ShoppingRoomService


class ShoppingRoomController:
    def __init__(self):
        self.ShoppingRoomService = ShoppingRoomService()

    def generate_room(self):
        file = open('./Assets/RoomCollection/ShoppingRoom/shoppingRoom_1.txt', 'r')
        return self.ShoppingRoomService.generate_room(file)

    def draw_room(self, screen, room):
        self.ShoppingRoomService.draw_room(screen, room)
