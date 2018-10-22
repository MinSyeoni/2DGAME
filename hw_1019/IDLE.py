from pico2d import *

def enter_IDLE(self):
    self.timer = 1000
    self.frame = 0

def exit_IDLE(self):
    pass

def do_IDLE(self):
    self.frame = (self.frame + 1) % 8
    self.timer -= 1
    if self.timer == 0:
        self.add_event(SLEEP_TIMER)

def draw_IDLE(self):
    if self.dir == 1:
        self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
    else:
        self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
