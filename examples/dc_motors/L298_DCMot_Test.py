#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : rpi_dc_lib.py
Class  : L298NMDc
Tested : DC motor via L298N motor controller

Pinout used:
    ena - GPIO 26
    in1 - GPIO 19
    in2 - GPIO 13
    in3 - GPIO 21
    in4 - GPIO 20
    enB - GPIO 16

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import rpi_dc_lib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Motor instances at module level so estop can reference them
my_motor_one = rpi_dc_lib.L298NMDc(19, 13, 26, 50, True, "motor_one")
my_motor_two = rpi_dc_lib.L298NMDc(21, 20, 16, 50, True, "motor_two")


def stop_all():
    """Stop both motors — used as emergency stop callable."""
    my_motor_one.motor_stop()
    my_motor_two.motor_stop()


# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=stop_all, verbose=True)


def motorone():
    """TEST: testing motor 1"""
    print("TEST: testing motor 1")
    try:
        print("1. motor forward")
        my_motor_one.stop_motor = False
        my_motor_one.forward(15)
        input("press enter key to stop")
        my_motor_one.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("2. motor forward speed up")
        my_motor_one.stop_motor = False
        for i in range(15, 30):
            if my_motor_one.stop_motor:
                break
            my_motor_one.forward(i)
            time.sleep(1)
        my_motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("3. motor backward")
        my_motor_one.stop_motor = False
        my_motor_one.backward(15)
        input("press enter key to stop")
        my_motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("4. motor backward speed up")
        my_motor_one.stop_motor = False
        for i in range(15, 30):
            if my_motor_one.stop_motor:
                break
            my_motor_one.backward(i)
            time.sleep(1)
        my_motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("5. brake check")
        my_motor_one.stop_motor = False
        my_motor_one.forward(50)
        time.sleep(3)
        my_motor_one.brake(0)
        print("motor brake\n")

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        print("Unexpected error:")
    finally:
        my_motor_one.cleanup(False)


def motortwo():
    """TEST: testing motor 2"""
    print("TEST: testing motor 2")
    try:
        print("1. motor forward")
        my_motor_two.stop_motor = False
        my_motor_two.forward(15)
        input("press enter key to stop")
        my_motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("2. motor forward speed up")
        my_motor_two.stop_motor = False
        for i in range(15, 30):
            if my_motor_two.stop_motor:
                break
            my_motor_two.forward(i)
            time.sleep(1)
        my_motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("3. motor backward")
        my_motor_two.stop_motor = False
        my_motor_two.backward(15)
        input("press enter key to stop")
        my_motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("4. motor backward speed up")
        my_motor_two.stop_motor = False
        for i in range(15, 30):
            if my_motor_two.stop_motor:
                break
            my_motor_two.backward(i)
            time.sleep(1)
        my_motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("5. brake check")
        my_motor_two.stop_motor = False
        my_motor_two.forward(50)
        time.sleep(3)
        my_motor_two.brake(0)
        print("motor brake\n")

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        print("Unexpected error:")
    finally:
        my_motor_two.cleanup(False)


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("START")
    estop.enable()
    print("motorone tests")
    motorone()
    time.sleep(3)
    print("motortwo tests")
    motortwo()
    estop.cleanup()
    sys.exit()

# ===================== END ===============================
