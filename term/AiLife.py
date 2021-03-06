from pico2d import *

class AiLife:
    instance = None
    def singleton():
        if AiLife.instance == None:
            AiLife.instance = AiLife()
        return AiLife.instance
    def __init__(self):
        self.heart = 100
        self.font = load_font('ConsolaMalgun.TTF', 40)
    def draw(self,px,py):
        self.font.draw(60, 550, 'Ai Life:   %', (255, 255, 255))
        self.font.draw(230, 550, '%d' % (self.heart), (255, 0, 0))  # 생명 출력
    def update(self):
        pass