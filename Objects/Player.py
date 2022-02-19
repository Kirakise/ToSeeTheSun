import pygame.sprite
import pygame
WIDTH = 360
HEIGHT = 480

playerColor = (0, 255, 255)


def ks(x, y):
    return x, y + 1


def kw(x, y):
    return x, y - 1


def kd(x, y):
    return x + 1, y


def ka(x, y):
    return x - 1, y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(playerColor)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.actions = {pygame.K_s: ks,
                        pygame.K_a: ka,
                        pygame.K_w: kw,
                        pygame.K_d: kd}

    def Action(self, x):
        if x in self.actions.keys():
            tmp = self.actions[x](self.rect.x, self.rect.y)
            self.rect.x = tmp[0]
            self.rect.y = tmp[1]