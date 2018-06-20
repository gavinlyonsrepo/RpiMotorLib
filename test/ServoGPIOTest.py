#!/usr/bin/env python3
""" test example file for module : rpiMotorlib.py
file : rpiservolib.py class : SG90servo 
This file is for servos controlled by GPIO PWM"""

import time
import RPi.GPIO as GPIO
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')

from RpiMotorLib import rpiservolib

def main():
    """main function loop"""

    # ===== tests for servo SG90 ==========
    # initialize
    #  name="SG90servoX", freq=50, y_one=2, y_two=12
    myservotest  = rpiservolib.SG90servo("servoone", 50, 3, 11)

    # section 1
    # servo_pin, start=10, end=170, stepdelay=1,
    # stepsize=1, initdelay=1, verbose=False
    print("test 1 test method servo_move_step")
    input("Press <Enter> to continue Test1a")
    myservotest.servo_move_step(26, 10, 180, .1, 5, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test1b")
    myservotest.servo_move_step(26, 170, 10, .5, 20, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test1b")
    myservotest.servo_move_step(26, 10, 50, 1, 1, 1, True)
    time.sleep(1)


    # section 2 
    # test convert function
    print("Test 2: test method covert degree to duty cycle function")
    input("Press <Enter> to continue Test2")
    testdegree = float(input("What degree do you want?\t"))
    print("duty cycle percent = {} ".format(myservotest.convert_from_degree(testdegree)))
    


    # section 3
    # servo_pin=7, center=7.5, minduty=3,
    # maxduty=11, delay=0.5, verbose=False, initdelay=.05, sweeplen=1000000
    print("test 3 test method servo_sweep")
    input("Press <Enter> to continue Test3a1")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 3, 11, .5, True, .05, 10)
    # sweep from center to max
    input("Press <Enter> to continue Test3a2")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 11, .5, True, 2, 20)
    # sweep from center to min
    input("Press <Enter> to continue Test3a3")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 3, .5, True, .05)


    # section 4
    # servo_pin, start=10, end=170, stepdelay=1,
    # stepsize=1, initdelay=1, verbose=False
    print("test 4 test method servo_move")
    input("Press <Enter> to continue Test4b1")
    time.sleep(1)
    myservotest.servo_move(26, 12, .5, True)
    input("Press <Enter> to continue Test4b2")
    time.sleep(1)
    myservotest.servo_move(26, 2, .5, True)
    input("Press <Enter> to continue Test4b3")
    time.sleep(1)
    myservotest.servo_move(26, 7.5, .5, True)

    time.sleep(1)

# ===================MAIN===============================

if __name__ == '__main__':

    main()
    GPIO.cleanup()
    exit()


# =====================END===============================
