import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel
from random import randint
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from time import monotonic

Columns = [DigitalInOut(x) for x in (board.A2, board.A3, board.A4, board.A5, board.D2, board.D3, board.D4, board.D7)]
Rows = [DigitalInOut(x) for x in (board.D9, board.D10, board.D11, board.D12, board.D13)]

num_pixels = len(Columns) * len(Rows)
pixels = neopixel.NeoPixel(board.D5, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.RGB)

def setupmatrix():
	for Each in Rows:
		Each.direction = Direction.OUTPUT
		Each.value = 1  # 1 = dont register a press, 0 = register a press
	
	for Each in Columns:
		Each.direction = Direction.INPUT
		Each.pull = Pull.UP

def setuptoggles():
	rowlength = len(Columns)
	columnlength = len(Rows)
	l = rowlength * columnlength
	return [0 for i in range(l)]

def definemacro(which_macro):  # store many different keymaps and swap them out at will
	macros = ["macro1.py", "macro2.py", "macro3.py"]  # each keymap is stored in a different file
	file = open(macros[which_macro], "r")
	macro_keys = []
	for line in file:  # Each switch stores the buttons it will press in its own line, and each switch can press multiple keys at a time
		macro_keys.append(eval(line))
	return macro_keys

kbd = Keyboard()
queuepress = []
queuerelease = []
pressedkeys = []
KeyIndex = 0
Timer = 0
CurrentTime = 0

setupmatrix()
Toggles = setuptoggles()
Keys = definemacro(0)

print("Waiting for keypresses...")

while True:
	CycleTime = monotonic()  # Stores the current time before any of the looping.  This will be compared with later to tell me how long the cycle takes
	KeyIndex = 0  # Stores the index of the current key that is being cycled through
	for EachRow in Rows:  # Go through key-by-key and if one is pressed, add its corresponding key code to the queue
		RowIndex = Rows.index(EachRow)
		if RowIndex == 0:  # if we have cycled back to the start, then we need to set the last Row's value
			Rows[len(Rows)-1].value = 1
		else:  # Else just set the previous Row's value
			Rows[RowIndex - 1].value = 1
		EachRow.value = 0
		for EachColumn in Columns:
			ColumnIndex = Columns.index(EachColumn)
			if not EachColumn.value:
				if not Toggles[KeyIndex]:
					Toggles[KeyIndex] = 1
					print(str(Keys[KeyIndex][0]) + " added to queuepress")
					queuepress.append(Keys[KeyIndex])
					#for EachKeypress in KeyboardPress[0]:
						#queuepress.append(EachKeypress)
					pixels.fill((randint(0, 256), randint(0, 256), randint(0, 256)))
					pixels.show()
				# else:
					# key is held
			else:
				if Toggles[KeyIndex]:
					Toggles[KeyIndex] = 0
					print(str(Keys[KeyIndex][0]) + " added to queuerelease")
					queuerelease.append(Keys[KeyIndex])
					#for EachKeyrelease in KeyboardRelease[0]:
						#queuerelease.append(EachKeyrelease)
				# else:
					# Key is free
			KeyIndex += 1  # Finished processing the switch
	
	for release in queuerelease:
		kbd.release(*release[1])  # Release the key on the computer!
		print("Released " + release[0])
		for each in pressedkeys:  # remove keys from the pressed keys list when they are released
			if each == release[0]:
				pressedkeys.remove(release[0])
	if len(queuepress) > 0:  # are we trying to press a key?
		if len(pressedkeys) < 6:  # if we're already pressing 6 keys, don't even bother
			if len(queuepress) > 6:  # Always make sure we can only ever press 6 keys at a time
				print("Can't press that many keys at once!")
				queuepress = queuepress[:6]
			if len(pressedkeys) < 5:  # can we add more keys to be pressed?
				print("Number of keys currently pressed: " + str(len(pressedkeys)))
				maxcanpress = 6 - len(pressedkeys)  # only press more keys to reach the 6-key limit, dont go over it
				queuepress = queuepress[:maxcanpress]  # set the queue of keys to press to be equal to the first (6 keys minus the number of keys already pressed)
				for i in range(len(queuepress)):  # for each queued keypress, press all the keys within it
					for each in queuepress[i][1]:
						kbd.press(each)  # Press the key on the computer!
					print("Pressed " + queuepress[i][0])
					pressedkeys.append(queuepress[i][0])  # Add the keys to the list of pressed keys, to keep track of how many have been pressed
			else:
				print("Can't press any more keys!")
		else:
			print("Trying to press too many keys at once!")
	queuepress = []  # make sure to clear the queues at the end so it can be queued up for the next pass
	queuerelease = []
	
	if monotonic() - Timer >= 5:  # create a log to tell me how long it takes to cycle through the array without spamming the serial console
		print("Cycling through all the keys took " + str(monotonic() - CycleTime))
		Timer = monotonic()	