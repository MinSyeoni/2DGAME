from pico2d import *
import config

class Bullet:
    def __init__(self,playerX, playerY, targetX, targetY):
        self.frame = 0
        self.currX = playerX
        self.currY = playerY
        self.targetX = targetX
        self.targetY = targetY
        self.speedX,self.speedY= (self.targetX - self.currX) / 10, (self.targetY - self.currY) / 10
        self.timer = 0
        self.speed = 3
        self.size = 30
        self.image = load_image('bullet.png')
        self.shouldDelete = False

    def draw(self):
        self.image.clip_draw(self.frame*25, 0, 25, 25, self.currX, self.currY)
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def get_bb(self):
            return self.currX - 12.5, self.currY - 12.5, self.currX + 12.5, self.currY + 12.5

    def draw_bb(self):
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.timer += 1
        if self.timer > 15:
            self.frame = (self.frame + 1) % 8
            self.timer = 0

        pointX, pointY = self.targetX - self.currX, self.targetY - self.currY
        list = math.sqrt(pointX ** 2 + pointY ** 2)
        self.currX += self.speed * pointX / list
        self.currY += self.speed * pointY / list

        if self.currX > self.targetX - 5 and self.currX < self.targetX + 5:
            print(self, self.targetX, self.targetY, self.currX, self.currY)
            self.shouldDelete = True