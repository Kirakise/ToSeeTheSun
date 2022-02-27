import pygame

tile = pygame.image.load('./Assets/Sprites/frames/wall_banner_red.png')
floor = pygame.image.load('./Assets/Sprites/frames/floor_2.png')
rock = pygame.image.load('./Assets/Sprites/frames/wall_column_mid.png')
playerImg = pygame.image.load('./Assets/smth.png')


class MapService:
    def generateRoom(self):
        room = [[0 for x in range(30)] for y in range(30)]

        for i in range(30):
            for j in range(30):
                if i == 0 and j == 0:
                    room[i][j] = 'ltc'
                elif i == 0 and 0 < j < 29:
                    room[i][j] = 'lw'
                elif i == 0 and j == 29:
                    room[i][j] = 'lbc'
                elif i == 29 and j == 0:
                    room[i][j] = 'rtc'
                elif i == 29 and j == 29:
                    room[i][j] = 'rbc'
                elif 0 < i < 29 and (j == 0 or j == 29):
                    room[i][j] = 'mw'
                elif i == 29 and 0 < j < 29:
                    room[i][j] = 'rw'
                elif i != 0 or i != 29 and j != 0 or j != 29:
                    room[i][j] = 'fl'

        return room

    def drawMap(self, screen, gameMap):
        for x in range(len(gameMap)):
            for y in range(len(gameMap[x])):
                if gameMap[x][y] == 'ltc':
                    screen.blit(tile, (x * 16, y * 16))
                if gameMap[x][y] == 'lw':
                    screen.blit(tile, (x * 16, y * 16))
                if gameMap[x][y] == 'lbc':
                    screen.blit(tile, (x * 16, y * 16))
                if gameMap[x][y] == 'rtc':
                    screen.blit(tile, (x * 16, y * 16))
                if gameMap[x][y] == 'rbc':
                    screen.blit(tile, (x * 16, y * 16))
                if gameMap[x][y] == 'mw':
                    screen.blit(tile, (x * 16, y * 16))
                if gameMap[x][y] == 'rw':
                    screen.blit(tile, (x * 16, y * 16))
                if gameMap[x][y] == 'fl':
                    screen.blit(floor, (x * 16, y * 16))
                # if gameMap[x][y] == 'rk':
                #     screen.blit(rock, (x * 16, y * 16))