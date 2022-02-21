import pygame.sprite
import pygame
WIDTH = 360
HEIGHT = 480

playerImg = pygame.image.load('./Assets/smth.png')


def ks(x, y):
    return x, y + 1


def kw(x, y):
    return x, y - 1


def kd(x, y):
    return x + 1, y


def ka(x, y):
    return x - 1, y


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg.convert_alpha()
        screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.actions = {pygame.K_s: ks,
                        pygame.K_a: ka,
                        pygame.K_w: kw,
                        pygame.K_d: kd}
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
        x = "sad"
