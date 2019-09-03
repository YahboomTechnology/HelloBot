from microbit import *
import neopixel
import random

display.show(Image.HAPPY)
nq = neopixel.NeoPixel(pin6, 1)
np = neopixel.NeoPixel(pin9, 1)
number = [0, 255]

while True:
    if pin7.read_digital() == 0:
        nq[0] = (random.choice(number),
                 random.choice(number), random.choice(number))
        nq.show()
    if pin10.read_digital() == 0:
        np[0] = (random.choice(number),
                 random.choice(number), random.choice(number))
        np.show()
    sleep(500)
