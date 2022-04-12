from Map.Room.TreasureRoomController import TreasureRoomController
from networkx.generators.random_graphs import erdos_renyi_graph

class MapService:
    def __init__(self):
        self.TreasureRoomController = TreasureRoomController()
        self.level_graph = {}

    def cretae_map_graph(self, room_quantity):
        tmp = {}
        for i in range(room_quantity):
            tmp[f'Room_{str(i)}'] = [self.TreasureRoomController.generate_room()]

        self.n = room_quantity
        self.p = 0.5

        self.level_graph = erdos_renyi_graph(self.n, self.p)

        for i in self.level_graph.edges:
            tmp[f'Room_{str(i[0])}'].append(f'Room_{str(i[1])}')

        self.level_graph = tmp
        return self.level_graph

    def find_collisions(self, room, x, y):
        print(room[x][y])
