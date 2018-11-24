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
        # self.b1 = load_image('image/store1.png')
        # self.b2 = load_image('image/store2.png')
        # self.b3 = load_image('image/store3.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 300)
        # self.b1.draw(200, 320)
        # self.b2.draw(400, 320)
        # self.b3.draw(600, 320)

class runsound:
    def __init__(self):
        self.run = load_wav('resource/run.wav')
        self.run.set_volume(20)
    def draw(self):
        pass
    def update(self):
        pass

class buttonsound:
    def __init__(self):
        self.sound = load_wav('resource/button.wav')
        self.sound.set_volume(100)
    def draw(self):
        pass
    def update(self):
        pass

class Button:
    def __init__(self, normal, selected, x, y):
        self.normalImage = load_image(normal)
        self.selectedImage = load_image(selected)
        self.x, self.y = x, y
        self.selected = False
    def draw(self):
        if self.selected:
            self.selectedImage.draw(self.x, self.y)
        else:
            self.normalImage.draw(self.x, self.y)
    def hits(self, x, y):
        hw, hh = self.normalImage.w // 2, self.normalImage.h // 2
        if x < self.x - hw: return False
        if x > self.x + hw: return False
        if y < self.y - hh: return False
        if y > self.y + hw: return False
        return True

buttons = []
def selectButton(b):
    size = len(buttons)
    for i in range(size):
        if buttons[i] == b:
            print(str(i) + ' has been selected')
            buttons[i].selected = True
        else:
            buttons[i].selected = False

def handle_events():
    global player
    global run
    global sound
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
                sound.sound.play(1)
            x, y = event.x, get_canvas_height() - event.y
            for b in buttons:
                if b.hits(x, y):
                    selectButton(b)

def enter():
    global store
    global player
    global life
    global coin
    global run
    global sound
    global buttons
    sound = buttonsound()
    coin = Coin()
    life = Life()
    store = Store()
    player = Player()
    run = runsound()
    buttons.append(Button('image/store1.png', 'image/store1.png',200,320))
    buttons.append(Button('image/store2.png', 'image/store2.png', 400, 320))
    buttons.append(Button('image/store3.png', 'image/store3.png', 600, 320))

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
    for b in buttons:
        b.draw()
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