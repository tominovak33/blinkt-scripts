from blinkt import set_pixel, show
import random
import time

while True:
	for led in range(0,8):
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		a = random.randint(0,1)
		set_pixel(led, r, g, b, a)
	show()
	time.sleep(0.1)
