from pico2d import *

class Bullet:
    def __init__(self,playerX, playerY, targetX, targetY):
        self.frame = 0

        self.currX = playerX
        self.currY = playerY
        self.targetX = targetX
        self.targetY = targetY
        self.speedX,self.speedY= (self.targetX - self.currX) / 10, (self.targetY - self.currY) / 10
        self.timer = 0
        self.speed = 1
        self.image = load_image('image/bullet.png')

        self.attack = [] # 총알 공격
        self.shouldDelete = False

    def draw(self):

        self.image.clip_draw(self.frame*25, 0, 25, 25, self.currX, self.currY)

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