import numpy as np

def unit_step(v):
	""" Heavyside Step function. v must be a scalar"""
	if v >= 0:
		return 1
	else:
		return 0
	
def perceptron(x, w, b):
	""" Function implemented by a perceptron with 
		weight vector w and bias b """
	v = np.dot(w, x) + b
	y = unit_step(v)
	return y
	