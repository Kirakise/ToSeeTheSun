from Map.Room.MonsterRoomService import MonsterRoomService


class MonsterRoomController:
    def __init__(self):
        self.MonsterRoomService = MonsterRoomService()

    def generate_monster_room(self):
        return self.MonsterRoomService.generate_monster_room(18, 30)

    def draw_room(self, screen, room):
        self.MonsterRoomService.draw_room(screen, room)
