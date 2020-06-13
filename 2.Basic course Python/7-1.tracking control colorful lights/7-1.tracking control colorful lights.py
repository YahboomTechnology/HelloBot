from microbit import *
import neopixel
import microbit
microbit.display.off()

np = neopixel.NeoPixel(pin2, 4)
while True:
    if pin0.read_digital() == 1 and pin1.read_digital() == 1:
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np.show()
    elif pin0.read_digital() == 1 and pin1.read_digital() == 0:
        np[1] = (255, 0, 0)
        np[2] = (0, 255, 0)
        np.show()
    elif pin0.read_digital() == 0 and pin1.read_digital() == 1:
        np[1] = (0, 255, 0)
        np[2] = (255, 0, 0)
        np.show()
    elif pin0.read_digital() == 0 and pin1.read_digital() == 0:
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np.show()