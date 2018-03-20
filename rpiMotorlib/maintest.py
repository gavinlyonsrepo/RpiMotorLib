#!/usr/bin/env python3
""" test example file for rpiMotorlib.py """

import time 
import RPi.GPIO as GPIO
import rpiMotorlib

def main():
    """main function loop"""
    
    # ====== tests for motor 28BYJ48 SECTION 1 ====
    
    GpioPins = [18, 23, 24, 25]
    # Declare an named instance of class pass a name
    mymotortest = rpiMotorlib.BYJMotor("NotorTwo")
    time.sleep(0.5)
    mymotortest.motorRun(GpioPins,.001,1000,True,True,"half")
    
    '''
    mymotortest.motorRun([18, 23, 24, 25],.01,100, True, True,"full")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.001,512, False, True,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.01,512, False, True,"wave")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.01, 250, False, False,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.5, 2, True, True,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.001,2000,False,False,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins)
    '''
    
    # ===== tests for sevro SG90 SECTION 2 ========== 
    # initialize
    myservotest  = rpiMotorlib.SG90servo("servoone")
    
    # full sweep 2A
    # myservotest.servoSweep(7, 7.5, 3, 11, .5, True)
    time.sleep(1)
    # sweep from center to max 
    #m yservotest.servoSweep(7, 7.5, 7.5, 11, .5, False)
    # sweep from center to min
    # myservotest.servoSweep(7, 7.5, 7.5, 3, .5, False)
    
     # single move 2B
    
    #myservotest.servoMove(7, 11, .5, True)
    time.sleep(1)
    myservotest.servoMove(7, 2, .5, False)
    time.sleep(1)
    # myservotest.servoMove(7, 7.5, .5, False)
    time.sleep(1)
    
# ===================MAIN===============================

if __name__ == '__main__':
   
    main()
    GPIO.cleanup()
    exit()
    

# =====================END===============================
