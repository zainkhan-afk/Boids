import cv2
import numpy as np
import config as cfg
from utils import *

class Renderer:
	def __init__(self):
		self.canvas = np.zeros((cfg.CANVAS_H, cfg.CANVAS_W, 3)).astype("uint8")
		self.draw_pts = np.array([
								[0, 9],
								[-3, 0],
								[3, 0]
								])


	def draw(self, birds):
		for bird in birds:
			x = int(bird.pos.x)
			y = int(bird.pos.y)

			angle = bird.vel.angle - np.pi/2

			new_pts = get_transformed_pts(angle, self.draw_pts, bird)

			for i in range(len(new_pts)-1):
				pt1 = new_pts[i]
				pt2 = new_pts[i+1]
				cv2.line(self.canvas, pt1, pt2, bird.color, 1)

			pt1 = new_pts[0]
			pt2 = new_pts[-1]
			cv2.line(self.canvas, pt1, pt2, bird.color, 1)

			# cv2.circle(self.canvas, (x, y), 5, bird.color, -1)
			# cv2.circle(self.canvas, (x, y), 5, (255, 255, 255), 1)
			# cv2.circle(self.canvas, (x, y), cfg.BIRD_MIN_RADIUS, (255, 0, 0), 1)

	def render(self):
		cv2.imshow("canvas", self.canvas)
		return cv2.waitKey(30)

	def clear(self):
		self.canvas = np.zeros((cfg.CANVAS_H, cfg.CANVAS_W, 3)).astype("uint8")