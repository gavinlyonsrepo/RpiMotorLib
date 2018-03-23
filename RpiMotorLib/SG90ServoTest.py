#!/usr/bin/env python3
""" test example file for rpiMotorlib.py """

import time 
import RPi.GPIO as GPIO
from RpiMotorLib import SG90servo

def main():
    """main function loop"""
    
    # ===== tests for sevro SG90 SECTION  ========== 
    # initialize
    myservotest  = SG90servo("servoone")
    
    # full sweep 2A
    input("Press <Enter> to continue Test1a1")
    time.sleep(1)
    myservotest.servo_sweep(7, 7.5, 3, 11, .5, True)
    # sweep from center to max 
    input("Press <Enter> to continue Test1a2")
    time.sleep(1)
    myservotest.servo_sweep(7, 7.5, 7.5, 11, .5, False)
    # sweep from center to min
    input("Press <Enter> to continue Test1a3")
    time.sleep(1)
    myservotest.servo_sweep(7, 7.5, 7.5, 3, .5, False)

     # single move 2B
    input("Press <Enter> to continue Test2b1")
    time.sleep(1)
    myservotest.servo_move(7, 11, .5, True)
    input("Press <Enter> to continue Test2b2")
    time.sleep(1)
    myservotest.servo_move(7, 2, .5, False)
    input("Press <Enter> to continue Test2b3")
    time.sleep(1)
    myservotest.servo_move(7, 7.5, .5, False)
   
    time.sleep(1)
    
# ===================MAIN===============================

if __name__ == '__main__':
   
    main()
    GPIO.cleanup()
    exit()
    

# =====================END===============================
