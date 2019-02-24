"""

Wood Elf
By J.H.Grace

A CircuitPython-based keyboard matrix

"""

import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel
from random import randint
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from time import monotonic, sleep
			
kbd = Keyboard()  # This is the virtual keyboard device.  Currently, CircuitPython only supports a single virtual keyboard.  The hope is one day this may change, and I'll be able to have full n-key rollover.  For now though, only 6-key rollover is supported.
QueuePress = []  # Each cycle, all pressed keys with simple keypresses are added to this queue and processed afterwards.
QueueRelease = []  # Ditto as above, but for keys that were pressed and are now released.
PressedKeys = []  # This stores all keys that are currently pressed to the virtual keyboard.
KeyIndex = 0  # Stores the index of the current key that is being cycled through.
Timer = 0  # For debug purposes.

Columns = [DigitalInOut(x) for x in (board.A2, board.A3, board.A4, board.A5, board.D2, board.D3, board.D4, board.D7)]
Rows = [DigitalInOut(x) for x in (board.D9, board.D10, board.D11, board.D12, board.D13)]

num_pixels = len(Columns) * len(Rows)  # Assumes a perfect and full array of keys.
pixels = neopixel.NeoPixel(board.D5, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.RGB)

def setupmatrix():  # By turning rows on and off and listening for changes in voltage down the columns, its possible to have far more keys than you have GPIO ports
	for Each in Rows:  # The rows act as the GND end.  Setting them to 0 makes them available for pulling a key down.  Setting them to 1 stops the key from pulling the voltage down.
		Each.direction = Direction.OUTPUT
		Each.value = 1  # 1 = Don't register a press, 0 = register a press.
	
	for Each in Columns:  # The columns act as the inputs, listening for voltage changes.
		Each.direction = Direction.INPUT
		Each.pull = Pull.UP

def setuptoggles(item):  # By storing the state of each key, we can avoid pressing the same key over and over again unintentionally.
	rowlength = len(Columns)
	columnlength = len(Rows)
	Setup = []
	for each in range(rowlength * columnlength):
		Setup.append(item)  # Each key starts in the state of un-pressed.
	return Setup

def definemacro(which_macro):  # Store many different keymaps and swap them out at will.
	macros = ["macro1.py", "macro2.py", "macro3.py"]  # each keymap is stored in a different file.
	file = open(macros[which_macro], "r")
	macro_keys = []  # The syntax for the macro array is like so:
	"""
	["name of key", 
	is it a macro(1), or a regular keypress(0), 
	[[to press(1) or release(0) the key, how long to press or release it for in seconds, the key to press or release], ]
	does it loop while held(1) or not(0)]
	"""
	for line in file:  # Each switch stores the buttons it will press in its own line, and each switch can press multiple keys at a time.
		macro_keys.append(eval(line))
	return macro_keys

def nkeyro(key):  # n = 6 until multiple keyboard() objects are supported.
	result = False
	if len(PressedKeys) < 6:  # Can we press another key?
		kbd.press(key)  # Press the key.
		result = True
	else:  # We can't press any more keys.
		print("Can't press any more keys!")
	return result
	
def queuepress(queue):
	if len(queue) > 0:  # Are we trying to press a key?
		for eachmacro in queue:
			if not eachmacro[1] :  # Do a normal KeyPress.
				for eachkey in eachmacro[2]:  # for each key inside the macro for that switch, try to press it.
					if nkeyro(eachkey):  # Try to press the key
						print("Pressed [" + eachmacro[0] + ", " + str(eachmacro[2].index(eachkey)) + "].")
						PressedKeys.append([eachmacro[0], eachkey])
					else:
						print("Can't press " + eachmacro[0] + ".")
			#else:  # Run the macro.
				
		
		"""
		if len(PressedKeys) < 6:  # If we're already pressing 6 keys, don't even bother.
			if len(queue) > 6:  # Always make sure we can only ever press 6 keys at a time
				print("Can't press that many keys at once!").
				queue = queue[:6]
			
			if len(PressedKeys) < 5:  # Can we add more keys to be pressed?
				print("Number of keys currently pressed: " + str(len(PressedKeys)))
				maxcanpress = 6 - len(PressedKeys)  # Only press more keys to reach the 6-key limit, dont go over it.
				queue = queue[:maxcanpress]  # Set the queue of keys to press to be equal to the first (6 keys minus the number of keys already pressed).
				
				for i in range(len(queue)):  # For each queued keypress, press all the keys within it.
					
					for each in queue[i][2]:
						kbd.press(each)  # Press the key on the computer!
					
					print("Pressed " + queue[i][0])
					PressedKeys.append(queue[i][0])  # Add the keys to the list of pressed keys, to keep track of how many have been pressed.
			else:
				print("Can't press any more keys!")
		else:
			print("Trying to press too many keys at once!")
		"""
	
	

def queuerelease(queue):
	if len(queue) > 0:  # Are we trying to release a key?
		for release in queue:
			if not release[1] :  # Do a normal key release.
				for eachkey in release[2]:
					kbd.release(eachkey)  # Release the key on the computer!
					print("Released [" + release[0] + ", " + str(release[2].index(eachkey)) + "]")
					for each in PressedKeys:  # remove keys from the pressed keys list when they are released
						if each[0] == release[0]:
							PressedKeys.remove(each)
							print("Removed [" + release[0] + ", " + str(release[2].index(eachkey)) + "] from the list of pressed keys.")

# Go through all the steps to set up the matrix and virtual keys etc.
setupmatrix()
Toggles = setuptoggles(0)  # Store whether a key is pressed or not pressed.
Keys = definemacro(0)

print("Waiting for keypresses...")

while True:
	CycleTime = monotonic()  # Stores the current time before any of the looping.  This will be compared with later to tell me how long the cycle takes
	KeyIndex = 0  # Reset the index of the current key that is being cycled through.
	
	for EachRow in Rows:  # Go through key-by-key and if one is pressed, add its corresponding key code to the queue.
		RowIndex = Rows.index(EachRow)
		if RowIndex == 0:  # if we have cycled back to the start, then we need to set the last Row's value
			Rows[len(Rows)-1].value = 1
		else:  # Else just set the previous Row's value
			Rows[RowIndex - 1].value = 1
		EachRow.value = 0
		
		for EachColumn in Columns:
			ColumnIndex = Columns.index(EachColumn)
			
			if not EachColumn.value:  # Is a key pressed?
				if not Toggles[KeyIndex]:  # Has it been pressed before?
					Toggles[KeyIndex] = 1  # Store the state of the key as being pressed currently.
					print(str(Keys[KeyIndex][0]) + " added to QueuePress.")
					QueuePress.append(Keys[KeyIndex])
					pixels.fill((randint(0, 256), randint(0, 256), randint(0, 256)))
					pixels.show()
				# else:
					# key is held
			else:
				if Toggles[KeyIndex]:
					Toggles[KeyIndex] = 0
					print(str(Keys[KeyIndex][0]) + " added to QueueRelease.")
					QueueRelease.append(Keys[KeyIndex])
					
				# else:
					# Key is free
			KeyIndex += 1  # Finished processing the switch
	
	# Press and release the keys in the queue.
	queuerelease(QueueRelease)	
	queuepress(QueuePress)
	# Make sure to clear the queues at the end so it can be queued up for the next pass.
	QueuePress = []
	QueueRelease = []
	
	if monotonic() - Timer >= 5:  # create a log to tell me how long it takes to cycle through the array without spamming the serial console.
		print("Cycling through all the keys took " + str(monotonic() - CycleTime) + "seconds.")
		Timer = monotonic()	