from pico2d import *
import random
import math

KPU_WIDTH, KPU_HEIGHT = 800, 600

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
        print(self.image)
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if len(point) > 0:
            (tx,ty) = point[0]
            pointX, pointY = tx - self.x, ty - self.y
            list = math.sqrt(pointX ** 2 + pointY ** 2)
            if list > 0:
                self.x += self.speed * pointX / list
                self.y += self.speed * pointY / list
                if pointX < 0 and self.x < tx: self.x = tx
                if pointX > 0 and self.x > tx: self.x = tx
                if pointY < 0 and self.y < tx: self.y = ty
                if pointY < 0 and self.y < tx: self.y = ty
            if(self.x, self.y) == (tx,ty):
                del point[0]

def handle_events():
    global running
    global point
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == 1:
                tx, ty = event.x, KPU_HEIGHT - 1 - event.y
                point += [(tx,ty)]
            else:
                point = []

open_canvas(KPU_WIDTH, KPU_HEIGHT)

boys = [Boy() for i in range(20)]
grass = Grass()
running = True
x,y = KPU_WIDTH, KPU_HEIGHT
tx,ty=x,y
frame = 0
point = []
goal = load_image('goal.png')

while running:
    handle_events()

    for boy in boys:
        boy.update()

    clear_canvas()
    grass.draw()

    for loc in point:
        goal.draw(loc[0], loc[1])

    for boy in boys:
        boy.draw()

    update_canvas()

    delay(0.01)
    handle_events()
close_canvas()