from pico2d import *
import game_framework
import tutorial_state
import game_state

name = "TitleState"
image = None

class title:
    def __init__(self):
        self.image = load_image('image/title.png')
        self.bgm = load_music('resource/title.mp3')
        self.bgm.set_volume(100)
        self.bgm.repeat_play()
    def draw(self):
        self.image.draw(400, 300)
    def update(self):
        pass

def enter():
    global bg
    bg = title()

def draw():
    global bg
    clear_canvas()
    bg.draw()
    update_canvas()

def update():
    pass

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(tutorial_state)

if __name__ == '__main__':
    main()