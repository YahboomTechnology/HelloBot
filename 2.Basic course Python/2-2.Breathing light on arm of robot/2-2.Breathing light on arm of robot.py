from microbit import *
import neopixel
import microbit
microbit.display.off()

display.show(Image.HAPPY)
np1 = neopixel.NeoPixel(pin6, 1)
np2 = neopixel.NeoPixel(pin9, 1)

while True:
    for num in range(0, 255):
        for pixel_id in range(0, len(np1)):
            np1[pixel_id] = (num, 0, num)
            np1.show()
            sleep(10)
        for pixel_id in range(0, len(np2)):
            np2[pixel_id] = (num, 0, num)
            np2.show()
            sleep(10)