#!/usr/bin/env python3
""" test example file for rpiMotorlib.py """

import time 
import RPi.GPIO as GPIO

from RpiMotorLib import BYJMotor

def main():
    """main function loop"""
    
    # ====== tests for motor 28BYJ48 SECTION 1 ====
    
    GpioPins = [18, 23, 24, 25]
    # Declare an named instance of class pass a name
    mymotortest = BYJMotor("MyMotorOne")
    time.sleep(0.5)
    input("Press <Enter> to continue Test1")
    mymotortest.motor_run(GpioPins,.01,512, False, True,"full")
    time.sleep(2)
    input("Press <Enter> to continue  Test2")
    mymotortest.motor_run(GpioPins,.01,512, False, True,"wave")
    time.sleep(2)
    input("Press <Enter> to continue  Test3")
    mymotortest.motor_run(GpioPins,.01, 100, False, False,"half")
    time.sleep(2)
    input("Press <Enter> to continue Test4")
    mymotortest.motor_run(GpioPins,.1, 200, True, True,"half")
    time.sleep(2)
    input("Press <Enter> to continue Test5")
    mymotortest.motor_run(GpioPins,.001,2000,False,False,"half")
    time.sleep(2)
    input("Press <Enter> to continue Test6")
    mymotortest.motor_run(GpioPins)
    
    
# ===================MAIN===============================

if __name__ == '__main__':
   
    main()
    GPIO.cleanup()
    exit()
    

# =====================END===============================
