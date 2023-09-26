# Example by RoboticX
####################
# Required Packages to be installed

# pip install pyserial
# pip install pynput
####################
# Run this Python script on your computer while Arduino is connected to USB.
####################
"""
Direction abbreviations:::

"U": Up Key,
"D": Down Key,
"L": Left Key,
"R": Right Key
"""

import serial
from pynput.keyboard import Key, Controller

keyboard = Controller()

encoding = 'utf-8'
port = "COM3"  # check out your port
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

if not s.isOpen():
    s.open()


def take_action(result):
    key_map = {"U": Key.up, "D": Key.down, "L": Key.left, "R": Key.right}
    if result in key_map:
        key = key_map.get(result)
        keyboard.press(key)
        print(f"{key} is pressed")
        keyboard.release(key)


def get_arduino_msg():
    while True:
        i = s.read()
        msg = i.decode(encoding)
        print("msg from Arduino:::", msg)

        take_action(msg)


if __name__ == "__main__":
    get_arduino_msg()
