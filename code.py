import usb_hid
import json
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import board
from digitalio import DigitalInOut, Direction, Pull

snippets = []
with open('snippets.json') as f:
    snippets = json.load(f)

iteration = 0

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
button = DigitalInOut(board.GP12)
button.direction = Direction.INPUT
button.pull = Pull.UP

while True:
    if not button.value:
        if iteration != 0:
            snippet = snippets[(iteration - 1) % len(snippets)]
            for _ in snippet:
                kbd.press(Keycode.BACKSPACE)
                kbd.release_all()
        snippet = snippets[iteration % len(snippets)]
        layout.write(snippet)
        iteration += 1
    time.sleep(0.1)