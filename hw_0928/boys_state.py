from pico2d import *
from hw_0928 import game_framework
from hw_0928 import title_state
import random
from enum import Enum

BOYS_COUNT = 100

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(90,550)
        self.speed = random.uniform(1.0,3.0)
        self.frame = random.randint(0,7)
        self.point = []
        if Boy.image == None:
            Boy.image = load_image('../image/run_animation.png')
        self.goal = load_image('../image/goal.png')
        print(self.image)
    def draw(self):
        for goal in self.point:
            self.goal.draw(goal[0],goal[1])
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if len(self.point) > 0:
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

def enter():
    global boys, grass

    boys = [ Boy() for i in range(BOYS_COUNT) ]
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
    close_canvas()

if __name__ == '__main__':
    main()