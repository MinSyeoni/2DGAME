from pico2d import *
import random
import Player
import game_framework

class Ai:
    RUN_SPEED_PPS = 300
    FIELD_MARGIN = 50

    def __init__(self):
        self.x = random.randint(100,700)
        self.y = random.randint(150,500)
        self.attackX = self.x
        self.field_width = 800
        self.field_height = 600
        self.speed = 1
        self.timer = 0
        self.dx = 0
        self.dy = 0
        self.frame = random.randint(0,7)
        self.ai_image = load_image('image/ai_ani2.png')
        self.goto = 0 # 0 업 1 다운
        self.state = 0 # 0 왼쪽 1 오른쪽 2 위 3 아래
        self.idle = 0 # 0 이동중 1 왼쪽  2 오른쪽
        self.attack_count = 0#ai 공격
        self.ai = [(self.x,self.y)] #ai 좌표
        self.attack_timer = 0
        self.pointX = 0
        self.pointY = 0
        self.ai_attack_image1 = load_image('image/ai_attack.png')
        self.ai_attack_image2 = load_image('image/ai_attack2.png')


    def enter(self):
        global player
        player = Player()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self, px):
        global attackX
        if self.x > px:
            self.ai_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
            self.ai_attack_image1.draw(self.attackX, self.y)
        else:
            self.ai_image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
            self.ai_attack_image2.draw(self.attackX, self.y)

    def update(self, px, py):
        global attackX

        self.timer+=1
        if self.timer > 50:
            self.frame = (self.frame + 1) % 8
            self.attack_count += 1
            self.timer = 0

        pointX, pointY = px - self.x, py - self.y
        list = math.sqrt(pointX ** 2 + pointY ** 2)

        self.x += self.speed * pointX / list
        self.y += self.speed * pointY / list

        distance = Ai.RUN_SPEED_PPS * game_framework.frame_time
        self.x += (self.dx * distance)
        self.y += (self.dy * distance)
        self.x = clamp(Ai.FIELD_MARGIN, self.x, self.field_width - Ai.FIELD_MARGIN)
        self.y = clamp(Ai.FIELD_MARGIN, self.y, self.field_height - Ai.FIELD_MARGIN)