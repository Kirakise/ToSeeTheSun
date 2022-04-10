from networkx.generators.random_graphs import erdos_renyi_graph

from Map.Room.MonsterRoomController import MonsterRoomController


class MapService:
    def __init__(self, num):
        self.MonsterRoomController = MonsterRoomController()
        tmp = {}
        for i in range(num):
            tmp[f'Room {str(i)}'] = [self.MonsterRoomController.generate_room()]

        self.n = 6
        self.p = 0.5

        self.level_graph = erdos_renyi_graph(self.n, self.p)
        for i in self.level_graph.edges:
            tmp[f'Room {str(i[0])}'].append(f'Room {str(i[1])}')
        self.level_graph = tmp
        print(tmp)
