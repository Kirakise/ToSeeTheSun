import pygame.sprite
import pygame
import ScreenAndObjs as SO
import Objects.Bullet as Bt
WIDTH = 360
HEIGHT = 480

playerImg = pygame.image.load('./Assets/smth.png')


def ks(x, y):
    if y >= HEIGHT:
        return x, y
    return x, y + 2


def kw(x, y):
    if y <= 0:
        return x, y
    return x, y - 2


def kd(x, y):
    if x >= WIDTH:
        return x, y
    return x + 2, y


def ka(x, y):
    if x <= 0:
        return x, y
    return x - 2, y

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
        self.actions = {pygame.K_s: ks,
                        pygame.K_a: ka,
                        pygame.K_w: kw,
                        pygame.K_d: kd}
        self.shoot = {pygame.K_UP: au,
                      pygame.K_LEFT: al,
                      pygame.K_RIGHT: ar,
                      pygame.K_DOWN: ad}
        self.modifyers = []


    def Tick(self):
        for i in self.modifyers:
            tmp = i(self.rect.x, self.rect.y)
            self.rect.x = tmp[0]
            self.rect.y = tmp[1]


    def Action(self, x, MODE):
        if x in self.actions.keys():
            if MODE == 1:
                self.modifyers.append(self.actions[x])
            else:
                self.modifyers.remove(self.actions[x])
        elif x in self.shoot.keys():
            self.shoot[x](self.rect.x, self.rect.y)
