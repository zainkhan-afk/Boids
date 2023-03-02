import numpy as np
import config as cfg
from vector import Vector
import random
import numpy as np

class Solver:
	def __init__(self):
		self.horizontal = Vector(x = 1, y = 0)
		self.vertical   = Vector(x = 0, y = 1)

	def avoid_corners(self, bird):
		turn_vel = Vector(x = 0, y = 0)
		if bird.pos.x>cfg.CANVAS_W - cfg.BORDER_MARGIN:
			dist = abs(cfg.CANVAS_W - cfg.BORDER_MARGIN - bird.pos.x)
			turn_vel += (self.horizontal*-1*dist)

		elif bird.pos.x<cfg.BORDER_MARGIN:
			dist = abs(cfg.BORDER_MARGIN- bird.pos.x)
			turn_vel += (self.horizontal*dist)


		if bird.pos.y>cfg.CANVAS_H - cfg.BORDER_MARGIN:
			dist = abs(cfg.CANVAS_H - cfg.BORDER_MARGIN - bird.pos.y)
			turn_vel += (self.vertical*-1*dist)

		elif bird.pos.y<cfg.BORDER_MARGIN:
			dist = abs(cfg.BORDER_MARGIN - bird.pos.y)
			turn_vel += (self.vertical*dist)

		return turn_vel

	def solve(self, birds):
		for bird1 in birds:
			bird_close = False

			vel = Vector(x = 0, y = 0)
			dist_in_protected_range = Vector(x = 0, y = 0)
			alignment_vel = Vector(x = 0, y = 0)
			avg_bird_pos = Vector(x = 0, y = 0)
			
			n_neighboring_boids = 0
			for bird2 in birds:
				if bird1 == bird2:
					continue

				direction = bird1.pos - bird2.pos

				if direction.magnitude<cfg.VISUAL_RANGE:
					# Separation
					if direction.magnitude<cfg.PROTECTED_RADIUS:
						dist_in_protected_range += direction

					# Alignment
					else:
						alignment_vel += bird2.vel
						avg_bird_pos += bird2.pos
						n_neighboring_boids += 1

			if n_neighboring_boids>0:
				alignment_vel = alignment_vel * (1/n_neighboring_boids)
				alignment_vel = alignment_vel - bird1.vel


				avg_bird_pos = avg_bird_pos * (1/n_neighboring_boids)
				avg_bird_pos = avg_bird_pos - bird1.pos

			turn_vel = self.avoid_corners(bird1)
			vel += dist_in_protected_range*cfg.AVOID_FACTOR
			vel += alignment_vel*cfg.ALIGNMENT_FACTOR
			vel += avg_bird_pos*cfg.CENTERING_FACTOR
			vel += turn_vel*cfg.TURN_FACTOR

			bird1.update(vel)