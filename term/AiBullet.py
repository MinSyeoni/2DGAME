from pico2d import *
import game_framework
import game_world

class Missile:
	image = None
	RUN_SPEED_PPS = 200

	def __init__(self,x,y,dx,dy,size):
		self.x, self.y = x, y
		self.dx, self.dy = dx, dy
		self.size = size
		self.time = 0
		if (Missile.image == None):
			Missile.image = load_image('image/ai_attack.png')

	def draw(self):
		self.image.draw(self.x, self.y, self.size, self.size)

	def update(self):
		self.time += game_framework.frame_time
		if game_world.isPaused():
			return
		self.x += Missile.RUN_SPEED_PPS * game_framework.frame_time * self.dx
		self.y += Missile.RUN_SPEED_PPS * game_framework.frame_time * self.dy
		if self.x < -self.size or self.y < -self.size or \
			self.x > get_canvas_width() + self.size or self.y > get_canvas_height() + self.size:
			game_world.remove_object(self)

	def isInField(self, width, height):
		if (self.x < 0): return False
		if (self.y < 0): return False
		if (self.x > width): return False
		if (self.y > height): return False
		return True
