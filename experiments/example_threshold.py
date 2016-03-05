#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_line import BrickletLine

HOST = "localhost"
PORT = 4223
UID = "mRW"  # Change to your UID
count = 0


def cb_reflectivity_reached(reflectivity):
    # Callback function for reflectivity reached callback
    global count
    count += 1


if __name__ == "__main__":
    ipcon = IPConnection()  # Create IP connection
    l = BrickletLine(UID, ipcon)  # Create device object

    ipcon.connect(HOST, PORT)  # Connect to brickd
    l.set_debounce_period(1)

    # Register reflectivity reached callback to function cb_reflectivity_reached
    l.register_callback(l.CALLBACK_REFLECTIVITY_REACHED, cb_reflectivity_reached)

    # Configure threshold for reflectivity "greater than 2000"
    l.set_reflectivity_callback_threshold(">", 2000, 0)

    input("Press key to exit\n")  # Use input() in Python 3
    ipcon.disconnect()
    print(count/4)
