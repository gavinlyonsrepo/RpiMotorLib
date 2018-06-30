#!/usr/bin/env python3
""" test example file for: module rpiMotorlib.py 
file: rpi_pservo_lib class:ServoPigpio,
Run a servo using pigpio library RPI """

import time
import RPi.GPIO as GPIO
# import sys
# sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from RpiMotorLib import rpi_pservo_lib

def main():
    """main function loop"""

    # ===== tests for servo SG90 ==========
    # initialize
    # name="SG90servoY", freq=50, y_one=1000, y_two=2000)
    myservotest  = rpi_pservo_lib.ServoPigpio("servoone", 50, 1000, 2000 )

    # Section 1
    # servo_pin, position=1500,
    # delay=0.5, verbose=False, initdelay=.05
    print("\nTest 1x servo_move_step")
    input("Press <Enter> to continue Test1a")
    myservotest.servo_move_step(26, 15, 180, .1, 5, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test1b")
    myservotest.servo_move_step(26, 170, 15, .5, 20, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test1b")
    myservotest.servo_move_step(26, 10, 50, 1, 1, 1, True)
    time.sleep(1)
    
    # section 2
    # test convert function - degree to pulse width
    input("Press <Enter> to continue Test2")
    print("\nTest 2x degree conversion function check")
    testdegree = float(input("What degree do you want?\t"))
    print("Pulse width micro seconds = {} ".format(myservotest.convert_from_degree(testdegree)))
    

    
    # full sweep section 3 testing sevro sweep
    # servo_sweep(self, servo_pin=7, center=1500, minduty=1000,
    # maxduty=2000, delay=0.5, verbose=False, initdelay=.05, sweeplen=1000000)
    print("\nTest 3x servo Sweep")
    input("Press <Enter> to continue Test3a1")
    time.sleep(1)
    myservotest.servo_sweep(26, 1500, 700, 2000, .5, True, .05, 10)
    # sweep from center to max
    input("Press <Enter> to continue Test3a2")
    time.sleep(1)
    myservotest.servo_sweep(26, 1500, 1500, 2000, .5, True, 2, 20)
    # sweep from center to min
    input("Press <Enter> to continue Test3a3")
    time.sleep(1)
    myservotest.servo_sweep(26, 1500, 1500, 800, .5, True, .05)
    
    
    
    # single move section 4
    # servoMove(servo_pin, position, delay, verbose)
    print("\nTest 4x servo_move test")
    input("Press <Enter> to continue Test4b1")
    time.sleep(1)
    myservotest.servo_move(26, 2000, .5, True,.05)
    input("Press <Enter> to continue Test4b2")
    time.sleep(1)
    myservotest.servo_move(26, 1000, .5, True,.5)
    input("Press <Enter> to continue Test4b3")
    time.sleep(1)
    myservotest.servo_move(26, 1500, .5, True,4)
    
    time.sleep(1)

# ===================MAIN===============================

if __name__ == '__main__':

    main()
    exit()


# =====================END===============================
