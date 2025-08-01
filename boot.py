class Pixel:
    def __init__(self, pin):
        import neopixel
        import machine
        self.pin = machine.Pin(pin)
        self.np = neopixel.NeoPixel(self.pin, 1)

    def set(self, r, g, b):
        self.np[0] = (r, b, b)
        self.np.write()

from time import sleep

pixel = Pixel(16)

pixel.set(255, 0, 0)
sleep(0.1)
pixel.set(0, 0, 0)
sleep(0.1)
