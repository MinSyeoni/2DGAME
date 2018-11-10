from pico2d import *

class Coin:
    def __init__(self):
        self.image = load_image('image/coin.png')
        self.coin = 100
        self.font = load_font('resource/ConsolaMalgun.TTF', 40)
    def draw(self):
        self.image.draw(600,550)
        self.font.draw(650, 550, '%d ' % (self.coin),(250,250,0)) #코인 출력

    def update(self):
        pass