import math

def polygon_area(ns, ls):
	length = ls ** 2
	t = math.pi/ns
	tr = math.tan(t)
	return ns * length / tr / 4

print polygon_area(7, 3)