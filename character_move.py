from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0
y = 90
frame = 0
while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5

    if (x == 770):
        x = 770
        y+=5

    if (x == 770 and y >= 570):
        y = 570
        x -= 5

    if (x == 0 and y==570):
        y -=5

    delay(0.05)
    get_events()

close_canvas()