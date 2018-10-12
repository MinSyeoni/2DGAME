from pico2d import *

import random

class Player:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = random.randint(150,500)
        self.speed = 2
        self.frame = random.randint(0,7)
        self.player_image = load_image('image/run_stand_ani.png')
        self.goto = 0 # 0 업 1 다운
        self.state = 0 # 0 왼쪽 1 오른쪽 2 위 3 아래
        self.idle = 0 # 0 이동중 1 왼쪽  2 오른쪽
        self.attack = [] # 총알 공격
        self.attack_image = load_image('image/attack.png')

    def draw(self):

        if self.state == 0 or (self.idle == 1 and self.goto != 2):
            self.player_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.state == 1 or (self.idle == 2 and self.goto != 2) :
            self.player_image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        elif self.idle == 1:
            self.player_image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        elif self.idle == 2:
            self.player_image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.player_image.clip_draw(self.frame*100, self.state * 100, 100, 100, self.x, self.y)

        for attack_image in self.attack:
            self.attack_image.draw(attack_image[0], attack_image[1])

    def update(self):
        self.frame = (self.frame + 1) % 8

        if len(self.attack) > 0:
            (tx,ty) = self.attack[0]
            attackX, attackY = tx - self.x, ty - self.y
            list = math.sqrt(attackX ** 2 + attackY ** 2)
            if list > 0:
                self.x += self.speed * attackX / list
                self.y += self.speed * attackY / list
                if attackX < 0 and self.x < tx: self.x = tx
                if attackX > 0 and self.x > tx: self.x = tx
                if attackY < 0 and self.y < ty: self.y = ty
                if attackY > 0 and self.y > ty: self.y = ty
            if(self.x, self.y) == (tx,ty):
                del self.attack[0]