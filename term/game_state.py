from pico2d import *
import game_framework
import tutorial_state
import game_world
from Player import Player
from Bullet import Bullet
from Life import Life
from Coin import Coin
from Ai import Ai

name = "GameState"
image = None
global Boundingbox
Boundingbox = 0

class Ingame:
    def __init__(self):
        self.image = load_image('image/background.png')
        self.bgm = load_wav('resource/gamestate.WAV')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()
    def draw(self):
        self.image.draw(400, 300)
    def update(self):
        pass

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
    global player,bullets,bg,ai,life,coin,run,bullet
    player = Player()
    bg = Ingame()
    life = Life()
    coin = Coin()
    ai = Ai()
    bullets = []
    run = runsound()
    bullet = bulletsound()

def draw():
    global player,bullets,bg,ai,coin,Boundingbox
    clear_canvas()
    bg.draw()
    ai.draw(player.x)
    player.draw()
    life.draw()
    coin.draw()

    for loc in player.attack:
        player.attack_image.draw(loc[0], loc[1])

    for member in bullets:
        member.draw()

    if Boundingbox == 1:
        player.draw_bb()
        for member in bullets:
            member.draw_bb()
        for member in ai:
            member.draw_bb()
        for member in player:
            member.draw_bb()
    update_canvas()

def collides(a, b):
    if not hasattr(a, 'get_bb'): return False
    if not hasattr(b, 'get_bb'): return False

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def update():
    global player,bullets
    game_world.update()
    player.update()
    ai.update(player.x, player.y)

    for member in bullets:
        member.update()
    bullets = [b for b in bullets if not b.shouldDelete]

    # game_world.update()
    # for bullets in game_world.objects_at_layer(game_world.layer_obstacle()):
    #     if collides(player, bullets):
    #         print("Collision:", bullets)
    #         game_world.remove_object(bullets)

def handle_events():
    global running
    global player,tx,ty
    global bullets

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif 99 < player.x < 150 and 300 < player.y < 350:
            game_framework.change_state(tutorial_state)
            bg.bgm.stop()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:  ##왼쪽
                player.state = 0
                run.run.play(1)
            elif event.key == SDLK_d:  ##오른쪽
                player.state = 1
                run.run.play(1)
            elif event.key == SDLK_w:  ##위
                player.goto = 0
                run.run.play(1)
            elif event.key == SDLK_s:  ##아래
                player.goto = 1
                run.run.play(1)

        elif event.type == SDL_KEYUP:  # 키 안누를때 앉기
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

def exit():
    game_world.clear()

if __name__ == '__main__':
    main()