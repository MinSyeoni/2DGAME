from pico2d import *
import random
import Player
import game_framework

class Ai:
    RUN_SPEED_PPS = 300

    def __init__(self):
        self.x = random.randint(600,700)
        self.y = random.randint(450,500)
        self.field_width = 800
        self.field_height = 600
        self.speed = 0.2
        self.size = 60
        self.timer = 0
        self.dx = 0
        self.dy = 0
        self.frame = random.randint(0,7)
        self.ai_image = load_image('image/ai_ani2.png')
        self.goto = 0 # 0 업 1 다운
        self.state = 0 # 0 왼쪽 1 오른쪽 2 위 3 아래
        self.idle = 0 # 0 이동중 1 왼쪽  2 오른쪽
        self.ai = [(self.x,self.y)] #ai 좌표
        self.pointX = 0
        self.pointY = 0

    def enter(self):
        global player
        player = Player()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self, px):
        if self.x > px:
            self.ai_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        else:
            self.ai_image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

    def update(self, px, py):
        # self.timer+=1
        # if self.timer > 50:
        #     self.frame = (self.frame + 1) % 8
        #     self.timer = 0

        pointX, pointY = px - self.x, py - self.y
        list = math.sqrt(pointX ** 2 + pointY ** 2)

        self.x += self.speed * pointX / list
        self.y += self.speed * pointY / list

        self.distance = Ai.RUN_SPEED_PPS * game_framework.frame_time