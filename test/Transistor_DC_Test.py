#!/usr/bin/env python3
""" test example file for rpiMotorlib.py : transistor DC motor """

import time 
import RPi.GPIO as GPIO
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
#from rpi_dc_lib import TranDc

from RpiMotorLib import rpi_dc_lib

def motorone():
    
    print(" TEST: testing motor 1") 
    # Motorssetup
    MotorOne = rpi_dc_lib.TranDc(26 ,200 ,True)

    # ================ Motors one test  section 1=============
    
    input("press key to speed up") 
    step_delay = .05
    for speed in range(0,100):
        MotorOne.dc_motor_run(speed, step_delay)
    time.sleep(5)
    input("press key to speed down") 
    for speed in range(100,0,-1):
        MotorOne.dc_motor_run(speed, step_delay)
    MotorOne.dc_clean_up()  
# ===================MAIN===============================

if __name__ == '__main__':
   
    print("START")
    print("motorone tests")
    motorone()
    GPIO.cleanup()
    exit()
    
# =====================END===============================
