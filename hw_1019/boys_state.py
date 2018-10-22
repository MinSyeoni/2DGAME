from pico2d import *
import game_framework
import title_state
import random
import json
import time

from enum import Enum

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None
    RUN_LEFT, RUN_RIGHT, IDLE_LEFT, IDLE_RIGHT = 0, 1, 2, 3
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(90,550)
        self.speed = random.uniform(1.0,3.0)
        self.frame = random.randint(0,7)
        self.point = []
        self.dir = 1
        self.state = self.IDLE_RIGHT
        if Boy.image == None:
            Boy.image = load_image('../image/animation_sheet.png')
        self.goal = load_image('../image/goal.png')
        self.stand_frames = 0
        self.run_frames = 0
        print(self.image)

    def draw(self):
        for goal in self.point:
            self.goal.draw(goal[0],goal[1])
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)
        if len(self.point) == 0:
            if self.state == Boy.RUN_RIGHT :
                self.state = Boy.IDLE_RIGHT
            else:
                self.state = Boy.IDLE_RIGHT
        else:
            (tx,ty) = self.point[0]
            pointX, pointY = tx - self.x, ty - self.y
            list = math.sqrt(pointX ** 2 + pointY ** 2)
            if list > 0:
                self.x += self.speed * pointX / list
                self.y += self.speed * pointY / list
                if pointX < 0 and self.x < tx: self.x = tx
                if pointX > 0 and self.x > tx: self.x = tx
                if pointY < 0 and self.y < ty: self.y = ty
                if pointY > 0 and self.y > ty: self.y = ty
            if(tx,ty) == (self.x,self.y):
                del self.point[0]
                self.determine_state()

    def determine_state(self):
        if len(self.point) ==0:
            self.state = Boy.IDLE_RIGHT if self.state == Boy.IDLE_LEFT else Boy.RUN_RIGHT
        else:
            tx,ty = self.point[0]
            self.state = Boy.RUN_RIGHT if tx > self.x else Boy.RUN_LEFT

    def handle_left_run(self):
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RUN_LEFT
            self.x = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.IDLE_LEFT
            self.run_frames = 0

    def handle_right_run(self):
        self.run_frames += 1
        if self.x > 800:
            self.state = self.RUN_RIGHT
            self.x = 800

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.IDLE_RIGHT
            self.run_frames = 0

    handle_state = {
        RUN_LEFT: handle_left_run,
        RUN_RIGHT: handle_right_run,
        IDLE_LEFT: handle_left_stand,
        IDLE_RIGHT: handle_right_stand
    }

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

def handle_events():
    global running
    global point
    global boy
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        else:
            boy.handle_state

def update(self):
    self.frame = (self.frame + 1) % 8
    self.handle_state[self.state](self)

def draw():
    global grass, boy
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def update():
    global boy
    boy.update()
    delay(0.03)

def exit():
    pass

if __name__ == '__main__':
    main()