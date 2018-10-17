from pico2d import *
from hw_0928 import game_framework
from hw_0928 import title_state
import random
from enum import Enum

BOYS_COUNT = 1000

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None

    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(90,550)
        self.speed = random.uniform(1.0,3.0)
        self.frame = random.randint(0,7)
        self.point = []
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('../image/animation_sheet.png')
        self.goal = load_image('../image/goal.png')
        self.run_frames = 0
        print(self.image)

    def draw(self):
        for goal in self.point:
            self.goal.draw(goal[0],goal[1])
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

        if len(self.point) > 0:
            (tx,ty) = self.point[0]
            pointX, pointY = tx - self.x, ty - self.y
            list = math.sqrt(pointX ** 2 + pointY ** 2)
            if list > 0:
                self.x += self.speed * pointX / list
                self.y += self.speed * pointY / list
                if pointX < 0 and self.x < tx: self.x = tx
                if pointX > 0 and self.x > tx: self.x = tx
                if pointY < 0 and self.y < tx: self.y = ty
                if pointY > 0 and self.y > tx: self.y = ty
            if(tx,ty) == (self.x,self.y):
                del self.point[0]

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }
def create_team():
    team_data_text = '  \
                     { "Tiffany" : {"StartState":"LEFT_RUN", "x":100, "y":100},     \
                            "Yuna"    : {"StartState":"RIGHT_RUN", "x":200, "y":200},  \
                            "Sunny"   : {"StartState":"LEFT_STAND", "x":300, "y":300},   \
                            "Yuri"    : {"StartState":"RIGHT_STAND", "x":400, "y":400},  \
                            "Jessica" : {"StartState":"LEFT_RUN", "x":500, "y":500}      \
                     }  '
    player_state_table = {
        "LEFT_RUN": Boy.LEFT_RUN,
        "RIGHT_RUN": Boy.RIGHT_RUN,
        "LEFT_STAND": Boy.LEFT_STAND,
        "RIGHT_STAND": Boy.RIGHT_STAND
    }
    team_data = json.loads(team_data_text)

    team = []
    for name in team_data:
        player = Boy()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_table[team_data[name]['StartState']]
        team.append(player)
    return team

    #team_data = json.loads(team_data_text)
    team_data_file = open('team_data.txt', 'r')
    team_data = json.load(team_data_file)
    team_data_file.close()


def handle_events():
    global running
    global point
    global boys
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                for b in boys:
                    tx, ty = event.x, 600 - 1- event.y
                    b.point += [(tx, ty)]
            else:
               for b in boys:
                   b.point = []



def update(self):
    self.frame = (self.frame + 1) % 8
    self.handle_state[self.state](self)

def enter():
    global boys, grass

    boys = []
    fh = open('boys_data.json')
    data = json.load(fh)
    for e in data['boys']:
        b = Boy()
        b.name = e['name']
        b.x = e['x']
        b.y = e['y']
        b.speed = e['speed']
        boys.append(b)

    grass = Grass()

def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw()
    update_canvas()

def update():
    global boys
    for b in boys:
        b.update()
    delay(0.01)

def exit():
    close_canvas()

if __name__ == '__main__':
    main()