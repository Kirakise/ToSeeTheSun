import pygame.sprite
import pygame
import ScreenAndObjs as SO
import Objects.Bullet as Bt
WIDTH = SO.WIDTH
HEIGHT = SO.HEIGHT

playerImg = pygame.image.load('./Assets/smth.png')


def ks(x, y, speed):
    if y >= HEIGHT:
        return x, y
    return x, y + speed


def kw(x, y, speed):
    if y <= 0:
        return x, y
    return x, y - speed


def kd(x, y, speed):
    if x >= WIDTH:
        return x, y
    return x + speed, y


def ka(x, y, speed):
    if x <= 0:
        return x, y
    return x - speed, y

def au(x, y):
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (0, -10), "BUL" + str(SO.BulletCount))
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1

def al(x, y):
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (-10, 0), "BUL" + str(SO.BulletCount))
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1

def ar(x, y):
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (10, 0), "BUL" + str(SO.BulletCount))
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1

def ad(x, y):
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (0, 10), "BUL" + str(SO.BulletCount))
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg.convert_alpha()
        SO.screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.inv = 0;
        self.actions = {pygame.K_s: ks,
                        pygame.K_a: ka,
                        pygame.K_w: kw,
                        pygame.K_d: kd}
        self.shoot = {pygame.K_UP: au,
                      pygame.K_LEFT: al,
                      pygame.K_RIGHT: ar,
                      pygame.K_DOWN: ad}
        self.inventory = []
        self.traits = {'speed': 2, 'hp': 3, 'damage': 1}
        self.modifyers = []


    def Tick(self):
        for i in self.modifyers:
            tmp = i(self.rect.x, self.rect.y, self.traits['speed'])
            self.rect.x = tmp[0]
            self.rect.y = tmp[1]
        for i in SO.items:
            if abs(i.rect.x - self.rect.x) <= 10 and abs(i.rect.y - self.rect.y) <= 10 and len(self.inventory) < 3:
                self.inventory.append(i)
                i.Add()
        if self.inv != 0:
            self.inv -= 1


    def Action(self, x, MODE):
        if x in self.actions.keys():
            if MODE == 1:
                self.modifyers.append(self.actions[x])
            else:
                self.modifyers.remove(self.actions[x])
        elif x in self.shoot.keys() and MODE == 1:
            self.shoot[x](self.rect.x, self.rect.y)
