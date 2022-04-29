import ScreenAndObjs as SO
import random
import pygame

#Абстрактный класс отвечающий за любой предмет
class Item(pygame.sprite.Sprite):
    def init(self, x, y): #Инициализация, в качестве входных параметров указываются координаты спавна
        pygame.sprite.Sprite.__init__(self)
        self.image = SO.playerImg.convert_alpha()
        SO.screen.blit(SO.playerImg, (x, y))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.id = SO.ItemNum
        SO.ItemNum += 1
        SO.items.append(self)
        SO.sprites.add(self)


    def Add(self): #Функция добавляет артефакт в инвентарь к игроку
        for i in self.traits.keys():
            SO.objects['Player'].traits[i] += self.traits[i]
            SO.sprites.remove(self)
            SO.items.remove(self)

    def Remove(self): #Функция удаляет артефакт из инвентаря
        for i in self.traits.keys():
            SO.objects['Player'].traits[i] -= self.traits[i]
            self.rect.center = SO.objects["Player"].rect.center
            SO.sprites.add(self)
            SO.items.add(self)

#Артефакт для ускорения
class SpeedArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'speed': 3}
#Артефакт на +хп
class HPArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'hp': 1}
#Артефакт на +урон
class AttackArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'damage': 1}
#Артефакт на +скорость ататки
class AttackSpeedArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'AttackSpeed' : 10}
#Сундук, артефакт который генерирует другие артефакты
class TreasureChest(Item):
    def __init__(self, x, y):
        self.init(x, y)
    #Функция создания рандомного артефакта
    def Add(self):
        a = random.randint(0, 3)
        print(a)
        x = self.rect.x
        y = self.rect.y
        b = [HPArt, AttackArt, SpeedArt, AttackSpeedArt]
        b[a](x, y)
        SO.sprites.remove(self)
        SO.items.remove(self)
        SO.objects["Player"].inventory.remove(self)

