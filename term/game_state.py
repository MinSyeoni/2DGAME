from pico2d import *
import game_framework
import tutorial_state
import game_world
import random
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
    def draw(self):
        self.image.draw(400, 300)

def enter():
    global player,tutorial,bullets,ingame,ai,life,coin
    player = Player()
    ingame = Ingame()
    life = Life()
    coin = Coin()
    ai = Ai()
    bullets = []

def handle_events():
    global running
    global player,tx,ty
    global attack
    global bullets

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif 99 < player.x < 150 and 300 < player.y < 350:
            game_framework.change_state(tutorial_state)

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:  ##왼쪽
                player.state = 0
            elif event.key == SDLK_d:  ##오른쪽
                player.state = 1
            elif event.key == SDLK_w:  ##위
                player.goto = 0
            elif event.key == SDLK_s:  ##아래
                player.goto = 1

        elif event.type == SDL_KEYUP:  # 키 안누를때 앉기
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

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def draw():
    global player,tutorial,bullets,ingame,ai,coin,Boundingbox
    clear_canvas()
    ingame.draw()
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
    global player,bullets, ai,Boundingbox
    game_world.update()
    player.update()
    ai.update(player.x,player.y)

    if player.state == 0:
        player.x -= 1
        if player.x < 100:
            player.x = 100
    elif player.state == 1:
        player.x += 1
        if player.x >700:
            player.x = 700

    if player.goto == 0:
        player.y += 1
        if player.y > 520:
            player.y = 520
    elif player.goto == 1:
        player.y -= 1
        if player.y < 150:
            player.y = 150

    for member in bullets:
        member.update()

    #for bullets in game_world.objects_at_layer(game_world.layer_obstacle):
    if collides(ai, bullets):
        print("Collision:", bullets)
        game_world.remove_object(bullets)

    bullets = [b for b in bullets if not b.shouldDelete]

def exit():
    pass

if __name__ == '__main__':
    main()