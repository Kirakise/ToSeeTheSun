from Map.Room.RoomService import RoomService


class RoomController:
    def __init__(self):
        self.RoomService = RoomService()

    def generate_room(self):
        file = open('./Assets/RoomCollection/StartRoom/startRoom.txt', 'r')
        return self.RoomService.generate_room(file)

    def draw_room(self, screen, room):
        self.RoomService.draw_room(screen, room)
