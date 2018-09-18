from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 800, 600

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x,y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
speed = 1

while running:
    clear_canvas()
    grass.draw(KPU_WIDTH // 2, KPU_HEIGHT // 20)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()