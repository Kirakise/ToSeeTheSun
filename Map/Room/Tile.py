import pygame

class Tile:
    def __init__(self, tile_type, x_cord, y_cord):
        self.xSize = 32
        self.ySize = 32

        self.x_cord = x_cord
        self.y_cord = y_cord

        self.tile_type = tile_type
        self.static_type = tile_type
        self.dynamic_type = '_'

        if '_' in self.tile_type:
            self.tile_type = self.tile_type.split('_')[0]
            self.dynamic_type = self.tile_type.split('_')[1]

    def get_tile_type(self):
        return self.tile_type

    def draw_tile(self, screen, picture):
        # screen.blit(picture, (x * self.xSize, y * self.ySize))
        screen.blit(picture, (self.x_cord, self.y_cord))



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

    def room_chest(self):
        return 'chest'
