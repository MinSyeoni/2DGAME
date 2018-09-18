from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 20
y = 90
frame = 0
x_center = 400
y_center = 300
radianAngle = 0
radius = 200

while (True):
    while (x < 800 - 20):
        clear_canvas()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x + 2
        delay(0.01)
    while (y < 600 - 40):
        clear_canvas()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y = y + 2
        delay(0.01)
    while (x > 0 + 20):
        clear_canvas()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - 2
        delay(0.01)
    while (y > 0 + 90):
        clear_canvas()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y = y - 2
        delay(0.01)

    x=400
    y=300

    while (x==400 and y==300):
        while (radianAngle <= 6.28):
            radianAngle += 0.1

            X = x_center + math.cos(radianAngle) * radius
            Y = y_center + math.sin(radianAngle) * radius

            clear_canvas()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, X, Y)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
        delay(0.01)
        get_events()
        x = 20
        y = 90
        radianAngle=0
    get_events()
get_events()
close_canvas()