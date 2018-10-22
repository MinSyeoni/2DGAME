from pico2d import *
import game_framework
import tutorial_state
import random
from Player import Player
from Bullet import Bullet

name = "GameState"
image = None

class Ingame:
    def __init__(self):
        self.image = load_image('image/background.png')
    def draw(self):
        self.image.draw(400, 300)

class Ai:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = random.randint(150,500)
        self.speed = 2
        self.frame = random.randint(0,7)
        self.ai_image = load_image('image/ai_ani2.png')
        self.goto = 0 # 0 업 1 다운
        self.state = 0 # 0 왼쪽 1 오른쪽 2 위 3 아래
        self.idle = 0 # 0 이동중 1 왼쪽  2 오른쪽
        self.ai_attack = [] #ai 공격
        self.ai = [(self.x,self.y)] #ai 좌표
        self.ai_attack_image = load_image('image/ai_attack.png')

    def enter(self):
        global player
        player = Player()

    def draw(self, px):
        if self.x > px:
            self.ai_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        else:
            self.ai_image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

        for ai_attack in self.ai_attack:
            self.ai_attack_image.draw(ai_attack[0], ai_attack[1])

    def update(self, px, py):
        self.frame = (self.frame + 1) % 8

        pointX, pointY = px - self.x, py - self.y
        list = math.sqrt(pointX ** 2 + pointY ** 2)

        # self.x -= (self.x - px) / 20
        # self.y -= (self.y - py) / 20

        self.x += self.speed * pointX / list
        self.y += self.speed * pointY / list


def enter():
    global player,tutorial,bullets,ingame,ai
    player = Player()
    ingame = Ingame()
    ai = Ai()
    bullets = []

def draw():
    global player,tutorial,bullets,ingame,ai
    clear_canvas()
    ingame.draw()
    ai.draw(player.x)
    player.draw()

    for loc in player.attack:
        player.attack_image.draw(loc[0], loc[1])

    for member in bullets:
        member.draw()
    update_canvas()

def handle_events():
    global running
    global player, ai,tx,ty
    global attack
    global bullets

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(tutorial_state)

        #tx, ty = event.x, 600 - 1 - event.y
           # ai += [(tx, ty)]

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

def update():
    global player,bullets, ai

    player.update()
    ai.update(player.x,player.y)


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
    close_canvas()

if __name__ == '__main__':
    main()