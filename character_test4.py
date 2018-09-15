Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from pico2d import *
Pico2d is prepared.
>>> open_canvas()
>>> character = load_image('character.png')
cannot load character.png
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    character = load_image('character.png')
  File "C:\Users\민수연\AppData\Local\Programs\Python\Python37\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> os.chdir('C:/Users/민수연/Desktop/수업/2d게임프로그래밍/GIT/2DGAME/2DGAME')
>>> character = load_image('character.png')
>>> character.draw(100,100)
>>> character.draw(200,200)
>>> update_canvas()
>>> 
 RESTART: C:/Users/민수연/Desktop/수업/2d게임프로그래밍/GIT/2DGAME/2DGAME/character_test3.py 
Pico2d is prepared.
>>> 
 RESTART: C:/Users/민수연/Desktop/수업/2d게임프로그래밍/GIT/2DGAME/2DGAME/character_test3.py 
Pico2d is prepared.
>>> 
 RESTART: C:/Users/민수연/Desktop/수업/2d게임프로그래밍/GIT/2DGAME/2DGAME/character_test3.py 
Pico2d is prepared.
>>> 
 RESTART: C:/Users/민수연/Desktop/수업/2d게임프로그래밍/GIT/2DGAME/2DGAME/character_test3.py 
Pico2d is prepared.
>>> 
