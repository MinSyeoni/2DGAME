from pico2d import *

class ParallexLayer:
    def __init__(self, imageName, speed):
        self.image = load_image(imageName)
        self.width, self.height = self.image.w, self.image.h
        self.canvas_widht = 800
        self.canvas_height = 600
        self.speed = speed
    def draw(self):
        self.image.clip_draw_to_origin(self.x1, 0, self.width1, self.height, 0, 0)
        self.image.clip_draw_to_origin(self.x2, 0, self.width2, self.height, self.width1, 0)
    def update(self, x):
        self.x1 = int(x * self.speed) % self.image.w
        self.width1 = self.image.w - self.x1
        self.x2 = 0
        self.width2 = self.canvas_widht - self.width1

class ParallaxBackground:
    def __init__(self):
        ##배경 하늘 나무 땅 순서
        self.layers = [\
            ParallexLayer('../image/b0.png', 0.3), \
            ParallexLayer('../image/b1.png', 0.7), \
            ParallexLayer('../image/b2.png', 1.0), \
        ]
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 2000, 100,
        self.x, self.y = 0, 0
        self.target = None
    def clamp(self, o):
        o.x = clamp(self.min_x, o.x, self.max_x)
        o.y = clamp(self.min_y, o.y, self.max_y)
    def draw(self):
        for Parallex in self.layers:
            Parallex.draw()
    def update(self):
        self.x = int(self.target.x - 100)
        for Parallex in self.layers:
            Parallex.update(self.x)

class Background:
    def __init__(self):
        self.image = load_image('../image/futsal_court.png')
        self.canvas_widht = 800
        self.canvas_height = 600
        self.width = self.image.w
        self.height = self.image.h
        self.x, self.y = 0, 0
        self.target = None
    def draw(self):
        self.image.clip_draw_to_origin(self.x, self.y, self.canvas_widht, self.canvas_height, 0, 0)
    def update(self):
        if self.target == None:
            return
        self.x = clamp(0, int(self.target.x - self.canvas_widht // 2), self.width - self.canvas_widht)
        self.y = clamp(0, int(self.target.y - self.canvas_height // 2), self.height - self.canvas_height)

class InfiniteBackground:
    def __init__(self):
        self.image = load_image('../image/futsal_court.png')
        self.canvas_widht = 800
        self.canvas_height = 600
        self.width = self.image.w
        self.height = self.image.h
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 1700, 1000,
        self.x, self.y = 0, 0
        self.target = None
    def clamp(self, o):
        o.x = clamp(self.min_x, o.x, self.max_x)
        o.y = clamp(self.min_y, o.y, self.max_y)
    def draw(self):
        self.image.clip_draw_to_origin(self.x3, self.y3, self.width3, self.height3, 0, 0)
        self.image.clip_draw_to_origin(self.x2, self.y2, self.width2, self.height2, 0, self.height3)
        self.image.clip_draw_to_origin(self.x4, self.y4, self.width4, self.height4, self.width3, 0)
        self.image.clip_draw_to_origin(self.x1, self.y1, self.width1, self.height1, self.width3, self.height3)
    def update(self):
        if self.target == None:
            return
        self.x = int(self.target.x - self.canvas_widht // 2)
        self.y = int(self.target.y - self.canvas_height // 2)
        self.x3 = self.x % self.width
        self.y3 = self.y % self.height
        self.width3 = self.width - self.x3
        self.height3 = self.height - self.y3

        self.x2 = self.x3
        self.y2 = 0
        self.width2 = self.width3
        self.height2 = self.canvas_height - self.height3

        self.x4 = 0
        self.y4 = self.y3
        self.width4 = self.canvas_widht - self.width3
        self.height4 = self.height3

        self.x1 = 0
        self.y1 = 0
        self.width1 = self.width4
        self.height1 = self.height2

        #print(self.x,self.y)