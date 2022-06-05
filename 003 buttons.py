from microbit import *

while True:
    display.clear()
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.HEART)
