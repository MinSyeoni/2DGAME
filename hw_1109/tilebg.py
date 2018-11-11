from pico2d import *
import json

MARGIN = 25
class TiledBackground:
    def __init__(self):
        file = open('desert.json', 'r')
        dict = json.load(file)
        file.close()
        layer = dict["layers"][0]
        self.image = load_image('../image/tmw_desert_spacing.png')
        self.tilesCountX, self.tilesCountY = 8, 6
        self.data = layer["data"]
        self.mapWidth = layer["width"]
        self.mapHeight = layer["height"]
        self.tileWidth = dict["tilewidth"]
        self.tileHeight = dict["tileheight"]
        self.canvas_widht = 800
        self.canvas_height = 600
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = self.mapWidth * self.tileWidth, self.mapHeight * self.tileHeight
        print(self.max_x, self.max_y)
        self.x, self.y = 0, 0
        self.target = None
        self.xxx = 0
    def clamp(self, o):
        o.x = int(clamp(self.min_x + MARGIN, o.x, self.max_x - MARGIN))
        o.y = int(clamp(self.min_y + MARGIN, o.y, self.max_y - MARGIN))
    def draw(self):
        tile_x = self.x // self.tileWidth
        tile_y = self.y // self.tileWidth
        beg_x = - int(self.x % self.tileWidth)
        beg_y = - int(self.y % self.tileHeight)
        y = beg_y
        ty = tile_y
        while y < self.canvas_height:
            x = beg_x
            tx = tile_x
            ti = (self.mapHeight - ty - 1) * self.mapWidth + tx
            while x < self.canvas_widht:
                tile = self.data[ti]
                rect = self.rectForTile(tile)
                self.image.clip_draw_to_origin(*rect, x, y)
                if (self.xxx == 0):
                    print(x, y)
                x += self.tileWidth
                ti += 1
            y += self.tileHeight
            ty += 1
        self.xxx = 1
        pass
    def rectForTile(self, tile):
        x = (tile - 1) % self.tilesCountX
        y = self.tilesCountY - 1 - (tile - 1) // self.tilesCountX
        src_x = x * (self.tileWidth + 1) + 1
        src_y = y * (self.tileHeight + 1) + 1
        return src_x, src_y, self.tileWidth, self.tileHeight
    def update(self):
        if self.target == None:
            return
        self.x = clamp(0, int(self.target.x - self.canvas_widht // 2), self.max_x - self.canvas_widht)
        self.y = clamp(0, int(self.target.y - self.canvas_height // 2), self.max_y - self.canvas_height)