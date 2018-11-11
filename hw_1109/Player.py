from pico2d import *
import random
import time

class IdleState:
    @staticmethod
    def enter(player):
        player.timer = 100
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def update(player):
        player.frame = (player.frame + 1) % 8
        player.timer -= 1
        if player.timer == 0:
            player.set_state(SleepState)
        print(player.timer)
    @staticmethod
    def draw(player):
        y = 200 if player.dir == 0 else 300
        Player.image.clip_draw(player.frame * 100, y, 100, 100, *player.pos())

class RunState:
    MARGIN = 25
    @staticmethod
    def enter(player):
        player.time = time.time()
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def update(player):
        elapsed = time.time() - player.time
        mag = 2 if elapsed > 2.0 else 1
        player.frame = (player.frame + 1) % 8
        player.x = player.x + mag * player.mag * player.dx
        player.y = player.y + mag * player.mag * player.dy
        if hasattr(player.bg, 'clamp'):
            player.bg.clamp(player)
    @staticmethod
    def draw(player):
        src_y = 0 if player.dir == 0 else 100
        Player.image.clip_draw(player.frame * 100, src_y, 100, 100, *player.pos())

class SleepState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def update(player):
        player.frame = (player.frame + 1) % 8
    @staticmethod
    def draw(player):
        if player.dir == 1:
            Player.image.clip_composite_draw(player.frame * 100, 300, 100, 100, 3.141592/2, '', player.x-25, player.y-25, 100, 100)
        else:
            Player.image.clip_composite_draw(player.frame * 100, 200, 100, 100, 3.141592/2, '', player.x+25, player.y-25, 100, 100)

class Player:
    image = None
    def __init__(self):
        self.x = random.randint(0, 200)
        self.y = 90
        self.speed = random.uniform(5.0, 8.0)
        self.frame = random.randint(0, 7)
        self.state = None
        self.set_state(IdleState)
        self.dir = 1
        self.dx = 0
        self.dy = 0
        self.mag = 1
        if Player.image == None:
            Player.image = load_image('../image/run_stand_ani.png')

    def pos(self):
        return self.x - self.bg.x, self.y - self.bg.y

    def draw(self):
        self.state.draw(self)

    def update(self):
        self.state.update(self)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:  ##왼쪽
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            elif event.key == SDLK_d:  ##오른쪽
                self.dx += self.speed
                if self.dx > 0: self.dir = 1
            elif event.key == SDLK_w:  ##위
                self.dy += self.speed
            elif event.key == SDLK_s:  ##아래
                self.dy -= self.speed

        elif event.type == SDL_KEYUP:  # 키 안누를때 앉기
            if event.key == SDLK_a:  ##왼쪽
                self.dx += self.speed
                if self.dx > 0: self.dir = 1
            elif event.key == SDLK_d:  ##오른쪽\
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            if event.key == SDLK_w:  ##위쪽
                self.dy -= self.speed
            elif event.key == SDLK_s:  ##아래쪽\
                self.dy += self.speed

        self.set_state(IdleState if self.dx == 0 and self.dy == 0 else RunState)

    def set_state(self, state):
        if self.state == state: return

        if self.state and self.state.exit:
            self.state.exit(self)

        self.state = state

        if self.state.enter:
            self.state.enter(self)