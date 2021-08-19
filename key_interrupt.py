import board
import digitalio

switch1 = digitalio.DigitalInOut(board.GP6)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(board.GP7)
switch2.switch_to_input(pull=digitalio.Pull.UP)
