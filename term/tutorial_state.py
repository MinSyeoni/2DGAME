from pico2d import *
from term import game_framework
from term import title_state
import random

class Tutorial:
    def __init__(self):
        self.image = load_image('image/tutorial.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 300)

class Player:
    def __init__(self):
        self.x = random.randint(90,700)
        self.y = random.randint(100,500)
        self.speed = random.uniform(1.0,3.0)
        self.frame = random.randint(0,7)
        self.image = load_image('image/run_stand_ani.png')
        self.state = 0 # 0 - 멈춤, 1- 왼쪽, 2 - 오른쪽, 3 - 위, 4 - 아래
        print(self.image)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        events = get_events()
        self.frame = (self.frame + 1) % 8


def enter():
    global player,tutorial
    player = Player()
    tutorial = Tutorial()

def draw():
    global player,tutorial
    clear_canvas()
    tutorial.draw()
    player.draw()
    update_canvas()

def update():
    global player
    player.update()
    if player.state == 1:
        player.x -= 5
        if player.x < 100: # 이동범위 제한
            player.x = 100
    elif player.state == 2:
        player.x += 5
        if player.x >700:
            player.x = 700
    elif player.state == 3:
        player.y += 5
        if player.y > 520:
            player.y = 520
    elif player.state == 4:
        player.y -= 5
        if player.y < 150:
            player.y = 150

    delay(0.05)

def handle_events():
    global running
    global player

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:     ##왼쪽
                player.state = 1
            elif event.key == SDLK_d:   ##오른쪽
                player.state = 2
            elif event.key == SDLK_w:   ##위
                player.state = 3
            elif event.key == SDLK_s:   ##아래
                player.state = 4
        elif event.type == SDL_KEYUP:
            player.state = 0

def exit():
    close_canvas()

if __name__ == '__main__':
    main()