from pico2d import *

class Bullet:
    def __init__(self,playerX, playerY, targetX, targetY):
        self.frame = 0

        self.currX = playerX
        self.currY = playerY
        self.targetX = targetX
        self.targetY = targetY
        self.speedX,self.speedY= (self.targetX - self.currX) / 10, (self.targetY - self.currY) / 10

        self.speed = 2
        self.image = load_image('image/bullet.png')

        self.attack = [] # 총알 공격
    def draw(self):

        self.image.clip_draw(self.frame*25, 0, 25, 25, self.currX, self.currY)

    def update(self):

        self.frame = (self.frame + 1) % 8

        self.currX += self.speedX
        self.currY += self.speedY

        if self.currX > self.targetX - 5 and self.currX < self.targetX + 5 :
            del(self)
