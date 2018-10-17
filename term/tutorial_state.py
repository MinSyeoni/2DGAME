from pico2d import *
import game_framework
import title_state
import game_state
import store_state
from Player import Player
from Bullet import Bullet
import random

name = "TutorialState"
image = None

class Tutorial:
    def __init__(self):
        self.image = load_image('image/tutorial.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 300)

def enter():
    global player,tutorial,bullets
    player = Player()
    tutorial = Tutorial()
    bullets = []

def handle_events():
    global running
    global player
    global attack
    global bullets

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else :
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif 350< player.x <400 and 450 < player.y < 520:
                game_framework.change_state(store_state)
            elif 650 < player.x < 700 and 300 < player.y <350:
                game_framework.change_state(game_state)

        # if event.type == SDL_QUIT:
        #     running = False
        #
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

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                tx, ty = event.x, 600 - 1 - event.y
                newBullet = Bullet(player.x, player.y, tx, ty)
                bullets.append(newBullet)

def draw():
    global player,tutorial,bullets
    clear_canvas()
    tutorial.draw()
    player.draw()

    for loc in player.attack:
        player.attack_image.draw(loc[0], loc[1])

    for member in bullets:
        member.draw()
    update_canvas()

def update():
    global player
    global bullets
    player.update()
    if player.state == 0:
        player.x -= 5
        if player.x < 100:
            player.x = 100
    elif player.state == 1:
        player.x += 5
        if player.x >700:
            player.x = 700

    if player.goto == 0:
        player.y += 5
        if player.y > 520:
            player.y = 520
    elif player.goto == 1:
        player.y -= 5
        if player.y < 150:
            player.y = 150
    delay(0.05)

    for member in bullets:
        member.update()

    bullets = [b for b in bullets if not b.shouldDelete]

def exit():
    global image
    del(image)

if __name__ == '__main__':
    main()