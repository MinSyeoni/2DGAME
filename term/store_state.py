from pico2d import *
import game_framework
import tutorial_state
from Player import Player

name = "StoreState"
image = None

class Store:
    def __init__(self):
        self.image = load_image('image/store_back.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 300)

def enter():
    global store
    global player
    store = Store()
    player = Player()

def handle_events():
    global player
    print(player.x, player.y)
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
            elif event.key == SDLK_d:   ##오른쪽
                player.state = 1
            elif event.key == SDLK_w:   ##위
                player.goto = 0
            elif event.key == SDLK_s:   ##아래
                player.goto = 1

        elif event.type == SDL_KEYUP: # 키 안누를때 앉기
            if event.key == SDLK_a:  ##왼쪽
                player.idle = 1
            elif event.key == SDLK_d:  ##오른쪽\
                player.idle = 2
            player.state = 2
            player.goto = 2

def draw():
    global store
    global player

    clear_canvas()
    store.draw()
    player.draw()
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