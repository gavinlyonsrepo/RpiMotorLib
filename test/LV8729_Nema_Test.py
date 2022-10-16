#!/usr/bin/env python3
""" test example file for rpiMotorlib.py LV8729 NEMA"""

import time
import RPi.GPIO as GPIO

"""
# Next 3 lines for development, local library testing import
# Comment out in production release and change RpiMotorLib.A4988Nema to A4988Nema 
# below when declaring mymotortest
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from RpiMotorLib import A4988Nema
"""

# Production installed library import , comment out in debug
from RpiMotorLib import RpiMotorLib

"""
# Comment in To Test motor stop, put push button to VCC on GPIO 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

def main():
    """main function loop"""

    """
    # Comment in To Test motor stop , put push button to VCC on GPIO 17
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    """
    
    # ====== Tests for motor ======

    # Microstep Resolution MS1-MS3 -> GPIO Pin , can be set to (-1,-1,-1) to turn off 
    GPIO_pins = (14, 15, 18) 
    direction= 20       # Direction -> GPIO Pin
    step = 21      # Step -> GPIO Pin
    
    # Declare an named instance of class pass GPIO-PINs
    # (self, direction_pin, step_pin, mode_pins , motor_type):
    
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "LV8729")
    
    # ====================== section A ===================
    print("TEST SECTION A")

    # motor_go(clockwise, steptype", steps, stepdelay, verbose, initdelay)
    input("TEST: Press <Enter> to continue  Full 180 turn Test1")
    mymotortest.motor_go(False, "Full" , 100, .05, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  full 180 clockwise Test2")
    mymotortest.motor_go(True, "Full" , 100, .05, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  timedelay Test3")
    mymotortest.motor_go(True, "Full" , 10, 1, True, .05)
    time.sleep(1)

    # ========================== section B =========================
    print("TEST SECTION B")

    # motor_go(clockwise, steptype", steps, stepdelay, verbose, initdelay)
    input("TEST: Press <Enter> to continue  half Test4")
    mymotortest.motor_go(False, "Half" , 400, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/ 4 Test5")
    mymotortest.motor_go(False, "1/4" , 800, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/8 Test6")
    mymotortest.motor_go(False, "1/8" , 1600, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue  1/16 Test7")
    mymotortest.motor_go(False, "1/16" , 3200, .005, True, .05)
    time.sleep(1)
    
    # ========================== section C =========================
    print("TEST SECTION C")

    # motor_go(clockwise, steptype", steps, stepdelay, verbose, initdelay)
    input("TEST: Press <Enter> to continue  1/32 Test8")
    mymotortest.motor_go(False, "1/32" , 6400, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/ 64 Test9")
    mymotortest.motor_go(False, "1/64" , 12800, .005, True, .05)
    time.sleep(1)
    input("TEST: Press <Enter> to continue 1/128 Test10")
    mymotortest.motor_go(False, "1/128" , 25600, .005, True, .05)
    time.sleep(1)


"""
# Comment in for testing motor stop
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
