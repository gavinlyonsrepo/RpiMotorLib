#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : rpi_dc_lib.py
Class  : TB6612FNGDc
Tested : DC motor via TB6612FNG motor controller

Pinout used:
    PWA    - GPIO 13
    AI1    - GPIO 22
    AI2    - GPIO 27
    PWB    - GPIO 18
    BI1    - GPIO 23
    BI2    - GPIO 24
    STANDBY - GPIO 25

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import rpi_dc_lib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Pin definitions
PWA = 13
AI1 = 22
AI2 = 27
PWB = 18
BI1 = 23
BI2 = 24
STANDBY = 25
FREQ = 50

# Motor instances at module level so estop can reference them
motor_one = rpi_dc_lib.TB6612FNGDc(AI1, AI2, PWA, FREQ, True, "motor_one")
motor_two = rpi_dc_lib.TB6612FNGDc(BI1, BI2, PWB, FREQ, True, "motor_two")


def stop_all():
    """Stop both motors — used as emergency stop callable."""
    motor_one.motor_stop()
    motor_two.motor_stop()


# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=stop_all, verbose=True)


def motorone():
    """Set of tests to run on DC motor connected to A channel."""
    print("TEST: testing motor 1")
    try:
        print("1. motor forward")
        motor_one.stop_motor = False
        motor_one.forward(15)
        input("press key to stop")
        motor_one.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("2. motor forward speed up")
        motor_one.stop_motor = False
        for i in range(15, 30):
            if motor_one.stop_motor:
                break
            motor_one.forward(i)
            time.sleep(1)
        motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("3. motor backward")
        motor_one.stop_motor = False
        motor_one.backward(15)
        input("press key to stop")
        motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("4. motor backward speed up")
        motor_one.stop_motor = False
        for i in range(15, 30):
            if motor_one.stop_motor:
                break
            motor_one.backward(i)
            time.sleep(1)
        motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("5. brake check")
        motor_one.stop_motor = False
        motor_one.forward(50)
        time.sleep(3)
        motor_one.brake(0)
        print("motor brake\n")

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        print("Unexpected error:")


def motortwo():
    """Set of tests to run on DC motor connected to B channel."""
    print("TEST: testing motor 2")
    try:
        print("1. motor forward")
        motor_two.stop_motor = False
        motor_two.forward(15)
        input("press key to stop")
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("2. motor forward speed up")
        motor_two.stop_motor = False
        for i in range(15, 30):
            if motor_two.stop_motor:
                break
            motor_two.forward(i)
            time.sleep(1)
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("3. motor backward")
        motor_two.stop_motor = False
        motor_two.backward(15)
        input("press key to stop")
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("4. motor backward speed up")
        motor_two.stop_motor = False
        for i in range(15, 30):
            if motor_two.stop_motor:
                break
            motor_two.backward(i)
            time.sleep(1)
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("5. brake check")
        motor_two.stop_motor = False
        motor_two.forward(50)
        time.sleep(3)
        motor_two.brake(0)
        print("motor brake\n")

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        print("Unexpected error:")


def motorboth():
    """Set of tests to run on both motors simultaneously."""
    print("TEST: testing both motors")
    try:
        print("Both motors forward")
        motor_one.stop_motor = False
        motor_two.stop_motor = False
        motor_one.forward(25)
        motor_two.forward(25)
        input("press key to stop")
        motor_one.stop(0)
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        print("Unexpected error:")
    finally:
        motor_one.cleanup(False)
        motor_two.cleanup(False)


# ===================== MAIN ===============================

if __name__ == '__main__':
    try:
        print("START")
        estop.enable()
        motor_one.standby(STANDBY, True)   # enable controller via STBY pin
        motorone()
        time.sleep(3)
        motortwo()
        time.sleep(3)
        motorboth()
        time.sleep(1)
        estop.cleanup()
    finally:
        motor_one.standby(STANDBY, False)  # disable controller via STBY pin

    sys.exit()

# ===================== END ===============================
