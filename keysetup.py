from board import SCL, SDA
from busio import I2C
from adafruit_mcp230xx import MCP23017

i2c = I2C(SCL, SDA)
mcp1 = MCP23017(i2c, address=0x20)  # I can add up to 8 of these if I remember correctly, each for 16 keys each.  I could matrix them to get more, but that adds more delay and I'm running in to a speed issue as-is

kbd_switches = [
    mcp1.get_pin(8),
    mcp1.get_pin(9),
    mcp1.get_pin(10),
    mcp1.get_pin(11)
    ]