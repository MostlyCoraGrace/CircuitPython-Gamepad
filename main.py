import digitalio

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

from keysetup import kbd_pins

kbd = Keyboard()
kbd_keys = []
toggles = []
queuepress = []
queuerelease = []
prev = []

macros = ["macro1.py", "macro2.py", "macro3.py"]
which_macro = 0
macro = macros[which_macro]

for pin in kbd_pins:
	pin.direction = digitalio.Direction.INPUT
	pin.pull = digitalio.Pull.UP
	toggles.append(False)

file = open(macro, "r")
for line in file:
	kbd_keys.append(eval(line))

print("Waiting for Keypresses")

while True:
	for key in kbd_pins:
		key_index = kbd_pins.index(key)
		
		if not key.value:  # pressed?
			if not toggles[key_index]:
				toggles[key_index] = True
				key_press = kbd_keys[key_index]
				for press in key_press:
					queuepress.append(press)
		else:
			if toggles[key_index]:
				toggles[key_index] = False
				key_release = kbd_keys[key_index]
				for release in key_release:
					queuerelease.append(release)

	queuepress = queuepress[:5]
	for release in queuerelease:
		kbd.release(release)					
	for press in queuepress:
		kbd.press(press)

	
	queuepress = []
	queuerelease = []