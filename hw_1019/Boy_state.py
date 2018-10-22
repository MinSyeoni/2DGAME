from pico2d import *
import random
import time

# Boy State
IDLE, RUN, SLEEP = range(3)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP }
next_state_table = {
    IDLE: {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN: RUN, LEFT_DOWN: RUN, TIME_OUT: SLEEP},
    RUN: {RIGHT_UP: IDLE, LEFT_UP: IDLE, LEFT_DOWN: IDLE, RIGHT_DOWN: IDLE},
    SLEEP: {LEFT_DOWN: RUN, RIGHT_DOWN: RUN}}

def change_state(self,  state):
    self.exit_state[self.cur_state](self)
    self.enter_state[state](self)
    self.cur_state = state

enter_state = {IDLE: enter_IDLE, RUN: enter_RUN, SLEEP: enter_SLEEP}
exit_state =  {IDLE: exit_IDLE,  RUN: exit_RUN,  SLEEP: exit_SLEEP}
do_state =    {IDLE: do_IDLE,    RUN: do_RUN,    SLEEP: do_SLEEP}
draw_state =  {IDLE: draw_IDLE,  RUN: draw_RUN,  SLEEP: draw_SLEEP}

def update(self):
    self.do_state[self.cur_state](self)
    if len(self.event_que) > 0:
        event = self.event_que.pop()
        self.change_state(next_state_table[self.cur_state][event])

def draw(self):
    self.draw_state[self.cur_state](self)

def handle_event(self, event):
    if (event.type, event.key) in key_event_table:
        key_event = key_event_table[(event.type, event.key)]
        if key_event == RIGHT_DOWN:
            self.velocity += 1
        elif key_event == LEFT_DOWN:
            self.velocity -= 1
        elif key_event == RIGHT_UP:
            self.velocity -= 1
        elif key_event == LEFT_UP:
            self.velocity += 1
        self.add_event(key_event)
