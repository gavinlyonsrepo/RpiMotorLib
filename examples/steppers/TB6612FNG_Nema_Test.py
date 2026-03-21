#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : BYJMotor
Tested : TB6612FNG controller bipolar stepper motor

Pinout used:
    ain1 - GPIO 19
    ain2 - GPIO 26
    bin1 - GPIO 21
    bin2 - GPIO 13

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.

"""

import sys
import time
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Declare an named instance of class pass a name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=mymotortest.motor_stop, verbose=True)

def main():
    # pylint: disable=too-many-statements
    """main function loop tests for motor TB6612FNG StepTest"""
    estop.enable()
    # GPIO
    ain1 = 19
    ain2 = 26
    bin1 = 21
    bin2 = 13
    gpio_pins = [ain1, bin1, ain2, bin2]

    time.sleep(1)
    input("Press <Enter> to continue Test1")

    # Test One
    wait = 0.5
    steps = 50 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "full"
    initdelay = 1
    mymotortest.motor_run(gpio_pins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    time.sleep(1)
    input("Press <Enter> to continue  Test2")

    # Test Two
    wait = 0.1
    steps = 25 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "full"
    initdelay = 1
    mymotortest.motor_run(gpio_pins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    time.sleep(1)
    input("Press <Enter> to continue  Test3")

    # Test Three
    wait = 0.2
    steps = 25 # No of step sequences
    ccwise = False
    verbose= True
    steptype = "half"
    initdelay = 1
    mymotortest.motor_run(gpio_pins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test4")

    # Test 4
    wait = 0.05
    steps = 50 # No of step sequences
    ccwise = True
    verbose= True
    steptype = "half"
    initdelay = 1
    mymotortest.motor_run(gpio_pins, wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test5")

    # Test 5
    wait = 0.02
    steps = 25 # No of step sequences
    ccwise = False
    verbose= False
    steptype = "wave"
    initdelay = 5
    mymotortest.motor_run(gpio_pins, wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    input("Press <Enter> to continue  Test6")

    # Test 6
    wait = 0.02
    steps = 10 # No of step sequences
    ccwise = True
    verbose= True
    steptype = "wave"
    initdelay = 1
    mymotortest.motor_run(gpio_pins, wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    estop.cleanup()


# ===================MAIN===============================
if __name__ == '__main__':

    print("START")
    main()
    sys.exit()
# =====================END===============================
