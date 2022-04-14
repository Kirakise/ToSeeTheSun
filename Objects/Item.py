import ScreenAndObjs as SO
import random
import pygame

class Item(pygame.sprite.Sprite):
    def init(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = SO.playerImg.convert_alpha()
        SO.screen.blit(SO.playerImg, (x, y))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.id = SO.ItemNum
        SO.ItemNum += 1
        SO.items.append(self)
        SO.sprites.add(self)


    def Add(self):
        for i in self.traits.keys():
            SO.objects['Player'].traits[i] += self.traits[i]
            SO.sprites.remove(self)
            SO.items.remove(self)

    def Remove(self):
        for i in self.traits.keys():
            SO.objects['Player'].traits[i] -= self.traits[i]
            self.rect.center = SO.objects["Player"].rect.center
            SO.sprites.add(self)
            SO.items.add(self)


class SpeedArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'speed': 3}

class HPArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'hp': 1}

class AttackArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'damage': 1}

class AttackSpeedArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'AttackSpeed' : 10}

class TreasureChest(Item):
    def __init__(self, x, y):
        self.init(x, y)

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

