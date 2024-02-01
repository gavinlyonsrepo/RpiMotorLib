#!/usr/bin/env python3
""" test example file for: module rpiMotorlib.py 
file: rpi_pservo_lib class:ServoPigpio,
Run a servo using pigpio library RPI
make sure to start the pigpio dameon , sudo pigpiod

Comment in code  blocks marked:
"EMERGENCY STOP BUTTON CODE" to Test motor stop method with Push Button
and place push button to VCC on GPIO 17 :: VCC - PB1Pin1 , GPIO17 - PB1Pin2
"""

import time

"""
# For development USE local library testing import
# 1. Comment in Next 3 lines 
# 2. Comment out in "Production installed library import"
# 3. change rpi_pservo_lib.ServoPigpio to ServoPigpio below
import sys
sys.path.insert(0, '/home/gavin/Documents/tech/RpiMotorLib/RpiMotorLib')
from rpi_pservo_lib import ServoPigpio
"""

# Production installed library import
from RpiMotorLib import rpi_pservo_lib

"""
# EMERGENCY STOP BUTTON CODE: See docstring
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

# initialize(name freq, y_one, y_two)
myservotest  = rpi_pservo_lib.ServoPigpio("servoone", 50, 1000, 2000 )

def main():
    """main function loop"""

    # ===== Tests for servo  ==========
    
    """
    # EMERGENCY STOP BUTTON CODE:  See docstring
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    """
    
    # == Test Section 1 method servo_move_step==
    
    # Args (servo_pin, start, end, stepdelay, stepsize, initdelay, verbose)
    print("\nTest 1x servo_move_step")
    input("Press <Enter> to continue Test 1a")
    myservotest.servo_move_step(26, 15, 180, .1, 5, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test 1b")
    myservotest.servo_move_step(26, 170, 15, .5, 20, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test 1c")
    myservotest.servo_move_step(26, 10, 50, 1, 1, 1, True)
    time.sleep(1)
    
    # == Test Section 2 degree to pulse width == 
    
    input("Press <Enter> to continue Test2")
    print("\nTest 2x degree conversion function check")
    testdegree = float(input("What degree do you want?\t"))
    print("Pulse width micro seconds = {} ".format(myservotest.convert_from_degree(testdegree)))
    

    # == Test Section 3 servo_sweep == 
    
    # args (servo_pin, center=, minduty,maxduty,delay,verbose,initdelay,sweeplen)
    print("\nTest 3x servo Sweep")
    input("Press <Enter> to continue Test 3a")
    time.sleep(1)
    myservotest.servo_sweep(26, 1500, 700, 2000, .5, True, .05, 10)
    # sweep from center to max
    input("Press <Enter> to continue Test 3b")
    time.sleep(1)
    myservotest.servo_sweep(26, 1500, 1500, 2000, .5, True, 2, 20)
    # sweep from center to min
    input("Press <Enter> to continue Test 3c")
    time.sleep(1)
    myservotest.servo_sweep(26, 1500, 1500, 800, .5, True, .05)
    
    
    #== Test Section 4 servo_sweep == 
    # servoMove(servo_pin, position, delay, verbose, initdelay)
    print("\nTest 4x servo_move test")
    input("Press <Enter> to continue Test 4a")
    time.sleep(1)
    myservotest.servo_move(26, 2000, .5, True,.05)
    input("Press <Enter> to continue Test 4b")
    time.sleep(1)
    myservotest.servo_move(26, 1000, .5, True,.5)
    input("Press <Enter> to continue Test 4c")
    time.sleep(1)
    myservotest.servo_move(26, 1500, .5, True,4)
    
    time.sleep(1)


"""
# EMERGENCY STOP BUTTON CODE: See docstring
def button_callback(channel):
    print("Test file: Stopping motor")
    myservotest.servo_stop()
"""

# ===================MAIN===============================

if __name__ == '__main__':

    main()
    exit()


# =====================END===============================
