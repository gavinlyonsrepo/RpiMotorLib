#!/usr/bin/env python3
""" test example file for rpiMotorlib.py L298 stepper tests"""

import time 
import RPi.GPIO as GPIO

# Next 3 lines for development, local library testing import
# Comment out in production release and change RpiMotorLib.BYJMotor to BYJMotor
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
#from RpiMotorLib import BYJMotor

# Production installed library import 
from RpiMotorLib import RpiMotorLib

# Declare an named instance of class pass a name and type of motor
# type of motor(Nema) is case sensitive  
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")

"""
# To Test motor stop put push button to VCC on GPIO 17 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

def main():
    """main function loop"""
    
    # ====== tests for motor L298STepTest ====
    
    # To Test motor stop , put push button to VCC on GPIO 17 
    # GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
    
    # Connect GPIO to [IN1 , IN2 , IN3 ,IN4] on Motor PCB
    GpioPins = [19, 26, 21, 13]
    
    # Arguments  for motor run function
    # (GPIOPins, stepdelay, steps, counterclockwise, verbose, steptype, initdelay)
    input("Press <Enter> to continue Test1")
    mymotortest.motor_run(GpioPins,.5, 20, False, True,"full" ,1 )
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
    mymotortest.motor_run(GpioPins,.02,25,False,False,"half", 3)


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
