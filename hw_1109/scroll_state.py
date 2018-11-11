from pico2d import *
import game_framework
from Player import Player
import game_world
from bg import InfiniteBackground as Background

def handle_events():
    global player
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        else:
            player.handle_event(e)

def enter():
    global player

    player = Player()
    bg = Background()

    player.bg = bg
    bg.target = player

    game_world.add_object(bg, game_world.layer_bg)
    game_world.add_object(player, game_world.layer_player)

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def update():
    game_world.update()
    delay(0.03)

def exit():
    game_world.clear()

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()