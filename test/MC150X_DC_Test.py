#!/usr/bin/env python3
""" test example file for rpiMotorlib.py
testfile for  two DC motor run by MX1508 motor test"""

import time
import RPi.GPIO as GPIO

"""
# Next 2 lines for development local library path testing import
# Comment out in production release
import sys
sys.path.insert(0, '/home/gavin/Documents/tech/RpiMotorLib/')
"""

"""
# pipx installed path, use this if you have installed package with pipx
import sys
sys.path.insert(0, '/home/gavin/.local/pipx/venvs/rpimotorlib/lib/python3.11/site-packages/')
"""

# Production installed library import
from RpiMotorLib import rpi_dc_lib

# ====== tests MX1508 connections====

# + = Motor voltage (2-10 volts)
# - = GND
# my pin-outs MX1508
# inT1 GPIO 26 
# inT2 GPIO 19
# inT3 GPIO 20
# inT4 GPIO 21


def motorone():

    print(" TEST: testing motor 1")
    # Motors setup
    MotorOne = rpi_dc_lib.MC150XDc(26 ,19 ,50 ,True, "motor_one")

    # ================ Motors one test  section =============
    try:
        print("1. motor forward")
        MotorOne.forward(15)
        input("press key to stop")
        print("motor stop\n")
        MotorOne.standby(0)
        time.sleep(3)

        print("2. motor forward speed up")
        for i in range(15,30):
            MotorOne.forward(i)
            time.sleep(1)
        MotorOne.standby(0)
        print("motor stoped\n")
        time.sleep(3)

        print("3. motor backward")
        MotorOne.backward(15)
        input("press key to stop")
        MotorOne.standby(0)
        print("motor stopped\n")
        time.sleep(3)

        print("4. motor backward speed up")
        for i in range(15,30):
            MotorOne.backward(i)
            time.sleep(1)
        MotorOne.standby(0)
        print("motor stopped\n")
        time.sleep(3)

        print("5  brake check")
        MotorOne.forward(50)
        time.sleep(3)
        MotorOne.brake(100)
        print("motor brake\n")

    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorOne.cleanup(False)
        print("=== End Motor One ===")


def motortwo():

    print(" TEST: testing motor ")
    # Motors setup
    MotorTwo = rpi_dc_lib.MC150XDc(20 ,21 ,50 ,True, "motor_two")

    # ================ Motors two test section =============
    try:
        print("1. motor forward")
        MotorTwo.forward(15)
        input("press key to stop")
        MotorTwo.standby(0)
        print("motor stop\n")
        time.sleep(3)


        print("2. motor forward speed up")
        for i in range(15,30):
            MotorTwo.forward(i)
            time.sleep(1)
        MotorTwo.standby(0)
        print("motor stop\n")
        time.sleep(3)


        print("3. motor backward")
        MotorTwo.backward(15)
        input("press key to stop")
        MotorTwo.standby(0)
        print("motor stop\n")
        time.sleep(3)


        print("4. motor backward speed up")
        for i in range(15,30):
            MotorTwo.backward(i)
            time.sleep(1)
        MotorTwo.standby(0)
        print("motor stop\n")
        time.sleep(3)

        print("5  brake check")
        MotorTwo.forward(50)
        time.sleep(3)
        MotorTwo.brake(100)
        print("motor brake\n")

    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorTwo.cleanup(False)
        print("=== End Motor Two ===")

# ===================MAIN===============================

if __name__ == '__main__':

    print("=== START ===")
    print("=== motor one tests ===")
    motorone()
    time.sleep(3)
    print("=== motor two tests ===")
    motortwo()
    print("=== End All===")
    exit()



# =====================END===============================
