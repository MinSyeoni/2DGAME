from pico2d import *
from term import game_framework
from term import title_state
from term import game_state
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
        self.speed = 2
        self.frame = random.randint(0,7)
        self.goto = 0 # 0 업 1 다운
        self.player_image = load_image('image/run_stand_ani.png')
        self.state = 0 # 0 왼쪽 1 오른쪽 2 위 3 아래
        self.idle = 0 # 0 이동중 1 왼쪽  2 오른쪽
        self.attack = [] # 총알 공격
        self.attack_image = load_image('image/attack.png')

    def draw(self):
        for attack_image in self.attack:
            self.attack_image.draw(attack[0], attack[1])

        if self.state == 0 or (self.idle == 1 and self.goto != 2):
            self.player_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.state == 1 or (self.idle == 2 and self.goto != 2) :
            self.player_image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        elif self.idle == 1:
            self.player_image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        elif self.idle == 2:
            self.player_image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.player_image.clip_draw(self.frame*100, self.state * 100, 100, 100, self.x, self.y)

    def update(self):
        events = get_events()
        self.frame = (self.frame + 1) % 8

        if len(self.attack) > 0:
            (tx,ty) = self.attack[0]
            attackX, attackY = tx - self.x, ty - self.y
            list = math.sqrt(attackX ** 2 + attackY ** 2)
            if list > 0:
                self.x += self.speed * attackX / list
                self.y += self.speed * attackY / list
                if attackX < 0 and self.x < tx: self.x = tx
                if attackX > 0 and self.x > tx: self.x = tx
                if attackY < 0 and self.y < tx: self.y = ty
                if attackY > 0 and self.y > tx: self.y = ty
            if(self.x, self.y) == (tx,ty):
                del self.attack[0]

    def handel_events(self):
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    for attack_image in attack:
                        tx, ty = event.x, 600 - 1- event.y
                        attack_image.attack += [(tx, ty)]
                else:
                    for attack_image in attack:
                        attack_image.attack = []

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

    if 650 < player.x < 700 and 300 < player.y <350:
        game_framework.change_state(game_state)

def handle_events():
    global running
    global player
    global attack

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

def exit():
    close_canvas()

if __name__ == '__main__':
    main()