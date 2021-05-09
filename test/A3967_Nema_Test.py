#!/usr/bin/env python3
""" test example file for rpiMotorlib.py   motor A3967 NEMA """

import time
import RPi.GPIO as GPIO

"""
# Next 3 lines for development, local library testing import
# Comment out in production release and change RpiMotorLib.A3967EasyNema 
# to A3967EasyNema below
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from RpiMotorLib import A3967EasyNema
"""

# Production installed library import
from RpiMotorLib import RpiMotorLib

"""
# Comment in To Test motor stop, put push button to VCC on GPIO 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

def main():
    """main function loop"""

    # ====== Tests for motor A3967 NEMA ====
    """
    # Comment in To Test motor stop , put push button to VCC on GPIO 17
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    """
    
    # Full = 200 steps per revolution
    # Half = 400
    # 1/4 =  800
    # 1/8 =  1600

    #GPIO pins
    GPIO_pins = (6, 13) # Microstep Resolution MS1-MS2 -> GPIO Pin Set, Can be set to (-1,-1) 
    direction= 26       # Direction -> GPIO Pin
    step = 19           # Step -> GPIO Pin

    # Declare an named instance of class pass GPIO-PINs
    # (direction_pin, step_pin, mode_pins):
    mymotortest = RpiMotorLib.A3967EasyNema(direction, step, GPIO_pins)
    
    
    # ====================== section A ===================
    print("TEST SECTION A")
    
    # motor_move(stepdelay, steps, clockwise, verbose, steptype, initdelay):
    input("TEST: Press <Enter> for Test1, full mode, full turn")
    mymotortest.motor_move(.005, 200 , False, True, "Full", .05)
    time.sleep(1)
    
    
    input("TEST: Press <Enter> for Test2, half mode, full turn")
    mymotortest.motor_move(.005, 400 , False, True, "Half", .05)
    time.sleep(1)
    

    input("TEST: Press <Enter> for Test3, 1/4 mode, full turn")
    mymotortest.motor_move(.008, 800 , False, True, "1/4", .05)
    time.sleep(1)
    
    input("TEST: Press <Enter> for Test4, 1/8 mode, full turn")
    mymotortest.motor_move(.006, 1600 , False, True, "1/8", .05)
    time.sleep(1)
    
    # ========================== section B =========================
    print("TEST SECTION B")

    # motor_move(stepdelay, steps, clockwise, verbose, steptype, initdelay):
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


"""
# Comment in for testing motor stop function ,  put push button to VCC on GPIO 17
def button_callback(channel):
    print("Test file: Stopping motor")
    mymotortest.motor_stop()
"""

# ===================MAIN===============================

if __name__ == '__main__':

    print("TEST START")
    main()
    GPIO.cleanup()
    print("TEST END")
    exit()



# =====================END===============================
