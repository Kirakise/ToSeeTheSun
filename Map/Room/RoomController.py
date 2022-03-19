from Map.Room.RoomService import RoomService


class RoomController:
    def __init__(self):
        self.RoomService = RoomService()

    def generate_start_room(self):
        return self.RoomService.generate_start_room(18, 30)

    def draw_room(self, screen, room):
        self.RoomService.draw_room(screen, room)
