from pico2d import *
from hw_0928 import game_framework
from hw_0928 import title_state
import random
import json
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
            self.state = self.state == Boy.RUN_RIGHT
        else:
            (tx,ty) = self.point[0]
            pointX, pointY = tx - self.x, ty - self.y
            list = math.sqrt(pointX ** 2 + pointY ** 2)
            if list > 0:
                self.x += self.speed * pointX / list
                self.y += self.speed * pointY / list
                if pointX < 0 and self.x < tx: self.x = tx
                if pointX > 0 and self.x > tx: self.x = tx
                if pointY < 0 and self.y < tx: self.y = ty
                if pointY > 0 and self.y > tx: self.y = ty
            if(tx,ty) == (self.x,self.y):
                del self.point[0]

    def determine_state(self):
        if len(self.point) ==0:
            self.state = Boy.IDLE_RIGHT if self.state == Boy.RUN_RIGHT else Boy.IDLE_LEFT
        else:
            tx,ty = self.point[0]
            self.state = Boy.RUN_RIGHT if tx > self.x else Boy.RUN_LEFT

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RUN_RIGHT
            self.x = 0
        if self.run_frames == 100:
            self.state = self.IDLE_LEFT
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RUN_LEFT
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.RUN_LEFT
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    handle_state = {
        RUN_LEFT: handle_left_run,
        RUN_RIGHT: handle_right_run,
        IDLE_LEFT: handle_left_stand,
        IDLE_RIGHT: handle_right_stand
    }

def handle_events():
    global running
    global point
    global boys
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                for b in boys:
                    tx, ty = event.x, 600 - 1- event.y
                    b.point += [(tx, ty)]
            else:
               for b in boys:
                   b.point = []

def update(self):
    self.frame = (self.frame + 1) % 8
    self.handle_state[self.state](self)

def enter():
    global boys, grass

    boys = []
    fh = open('boys_data.json')
    data = json.load(fh)
    for e in data['boys']:
        b = Boy()
        b.name = e['name']
        b.x = e['x']
        b.y = e['y']
        b.speed = e['speed']
        boys.append(b)

    grass = Grass()

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
    pass

if __name__ == '__main__':
    main()