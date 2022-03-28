import pygame.sprite
import pygame
import ScreenAndObjs as SO
import Objects.Bullet as Bt
WIDTH = SO.WIDTH
HEIGHT = SO.HEIGHT

playerImg = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/player/base/elf_m.png')


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
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (0, -10), "BUL" + str(SO.BulletCount), "Player")
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1

def al(x, y):
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (-10, 0), "BUL" + str(SO.BulletCount), "Player")
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1

def ar(x, y):
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (10, 0), "BUL" + str(SO.BulletCount), "Player")
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1

def ad(x, y):
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (0, 10), "BUL" + str(SO.BulletCount), "Player")
    SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
    SO.BulletCount += 1

def shoot(x, y, dirx, diry):
    if dirx == 0 and diry == 0:
        return
    SO.objects["BUL" + str(SO.BulletCount)] = Bt.Bullet(x, y, (dirx * 10, diry * 10), "BUL" + str(SO.BulletCount), "Player")
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
        self.shoot = {pygame.K_UP: (0, -1),
                      pygame.K_LEFT: (-1, 0),
                      pygame.K_RIGHT: (1, 0),
                      pygame.K_DOWN: (0, 1)}
        self.inventory = []
        self.traits = {'speed': 2, 'hp': 3, 'damage': 1, 'AttackSpeed': 10}
        self.lastAttack = 0
        self.modifyers = []
        self.attackMods = [0,0]


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
        self.lastAttack -= 1
        if self.lastAttack <= 0:
            shoot(self.rect.x, self.rect.y, self.attackMods[0], self.attackMods[1])
            self.lastAttack = self.traits["AttackSpeed"]


    def Action(self, x, MODE):
        if x in self.actions.keys():
            if MODE == 1:
                self.modifyers.append(self.actions[x])
            else:
                self.modifyers.remove(self.actions[x])
        if x in self.shoot.keys() and MODE == 1:
            self.attackMods[0] += self.shoot[x][0]
            self.attackMods[1] += self.shoot[x][1]
        if x in self.shoot.keys() and MODE == 0:
            self.attackMods[0] -= self.shoot[x][0]
            self.attackMods[1] -= self.shoot[x][1]
