from pico2d import *
import random
import config
import game_framework

class Player:
    RUN_SPEED_PPS = 200
    def __init__(self):
        self.x = 300
        self.y = 200
        self.speed = 5
        self.timer = 0
        self.size = 60
        self.mouse_control = False
        # self.angle = 0
        self.frame = random.randint(0,7)
        self.player_image = load_image('run_stand_ani.png')
        self.goto = 0 # 0 업 1 다운
        self.state = 0 # 0 왼쪽 1 오른쪽 2 위 3 아래
        self.idle = 0 # 0 이동중 1 왼쪽  2 오른쪽
        self.attack = [] # 총알 공격

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

        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.timer += 1
        if self.timer > 15:
            self.frame = (self.frame + 1) % 8
            self.timer = 0
        self.distance = Player.RUN_SPEED_PPS * game_framework.frame_time

        if self.state == 0:
            self.x -= 2
            if self.x < 100:
                self.x = 100
        elif self.state == 1:
            self.x += 2
            if self.x > 700:
                self.x = 700

        if self.goto == 0:
            self.y += 2
            if self.y > 520:
                self.y = 520
        elif self.goto == 1:
            self.y -= 2
            if self.y < 150:
                self.y = 150