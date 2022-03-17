from Map.Room.RoomService import RoomService


class RoomController:
    def __init__(self):
        self.floor = ''
        self.RoomService = RoomService()

    def generate_start_room(self):
        return self.RoomService.generate_start_room(18, 30)

    def generate_monster_room(self):
        return self.RoomService.generate_monster_room(18, 30)

    def generate_treasure_room(self):
        return self.RoomService.generate_treasure_room(18, 30)

    def generate_shop_room(self):
        return self.RoomService.generate_shop_room(18, 30)

    def generate_boss_room(self):
        return self.RoomService.generate_boss_room(18, 30)

    def draw_room(self, screen, room):
        self.RoomService.draw_room(screen, room)
