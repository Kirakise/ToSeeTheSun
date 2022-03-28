import pygame
import ScreenAndObjs as SO

WIDTH = SO.WIDTH
HEIGHT = SO.HEIGHT

playerImg = pygame.image.load('./Assets/smth.png')

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dir, num, caster):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        self.image = playerImg.convert_alpha()
        SO.screen.blit(playerImg, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dir = dir
        self.caster = caster

    def Tick(self):
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
