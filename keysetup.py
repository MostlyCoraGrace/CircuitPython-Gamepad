from board import A1, A2, SCL, SDA
from busio import I2C
from adafruit_mcp230xx import MCP23017
from analogio import AnalogIn

i2c = I2C(SCL, SDA)

mcp1 = MCP23017(i2c, address=0x20)


kbd_pins = [
    mcp1.get_pin(8),
    mcp1.get_pin(9),
    mcp1.get_pin(10),
    mcp1.get_pin(11)
    ]