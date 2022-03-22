import ScreenAndObjs as SO
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


    def Add(self):
        for i in self.traits.keys():
            SO.objects['Player'].traits[i] += self.traits[i]

    def Remove(self):
        for i in self.traits.keys():
            SO.objects['Player'].traits[i] -= self.traits[i]


class SpeedArt(Item):
    def __init__(self, x, y):
        self.init(x, y)
        self.traits = {'speed': 3}

class HPArt(Item):
    def __init(self, x, y):
        self.init(x, y)
        self.traits = {'hp': 1}