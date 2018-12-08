from pico2d import *
import game_framework
import game_world
import store_state
import random
from Player import Player
from Bullet import Bullet
from Life import Life
from Coin import Coin
from Ruin import Ruin
from Ai import Ai
from AiBullet import Missile
from AiLife import AiLife
from Ui import Button

name = "GameState"
image = None
global Boundingbox
Boundingbox = 0

GAMESTATE_READY, GAMESTATE_INPLAY, GAMESTETE_GAMEOVER, GAMESTATE_PAUSED = range(4)
gameState = GAMESTATE_READY

class Ingame:
    def __init__(self):
        self.image = load_image('image/background.png')
    def draw(self):
        self.image.draw(400, 300)
    def update(self):
        pass

buttons = []
def selectButton(b):
    global gameState
    sizes = len(buttons)
    for i in range(sizes):
        if buttons[i] == b:
            print(str(i) + ' has been selected')
            buttons[i].selected = True
            if buttons[0].selected == True:
                game_framework.change_state(store_state)
            if buttons[1].selected == True:
                game_framework.quit()
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

class clear:
    def __init__(self):
        self.image = load_image('image/gameclear.png')
    def draw(self):
        self.image.draw(400,300)
    def update(self):
        pass

def enter():
    global player_game,bullets,bg_game,ai_game,life_game,coin_game,run_gamesound,bullet_gamesound,m1,m2,aiLife_game,die_game,start_gamepng,clear_game,ruin_game
    global gameState
    player_game = Player()
    start_gamepng = start()
    bg_game = Ingame()
    life_game = Life.singleton()
    clear_game = clear()
    coin_game = Coin.singleton()
    ruin_game = Ruin.singleton()
    aiLife_game = AiLife.singleton()
    ai_game = Ai()
    bullets = []
    run_gamesound = runsound()
    bullet_gamesound = bulletsound()
    # die_game = die()
    # game_world.add_object(player_game,game_world.layer_player)
    global gameoverimage
    gameoverimage = load_image('image/gameover.png')

    global gameState
    gameState = GAMESTATE_READY
    game_world.isPaused = isPaused
    global buttons
    buttons.append(Button('image/store.png', 'image/store.png', 300, 140))
    buttons.append(Button('image/exit.png', 'image/exit.png', 500, 140))

def isPaused():
    global gameState
    return gameState != GAMESTATE_INPLAY

def start_game():
    global gameState
    gameState = GAMESTATE_INPLAY
    game_world.remove_objects_at_layer(game_world.layer_obstacle)
    life_game.heart = 5
    global music_game
    music_game = load_music('resource/gamestate.mp3')
    music_game.set_volume(100)
    music_game.repeat_play()

def ready_game():
    global gameState
    gameState = GAMESTATE_READY
    game_world.remove_objects_at_layer(game_world.layer_obstacle)

def end_game():
    global gameState,diepng
    gameState = GAMESTETE_GAMEOVER
    global music_game
    music_game.stop()
    diepng = load_image('image/gameover.png')
    # diepng.draw(400, 300)

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
    global player_game,bullets,bg_game,ai_game,coin_game,Boundingbox,aiLife_game,die_game,start_gamepng,ruin_game
    global gameState
    clear_canvas()
    bg_game.draw()
    player_game.draw()
    ai_game.draw(player_game.x)
    life_game.draw()
    coin_game.draw()
    ruin_game.draw()
    aiLife_game.draw(player_game.x,player_game.y)
    game_world.draw()
    if gameState == GAMESTATE_READY:
        start_gamepng.draw()
    print(game_world.count_at_layer(game_world.layer_obstacle))
    for loc in player_game.attack:
        player_game.attack_image.draw(loc[0], loc[1])

    for member in bullets:
        member.draw()

    if Boundingbox == 1:
        player_game.draw_bb()
        for member in bullets:
            member.draw_bb()
        for member in ai_game:
            member.draw_bb()
        for member in player_game:
            member.draw_bb()

    if life_game.heart <= 0:
        gameState = GAMESTETE_GAMEOVER
        life_game.heart = 0
        end_game()
        for b in buttons:
            b.draw()

    if aiLife_game.heart <= 0 or ruin_game.ruin == 100:
        gameState = GAMESTATE_PAUSED
        clear_game.draw()

    if gameState == GAMESTETE_GAMEOVER:
        diepng.draw(400, 300)

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
    global player_game,bullets,bg_game,life_game,ai_game,die_game
    game_world.update()
    obstacle_count = game_world.count_at_layer(game_world.layer_obstacle)
    ai_game.update(player_game.x, player_game.y)
    player_game.update()
    if obstacle_count < 7:
        createMissle()

    for m in game_world.objects_at_layer(game_world.layer_obstacle):
        collides = collides_distance(player_game, m)
        if (collides):
            life_game.heart -= 1
            game_world.remove_object(m)
            break

    collides = collides_die(ai_game, player_game) ## player와 ai충돌시 게임오버
    if (collides):
        life_game.heart = 0
        end_game()
        for b in buttons:
            b.draw()

    if aiLife_game.heart <= 0:
        aiLife_game.heart = 0

    for member in bullets:
        member.update()
        collides = collides_bullet(ai_game, member)
        if (collides):
            aiLife_game.heart -= 5
            coin_game.coin += 30
            bullets = [b for b in bullets if b.shouldDelete]
            break
    bullets = [b for b in bullets if not b.shouldDelete]

    if player_game.x <150 and player_game.y <200:
        ruin_game.ruin += 0.05
        if ruin_game.ruin >= 100:
            ruin_game.ruin = 100

def handle_events():
    global running
    global player_game,tx,ty
    global bullets, gameState

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:  ##왼쪽
                player_game.state = 0
                run_gamesound.run.play(1)
            elif event.key == SDLK_d:  ##오른쪽
                player_game.state = 1
                run_gamesound.run.play(1)
            elif event.key == SDLK_w:  ##위
                player_game.goto = 0
                run_gamesound.run.play(1)
            elif event.key == SDLK_s:  ##아래
                player_game.goto = 1
                run_gamesound.run.play(1)

        elif event.type == SDL_KEYUP:  # 키 안누를때 앉기
            if event.key == SDLK_a:  ##왼쪽
                player_game.idle = 1
            elif event.key == SDLK_d:  ##오른쪽\
                player_game.idle = 2
            player_game.state = 2
            player_game.goto = 2

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if gameState == GAMESTATE_READY:
                start_game()

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                bullet_gamesound.bullet.play(1)
                tx, ty = event.x, 600 - 1 - event.y
                newBullet = Bullet(player_game.x, player_game.y, tx, ty)
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