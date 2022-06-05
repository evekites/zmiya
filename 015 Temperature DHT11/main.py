import microbit as uBit
from dht11 import *

sensor = DHT11(uBit.pin0)
while True:
    try:
        t, h = sensor.read()
        print("%2.1f%sC  %2.1f%% " % (t, DEGREES, h))
    except DataError as e:
        print("Error : " + str(e))
    time.sleep(2)
