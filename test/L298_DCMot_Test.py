#!/usr/bin/env python3
""" test example file for rpiMotorlib.py L298 dc motor"""

import time 
import RPi.GPIO as GPIO

"""
# Next 3 lines for development local library path testing import
# Comment out in production release and change rpi_dc_lib.L298NMDc to L298NMDc 
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from rpi_dc_lib import L298NMDc
"""

# Production installed library import 
from RpiMotorLib import rpi_dc_lib 

# ====== tests for  DC motor L298 ====
# ena - - 26
# in1 - - 19
# in2 - - 13
# in3 - - 21
# in4 - - 20
# enB - - 16

# ======== test motor 1 ==================

def motorone():
    
    print(" TEST: testing motor 1") 
    # Motorssetup
    MotorOne = rpi_dc_lib.L298NMDc(19 ,13 ,26 ,50 ,True, "motor_one")

    # ================ Motors one test  section 1=============
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
        MotorOne.brake(0)
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
    # Motorssetup
    MotorTwo = rpi_dc_lib.L298NMDc(21 ,20 ,16 ,50 ,True, "motor_two")

    # ================ Motors two test  section 1=============
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
        
         
        print("5 .brake check")
        MotorTwo.forward(50)
        time.sleep(3)
        MotorTwo.brake(0)
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
