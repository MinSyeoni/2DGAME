from pico2d import *
os.chdir('C:/Users/민수연/Desktop/수업/2d게임프로그래밍/GIT/2DGAME/2DGAME')
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x = 0
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)
    
close_canvas()
