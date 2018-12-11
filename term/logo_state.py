from pico2d import *
import game_framework
import title_state

name = "StartState"
logo = None
logo_time = 0.0

def enter():
    global logo
    logo = load_image('logo.png')

def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    global logo
    clear_canvas()
    logo.draw(400, 300)
    update_canvas()

def exit():
    global logo
    del logo

def handle_events():
    pass

def pause():
    pass

def resume():
    pass

def main():
    enter()

if __name__ == '__main__':
    main()
