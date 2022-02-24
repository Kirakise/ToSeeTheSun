import pygame
import ScreenAndObjs as SO

WIDTH = 360
HEIGHT = 480

playerImg = pygame.image.load('./Assets/smth.png')

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dir, num):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        self.image = playerImg.convert_alpha()
        SO.screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dir = dir

    def Tick(self):
        if self.rect.x + self.dir[0] <= 0 or self.rect.x + self.dir[0] >= WIDTH \
                or self.rect.y + self.dir[1] <= 0 or self.rect.y + self.dir[1] >= HEIGHT:
                    SO.sprites.remove(SO.objects[self.num])
                    SO.objects.pop(self.num)

        if SO.EnemyNum in SO.objects.keys() and abs(self.rect.x - SO.objects[SO.EnemyNum].rect.x) < 5 \
                and abs(self.rect.y - SO.objects[SO.EnemyNum].rect.y) < 5:
            SO.sprites.remove(SO.objects[self.num])
            SO.objects.pop(self.num)
            SO.sprites.remove(SO.objects[0])
            SO.objects.pop(0)
        self.rect.x += self.dir[0]
        self.rect.y += self.dir[1]