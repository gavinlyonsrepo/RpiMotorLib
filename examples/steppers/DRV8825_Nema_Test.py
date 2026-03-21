#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : A4988Nema
Tested : DRV8825 Nema stepper motor

Steps per revolution:
    Full = 200
    Half = 400
    1/4  = 800
    1/8  = 1600
    1/16 = 3200
    1/32 = 6400

Pinout used:
    DIRECTION - GPIO 20
    STEP      - GPIO 21
    M0        - GPIO 13
    M1        - GPIO 19
    M2        - GPIO 26
    Note: pass (-1,-1,-1) for mode pins to hardwire MS resolution and save GPIO pins.

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# GPIO pins
GPIO_PINS = (13, 19, 26)  # Microstep Resolution M0-M1-M2
DIRECTION = 20             # Direction -> GPIO pin
STEP = 21                  # Step -> GPIO pin

# Declare a named instance of class
# (direction_pin, step_pin, mode_pins, motor_type)
mymotortest = RpiMotorLib.A4988Nema(DIRECTION, STEP, GPIO_PINS, "DRV8825")

# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=mymotortest.motor_stop, verbose=True)


def main():
    # pylint: disable=too-many-statements
    """main function loop"""
    estop.enable()

    # === Section A ===
    print("TEST SECTION A")
    # motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)
    input("TEST: Press <Enter> to continue Full 180 turn Test 1")
    mymotortest.motor_go(False, "Full", 100, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue Full 180 clockwise Test 2")
    mymotortest.motor_go(True, "Full", 100, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue Full 180 no verbose Test 3")
    mymotortest.motor_go(False, "Full", 100, .005, False, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue timedelay Test 4")
    mymotortest.motor_go(True, "Full", 10, 1, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue Full initdelay Test 5")
    mymotortest.motor_go(True, "Full", 90, .01, True, 10)
    time.sleep(1)

    # === Section B ===
    print("TEST SECTION B")
    input("TEST: Press <Enter> to continue Half Test 6")
    mymotortest.motor_go(False, "Half", 400, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/4 Test 7")
    mymotortest.motor_go(False, "1/4", 800, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/8 Test 8")
    mymotortest.motor_go(False, "1/8", 1600, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/16 Test 9")
    mymotortest.motor_go(False, "1/16", 3200, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/32 Test 10")
    mymotortest.motor_go(False, "1/32", 6400, .005, True, .05)
    time.sleep(1)

    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("TEST START")
    main()
    print("TEST END")
    sys.exit()

# ===================== END ===============================
