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

state = 7


def button_func(button1_value, button2_value, frozen=False):
    global state
    if button1_value == 0 and button2_value == 0:
        pass
        return True
    if button1_value == 0 or button2_value == 0:
        if not frozen:
            state += button1.value - button2.value
        return True
    return False


while True:
    state = min(max(state, -1), 8)
    print("state:", state)

    if state == 0:
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

            if button_func(button1.value, button2.value):
                break

    elif state == 1:
        for i in range(360):
            pixels_0.fill(angle_to_rgb(i / 360))
            pixels_1.fill(angle_to_rgb(i / 360))
            pixels_2.fill(angle_to_rgb(i / 360))
            pixels_0.show()
            pixels_1.show()
            pixels_2.show()
            time.sleep(0.0001)
            if button_func(button1.value, button2.value):
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

            if button_func(button1.value, button2.value):
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
            if button_func(button1.value, button2.value):
                break

    elif state == 4:
        while True:
            for i in range(360):
                for j in range(num_pixels):
                    pixels_0[j] = angle_to_rgb((i + 10 * j) / 360)
                    pixels_1[j] = angle_to_rgb((i + 10 * j + 120) / 360)
                    pixels_2[j] = angle_to_rgb((i + 10 * j + 240) / 360)
                    pixels_0.show()
                    pixels_1.show()
                    pixels_2.show()
                    time.sleep(0.0001)
                    if button_func(button1.value, button2.value):
                        break
                if button_func(button1.value, button2.value, True):
                    break
            if button_func(button1.value, button2.value, True):
                break

    elif state == 5:
        while True:
            for i in range(360):
                for j in range(num_pixels):
                    pixels_0[j] = angle_to_rgb((i + 10 * j) / 360)
                    pixels_1[j] = angle_to_rgb((i + 10 * j) / 360)
                    pixels_2[j] = angle_to_rgb((i + 10 * j) / 360)
                    pixels_0.show()
                    pixels_1.show()
                    pixels_2.show()
                    time.sleep(0.0001)
                    if button_func(button1.value, button2.value):
                        break
                if button_func(button1.value, button2.value, True):
                    break
            if button_func(button1.value, button2.value, True):
                break

    elif state == 6:
        while True:
            for i in range(9):
                pixels_0.fill(angle_to_rgb(i / 9))
                pixels_1.fill(angle_to_rgb((i + 3) / 9))
                pixels_2.fill(angle_to_rgb((i + 6) / 9))

                pixels_0.show()
                pixels_1.show()
                pixels_2.show()
                time.sleep(0.1)
                if button_func(button1.value, button2.value):
                    break
            if button_func(button1.value, button2.value, True):
                break

    elif state == 7:
        for i in range(0, 512 * 10):
            pixels_0.brightness = abs((i % 512) - 255) / 255
            pixels_1.brightness = abs((i % 512) - 255) / 255
            pixels_2.brightness = abs((i % 512) - 255) / 255
            pixels_0.fill(angle_to_rgb(i / 1280))
            pixels_1.fill(angle_to_rgb(i / 1280))
            pixels_2.fill(angle_to_rgb(i / 1280))

            pixels_0.show()
            pixels_1.show()
            pixels_2.show()
            time.sleep(0.01)

            if button_func(button1.value, button2.value):
                break

    elif state == 8 or state == -1:
        pixels_0.brightness = 0
        pixels_1.brightness = 0
        pixels_2.brightness = 0
        pixels_0.show()
        pixels_1.show()
        pixels_2.show()
        button_func(button1.value, button2.value)

    time.sleep(0.3)
