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
from AiBullet import Missile
from AiLife import AiLife

name = "GameState"
image = None
global Boundingbox
Boundingbox = 0

class Ingame:
    def __init__(self):
        self.image = load_image('image/background.png')
        self.bgm = load_music('resource/gamestate.mp3')
        self.bgm.set_volume(100)
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
    global player,bullets,bg,ai,life,coin,run,bullet,m1,m2,aiLife
    player = Player()
    bg = Ingame()
    life = Life()
    coin = Coin()
    aiLife = AiLife()
    ai = Ai()
    bullets = []
    run = runsound()
    bullet = bulletsound()
    game_world.add_object(player,game_world.layer_player)
    # for i in range(10):
    #    createMissle()

def createMissle():
    m = Missile(*gen_random(),60)
    game_world.add_object(m,game_world.layer_obstacle)

score = 0
def gen_random():
    global score
    field_width = 800
    field_height = 600
    dx,dy = random.random(),random.random()
    if (dx < 0.5): dx -= 1
    if (dy < 0.5): dy -= 1

    side = random.randint(1,4)
    if(side == 1):
        x,y = random.randint(0,field_width),0
        if(dy < 0): dy = -dy
    if (side == 2):
        x, y = random.randint(0, field_height), 0
        if (dx < 0): dx = -dx
    if (side == 3):
        x, y = random.randint(0, field_width), field_height
        if (dy > 0): dy = -dy
    if (side == 4):
        x, y = field_width, random.randint(0, field_height)
        if (dx < 0): dx = -dx

    speed = 1 + score / 60
    dx,dy = dx * speed, dy * speed
    return x,y,dx,dy

def draw():
    global player,bullets,bg,ai,coin,Boundingbox,aiLife
    clear_canvas()
    bg.draw()
    ai.draw(player.x)
    life.draw()
    coin.draw()
    aiLife.draw(player.x,player.y)
    game_world.draw()
    print(game_world.count_at_layer(game_world.layer_obstacle))
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

def collides_distance(a, b):
    dx, dy = a.x - b.x, a.y - b.y
    sq_dist = dx ** 2 + dy ** 2
    radius_sum = a.size / 2 + b.size / 2
    return sq_dist < radius_sum ** 2

def update():
    global player,bullets,bg,life
    game_world.update()
    obstacle_count = game_world.count_at_layer(game_world.layer_obstacle)
    ai.update(player.x, player.y)
    if obstacle_count < 10:
        createMissle()

    for member in bullets:
        member.update()
    bullets = [b for b in bullets if not b.shouldDelete]

    for m in game_world.objects_at_layer(game_world.layer_obstacle):
        collides = collides_distance(player, m)
        if (collides):
            life.heart -= 1
            print("player life = ",life.heart)
            game_world.remove_object(m)
            break

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
        # elif 99 < player.x < 150 and 300 < player.y < 350:
        #     game_framework.change_state(tutorial_state)

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