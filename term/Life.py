from pico2d import *

class Life:
    def __init__(self):
        self.image = load_image('image/life.png')

    def draw(self):
        self.image.draw(550,550)

    def update(self):
        pass