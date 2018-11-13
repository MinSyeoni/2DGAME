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

class key:
    def __init__(self):
        self.timer = 0
        self.key_sound = load_wav('resource/button.wav')
        self.key_sound.set_volume(100)
    def draw(self):
        pass
    def update(self):
        self.timer += 0.1
        print(self.timer)

def enter():
    global bg,button
    bg = title()
    button = key()

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
    global bg,button
    i = 0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                button.key_sound.play()
                while i >= 0:
                    # print(i)
                    i += 0.0001
                    if i > 17:
                        i = 17
                        break
                if i == 17:
                    game_framework.change_state(tutorial_state)


if __name__ == '__main__':
    main()