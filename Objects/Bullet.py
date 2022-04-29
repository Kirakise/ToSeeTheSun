import pygame
import ScreenAndObjs as SO
#Размеры экрана
WIDTH = SO.WIDTH
HEIGHT = SO.HEIGHT
#Текстуры снарядов для каждого направления
ArrowNorth = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow0.png')
ArrowNorthEast = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow1.png');
ArrowEast = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow2.png');
ArrowSouthEast = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow3.png');
ArrowSouth = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow4.png');
ArrowSouthWest = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow5.png');
ArrowWest = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow6.png');
ArrowNorthWest = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/effect/arrow7.png');


#Функция принимает направление в виде (0,1) и относительно направления выдает соответствующий спрайт снаряда
def getArrow(dir):
    if (dir[1] > 0):
        if (dir[0] > 0):
            return ArrowSouthEast
        if (dir[0] < 0):
            return ArrowSouthWest
        return ArrowSouth
    if (dir[1] < 0):
        if (dir[0] > 0):
            return ArrowNorthEast
        if (dir[1] < 0):
            return ArrowNorthWest
        return ArrowNorth
    if (dir[0] > 0):
        return ArrowEast
    return ArrowWest

#Класс отвечает за действие пули в игре
class Bullet(pygame.sprite.Sprite):
    #Инициализация, параметры по порядку: x и y координаты спавна, (x, y) направление снаряда, num - уникальный номер пули, caster - "Player" или "Mob"
    def __init__(self, x, y, dir, num, caster):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        playerImg = getArrow(dir)
        self.image = playerImg.convert_alpha()
        SO.screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dir = dir
        self.caster = caster

    def Tick(self): #Функция отвечает за поведение пули в каждый кадр игры
        if self.rect.x + self.dir[0] <= 0 or self.rect.x + self.dir[0] >= WIDTH \
                or self.rect.y + self.dir[1] <= 0 or self.rect.y + self.dir[1] >= HEIGHT:
                    SO.sprites.remove(SO.objects[self.num])
                    SO.objects.pop(self.num)

        for i in SO.enemies:
            if self.caster == "Player" and abs(self.rect.x - i.rect.x) < 10 and abs(self.rect.y - i.rect.y) < 10:
                SO.sprites.remove(SO.objects[self.num])
                SO.objects.pop(self.num)
                i.traits['hp'] -= SO.objects['Player'].traits['damage']
                if (i.traits['hp'] <= 0):
                    SO.sprites.remove(i)
                    SO.objects.pop("Enemy" + str(i.num))
                    SO.enemies.remove(i)
        if not self.caster == "Player" and abs(SO.objects["Player"].rect.x - self.rect.x) <= 10 and \
            abs(SO.objects["Player"].rect.y - self.rect.y) <= 10:
            SO.sprites.remove(SO.objects[self.num])
            SO.objects.pop(self.num)
            SO.objects["Player"].traits["hp"] -= SO.objects[self.caster].traits["damage"]
            if SO.objects["Player"].traits["hp"] <= 0:
                exit(3)
        self.rect.x += self.dir[0]
        self.rect.y += self.dir[1]
