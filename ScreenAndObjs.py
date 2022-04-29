import pygame

#Счетчики пуль, врагов, предметов, чтобы каждый имел уникальный id
BulletCount = 0 
EnemyNum = 0
ItemNum = 0

#Параметры экрана
WIDTH = 1366
HEIGHT = 768
FPS = 30
BLACK = (0, 0, 0)


#Спрайт
playerImg = pygame.image.load('./Assets/smth.png')
#Экран для взаимодействия, pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Список мобов
enemies = []
#Список всех обьектов которые должны действовать каждый кадр
objects = {}
#Список всех артефактов
items = []
#Все отображаемые обьекты
sprites = pygame.sprite.Group()
