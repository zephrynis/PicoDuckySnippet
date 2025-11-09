import usb_hid
import json
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import board
from digitalio import DigitalInOut, Direction, Pull

def validatejson(data):
    if not isinstance(data, dict):
        return False, "Snippets must be an object, see github repo for details"
    if len(data) == 0:
        return False, "Snippets object cannot be empty"
    for morse_code, item in data.items():
        if not isinstance(morse_code, str) or not isinstance(item, str):
            return False, "Both morse code and text must be strings"
        if not all(c in '.-' for c in morse_code):
            return False, f"Invalid morse code: {morse_code}"
        
    return True, "Valid"

snippets = {}

try:
    with open('snippets.json') as f:
        snippets = json.load(f)
        is_valid, message = validatejson(snippets)
        if not is_valid:
            snippets = {".": f"Invalid json: {message}"}
except Exception as e:
    snippets = {".": "Error loading snippets: " + str(e)}

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
button = DigitalInOut(board.GP12)
button.direction = Direction.INPUT
button.pull = Pull.UP

morse_buffer = ""
last_release_time = 0
press_start = 0

while True:
    current_time = time.monotonic()

    if morse_buffer and last_release_time > 0 and (current_time - last_release_time) > 1.0:
        print("buffer:", morse_buffer)
        if morse_buffer in snippets:
            snippet = snippets[morse_buffer]
            time.sleep(0.3)
            layout.write(snippet)
        else:
            unknown_msg = f"[Unknown code: {morse_buffer}]"
            layout.write(unknown_msg)
            time.sleep(1)
            for _ in unknown_msg:
                kbd.press(Keycode.BACKSPACE)
                kbd.release_all()
        morse_buffer = ""
        last_release_time = 0
            


    if morse_buffer and last_release_time > 0 and (current_time - last_release_time) > 3.0:
        morse_buffer = ""
        last_release_time = 0
    
    if not button.value:
        if press_start == 0:
            press_start = current_time
    
    else:
        if press_start > 0:
            press_duration = current_time - press_start
            if press_duration < 0.3:
                morse_buffer += "."
                print("Dot")
            else:
                morse_buffer += "-"
                print("Dash")
            last_release_time = current_time
            press_start = 0
    time.sleep(0.01)