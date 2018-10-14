from pico2d import *
from term import game_framework
from term import tutorial_state

class Store:
    def __init__(self):
        self.image = load_image('image/store_back.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 300)

def enter():
    global store
    store = Store()

def draw():
    global store
    clear_canvas()

    store.draw()

    update_canvas()

def exit():
    close_canvas()

if __name__ == '__main__':
    main()