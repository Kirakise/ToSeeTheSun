import random
from Map.MapService import MapService


class MapController:
    def __init__(self):
        self.floor = ''
        self.MapService = MapService()
        self.room = self.MapService.generateRoom()


    def generateRandomObstacles(self, room):
        obstaclesForRoom = 10
        random.seed(random.randint(1, 100))

        for i in range(len(room)):
            for j in range(len(room[i])):
                if ((i == 0 or i == 29) and 0 <= j <= 29) or (0 <= i <= 29 and (j == 0 or j == 29)):
                    continue
                elif random.randint(1, 10) == 3 and obstaclesForRoom != 0:
                    room[i][j] = 'rk'
                    obstaclesForRoom -= 1

        return room

    def drawMap(self, screen, gameMap):
        MapService.drawMap(self, screen, gameMap)
