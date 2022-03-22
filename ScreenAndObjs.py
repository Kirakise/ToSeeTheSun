import pygame


BulletCount = 0
EnemyNum = 0
ItemNum = 0


WIDTH = 1366
HEIGHT = 768
FPS = 30
BLACK = (0, 0, 0)



playerImg = pygame.image.load('./Assets/smth.png')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
enemies = []
objects = {}
items = []
sprites = pygame.sprite.Group()