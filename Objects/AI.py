import ScreenAndObjs as SO

class AI:
    def __init__(self):
        self.x = 0



class RangeAI:
    def Tick(self, obj):
        try:
            obj.rect.x -= (SO.objects["Player"].rect.x - obj.rect.x) / abs(SO.objects["Player"].rect.x - obj.rect.x) * obj.traits['speed']
        except ZeroDivisionError:
            obj.rect.x = obj.rect.x
        try:
            obj.rect.y -= (SO.objects["Player"].rect.y - obj.rect.y) / abs(SO.objects["Player"].rect.y - obj.rect.y) * obj.traits['speed']
        except ZeroDivisionError:
            obj.rect.y = obj.rect.y
        if SO.objects["Player"].inv == 0 and abs(obj.rect.x - SO.objects["Player"].rect.x) < 10 and abs(obj.rect.y - SO.objects["Player"].rect.y) < 10:
            SO.objects["Player"].traits["hp"] -= obj.traits['damage']
            SO.objects["Player"].inv += 20
            if SO.objects["Player"].traits["hp"] <= 0:
                exit(0);


class MeleeAI:
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