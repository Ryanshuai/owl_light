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
pixels_1 = neopixel.NeoPixel(board.GP1, num_pixels, auto_write=False)
pixels_2 = neopixel.NeoPixel(board.GP2, num_pixels, auto_write=False)

pixels_0.brightness = 0.5
pixels_1.brightness = 0.5
pixels_2.brightness = 0.5

button1 = digitalio.DigitalInOut(board.GP6)
button1.switch_to_input(pull=digitalio.Pull.UP)

button2 = digitalio.DigitalInOut(board.GP7)
button2.switch_to_input(pull=digitalio.Pull.UP)

state = 1
while True:
    state = min(max(state, 0), 5)
    print("state:", state)

    if state == 0:
        for i in range(360):
            pixels_0.fill(angle_to_rgb(i / 360))
            pixels_1.fill(angle_to_rgb(i / 360))
            pixels_2.fill(angle_to_rgb(i / 360))
            pixels_0.show()
            pixels_1.show()
            pixels_2.show()
            time.sleep(0.0001)
            if button1.value == 0:
                state += 1
                break
            if button2.value == 0:
                state -= 1
                break

    elif state == 1:
        pixels_0.fill((255, 100, 5))
        pixels_1.fill((255, 100, 5))
        pixels_2.fill((255, 100, 5))
        for i in range(-255, 255):
            pixels_0.brightness = abs(i) / 255 / 2
            pixels_1.brightness = abs(i) / 255 / 2
            pixels_2.brightness = abs(i) / 255 / 2
            pixels_0.show()
            pixels_1.show()
            pixels_2.show()
            time.sleep(0.01)

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
            pixels_1.brightness = abs(i) / 255
            pixels_2.brightness = abs(i) / 255
            pixels_0.show()
            pixels_1.show()
            pixels_2.show()
            time.sleep(0.001)

            if button1.value == 0:
                state += 1
                break
            if button2.value == 0:
                state -= 1
                break

    elif state == 3:
        for i in range(360):
            pixels_0.fill(angle_to_rgb(i / 360))
            pixels_1.fill(angle_to_rgb((i + 120) / 360))
            pixels_2.fill(angle_to_rgb((i + 240) / 360))
            pixels_0.show()
            pixels_1.show()
            pixels_2.show()
            time.sleep(0.0001)
            if button1.value == 0:
                state += 1
                break
            if button2.value == 0:
                state -= 1
                break

    elif state == 4:
        while True:
            for i in range(9):
                pixels_0.fill(angle_to_rgb(i / 9))
                pixels_1.fill(angle_to_rgb((i + 3) / 9))
                pixels_2.fill(angle_to_rgb((i + 6) / 9))
                pixels_0.show()
                pixels_1.show()
                pixels_2.show()
                time.sleep(0.1)
                if button1.value == 0:
                    state += 1
                    break
                if button2.value == 0:
                    state -= 1
                    break
            if button1.value == 0 or button2.value == 0:
                break

    elif state == 5:
        pixels_0.brightness = 0
        pixels_1.brightness = 0
        pixels_2.brightness = 0
        pixels_0.show()
        pixels_1.show()
        pixels_2.show()
        if button2.value == 0:
            state -= 1

    time.sleep(0.3)
