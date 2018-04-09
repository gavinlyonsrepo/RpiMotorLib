#!/usr/bin/env python3
""" test example file for rpiMotorlib.py """

import time 
import RPi.GPIO as GPIO
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')

from RpiMotorLib import BYJMotor

# 1.8 360/200 full / wave
# .9  360/400 half
# 200/8 = 25 *2 half 
# 200/4 = 50  full wave.


def main():
    """main function loop"""
    
    # ====== tests for motor L298STepTest ====
    
    GpioPins = [19, 13, 21, 20]
    # Declare an named instance of class pass a name and type of motor
   
    mymotortest = BYJMotor("MyMotorOne", "Nema")
    time.sleep(1)
    
    # motor_run(gpiopins, wait=.001, steps=512, ccwise=False, verbose=False, steptype="half", initdelay=.001):
    input("Press <Enter> to continue Test1")
    mymotortest.motor_run(GpioPins,.05, 20, False, True,"half" ,1 )
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
