#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : BYJMotor
Tested : L298 controller bipolar stepper motor

Pinout used:
    IN1 - GPIO 19
    IN2 - GPIO 26
    IN3 - GPIO 21
    IN4 - GPIO 13

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Declare an named instance of class pass a name and type of motor
# type of motor(Nema) is case sensitive
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")

# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=mymotortest.motor_stop, verbose=True)

def main():
    """main function loop"""
    estop.enable()
    # ====== tests for motor L298STepTest ====
    # Connect GPIO to [IN1 , IN2 , IN3 ,IN4] on Motor PCB
    gpio_pins= [19, 26, 21, 13]

    #Arguments  for motor run function
    #(GPIOPins, stepdelay, steps, counterclockwise, verbose, steptype, initdelay)
    input("Press <Enter> to continue Test1")
    mymotortest.motor_run(gpio_pins,.5, 20, False, True,"full" ,1 )
    time.sleep(1)
    input("Press <Enter> to continue  Test2")
    mymotortest.motor_run(gpio_pins,.1, 20 , False, True,"wave", 1)
    time.sleep(1)
    input("Press <Enter> to continue  Test3")
    mymotortest.motor_run(gpio_pins,.2, 10, False, True,"full", 1)
    time.sleep(1)
    input("Press <Enter> to continue  Test4")
    mymotortest.motor_run(gpio_pins,.05, 25, True, True,"half", 1)
    time.sleep(1)
    input("Press <Enter> to continue  Test5")
    mymotortest.motor_run(gpio_pins,.02,25,False,False,"half", 3)

    estop.cleanup()

# ===================MAIN===============================

if __name__ == '__main__':

    print("START")
    main()
    sys.exit()
# =====================END===============================
