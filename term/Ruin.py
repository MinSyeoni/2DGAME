from pico2d import *

class Ruin:
    instance = None
    def singleton():
        if Ruin.instance == None:
            Ruin.instance = Ruin()
        return Ruin.instance
    def __init__(self):
        self.image = load_image('image/ruin.png')
        self.ruin = 0
        self.font = load_font('resource/ConsolaMalgun.TTF', 40)
    def draw(self):
        self.image.draw(100,150)
        self.font.draw(60, 70, 'Ruin:   %', (255, 255, 255))
        self.font.draw(200, 70, '%d ' % (self.ruin),(250,0,0))
    def update(self):
        pass