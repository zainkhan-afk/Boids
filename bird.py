from vector import Vector
import random
import config as cfg

class Bird:
	def __init__(self, color = (255, 0, 0)):
		self.pos = Vector(x = random.randint(0, cfg.CANVAS_W), y = random.randint(0, cfg.CANVAS_H))
		self.vel = Vector(x = 0, y = 0)
		self.heading = random.random()
		self.color = color


	def update(self, vel):
		self.vel += vel
		self.vel = self.vel.clamp(cfg.MIN_VEL, cfg.MAX_VEL)


		self.pos += self.vel * cfg.DELTA_T