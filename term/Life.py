from pico2d import *

class Life:
    instance = None
    def singleton():
        if Life.instance == None:
            Life.instance = Life()
        return Life.instance
    def __init__(self):
        self.image = load_image('life.png')
        self.heart = 5
        self.font = load_font('ConsolaMalgun.TTF', 40)
    def draw(self):
        self.image.draw(500,550)
        self.font.draw(530, 550, '%d ' % (self.heart),(255,0,0))  # 생명 출력
    def update(self):
        pass