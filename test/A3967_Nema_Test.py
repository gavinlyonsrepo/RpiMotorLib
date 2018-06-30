#!/usr/bin/env python3
""" test example file for rpiMotorlib.py   motor A3967 NEMA """

import time 
import RPi.GPIO as GPIO



from RpiMotorLib import RpiMotorLib

# 200 steps full revolution
# 400 half
# 800 1/4
# 1600 1/8
# __init__(self, direction_pin, step_pin, mode_pins):
# motor_move(self, stepdelay=.05, steps=200, clockwise=False, verbose=False, steptype="Full",
 #                 ,  initdelay=.1):

def main():
    """main function loop"""
    
    # ====== tests for motor A3967 NEMA ====
    
    #GPIO pins 
    GPIO_pins = (6, 13) # Microstep Resolution MS1-MS2 -> GPIO Pin
    direction= 26       # Direction -> GPIO Pin
    step = 19    # Step -> GPIO Pin
    
    # Declare an named instance of class pass GPIO-PINs
    mymotortest = RpiMotorLib.A3967EasyNema(direction, step, GPIO_pins)
    
    # ====================== section A ===================
    print("TEST SECTION A")
    
    input("TEST: Press <Enter> for Test1 full mode full turn")
    mymotortest.motor_move(.005, 200 , False, True, "Full", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test2 half mode full turn")
    mymotortest.motor_move(.05, 400 , False, True, "Half", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test3 1/4 mode full turn")
    mymotortest.motor_move(.008, 800 , False, True, "1/4", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test4 1/8 mode full turn")
    mymotortest.motor_move(.006, 1600 , False, True, "1/8", .05)
    time.sleep(1)
    
    # ========================== section B =========================
    print("TEST SECTION B")
    input("TEST: Press <Enter> for Test5 , full mode, init delay")
    mymotortest.motor_move(.005, 100 , False, True, "Full", 5)
    time.sleep(1)
    input("TEST: Press <Enter> for Test6, full mode, direction turn")
    mymotortest.motor_move(.005, 100 , True, True, "Full", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test7, full mode, no verbose")
    mymotortest.motor_move(.005, 100 , False, False, "Full", .05)
    time.sleep(1)
    input("TEST: Press <Enter> for Test8, full mode, slow small turn")
    mymotortest.motor_move(1, 3 , False, True, "Full", .05)
    time.sleep(1)

# ===================MAIN===============================

if __name__ == '__main__':
   
    print("TEST START")
    main()
    GPIO.cleanup()
    print("TEST END")
    exit()
    
    

# =====================END===============================
