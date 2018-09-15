from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0
x_center = 400
y_center = 300
radianAngle = 10
radius = 200

while (True):
    radianAngle += 0.1
    X = x_center + math.cos(radianAngle) * radius
    Y = y_center + math.sin(radianAngle) * radius

    clear_canvas()
    grass.draw_now(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, X, Y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

close_canvas()