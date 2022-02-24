import pygame
import ScreenAndObjs as SO

playerImg = pygame.image.load('./Assets/smth.png')
WIDTH = 360
HEIGHT = 480

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg.convert_alpha()
        SO.screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 10, HEIGHT - 10)

    def Tick(self, AI = 0):
        if AI == 0:
            try:
                self.rect.x += (SO.objects["Player"].rect.x - self.rect.x) / abs(SO.objects["Player"].rect.x - self.rect.x)
            except ZeroDivisionError:
                self.rect.x = self.rect.x
            try:
                self.rect.y += (SO.objects["Player"].rect.y - self.rect.y) / abs(SO.objects["Player"].rect.y - self.rect.y)
            except ZeroDivisionError:
                self.rect.y = self.rect.y