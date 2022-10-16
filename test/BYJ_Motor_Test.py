#!/usr/bin/env python3
""" test example file for module:rpiMotorlib.py 
file: RpiMotorLib.py class BYJMotor
"""

import time 
import RPi.GPIO as GPIO

# Next 3 lines for development local library testing import
# Comment out in production release and change RpiMotorLib.BYJMotor to BYJMotor
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
#from RpiMotorLib import BYJMotor

# Production installed library import 
from RpiMotorLib import RpiMotorLib

"""
# Needed for testing motor stop 
# To Test motor stop put push button to VCC on GPIO 17 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

# Declare an named instance of class pass your custom name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

def main():
    """main function loop"""
    
    # ====== tests for motor 28BYJ48 ====
    
    # Needed for testing motor stop
    # GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    
    # Connect GPIO to [IN1 , IN2 , IN3 ,IN4] on Motor PCB
    GpioPins = [18, 23, 24, 25]
    
    # Arguments  for motor run function
    # (GPIOPins, stepdelay, steps, counterclockwise, verbose, steptype, initdelay)
    
    time.sleep(0.1)
    input("Press <Enter> to continue Test1")
    mymotortest.motor_run(GpioPins,.05,128, True, True,"full", .05)
    time.sleep(1)
    input("Press <Enter> to continue  Test2")
    mymotortest.motor_run(GpioPins,.001,256, False, True,"half", .05)
    time.sleep(1)
    input("Press <Enter> to continue  Test3")
    mymotortest.motor_run(GpioPins,.01, 5, False, True,"half", 2)
    time.sleep(1) 
    input("Press <Enter> to continue  Test4")
    mymotortest.motor_run(GpioPins,.05, 50, True, True,"wave", .05)
    time.sleep(1)
    input("Press <Enter> to continue  Test5")
    mymotortest.motor_run(GpioPins,.01,512,False,False,"half", .05)
  
"""
# needed for testing motor stop 
def button_callback(channel): 
    print("Test file: Stopping motor")
    mymotortest.motor_stop()   
"""

# ===================MAIN===============================

if __name__ == '__main__':
   
    print("START")
    main()
    GPIO.cleanup() # Optional 
    exit()
    
    
# =====================END===============================
