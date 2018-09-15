from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 400
y = 90
frame = 0

while (True):
    clear_canvas()
    grass.draw_now(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x = x + 2
    delay(0.01)
    get_events()

close_canvas()