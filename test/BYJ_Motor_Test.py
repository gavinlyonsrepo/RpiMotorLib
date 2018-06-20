#!/usr/bin/env python3
""" test example file for module:rpiMotorlib.py 
file: RpiMotorLib.py class BYJMotor
"""

import time 
import RPi.GPIO as GPIO
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
#from RpiMotorLib import BYJMotor

from RpiMotorLib import RpiMotorLib


def main():
    """main function loop"""
    
    # ====== tests for motor 28BYJ48 ====
    
    GpioPins = [18, 23, 24, 25]
    
    # Declare an named instance of class pass a name and type of motor
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    
    time.sleep(0.1)
    input("Press <Enter> to continue Test1")
    mymotortest.motor_run(GpioPins,.01,512, True, True,"full",10)
    time.sleep(1)
    input("Press <Enter> to continue  Test2")
    mymotortest.motor_run(GpioPins,.01,512, False, True,"wave", .05)
    time.sleep(1)
    input("Press <Enter> to continue  Test3")
    mymotortest.motor_run(GpioPins,.01, 1, False, True,"half", 2)
    time.sleep(1) 
    input("Press <Enter> to continue  Test4")
    mymotortest.motor_run(GpioPins,.05, 50, True, True,"half", .05)
    time.sleep(1)
    input("Press <Enter> to continue  Test5")
    mymotortest.motor_run(GpioPins,.001,1000,False,False,"half", .05)

    
    
# ===================MAIN===============================

if __name__ == '__main__':
   
    print("START")
    main()
    GPIO.cleanup()
    exit()
    
    

# =====================END===============================
