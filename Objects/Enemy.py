import pygame
import ScreenAndObjs as SO
import Objects.AI as AI

playerImg = pygame.image.load('./Assets/smth.png')
WIDTH = SO.WIDTH
HEIGHT = SO.HEIGHT

#Класс отвечает за враждебных мобов
class Enemy(pygame.sprite.Sprite):
    #Инициализация, параметры: тип атаки моба (рейндж = 1, мили = 0), x и y координаты спавна
    def __init__(self, type = 0, x = WIDTH - 10, y = HEIGHT - 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg.convert_alpha()
        SO.screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.num = SO.EnemyNum
        self.traits = {'hp': 5, 'speed': 1, 'damage': 1, 'AttackSpeed': 10}
        SO.EnemyNum += 1
        if type == 1:
            self.AI = AI.MeleeAI
        else:
            self.AI = AI.RangeAI
        SO.enemies.append(self)
        self.lastAttack = 0
        SO.objects["Enemy" + str(self.num)] = self
        SO.sprites.add(self)
    #Функция отвечает за поведение моба в каждый кадр игры
    def Tick(self):
        self.AI.Tick(self, self)
