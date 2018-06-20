#!/usr/bin/env python3
""" test example file for rpiMotorlib.py DRV8825 NEMA"""

import time 
import RPi.GPIO as GPIO
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')


from RpiMotorLib import RpiMotorLib

# 200 steps full revolution
# 400 half
# 800 1/4
# 1600 1/8
# 3200 1/16
# 6400 1/32
# __init__(self, direction_pin, step_pin, mode_pins ,motor_type):
# motor_go(clockwise=False, steptype="Full", steps=200, stepdelay=.005, verbose=False, initdelay=.05)

def main():
    """main function loop"""
    
    # ====== tests for motor ====
    
    #GPIO pins 
    GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
    direction= 20       # Direction -> GPIO Pin
    step = 21      # Step -> GPIO Pin
    
    # Declare an named instance of class pass GPIO-PINs
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "DRV8825")
    
    # ====================== section A ===================
    print("TEST SECTION A")
    
    input("TEST: Press <Enter> to continue  Full 180 turn Test1")
    mymotortest.motor_go(False, "Full" , 100, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  full 180 clockwise Test2")
    mymotortest.motor_go(True, "Full" , 100, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  full 180 no verbose Test3")
    mymotortest.motor_go(False, "Full" , 100, .005, False, .05)
    time.sleep(1) 
    input("TEST: Press <Enter> to continue  timedelay Test4")
    mymotortest.motor_go(True, "Full" , 10, 1, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  full initdelay Test5")
    mymotortest.motor_go(True, "Full" , 90, .01, True, 10)
    time.sleep(1)
    
    # ========================== section B =========================
    print("TEST SECTION B")
    
    input("TEST: Press <Enter> to continue  half Test1")
    mymotortest.motor_go(False, "Half" , 400, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/ 4 Test1")
    mymotortest.motor_go(False, "1/4" , 800, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/8 Test1")
    mymotortest.motor_go(False, "1/8" , 1600, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  1/16 Test1")
    mymotortest.motor_go(False, "1/16" , 3200, .005, True, .05) 
    time.sleep(1)
    
    input("TEST: Press <Enter> to continue  1/32 Test1")
    mymotortest.motor_go(False, "1/32" , 6400, .005, True, .05) 
    time.sleep(1)
    
# ===================MAIN===============================

if __name__ == '__main__':
   
    print("TEST START")
    main()
    GPIO.cleanup()
    print("TEST END")
    exit()
    
    

# =====================END===============================
