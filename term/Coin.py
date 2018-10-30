from pico2d import *

class Coin:
    def __init__(self):
        self.image = load_image('image/coin.png')

    def draw(self):
        self.image.draw(600,550)

    def update(self):
        pass