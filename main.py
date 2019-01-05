import digitalio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

from keysetup import kbd_switches  # imports all the hardware switch locations from the PCB

kbd = Keyboard()  # This is the virtual keyboard device
kbd_keys = []  # This is the array of all the virtual keys that the hardware keys will 'press' to the operating system
toggles = []  # An array to check whether the state of the switch has changed each tick to avoid pressing a key many times unintentionally
queue_press = []  # I'm looping through and adding all the changed key states and sending them in bulk after they've been checked
queue_release = []	# And these two queue arrays are those key state changes

def definemacro(index):	 # I'm not really using this yet, but hopefully one day I'll be able to store many different keymaps and swap them out at will
	macros = ["macro1.py", "macro2.py", "macro3.py"]  # each keymap is stored in a different file to make it readable and extensible
	which_macro = index
	macro = macros[which_macro]
	file = open(macro, "r")
	macro_keys = []
	for line in file:  # Each switch stores the buttons it will press in its own line, and each switch can press multiple keys at a time
		macro_keys.append(eval(line))
	return macro_keys
		
kbd_keys = definemacro(0)

for switch in kbd_switches:	 # Do the hardware setup so the Feather knows what to do
	switch.direction = digitalio.Direction.INPUT
	switch.pull = digitalio.Pull.UP
	toggles.append(False)  # each key starts in the state of being 'un-pressed'

print("Waiting for Keypresses")

while True:
	for key in kbd_switches:
		key_index = kbd_switches.index(key)
		
		if not key.value:  # was a key pressed?
			if not toggles[key_index]:  # Was the key previously un-pressed?  Only continue if the key's state has *changed*
				toggles[key_index] = True  # Change that key's state,
				queue_press.append(kbd_keys[key_index])	 # and add the keypresses to the queue to be pressed
		else:  # Yeah no shit, Sherlock; if the key is not pressed, it must be released!
			if toggles[key_index]:  # Was the key previously pressed?  Only continue if the key's state has *changed*
				toggles[key_index] = False  # Change that key's state,
				queue_release.append(kbd_keys[key_index])  # and add the keypresses to the queue to be released

	for release in queue_release:  # release first to *try* and avoid that 6-keypress limit that keyboards have.
		kbd.release(*release)					
	for press in queue_press:
		kbd.press(*press)

	
	queue_press = []  # clear the arrays and start again
	queue_release = []