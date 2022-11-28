# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import time
import busio
import board
import microcontroller
import terminalio
from digitalio import DigitalInOut, Direction
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20



# one-wire bus for DS18B20
ow_bus = OneWireBus(board.GP5)

# scan for temp sensor
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

#  function to convert celcius to fahrenheit
def c_to_f(temp):
    temp_f = (temp * 9/5) + 32
    return temp_f


#  temp_test = str(ds18.temperature)
#  unit = "C"
temp_test = str(c_to_f(ds18.temperature))


startTime = time.monotonic() 
mesTime = startTime

#logFile = open("log.dat", "w")

dt  = 5

while True:
    try:
        currentTime = time.monotonic()
        if (mesTime + dt) >= currentTime:
            mesTime = currentTime
            T = ds18.temperature
            runTime = mesTime - startTime
            print(runTime, T)
            with open("log.dat", "a") as logFile:
                logFile.write(f'{runTime},{T}')
            

    except Exception:
        continue
