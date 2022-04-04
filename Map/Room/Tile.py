class Tile:
    def __init__(self):
        self.xSize = 32
        self.ySize = 32

    def draw_tile(self, screen, tile, x, y):
        screen.blit(tile, (x * self.xSize, y * self.ySize))

    def left_top_corner(self):
        return 'ltc'

    def right_top_corner(self):
        return 'rtc'

    def left_bottom_corner(self):
        return 'lbc'

    def right_bottom_corner(self):
        return 'rbc'

    def left_wall(self):
        return 'lw'

    def right_wall(self):
        return 'rw'

    def top_middle_wall(self):
        return 'tmw'

    def bot_middle_wall(self):
        return 'bmw'

    def room_floor(self):
        return 'fl'

    def enemy_spawner(self):
        return 'enemy_spawner'

    def room_rock(self):
        return 'rock'

    def room_planks(self):
        return 'planks'

    def room_wood(self):
        return 'wood'

    def trader(self):
        return 'trader'

    def room_barrel(self):
        return 'barrel'

    def room_box(self):
        return 'box'
