from microbit import *
from ultrasonic import *

rf = Rangefinder(pin0)

display.show(Image.YES)

while True:
    dist = rf.distance_cm()
    print(int(dist))
    sleep(50)
