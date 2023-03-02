from bird import Bird
from renderer import Renderer
from solver import Solver
import config as cfg

birds = [Bird() for i in range(cfg.NUM_BIRDS)]
renderer = Renderer()
solver = Solver()

while True:
	solver.solve(birds)
	renderer.clear()
	renderer.draw(birds)
	
	k = renderer.render()
	
	if k == ord("q"):
		break