from pico2d import *
import game_framework
import game_world
import store_state
import random
from Player import Player
from Bullet import Bullet
from Life import Life
from Coin import Coin
from Ai import Ai
from AiBullet import Missile
from AiLife import AiLife
from Ui import Button

name = "GameState"
image = None
global Boundingbox
Boundingbox = 0

GAMESTATE_READY, GAMESTATE_INPLAY, GAMESTETE_GAMEOVER = range(3)
gameState = GAMESTATE_READY

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

class die:
    def __init__(self):
        self.image = load_image('image/gameover.png')
    def draw(self):
        self.image.draw(400,300)

buttons = []
def selectButton(b):
    sizes = len(buttons)
    for i in range(sizes):
        if buttons[i] == b:
            print(str(i) + ' has been selected')
            buttons[i].selected = True
            if buttons[1].selected == True:
                game_framework.change_state(store_state)
        else:
            buttons[i].selected = False

class start:
    def __init__(self):
        self.image = load_image('image/start.png')
    def draw(self):
        self.image.draw(400,300)

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
    global player,bullets,bg,ai,life,coin,run,bullet,m1,m2,aiLife,die,start
    global gameState
    player = Player()
    start = start()
    bg = Ingame()
    life = Life.singleton()
    coin = Coin.singleton()
    aiLife = AiLife.singleton()
    ai = Ai()
    bullets = []
    run = runsound()
    bullet = bulletsound()
    die = die()
    game_world.add_object(player,game_world.layer_player)

    global gameState
    gameState = GAMESTATE_READY
    game_world.isPaused = isPaused
    global buttons
    buttons.append(Button('image/replay.png', 'image/replay.png', 200, 140))
    buttons.append(Button('image/store.png', 'image/store.png', 400, 140))
    buttons.append(Button('image/exit.png', 'image/exit.png', 600, 140))

def isPaused():
    global gameState
    return gameState != GAMESTATE_INPLAY

def start_game():
    global gameState
    gameState = GAMESTATE_INPLAY

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
    global player,bullets,bg,ai,coin,Boundingbox,aiLife,die,start
    clear_canvas()
    bg.draw()
    ai.draw(player.x)
    life.draw()
    coin.draw()
    aiLife.draw(player.x,player.y)
    game_world.draw()
    if gameState == GAMESTATE_READY:
        start.draw()
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

    if life.heart <= 0:
        life.heart = 0
        die.draw()
        for b in buttons:
            b.draw()

    update_canvas()

def collides_distance(a, b):
    dx, dy = a.x - b.x, a.y - b.y
    sq_dist = dx ** 2 + dy ** 2
    radius_sum = a.size / 2 + b.size / 2
    return sq_dist < radius_sum ** 2

def collides_bullet(a, b):
    dx, dy = a.x - b.currX, a.y - b.currY
    sq_dist = dx ** 2 + dy ** 2
    radius_sum = a.size / 2 + b.size / 2
    return sq_dist < radius_sum ** 2

def collides_die(a, b):
    dx, dy = a.x - b.x, a.y - b.y
    sq_dist = dx ** 2 + dy ** 2
    radius_sum = a.size / 2 + b.size / 2
    return sq_dist < radius_sum ** 2

def update():
    global player,bullets,bg,life,ai,die
    game_world.update()
    obstacle_count = game_world.count_at_layer(game_world.layer_obstacle)
    ai.update(player.x, player.y)
    if obstacle_count < 10:
        createMissle()

    for m in game_world.objects_at_layer(game_world.layer_obstacle):
        collides = collides_distance(player, m)
        if (collides):
            life.heart -= 1
            game_world.remove_object(m)
            break

    collides = collides_die(ai, player) ## player와 ai충돌시 게임오버
    if (collides):
        life.heart = 0
        die.draw()
        for b in buttons:
            b.draw()

    for member in bullets:
        member.update()
        collides = collides_bullet(ai, member)
        if (collides):
            aiLife.heart -= 5
            bullets = [b for b in bullets if b.shouldDelete]
            break
    bullets = [b for b in bullets if not b.shouldDelete]



def handle_events():
    global running
    global player,tx,ty
    global bullets, gameState

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()

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

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if gameState == GAMESTATE_READY:
                start_game()

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                bullet.bullet.play(1)
                tx, ty = event.x, 600 - 1 - event.y
                newBullet = Bullet(player.x, player.y, tx, ty)
                bullets.append(newBullet)
            x, y = event.x, get_canvas_height() - event.y
            for b in buttons:
                if b.hits(x, y):
                    selectButton(b)
                    print(b)

def exit():
    game_world.clear()

if __name__ == '__main__':
    main()