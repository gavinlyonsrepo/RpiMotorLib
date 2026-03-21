#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : BYJMotor
Tested : MX1508 controller bipolar stepper motor

Pinout used:
    IN1 - GPIO 20
    IN2 - GPIO 21
    IN3 - GPIO 19
    IN4 - GPIO 26
    GPIO_PINS order passed to motor_run: [IN3, IN1, IN4, IN2]

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Declare a named instance of class
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")

# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=mymotortest.motor_stop, verbose=True)

# GPIO pins
GPIO_PINS = [19, 20, 26, 21]


def main():
    # pylint: disable=too-many-statements
    """main function loop tests for motor MX1508 StepTest"""
    estop.enable()

    time.sleep(1)
    input("Press <Enter> to continue Test 1")

    # Test 1 — 360 turn full step
    mymotortest.motor_run(GPIO_PINS, wait=0.5, steps=50, ccwise=False,
                          verbose=True, steptype="full", initdelay=1)
    time.sleep(1)
    input("Press <Enter> to continue Test 2")

    # Test 2 — 180 turn full step
    mymotortest.motor_run(GPIO_PINS, wait=0.1, steps=25, ccwise=False,
                          verbose=True, steptype="full", initdelay=1)
    time.sleep(1)
    input("Press <Enter> to continue Test 3")

    # Test 3 — 180 turn half step
    mymotortest.motor_run(GPIO_PINS, wait=0.2, steps=25, ccwise=False,
                          verbose=True, steptype="half", initdelay=1)
    input("Press <Enter> to continue Test 4")

    # Test 4 — 360 turn half step counter clockwise
    mymotortest.motor_run(GPIO_PINS, wait=0.05, steps=50, ccwise=True,
                          verbose=True, steptype="half", initdelay=1)
    input("Press <Enter> to continue Test 5")

    # Test 5 — 180 turn wave drive
    mymotortest.motor_run(GPIO_PINS, wait=0.02, steps=25, ccwise=False,
                          verbose=True, steptype="wave", initdelay=5)
    input("Press <Enter> to continue Test 6")

    # Test 6 — 72 turn wave drive counter clockwise
    mymotortest.motor_run(GPIO_PINS, wait=0.02, steps=10, ccwise=True,
                          verbose=True, steptype="wave", initdelay=1)

    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("START")
    main()
    sys.exit()

# ===================== END ===============================
