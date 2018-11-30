from pico2d import *
import game_framework
import tutorial_state
from Player import Player
from Coin import Coin
from Life import Life
from Ui import Button

name = "StoreState"
image = None

class Store:
    def __init__(self):
        self.image = load_image('image/store_back.png')
    def draw(self):
        self.image.draw(400, 300)

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

# class storelife:
#     def __init__(self):
#         self.x = 0
#         self.lifex = 0
#         self.font = load_font('resource/ConsolaMalgun.TTF', 40)
#     def draw(self):
#         self.font.draw(530, 550, '%d ' % (life.heart + self.x), (255, 0, 0))  # 생명 출력
#     def update(self):
#         self.lifex = life.heart + self.x
#         if self.lifex <= 0:
#             self.lifex = 0
#
# class storecoin:
#     def __init__(self):
#         self.x = 0
#         self.coinx = 0
#         self.font = load_font('resource/ConsolaMalgun.TTF', 40)
#     def draw(self):
#         if coin.coin + self.x >0:
#             self.font.draw(630, 550, '%d ' % (coin.coin + self.x), (250, 250, 0))  # 코인 출력
#         if coin.coin + self.x <=0:
#             self.font.draw(630, 550, '%d ' % (0), (250, 250, 0))
#     def update(self):
#         self.coinx = coin.coin + self.x
#         if self.coinx <=0:
#             self.coinx = 0
#         print("%d",self.coinx)

buttons = []
def selectButton(b):
    size = len(buttons)
    for i in range(size):
        if buttons[i] == b:
            print(str(i) + ' has been selected')
            buttons[i].selected = True
            if buttons[0].selected == True:
                s_life.x += 1
                s_coin.x -= 100
                if s_life.x >= 5:
                    s_life.x = 5
                print("heart +1")
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
                    print(b)

def enter():
    global store
    global player
    global life
    global coin
    global run
    global sound
    global buttons
    # global s_life
    # global s_coin
    # s_coin = storecoin()
    # s_life = storelife()
    sound = buttonsound()
    coin = Coin()
    life = Life.singleton()
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
    # life.draw(0)
    s_life.draw()
    s_coin.draw()
    for b in buttons:
        b.draw()
    update_canvas()

def update():
    global player
    global s_life
    player.update()
    s_coin.update()
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