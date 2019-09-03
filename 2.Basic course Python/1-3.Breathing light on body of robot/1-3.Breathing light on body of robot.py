from microbit import *
import neopixel

np = neopixel.NeoPixel(pin16, 4)
while True:
    for num in range(0, 255):
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (num, 0, num)
            np.show()
            sleep(10)
