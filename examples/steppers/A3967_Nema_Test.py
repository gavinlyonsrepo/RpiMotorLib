#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : A3967EasyNema
Tested : A3967 Easy Driver Nema stepper motor

Steps per revolution:
    Full = 200
    Half = 400
    1/4  = 800
    1/8  = 1600

Pinout used:
    DIRECTION - GPIO 26
    STEP      - GPIO 19
    MS1       - GPIO 6
    MS2       - GPIO 13

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# GPIO pins
DIRECTION = 26       # Direction -> GPIO pin
STEP = 19            # Step -> GPIO pin
GPIO_PINS = (6, 13)  # Microstep Resolution MS1-MS2, set to (-1,-1) to disable

# Declare a named instance of motor class
mymotortest = RpiMotorLib.A3967EasyNema(DIRECTION, STEP, GPIO_PINS)

# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=mymotortest.motor_stop, verbose=True)


def main():
    """Tests for motor A3967 NEMA."""
    estop.enable()

    # === Section A ===
    print("TEST SECTION A")
    # motor_move(stepdelay, steps, clockwise, verbose, steptype, initdelay)
    input("TEST: Press <Enter> for Test 1, full mode, full turn")
    mymotortest.motor_move(.005, 200, False, True, "Full", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test 2, half mode, full turn")
    mymotortest.motor_move(.005, 400, False, True, "Half", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test 3, 1/4 mode, full turn")
    mymotortest.motor_move(.008, 800, False, True, "1/4", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test 4, 1/8 mode, full turn")
    mymotortest.motor_move(.006, 1600, False, True, "1/8", .05)
    time.sleep(1)

    # === Section B ===
    print("TEST SECTION B")
    input("TEST: Press <Enter> for Test 5, full mode, init delay")
    mymotortest.motor_move(.005, 100, False, True, "Full", 5)
    time.sleep(1)
    input("TEST: Press <Enter> for Test 6, full mode, direction turn")
    mymotortest.motor_move(.005, 100, True, True, "Full", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test 7, full mode, no verbose")
    mymotortest.motor_move(.005, 100, False, False, "Full", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test 8, full mode, slow small turn")
    mymotortest.motor_move(1, 3, False, True, "Full", .05)
    time.sleep(1)

    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("TEST START")
    main()
    print("TEST END")
    sys.exit()

# ===================== END ===============================
