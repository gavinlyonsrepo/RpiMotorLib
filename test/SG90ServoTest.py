#!/usr/bin/env python3
""" test example file for rpiMotorlib.py """

import time 
import RPi.GPIO as GPIO
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')

from rpiservolib import SG90servo


def main():
    """main function loop"""
    
    # ===== tests for servo SG90 ========== 
    # initialize
    myservotest  = SG90servo("servoone", 50, 3, 11)
    
    
    
    input("Press <Enter> to continue Test1a")
    myservotest.servo_move_step(26, 10, 180, .1, 5, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test1b")
    myservotest.servo_move_step(26, 170, 10, .5, 20, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test1b")
    myservotest.servo_move_step(26, 10, 50, 1, 1, 1, True)
    time.sleep(1)
   
    
    # test convert function 
    input("Press <Enter> to continue Test2")
    testdegree = float(input("What degree do you want?\t"))
    print("duty cycle percent = {} ".format(myservotest.convert_from_degree(testdegree)))
    
    
   
    # full sweep section 3
    input("Press <Enter> to continue Test3a1")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 3, 11, .5, True)
    # sweep from center to max 
    input("Press <Enter> to continue Test3a2")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 11, .5, False)
    # sweep from center to min
    input("Press <Enter> to continue Test3a3")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 3, .5, False)

     # single move section 4
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
