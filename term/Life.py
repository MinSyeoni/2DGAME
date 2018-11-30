from pico2d import *

class Life:
    instance = None
    def singleton(self):
        if Life.instance == None:
            Life.instance = Life()
        return Life.instance
    def __init__(self):
        self.image = load_image('image/life.png')
        self.heart = 5
        self.font = load_font('resource/ConsolaMalgun.TTF', 40)
    def draw(self,x):
        self.image.draw(500,550)
        self.font.draw(530, 550, '%d ' % (self.heart+x),(255,0,0))  # 생명 출력
    def update(self):
        pass