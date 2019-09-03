from microbit import *
import neopixel

display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin6, 1)
for pixel_id in range(0, len(np)):
    np[0] = (255, 0, 0)
    np.show()
np = neopixel.NeoPixel(pin9, 1)
for pixel_id in range(0, len(np)):
    np[0] = (255, 0, 0)
    np.show()
