#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : BYJMotor
Tested : 28BYJ-48 unipolar stepper motor with ULN2003 controller

Pinout used:
    IN1 - GPIO 18
    IN2 - GPIO 23
    IN3 - GPIO 24
    IN4 - GPIO 25

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Declare a named instance of class
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=mymotortest.motor_stop, verbose=True)

# GPIO pins connected to IN1, IN2, IN3, IN4 on motor PCB
GPIO_PINS = [18, 23, 24, 25]


def main():
    """main function loop"""
    # Arguments for motor_run:
    # (GPIOPins, stepdelay, steps, counterclockwise, verbose, steptype, initdelay)

    estop.enable()

    time.sleep(0.1)
    input("Press <Enter> to continue Test 1")
    mymotortest.motor_run(GPIO_PINS, .05, 128, True, True, "full", .05)
    time.sleep(1)

    input("Press <Enter> to continue Test 2")
    mymotortest.motor_run(GPIO_PINS, .001, 256, False, True, "half", .05)
    time.sleep(1)

    input("Press <Enter> to continue Test 3")
    mymotortest.motor_run(GPIO_PINS, .01, 5, False, True, "half", 2)
    time.sleep(1)

    input("Press <Enter> to continue Test 4")
    mymotortest.motor_run(GPIO_PINS, .05, 50, True, True, "wave", .05)
    time.sleep(1)

    input("Press <Enter> to continue Test 5")
    mymotortest.motor_run(GPIO_PINS, .01, 512, False, True, "half", .05)

    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("START")
    main()
    sys.exit()

# ===================== END ===============================
