from Map.MapService import MapService


class MapController:
    def __init__(self):
        self.MapService = MapService()

    def cretae_map_graph(self, room_quantity):
        return self.MapService.cretae_map_graph(room_quantity)

    def find_collisions(self, room, x, y):
        self.MapService.find_collisions(room, x, y)
