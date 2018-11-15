from pico2d import *
import random
import config

class Player:
    def __init__(self):
        self.x = random.randint(300,500)
        self.y = random.randint(200,400)
        self.speed = 2
        self.timer = 0
        self.frame = random.randint(0,7)
        self.player_image = load_image('image/run_stand_ani.png')
        self.goto = 0 # 0 업 1 다운
        self.state = 0 # 0 왼쪽 1 오른쪽 2 위 3 아래
        self.idle = 0 # 0 이동중 1 왼쪽  2 오른쪽
        self.attack = [] # 총알 공격
        self.attack_image = load_image('image/attack.png')

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 30, self.y - 50, self.x + 30, self.y + 35

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

        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.timer += 1
        self.x += 0
        self.y += 0
        if self.timer > 15:
            self.frame = (self.frame + 1) % 8
            self.timer = 0

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

        if self.state == 0:
            self.x -= 1
            if self.x < 100:
                self.x = 100
        elif self.state == 1:
            self.x += 1
            if self.x > 700:
                self.x = 700

        if self.goto == 0:
            self.y += 1
            if self.y > 520:
                self.y = 520
        elif self.goto == 1:
            self.y -= 1
            if self.y < 150:
                self.y = 150