from Map.Room.RoomService_Yuki import RoomService


class GameManager:

    def __init__(self):
        self.room_service = RoomService()
        self.room_service.set_file_path('./Assets/RoomCollection/StartRoom/startRoom.txt')
        self.room_service.get_tile_matrix()

    def generate_static_room(self, screen):
        self.room_service.draw_static_room(screen)
