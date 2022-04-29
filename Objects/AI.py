import ScreenAndObjs as SO
import math
import Objects.Bullet as BO

class AI:
    def __init__(self):
        self.x = 0


#Класс для управления мобов с рендж атакой
class RangeAI:
    #функция отвечает за действие моба в каждый кадр, в качестве аргумента требует класс самого моба
    def Tick(self, obj):
        try:
            tempX = (SO.objects["Player"].rect.x - obj.rect.x) / abs(SO.objects["Player"].rect.x - obj.rect.x)
        except ZeroDivisionError:
            tempX = 0
        try:
            tempY = (SO.objects["Player"].rect.y - obj.rect.y) / abs(SO.objects["Player"].rect.y - obj.rect.y)
        except ZeroDivisionError:
            tempY = 0


        if math.sqrt((SO.objects["Player"].rect.x - obj.rect.x) ** 2 + (SO.objects["Player"].rect.y - obj.rect.y) ** 2) < 200:
            obj.rect.x -= tempX * obj.traits['speed']
            obj.rect.y -= tempY * obj.traits['speed']
        else:
            x = abs(SO.objects["Player"].rect.x - obj.rect.x) - abs(SO.objects["Player"].rect.x - obj.rect.x)
            if x <= 0:
                obj.rect.x += tempX * obj.traits['speed']
            else:
                obj.rect.y += tempY * obj.traits['speed']

        if SO.objects["Player"].inv == 0 and abs(obj.rect.x - SO.objects["Player"].rect.x) < 10 and abs(obj.rect.y - SO.objects["Player"].rect.y) < 10:
            SO.objects["Player"].traits["hp"] -= obj.traits['damage']
            SO.objects["Player"].inv += 20
            if SO.objects["Player"].traits["hp"] <= 0:
                exit(0);

        if obj.lastAttack == 0:
            try:
                tempX = (SO.objects["Player"].rect.x - obj.rect.x)
            except ZeroDivisionError:
                tempX = 0
            try:
                tempY = (SO.objects["Player"].rect.y - obj.rect.y)
            except ZeroDivisionError:
                tempY = 0

            temp = tempX
            tempX /= math.sqrt(tempX * tempX + tempY * tempY)
            tempY /= math.sqrt(temp * temp + tempY * tempY)
            SO.objects["BUL" + str(SO.BulletCount)] = BO.Bullet(obj.rect.x, obj.rect.y, (tempX * 10, tempY * 10), "BUL" + str(SO.BulletCount), "Enemy" + str(obj.num))
            SO.sprites.add(SO.objects["BUL" + str(SO.BulletCount)])
            SO.BulletCount += 1
            obj.lastAttack = obj.traits["AttackSpeed"]
        else:
            obj.lastAttack -= 1

#Класс для управления мобов с мили атакой
class MeleeAI:
    #функция отвечает за действие моба в каждый кадр, в качестве аргумента требует класс самого моба
    def Tick(self, obj):
        try:
            obj.rect.x += (SO.objects["Player"].rect.x - obj.rect.x) / abs(SO.objects["Player"].rect.x - obj.rect.x) * obj.traits['speed']
        except ZeroDivisionError:
            obj.rect.x = obj.rect.x
        try:
            obj.rect.y += (SO.objects["Player"].rect.y - obj.rect.y) / abs(SO.objects["Player"].rect.y - obj.rect.y) * obj.traits['speed']
        except ZeroDivisionError:
            obj.rect.y = obj.rect.y
        if SO.objects["Player"].inv == 0 and abs(obj.rect.x - SO.objects["Player"].rect.x) < 10 and abs(obj.rect.y - SO.objects["Player"].rect.y) < 10:
            SO.objects["Player"].traits["hp"] -= obj.traits['damage']
            SO.objects["Player"].inv += 20
            if SO.objects["Player"].traits["hp"] <= 0:
                exit(0);
