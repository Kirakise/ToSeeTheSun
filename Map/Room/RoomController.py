from Map.Room.RoomService import RoomService


class RoomController:
    def __init__(self):
        self.floor = ''
        self.RoomService = RoomService()
        self.room = self.RoomService.generate_room(18, 30)

    def draw_map(self, screen, game_map):
        self.RoomService.draw_map(screen, game_map)
