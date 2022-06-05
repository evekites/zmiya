from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    print(gesture)