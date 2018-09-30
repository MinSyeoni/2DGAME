from pico2d import *
from hw_0928 import game_framework
from hw_0928 import title_state

name = "StartState"
logo = None
logo_time = 0.0

def enter():
    global logo
    open_canvas()
    logo = load_image('../image/kpu_credit.png')

def exit():
    del logo

def draw():
    global logo
    clear_canvas()
    logo.draw(800, 600)
    update_canvas()

def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01

def handle_events():
    pass

def pause():
    pass

def resume():
    pass

