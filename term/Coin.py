from pico2d import *

class Coin:
    instance = None
    def singleton():
        if Coin.instance == None:
            Coin.instance = Coin()
        return Coin.instance
    def __init__(self):
        self.image = load_image('coin.png')
        self.coin = 1000
        self.font = load_font('ConsolaMalgun.TTF', 40)
    def draw(self):
        self.image.draw(600,550)
        self.font.draw(630, 550, '%d ' % (self.coin),(250,250,0)) #코인 출력
    def update(self):
        pass