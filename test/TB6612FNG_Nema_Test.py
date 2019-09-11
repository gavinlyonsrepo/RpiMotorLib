#!/usr/bin/env python3
""" test example file for rpiMotorlib.py TB6612FNG stepper tests"""

import time 
import RPi.GPIO as GPIO
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
#from RpiMotorLib import BYJMotor

from RpiMotorLib import RpiMotorLib


def main():
    """main function loop"""

    
    # ====== tests for motor TB6612FNG StepTest ====

    Motorname = "MyMotorOne" 
    Motortype = "Nema"
    # GPIO
    A11 = 19
    A12 = 26
    B11 = 21
    B12 = 13 
    GpioPins = [A11, B11, A12,B12]
    # Declare an named instance of class pass a name and type of motor
    mymotortest = RpiMotorLib.BYJMotor(Motorname, Motortype)
    time.sleep(1)
    input("Press <Enter> to continue Test1")
    
    # Test One
    wait = 0.5
    steps = 50 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "full"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    time.sleep(1)
    input("Press <Enter> to continue  Test2")
    
    
    # Test Two
    wait = 0.1
    steps = 25 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "full"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    time.sleep(1)
    input("Press <Enter> to continue  Test3")
    
    # Test Three
    wait = 0.2
    steps = 25 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "half"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test4")
    
    # Test 4
    wait = 0.05
    steps = 50 # No of step sequences
    ccwise = True
    verbose= True
    steptype = "half"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test5")
    
    # Test 5
    wait = 0.02
    steps = 25 # No of step sequences
    ccwise = False
    verbose= False
    steptype = "wave"
    initdelay = 5
    mymotortest.motor_run(GpioPins, wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test6")
    
    # Test 6
    wait = 0.02
    steps = 10 # No of step sequences
    ccwise = True
    verbose= True
    steptype = "wave"
    initdelay = 1
    mymotortest.motor_run(GpioPins, wait ,steps ,ccwise ,verbose, steptype ,initdelay)
# ===================MAIN===============================

if __name__ == '__main__':
   
    print("START")
    main()
    GPIO.cleanup()
    exit()
    
    

# =====================END===============================
