# The Feather ESP32 Reverse TFT has super confusing buttons:
# D0 has to be pulled high and read in reverse but D1 and D2 are the opposite.
# This makes that easier to handle.

import board
import digitalio


buttons = []


def initialize():
    buttons.append(digitalio.DigitalInOut(board.D0))
    buttons.append(digitalio.DigitalInOut(board.D1))
    buttons.append(digitalio.DigitalInOut(board.D2))
    buttons[0].switch_to_input(pull=digitalio.Pull.UP)
    buttons[1].switch_to_input(pull=digitalio.Pull.DOWN)
    buttons[2].switch_to_input(pull=digitalio.Pull.DOWN)

def read_buttons():
    return [ not buttons[0].value, buttons[1].value, buttons[2].value ]


