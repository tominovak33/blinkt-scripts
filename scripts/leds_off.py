from blinkt import set_pixel, show

for led in range(0,8):
	set_pixel(led, 0, 0, 0, 0)
	show()
