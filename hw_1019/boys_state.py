from pico2d import *
import game_framework
import title_state
import random
import json
from Boy import Boy

from enum import Enum
IDLE, RUN, SLEEP = range(3)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}

next_state_table = {
    IDLE: {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN: RUN, LEFT_DOWN: RUN, TIME_OUT: SLEEP},
    RUN: {RIGHT_UP: IDLE, LEFT_UP: IDLE, LEFT_DOWN: IDLE, RIGHT_DOWN: IDLE},
    SLEEP: {LEFT_DOWN: RUN, RIGHT_DOWN: RUN}}
class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

def handle_events():
    global running
    global point
    global boy
    global next_state_table

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            boy.velocity = - 1
            boy.change_state(1)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            boy.velocity = 1
            boy.change_state(1)
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            boy.velocity = 0
            boy.change_state(0)
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            boy.velocity = 0
            boy.change_state(0)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

def draw():
    global grass, boy
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def update():
    global boy
    boy.update()
    delay(0.01)

def exit():
    pass

if __name__ == '__main__':
    main()