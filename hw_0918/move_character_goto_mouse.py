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
x,y = KPU_WIDTH, KPU_HEIGHT
tx,ty=x,y
frame = 0
speed = 5

while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    handle_events()
    update_canvas()
    if x > tx:
        x -= speed
        if x < tx:
            x = tx
    elif x < tx:
        x += speed
        if x > tx:
            x = tx
    if y > ty:
        y -= speed
        if y < ty:
            x = tx
    elif y < ty:
        y += speed
        if y > ty:
            y = ty

    delay(0.05)
    handle_events()

close_canvas()