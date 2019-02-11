import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel
from random import randint
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

num_pixels = 1
pixels = neopixel.NeoPixel(board.D5, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.RGB)

Columns = [DigitalInOut(x) for x in (board.A2, board.A3, board.A4, board.A5, board.D2, board.D3, board.D4, board.D7)]
Rows = [DigitalInOut(x) for x in (board.D9, board.D10, board.D11, board.D12, board.D13)]

for Each in Rows:
	Each.direction = Direction.OUTPUT
	Each.value = 1  # 1 = dont register a press, 0 = register a press

for Each in Columns:
	Each.direction = Direction.INPUT
	Each.pull = Pull.UP

def setuptoggles():
	r = len(Columns)
	c = len(Rows)
	l = r * c
	t = [0 for i in range(l)]
	return t

Toggles = setuptoggles()

kbd = Keyboard()
queuepress = []
queuerelease = []
	
def definemacro(index):  # store many different keymaps and swap them out at will
	macros = ["macro1.py", "macro2.py", "macro3.py"]  # each keymap is stored in a different file
	which_macro = index
	macro = macros[which_macro]
	file = open(macro, "r")
	macro_keys = []
	for line in file:  # Each switch stores the buttons it will press in its own line, and each switch can press multiple keys at a time
		macro_keys.append(eval(line))
	return macro_keys
		
Keys = definemacro(0)

while True:
	KeyIndex = 0
	for EachRow in Rows:
		RowIndex = Rows.index(EachRow)
		if RowIndex == 0:
			Rows[len(Rows)-1].value = 1
		else:
			Rows[RowIndex - 1].value = 1
		EachRow.value = 0
		for EachColumn in Columns:
			ColumnIndex = Columns.index(EachColumn)
			if not EachColumn.value:
				if not Toggles[KeyIndex]:
					Toggles[KeyIndex] = 1
					KeyboardPress = Keys[KeyIndex]
					print(str(KeyboardPress[1]) + " pressed")
					queuepress.append(*KeyboardPress[0])
					pixels.fill((randint(0, 256), randint(0, 256), randint(0, 256)))
					pixels.show()
				# else:
					# key is held
			else:
				if Toggles[KeyIndex]:
					Toggles[KeyIndex] = 0
					KeyboardRelease = Keys[KeyIndex]
					print(str(KeyboardRelease[1]) + " released")
					queuerelease.append(*KeyboardRelease[0])
				# else:
					# Key is free
			KeyIndex += 1  # Finished processing the switch
	
	# ToDo!  Can only press 6 keys at a time, if i press more than that, it throws an error!  Currently, there's no protection against this.
	