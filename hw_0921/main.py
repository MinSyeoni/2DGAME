import random
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(90,550)
        self.speed = random.uniform(1.0,3.0)
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed

def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

boys = [Boy() for i in range(20)]
grass = Grass()
running = True

while running:
    handle_events()

    for boy in boys:
        boy.update()

    clear_canvas()
    grass.draw()
    for boy in boys:
        boy.draw()
    update_canvas()

    delay(0.03)

close_canvas()