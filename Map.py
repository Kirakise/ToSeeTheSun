import pygame

gameMap = '''
111111111111111111
1   1111         1
1                1
1                1
1                1
1   11111   111  1
1       111      1
1                1
1                1
111111111111111111
'''

tile = pygame.image.load("./Assets/smth.png")


class Map:
    def __init__(self):
        self.gameMap = gameMap.splitlines()
        self.tile = tile

    def drawMap(self, screen):
        for y, line in enumerate(self.gameMap):
            for x, c in enumerate(line):
                if c == '1':
                    screen.blit(tile, (x * 16, y * 16))
