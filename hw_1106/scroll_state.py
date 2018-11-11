from pico2d import *
import game_framework
from boy import Boy
import game_world
from math import atan2
from math import sqrt

DEL_MARGIN = 25
WIND_RESISTANCE = 0.99#7
BOUNCE_RESISTANCE = 0.70
GRAVITY = 10 / 33
BOUNCING_GROUND = 62

MIN_MOVE = 2

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Stick:
    def __init__(self):
        self.image = load_image('../image/stick.png')
        print(self.image)
        self.x= boy.x
        self.y= boy.y+100
        self.rad = 0
    def draw(self):
        self.image.clip_composite_draw(0, 0, 16, 77,
            self.rad, '', self.x , self.y, 20, 100)
        # self.image.draw(self.x,self.y)

    def update(self):
        pass

def enter():
    global boy, grass,stick

    boy = Boy()
    grass = Grass()
    stick = Stick()
    game_world.add_object(grass, game_world.layer_bg)
    game_world.add_object(boy, game_world.layer_player)
    game_world.add_object(stick, game_world.layer_stick)

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def collides(a, b):
    if not hasattr(a, 'get_bb'): return False
    if not hasattr(b, 'get_bb'): return False

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def update():
    game_world.update()
    for ball in game_world.objects_at_layer(game_world.layer_obstacle):
        if collides(boy, ball):
            print("Collision:", ball)
            game_world.remove_object(ball)
    delay(0.03)

def handle_events():
     global boy
     global stick
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             game_framework.quit()
         elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
             game_framework.pop_state()
         else:
             boy.handle_event(event)
         if event.type == SDL_MOUSEMOTION:
            tx, ty = event.x, 600 - 1 - event.y
            boy.getX = -(stick.x-tx)/150
            boy.getY = -(stick.y-ty)/150
            stick.rad = math.atan2(stick.x-tx, ty-stick.y)

def exit():
    game_world.clear()

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()