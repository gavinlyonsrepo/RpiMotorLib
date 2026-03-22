#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : rpi_dc_lib.py
Class  : TranDc
Tested : DC motor controlled via a transistor

To disable emergency stop, comment out the EstopEmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import time
import sys
from RpiMotorLib import rpi_dc_lib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Initialize motor (pin, freq, verbose)
my_motor_one = rpi_dc_lib.TranDc(27, 50, True)

# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=my_motor_one.motor_stop, verbose=True)


def motorone():
    """Run a DC motor transistor integration test."""
    print("TEST: testing motor 1")

    estop.enable()

    input("Press enter key to speed up")
    step_delay = .05
    my_motor_one.stop_motor = False
    for speed in range(0, 100):
        if my_motor_one.stop_motor:
            break
        my_motor_one.dc_motor_run(speed, step_delay)
    time.sleep(5)

    input("Press enter key to speed down")
    my_motor_one.stop_motor = False
    for speed in range(100, 0, -1):
        my_motor_one.dc_motor_run(speed, step_delay)
        if my_motor_one.stop_motor:
            break

    my_motor_one.dc_clean_up()
    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("START")
    print("motorone tests")
    motorone()
    sys.exit()

# ===================== END ===============================
