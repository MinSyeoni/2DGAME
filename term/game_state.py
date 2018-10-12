from pico2d import *
from term import game_framework
from term import tutorial_state
import random

class Boy:
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(90,550)
        self.speed = random.uniform(1.0,3.0)
        self.frame = random.randint(0,7)
        self.point = []
        self.image = load_image('image/run_stand_ani.png')
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8

def handle_events():
    global running
    global boys
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(tutorial_state)

def enter():
    global boys, grass
    boys = [ Boy() for i in range(20) ]

def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw()
    update_canvas()

def update():
    global boys
    for b in boys:
        b.update()
    delay(0.01)

def exit():
    close_canvas()

if __name__ == '__main__':
    main()