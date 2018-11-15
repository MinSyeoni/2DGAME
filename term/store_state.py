from pico2d import *
import game_framework
import tutorial_state
from Player import Player
from Coin import Coin
from Life import Life

name = "StoreState"
image = None

class Store:
    def __init__(self):
        self.image = load_image('image/store_back.png')
        self.b1 = load_image('image/store1.png')
        self.b2 = load_image('image/store2.png')
        self.b3 = load_image('image/store3.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 300)
        self.b1.draw(200, 320)
        self.b2.draw(400, 320)
        self.b3.draw(600, 320)

class runsound:
    def __init__(self):
        self.run = load_wav('resource/run.wav')
        self.run.set_volume(20)
    def draw(self):
        pass
    def update(self):
        pass

class button:
    def __init__(self):
        self.button = load_wav('resource/button.wav')
        self.button.set_volume(100)
    def draw(self):
        pass
    def update(self):
        pass

def enter():
    global store
    global player
    global life
    global coin
    global run
    global button
    button = button()
    coin = Coin()
    life = Life()
    store = Store()
    player = Player()
    run = runsound()

def handle_events():
    global player
    global run
    global button
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else :
            if 350< player.x < 430 and 100 < player.y < 180:
                game_framework.change_state(tutorial_state)

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:     ##왼쪽
                player.state = 0
                run.run.play(1)
            elif event.key == SDLK_d:   ##오른쪽
                player.state = 1
                run.run.play(1)
            elif event.key == SDLK_w:   ##위
                player.goto = 0
                run.run.play(1)
            elif event.key == SDLK_s:   ##아래
                player.goto = 1
                run.run.play(1)

        elif event.type == SDL_KEYUP: # 키 안누를때 앉기
            if event.key == SDLK_a:  ##왼쪽
                player.idle = 1
            elif event.key == SDLK_d:  ##오른쪽\
                player.idle = 2
            player.state = 2
            player.goto = 2

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                button.button.play(1)

def draw():
    global store
    global player
    global coin
    global life

    clear_canvas()
    store.draw()
    player.draw()
    coin.draw()
    life.draw()
    update_canvas()

def update():
    global player
    player.update()
    if player.state == 0:
        player.x -= 1
        if player.x < 100:
            player.x = 100
    elif player.state == 1:
        player.x += 1
        if player.x > 700:
            player.x = 700

    if player.goto == 0:
        player.y += 1
        if player.y > 520:
            player.y = 520
    elif player.goto == 1:
        player.y -= 1
        if player.y < 150:
            player.y = 150

def exit():
    pass

if __name__ == '__main__':
    main()