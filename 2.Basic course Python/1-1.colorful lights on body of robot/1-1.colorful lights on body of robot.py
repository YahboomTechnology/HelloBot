from microbit import *
import neopixel

np = neopixel.NeoPixel(pin16, 4)  # RGB light connects to micro:bit's P16 pin
while True:
    for pixel_id in range(0, len(np)):
        np[0] = (255, 0, 0)
        np.show()  # Show
        sleep(200)
