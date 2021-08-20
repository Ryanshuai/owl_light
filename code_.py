"""
NeoPixel example for Pico. Turns the NeoPixels red.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import time
import board
import neopixel
from _pixelbuf import colorwheel


# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 8

pixels_1 = neopixel.NeoPixel(board.GP0, num_pixels)
pixels_1.brightness = 0.5

pixels_2 = neopixel.NeoPixel(board.GP1, num_pixels, auto_write=False)
pixels_2.brightness = 0.5

def rainbow(speed):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels_2[i] = colorwheel(pixel_index & 255)
        pixels_2.show()
        time.sleep(speed)

while True:
    pixels_1.fill((255, 0, 0))
    rainbow(0)

