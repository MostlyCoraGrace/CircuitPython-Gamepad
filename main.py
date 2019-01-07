import digitalio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from board import SCL, SDA
from busio import I2C
from adafruit_mcp230xx import MCP23017

mcp1 = MCP23017(I2C(SCL, SDA), address=0x20)  # I can add up to 8 of these if I remember correctly, each for 16 keys each.  I could matrix them to get more, but that adds more delay and I'm running in to a speed issue as-is
kbd = Keyboard()  # This is the virtual keyboard device
kbd_keys = []  # This is the array of all the virtual keys that the hardware keys will 'press' to the operating system
toggles = []  # An array to check whether the state of the switch has changed each tick to avoid pressing a key many times unintentionally
kbd_switches = []  # the array of physical switch connections

for i in range(16):  # Do the hardware setup so the Feather knows what to do
    kbd_switches.append(mcp1.get_pin(i))
for switch in kbd_switches:
    switch.direction = digitalio.Direction.INPUT
    switch.pull = digitalio.Pull.UP
    toggles.append(False)  # each key starts in the state of being 'un-pressed'

def definemacro(index):  # I'm not really using this yet, but hopefully one day I'll be able to store many different keymaps and swap them out at will
    macros = ["macro1.py", "macro2.py", "macro3.py"]  # each keymap is stored in a different file to make it readable and extensible
    which_macro = index
    macro = macros[which_macro]
    file = open(macro, "r")
    macro_keys = []
    for line in file:  # Each switch stores the buttons it will press in its own line, and each switch can press multiple keys at a time
        macro_keys.append(eval(line))
    return macro_keys
        
kbd_keys = definemacro(0)

print("Waiting for Keypresses")

while True:
    buttons = []
    for i in range(16):
        buttons.append(bool(mcp1.gpio & 1 << i))  # each MCP23017 can output the state of all the GPIO keys at once, and this will make an array containing a bool for the state of each key.  MUCH faster than checking each key individually because I2C is relatively slow.
    for button in buttons:
        index = buttons.index(button)
        if not button:  # was a key pressed?
            if not toggles[index]:  # Was the key previously un-pressed?  Only continue if the key's state has *changed*
                toggles[index] = True  # Change that key's state,
                print("Key pressed")
                kbd.press(*kbd_keys[index])  # Press the key
        else:  # Yeah no shit, Sherlock; if the key is not pressed, it must be released!
            if toggles[index]:  # Was the key previously pressed?  Only continue if the key's state has *changed*
                toggles[index] = False  # Change that key's state,
                print("key released")
                kbd.release(*kbd_keys[index])  # Release the key