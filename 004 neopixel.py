from microbit import *
import neopixel
from random import randint
np = neopixel.NeoPixel(pin0, 30)

while True:
    red = randint(0, 60)
    green = randint(0, 60)
    blue = randint(0, 60)
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (red, green, blue)
        np.show()
    sleep(100)
