#!/usr/bin/env python3
""" test example file for: module rpiMotorlib.py
file: rpi_pservo_lib class:ServoPigpio,
Run a servo using pigpio library RPI

NOTE: pigpio does NOT support Raspberry Pi 5.
This example is for Pi 1/2/3/4 only.
Make sure to start the pigpio daemon before running:
    sudo pigpiod
    
Emergency stop wire a push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.(this is optional)
"""

import time
import sys
# Production installed library import
from RpiMotorLib import rpi_pservo_lib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop
# initialize(name freq, y_one, y_two)
myservotest  = rpi_pservo_lib.ServoPigpio("servoone", 50, 1000, 2000 )
# Initialize emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17,\
stop_callable=myservotest.servo_stop, bouncetime=200, verbose=True)

def main():
    """main function loop"""

    # Arm emergency stop before tests
    estop.enable()

    # ===== Tests for servo  ==========

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
    print(f"Pulse width micro seconds = {myservotest.convert_from_degree(testdegree)}")


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
    # Disarm emergency stop after tests
    estop.cleanup()



# ===================MAIN===============================

if __name__ == '__main__':

    main()
    sys.exit()


# =====================END===============================
