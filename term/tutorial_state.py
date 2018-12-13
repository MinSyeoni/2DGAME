from pico2d import *
import game_framework
import game_state
import store_state
from Player import Player
from Bullet import Bullet
import random

name = "TutorialState"
image = None

class Tutorial:
    def __init__(self):
        self.image = load_image('tutorial.png')
        print(self.image)
        self.bgm = load_music('tutorial.mp3')
        self.bgm.set_volume(100)
        self.bgm.repeat_play()
    def draw(self):
        self.image.draw(400, 300)

class runsound:
    def __init__(self):
        self.run = load_wav('run.wav')
        self.run.set_volume(20)
    def draw(self):
        pass
    def update(self):
        pass

class bulletsound:
    def __init__(self):
        self.bullet = load_wav('bullet.wav')
        self.bullet.set_volume(30)
    def draw(self):
        pass
    def update(self):
        pass

def enter():
    global player_tuto,tutorial,bullets,run_tutosound,bullet_tutosound
    player_tuto = Player()
    tutorial = Tutorial()
    run_tutosound = runsound()
    bullets = []
    bullet_tutosound = bulletsound()

def handle_events():
    global running
    global player_tuto
    global attack
    global bullets
    global run

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else :
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif 350< player_tuto.x < 430 and 450 < player_tuto.y < 530:
                game_framework.change_state(store_state)
            elif 650 < player_tuto.x < 750 and 300 < player_tuto.y <350:
                tutorial.bgm.pause()
                game_framework.change_state(game_state)

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:     ##왼쪽
                player_tuto.state = 0
                run_tutosound.run.play(1)
            elif event.key == SDLK_d:   ##오른쪽
                player_tuto.state = 1
                run_tutosound.run.play(1)
            elif event.key == SDLK_w:   ##위
                player_tuto.goto = 0
                run_tutosound.run.play(1)
            elif event.key == SDLK_s:   ##아래
                player_tuto.goto = 1
                run_tutosound.run.play(1)

        elif event.type == SDL_KEYUP: # 키 안누를때 앉기
            if event.key == SDLK_a:  ##왼쪽
                player_tuto.idle = 1
            elif event.key == SDLK_d:  ##오른쪽\
                player_tuto.idle = 2
            player_tuto.state = 2
            player_tuto.goto = 2

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                bullet_tutosound.bullet.play(1)
                tx, ty = event.x, 600 - 1 - event.y
                newBullet = Bullet(player_tuto.x, player_tuto.y, tx, ty)
                bullets.append(newBullet)

def draw():
    global player_tuto,tutorial,bullets
    clear_canvas()
    tutorial.draw()
    player_tuto.draw()

    for loc in player_tuto.attack:
        player_tuto.attack_image.draw(loc[0], loc[1])

    for member in bullets:
        member.draw()
    update_canvas()

def update():
    global player_tuto
    global bullets
    player_tuto.update()
    delay(0.007)
    for member in bullets:
        member.update()

    bullets = [b for b in bullets if not b.shouldDelete]

def exit():
    pass

if __name__ == '__main__':
    main()