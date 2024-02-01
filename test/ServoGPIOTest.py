#!/usr/bin/env python3
""" 
test example file for module : rpiMotorlib.py
file : rpiservolib.py class : SG90servo 
This file is for servos controlled by GPIO PWM

Comment in code  blocks marked:
"EMERGENCY STOP BUTTON CODE" to Test motor stop method with Push Button
and place push button to VCC on GPIO 17 :: VCC - PB1Pin1 , GPIO17 - PB1Pin2
"""

import time
import RPi.GPIO as GPIO


"""
# For development USE local library testing import
# 1. Comment in Next 3 lines 
# 2. Comment out in "Production installed library import"
# 3. change rpiservolib.SG90servo to SG90servo  below
import sys
sys.path.insert(0, '/home/gavin/Documents/tech/RpiMotorLib/RpiMotorLib')
from rpiservolib import SG90servo
"""

# Production installed library import
from RpiMotorLib import rpiservolib

"""
# EMERGENCY STOP BUTTON CODE: See docstring
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

#initialize (name, freq, y_one, y_two)
myservotest  = rpiservolib.SG90servo("servoone", 50, 3, 11)


def main():
    """main function loop"""

    # ===== Tests for servo  ==========

    """
    # EMERGENCY STOP BUTTON CODE:  See docstring
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    """
    # == Test 1 test method servo_move_step  ==

    # (servo_pin, start, end, stepdelay,stepsize, initdelay, verbose)
    print("Test 1: test method servo_move_step")
    input("Press <Enter> to continue Test 1a")
    myservotest.servo_move_step(26, 10, 180, .1, 5, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test 1b")
    myservotest.servo_move_step(26, 170, 10, .5, 20, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test 1c")
    myservotest.servo_move_step(26, 10, 50, 1, 1, 1, True)
    time.sleep(1)

    # == Test 2 convert function ==
    
    print("Test 2: test method covert degree to duty cycle function")
    input("Press <Enter> to continue Test2")
    testdegree = float(input("What degree do you want?\t"))
    print("duty cycle percent = {} ".format(myservotest.convert_from_degree(testdegree)))

    # == Test 3  test method servo_sweep ==

    # (servo_pin, center, minduty, maxduty, delay, verbose, initdelay, sweeplen)
    print("Test 3: test method servo_sweep")
    input("Press <Enter> to continue Test 3a")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 3, 11, .5, True, .05, 10)
    # sweep from center to max
    input("Press <Enter> to continue Test 3b")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 11, .5, True, 2, 20)
    # sweep from center to min
    input("Press <Enter> to continue Test 3c")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 3, .5, True, .05)

    # == Test 3  test method servo_move ==

    # servo_pin, position, delay, verbose, initdelay):
    print("test 4 test method servo_move")
    input("Press <Enter> to continue Test4a")
    time.sleep(1)
    myservotest.servo_move(26, 12, .5, True, 0)
    input("Press <Enter> to continue Test4b")
    time.sleep(1)
    myservotest.servo_move(26, 2, .5, True, 0)
    input("Press <Enter> to continue Test4c")
    time.sleep(1)
    myservotest.servo_move(26, 7.5, .5, True, 0)

    time.sleep(1)

"""
# EMERGENCY STOP BUTTON CODE: See docstring
def button_callback(channel):
    print("Test file: Stopping motor")
    myservotest.servo_stop()
"""

# ===================MAIN===============================

if __name__ == '__main__':

    main()
    GPIO.cleanup()
    exit()


# =====================END===============================
