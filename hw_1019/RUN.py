from pico2d import *

def enter_RUN(self):
    self.frame = 0
    self.dir = self.velocity

def exit_RUN(self):
    pass

def do_RUN(self):
    self.frame = (self.frame + 1) % 8
    self.x += self.velocity
    self.x = clamp(25, self.x, 800-25)

def draw_RUN(self):
    if self.velocity == 1:
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
    else:
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
