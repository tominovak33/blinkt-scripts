from blinkt import set_pixel, show
import random
import time

r = 0
g = 0
b = 0

while True:
    for led in range(0,8):
            set_pixel(led, 255, 255, 255, 0.1)
            show()
            time.sleep(1)

            set_pixel(led, 255, 0, 0, 0.1)
            show()
            time.sleep(1)

            set_pixel(led, 0, 255, 0, 0.1)
            show()
            time.sleep(1)

            set_pixel(led, 0, 0, 255, 0.1)
            show()
            time.sleep(1)

            set_pixel(led, 0, 0, 0, 0.1)
            show()
            time.sleep(0.5)
