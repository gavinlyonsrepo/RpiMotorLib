#!/usr/bin/env python3
""" 
Test example file for file: RpiMotorLib.py DRV8825 NEMA"

Comment in code  blocks marked:
"EMERGENCY STOP BUTTON CODE" to Test motor stop method with Push Button
and place push button to VCC on GPIO 17 :: VCC - PB1Pin1 , GPIO17 - PB1Pin2
"""

import time 
import RPi.GPIO as GPIO

"""
# For development USE local library testing import
# 1. Comment in Next 3 lines 
# 2. Comment out in "Production installed library import"
# 3. change RpiMotorLib.A4988Nema to A4988Nema below
import sys
sys.path.insert(0, '/home/gavin/Documents/tech/RpiMotorLib/RpiMotorLib')
from RpiMotorLib import A4988Nema 
"""

# Production installed library import 
from RpiMotorLib import RpiMotorLib

"""
# EMERGENCY STOP BUTTON CODE: See docstring
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

#GPIO pins 
# Microstep Resolution M0-M1-M2 -> GPIO Pin
# Note: you can Pass in (-1,-1,-1) if you wish to hardwire Ms-X to logic and 
# Save GPIO pins. 
GPIO_pins = (14, 15, 18)
direction= 20  # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO-PINs
#( self, direction_pin, step_pin, mode_pins ,motor_type)
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "DRV8825")

def main():
    """main function loop"""

    # ====== Tests for motor ====
    """
    # EMERGENCY STOP BUTTON CODE:  See docstring
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    """

    # ====================== section A ===================
    print("TEST SECTION A")
    
    # motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)
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
    
    # motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)
    input("TEST: Press <Enter> to continue  half Test6")
    mymotortest.motor_go(False, "Half" , 400, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/ 4 Test7")
    mymotortest.motor_go(False, "1/4" , 800, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/8 Test8")
    mymotortest.motor_go(False, "1/8" , 1600, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  1/16 Test9")
    mymotortest.motor_go(False, "1/16" , 3200, .005, True, .05) 
    time.sleep(1)
    input("TEST: Press <Enter> to continue  1/32 Test10")
    mymotortest.motor_go(False, "1/32" , 6400, .005, True, .05) 
    time.sleep(1)


"""
# EMERGENCY STOP BUTTON CODE: See docstring
def button_callback(channel):
    print("Test file: Stopping motor")
    mymotortest.motor_stop()
"""

# ===================MAIN===============================

if __name__ == '__main__':
   
    print("TEST START")
    main()
    GPIO.cleanup() # Optional
    print("TEST END")
    exit()
    
    

# =====================END===============================
