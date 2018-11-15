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
        self.bgm = load_music('resource/tutorial.mp3')
        self.bgm.set_volume(100)
        self.bgm.repeat_play()
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

class bulletsound:
    def __init__(self):
        self.bullet = load_wav('resource/bullet.wav')
        self.bullet.set_volume(30)
    def draw(self):
        pass
    def update(self):
        pass

def enter():
    global player,tutorial,bullets,run,bullet
    player = Player()
    tutorial = Tutorial()
    run = runsound()
    bullets = []
    bullet = bulletsound()

def handle_events():
    global running
    global player
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
            elif 350< player.x < 430 and 450 < player.y < 530:
                game_framework.change_state(store_state)
            elif 650 < player.x < 750 and 300 < player.y <350:
                tutorial.bgm.pause()
                game_framework.change_state(game_state)

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
                bullet.bullet.play(1)
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

    for member in bullets:
        member.update()

    bullets = [b for b in bullets if not b.shouldDelete]

def exit():
    pass

if __name__ == '__main__':
    main()