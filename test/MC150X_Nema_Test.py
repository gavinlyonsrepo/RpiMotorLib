#!/usr/bin/env python3
"""
test example file for rpiMotorlib.py MC1508 stepper tests

Comment in code  blocks marked:
"EMERGENCY STOP BUTTON CODE" to Test motor stop method with Push Button
and place push button to VCC on GPIO 17 :: VCC - PB1Pin1 , GPIO17 - PB1Pin2
"""

import time
import RPi.GPIO as GPIO

"""
# For development USE local library testing import
# 1. Comment in Next 2 lines
import sys
sys.path.insert(0, '/home/gavin/Documents/tech/RpiMotorLib/')
"""

"""
# pipx installed path, use this if you have installed package with pipx
import sys
sys.path.insert(0, '/home/gavin/.local/pipx/venvs/rpimotorlib/lib/python3.11/site-packages/')
"""

# Production installed library import
from RpiMotorLib import RpiMotorLib

"""
# EMERGENCY STOP BUTTON CODE: See docstring
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

# Declare an named instance of class pass a name and type of motor
Motorname = "MyMotorOne"
Motortype = "Nema"
mymotortest = RpiMotorLib.BYJMotor(Motorname, Motortype)


def main():
    """main function loop"""

    """
    # EMERGENCY STOP BUTTON CODE:  See docstring
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    """
    # GPIO
    IN1 = 20
    IN2 = 21
    IN3 = 19
    IN4 = 26
    GpioPins = [IN3, IN1, IN4,IN2]

    # ====== tests for motor MC1508 StepTest ====

    time.sleep(1)
    input("Press <Enter> to continue Test1")

    # Test One , 360 turn
    wait = 0.5
    steps = 50 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "full"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    time.sleep(1)
    input("Press <Enter> to continue  Test2")


    # Test Two, 180 turn
    wait = 0.1
    steps = 25 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "full"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    time.sleep(1)
    input("Press <Enter> to continue  Test3")

    # Test Three, 180 turn
    wait = 0.2
    steps = 25 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "half"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test4")

    # Test 4, 360 turn
    wait = 0.05
    steps = 50 # No of step sequences
    ccwise = True
    verbose= True
    steptype = "half"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test5")

    # Test 5 180 turn
    wait = 0.02
    steps = 25 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "wave"
    initdelay = 5
    mymotortest.motor_run(GpioPins, wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test6")

    # Test 6, 72 turn
    wait = 0.02
    steps = 10 # No of step sequences
    ccwise = True
    verbose= True
    steptype = "wave"
    initdelay = 1
    mymotortest.motor_run(GpioPins, wait ,steps ,ccwise ,verbose, steptype ,initdelay)


"""
# EMERGENCY STOP BUTTON CODE: See docstring
def button_callback(channel):
    print("Test file: Stopping motor")
    mymotortest.motor_stop()
"""

# ===================MAIN===============================

if __name__ == '__main__':

    print("START")
    main()
    GPIO.cleanup() # Optional
    exit()



# =====================END===============================
