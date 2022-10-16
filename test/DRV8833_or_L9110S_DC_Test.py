#!/usr/bin/env python3
""" test example file for rpiMotorlib.py 
testfile for  DC motor run by DRV8833 or L9110s test"""

import time 
import RPi.GPIO as GPIO

"""
# Next 3 lines for development local library path testing import
# Comment out in production release and change rpi_dc_lib.DRV8833NmDc to DRV8833NmDc
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from rpi_dc_lib import DRV8833NmDc
"""

# Production installed library import 
from RpiMotorLib import rpi_dc_lib 

# ====== tests L9110S -DRV8833   ====

# my pin-outs L9110S -DRV8833
# in1 A-1B - brown = 26
# in2 A-1A - blue = 19

# in3 B-1B - green = 13
# in4 B-1A - black = 21

# L9110S B output dir A output PWM


def motorone():
    
    print(" TEST: testing motor 1") 
    # Motors setup
    MotorOne = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,True, "motor_one")

    # ================ Motors one test  section =============
    try:
        print("1. motor forward")
        MotorOne.forward(15)
        input("press key to stop") 
        print("motor stop\n")
        MotorOne.stop(0)
        time.sleep(3)

        print("2. motor forward speed up")
        for i in range(15,30):
            MotorOne.forward(i)
            time.sleep(1)
        MotorOne.stop(0)
        print("motor stoped\n")
        time.sleep(3)
        
        print("3. motor backward")
        MotorOne.backward(15)
        input("press key to stop") 
        MotorOne.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("4. motor backward speed up")
        for i in range(15,30):
            MotorOne.backward(i)
            time.sleep(1)
        MotorOne.stop(0)
        print("motor stopped\n")
        time.sleep(3)
      
      
        print("5  brake check")
        MotorOne.forward(50)
        time.sleep(3)
        MotorOne.brake(100)
        print("motor brake\n")
        
    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorOne.cleanup(False)

    
def motortwo():
      
    print(" TEST: testing motor ") 
    # Motors setup
    MotorTwo = rpi_dc_lib.DRV8833NmDc(13 ,21 ,50 ,True, "motor_two")

    # ================ Motors two test section =============
    try:
        print("1. motor forward")
        MotorTwo.forward(15)
        input("press key to stop") 
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)
       

        print("2. motor forward speed up")
        for i in range(15,30):
            MotorTwo.forward(i)
            time.sleep(1)
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)  
          
        
        print("3. motor backward")
        MotorTwo.backward(15)
        input("press key to stop") 
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)
        

        print("4. motor backward speed up")
        for i in range(15,30):
            MotorTwo.backward(i)
            time.sleep(1)
        MotorTwo.stop(0)
        print("motor stop\n")
        time.sleep(3)
        
        print("5  brake check")
        MotorTwo.forward(50)
        time.sleep(3)
        MotorTwo.brake(100)
        print("motor brake\n")
        
    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorTwo.cleanup(False)
    
# ===================MAIN===============================

if __name__ == '__main__':
   
    print("START")
    print("motorone tests")
    motorone()
    time.sleep(3)
    print("motortwo tests")
    motortwo()
    exit()
    
    

# =====================END===============================
