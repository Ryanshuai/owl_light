"""
NeoPixel example for Pico. Displays a rainbow on the NeoPixels.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import time
import board
import neopixel
import digitalio

from rainbow import angle_to_rgb

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 8
pixels_0 = neopixel.NeoPixel(board.GP0, num_pixels, auto_write=False)
pixels_0.brightness = 0.5
pixels_1 = neopixel.NeoPixel(board.GP1, num_pixels, auto_write=False)
pixels_1.brightness = 0.5
pixels_2 = neopixel.NeoPixel(board.GP2, num_pixels, auto_write=False)
pixels_2.brightness = 0.5

button1 = digitalio.DigitalInOut(board.GP6)
button1.switch_to_input(pull=digitalio.Pull.UP)

button2 = digitalio.DigitalInOut(board.GP7)
button2.switch_to_input(pull=digitalio.Pull.UP)

# pixels_0.fill((255, 0, 0))
# while True:
#     for i in range(-255, 255):
#         pixels_0.brightness = abs(i) / 255
#         pixels_0.show()
#         time.sleep(0.01)


state = 0
while True:
    state %= 4
    if state == 0:
        for i in range(360):
            pixels_0.fill(angle_to_rgb(i / 360))
            pixels_0.show()
            pixels_1.fill(angle_to_rgb((i) / 360))
            pixels_1.show()
            pixels_2.fill(angle_to_rgb((i) / 360))
            pixels_2.show()
            time.sleep(0.0001)
            if button1.value == 0:
                state += 1
                break
            if button2.value == 0:
                state -= 1
                break


    if state == 1:
        pixels_0.fill((255, 0, 0))
        pixels_1.fill((255, 0, 0))
        pixels_2.fill((255, 0, 0))
        for i in range(-255, 255):
            pixels_0.brightness = abs(i) / 255
            pixels_0.show()
            pixels_1.brightness = abs(i) / 255
            pixels_1.show()
            pixels_2.brightness = abs(i) / 255
            pixels_2.show()
            time.sleep(0.1)

            if button1.value == 0:
                state += 1
                break
            if button2.value == 0:
                state -= 1
                break

    elif state == 2:
        pixels_0.fill((255, 0, 0))
        pixels_1.fill((0, 255, 0))
        pixels_2.fill((0, 0, 255))

        for i in range(-255, 255):
            pixels_0.brightness = abs(i) / 255
            pixels_0.show()
            pixels_1.brightness = abs(i) / 255
            pixels_1.show()
            pixels_2.brightness = abs(i) / 255
            pixels_2.show()
            time.sleep(0.01)

            if button1.value == 0:
                state += 1
                break
            if button2.value == 0:
                state -= 1
                break


    elif state == 3:
        pass

# while True:
#     for i in range(-1000, 1000):
#         pixels_0.brightness = abs(i) / 2550
#         pixels_0.show()
#         pixels_1.brightness = abs(i) / 2550
#         pixels_1.show()
#         pixels_2.brightness = abs(i) / 2550
#         pixels_2.show()
#         time.sleep(0.001)
