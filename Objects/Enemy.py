import pygame
import ScreenAndObjs as SO
import Objects.AI as AI

playerImg = pygame.image.load('./Assets/smth.png')
WIDTH = SO.WIDTH
HEIGHT = SO.HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type = 0, x = WIDTH - 10, y = HEIGHT - 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg.convert_alpha()
        SO.screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.num = SO.EnemyNum
        self.traits = {'hp': 5, 'speed': 1, 'damage': 1}
        SO.EnemyNum += 1
        if type == 1:
            self.AI = AI.MeleeAI
        else:
            self.AI = AI.RangeAI
        SO.enemies.append(self)
        SO.objects["Enemy" + str(self.num)] = self
        SO.sprites.add(self)

    def Tick(self):
        self.AI.Tick(self, self)