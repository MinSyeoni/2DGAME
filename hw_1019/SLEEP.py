from pico2d import *

def enter_SLEEP(self):
    self.frame = 0

def exit_SLEEP(self):
    pass

def do_SLEEP(self):
    self.frame = (self.frame + 1) % 8

def draw_SLEEP(self):
    if self.dir == 1:
        self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x-25, self.y-25, 100, 100)
    else:
        self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, 3.141592/2, '', self.x+25, self.y-25, 100, 100)
