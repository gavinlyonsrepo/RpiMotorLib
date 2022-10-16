#!/usr/bin/env python3
""" 
test example file for module:rpiMotorlib.py
file: RpiMotorLib.py class BYJMotor, 
use threading to run two motors at same time.
use push button(to VCC) on GPIO 17 to stop motors if necessary

"""

import time
import RPi.GPIO as GPIO
import concurrent.futures


# Next 3 lines for development local library testing import
# Comment out in production release and change RpiMotorLib.BYJMotor to BYJMotor
'''
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from RpiMotorLib import BYJMotor
'''

# Production installed library import
from RpiMotorLib import RpiMotorLib

# To Test motor stop, put push button to VCC on GPIO 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Declare two named instance of class, pass your name and type of motor
mymotortestOne = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
mymotortestTwo = RpiMotorLib.BYJMotor("MyMotorTwo", "28BYJ")


def main():
    """main function loop"""

    # To Test motor stop , put push button to VCC on GPIO 17
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)

    # Connect GPIO to [IN1 , IN2 , IN3 ,IN4] on Motor PCB
    GpioPins1 = [18, 23, 24, 25]
    GpioPins2 = [6, 13, 19, 26]

    # ====== tests for two motor 28BYJ48 ====
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(mymotortestOne.motor_run, GpioPins1,.05,128, False, False,"half", .05)
        f2 = executor.submit(mymotortestTwo.motor_run, GpioPins2,.05,128, False, False,"half", .05)


# Comment in for testing motor stop function
def button_callback(channel):
    print("Test file: Stopping motor")
    mymotortestOne.motor_stop()
    mymotortestTwo.motor_stop()


# ===================MAIN===============================

if __name__ == '__main__':

    print("START")
    main()
    GPIO.cleanup() # Optional
    print("END")
    exit()

# =====================END===============================
