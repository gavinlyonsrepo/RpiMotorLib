#!/usr/bin/env python3
""" test example file for rpiMotorlib.py TB6612FNG DC motor
3 functions Motorone =one motor running , motortwo =second motor running, motorboth = both motors running"""

import time
import RPi.GPIO as GPIO

"""
# Next 3 lines for development local library path testing import
# Comment out in production release and change rpi_dc_lib.TB6612FNGDc to TB6612FNGDc
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from rpi_dc_lib import TB6612FNGDc
"""

# Production installed library import 
from RpiMotorLib import rpi_dc_lib

# ====== tests for  DC motor driven by TB6612FNG ====
# TB66 -- GPIO RPI
PWA = 17
AI1 = 22
AI2 = 27
PWB = 18
BI1 = 23
BI2 = 24
Standby = 25

Freq = 50
# ======== test motor 1 ==================

def motorone():
    """ set of tests to run on one DC motor connected to A channel """
    print(" TEST: testing motor 1")
    # Motorssetup
    MotorOne = rpi_dc_lib.TB6612FNGDc(AI1 ,AI2 ,PWA ,Freq,True, "motor_one")
    # ================ Motors one test  section 1=============
    try:
        print("1. motor forward")
        MotorOne.forward(15)
        input("press key to stop")
        print("motor stop\n")
        MotorOne.stop(0)
        time.sleep(3)

        print("2. motor forward speed up")
        for i in range(15,30):
            MotorOne.forward(i)
            time.sleep(1)
        MotorOne.stop(0)
        print("motor stoped\n")
        time.sleep(3)

        print("3. motor backward")
        MotorOne.backward(15)
        input("press key to stop")
        MotorOne.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("4. motor backward speed up")
        for i in range(15,30):
            MotorOne.backward(i)
            time.sleep(1)
        MotorOne.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("5  brake check")
        MotorOne.forward(50)
        time.sleep(3)
        MotorOne.brake(0)
        print("motor brake\n")

    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorOne.cleanup(False)


def motortwo():
    """ set of tests to run on one DC motor connected to B channel """
    print(" TEST: testing motor ")
    # Motorssetup
    MotorTwo = rpi_dc_lib.TB6612FNGDc(BI1 ,BI2 ,PWB ,Freq ,True, "motor_two")

    # ================ Motors two test  section 1=============
    try:
        print("1. motor forward")
        MotorTwo.forward(15)
        input("press key to stop")
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)


        print("2. motor forward speed up")
        for i in range(15,30):
            MotorTwo.forward(i)
            time.sleep(1)
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)


        print("3. motor backward")
        MotorTwo.backward(15)
        input("press key to stop")
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)


        print("4. motor backward speed up")
        for i in range(15,30):
            MotorTwo.backward(i)
            time.sleep(1)
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)


        print("5 .brake check")
        MotorTwo.forward(50)
        time.sleep(3)
        MotorTwo.brake(0)
        print("motor brake\n")

    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorTwo.cleanup(False)


def motorboth():
    """ set of tests to run on two DC motors connected to A and B channel """
    print(" TEST: testing motor ")
    # Motorssetup
    MotorOne = rpi_dc_lib.TB6612FNGDc(AI1 ,AI2 ,PWA ,Freq,True, "motor_one both")
    MotorTwo = rpi_dc_lib.TB6612FNGDc(BI1 ,BI2 ,PWB ,Freq ,True, "motor_two both")

    # ================ Both Motors running =============
    try:
        print("Both motors forward")
        MotorOne.forward(25)
        MotorTwo.forward(25)
        input("press key to stop")
        print("motor stop\n")
        MotorOne.stop(0)
        MotorTwo.stop(0)
        time.sleep(3)


    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorOne.cleanup(False)
        MotorTwo.cleanup(False)

# ===================MAIN===============================

if __name__ == '__main__':
    try:
        print("START")
        rpi_dc_lib.TB6612FNGDc.standby(Standby, True)
        print("motorone tests")
        motorone()
        time.sleep(3)
        print("motortwo tests")
        motortwo()
        time.sleep(3)
        print("motor_both running test")
        motorboth()
        time.sleep(1)
    finally:
        rpi_dc_lib.TB6612FNGDc.standby(Standby, False)
        GPIO.cleanup() # optional

    exit()


# =====================END===============================
