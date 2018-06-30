#!/usr/bin/env python3
""" test example file for rpiMotorlib.py L298 stepper tests"""

import time 
import RPi.GPIO as GPIO
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
#from RpiMotorLib import BYJMotor

from RpiMotorLib import RpiMotorLib


def main():
    """main function loop"""
    
    # ====== tests for motor L298STepTest ====
    
    GpioPins = [19, 26, 21, 13]
    #GpioPins = [19, 13, 21, 20]
    # Declare an named instance of class pass a name and type of motor
   
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
    time.sleep(1)
    
    # motor_run(gpiopins, wait, steps, ccwise, verbose, steptype, initdelay):
    input("Press <Enter> to continue Test1")
    mymotortest.motor_run(GpioPins,.5, 200, False, True,"full" ,1 )
    time.sleep(1)
    input("Press <Enter> to continue  Test2")
    mymotortest.motor_run(GpioPins,.1, 20 , False, True,"wave", 1)
    time.sleep(1)
    input("Press <Enter> to continue  Test3")
    mymotortest.motor_run(GpioPins,.2, 10, False, True,"full", 1)
    time.sleep(1) 
    input("Press <Enter> to continue  Test4")
    mymotortest.motor_run(GpioPins,.05, 25, True, True,"half", 1)
    time.sleep(1)
    input("Press <Enter> to continue  Test5")
    mymotortest.motor_run(GpioPins,.02,25,False,False,"half", 5)

    
    
# ===================MAIN===============================

if __name__ == '__main__':
   
    print("START")
    main()
    GPIO.cleanup()
    exit()
    
    

# =====================END===============================
