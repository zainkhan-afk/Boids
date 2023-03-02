import numpy as np

def get_transformed_pts(angle, pts, bird):
	R = np.array([
					[np.cos(angle), -np.sin(angle), bird.pos.x],
					[np.sin(angle),  np.cos(angle), bird.pos.y]
				])
	pts = np.append(pts, np.ones((3, 1)), axis = 1)
	new_pts = (R@pts.T).astype("int")
	return new_pts.T