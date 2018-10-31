from pico2d import *

class Life:
    def __init__(self):
        self.image = load_image('image/life.png')
        self.life = 3
        self.font = load_font('resource/ConsolaMalgun.TTF', 40)

    def draw(self):
        self.image.draw(500,550)
        self.font.draw(530, 550, '%d ' % (self.life))  # 생명 출력

    def update(self):
        pass