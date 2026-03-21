#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : rpiservolib.py
Class  : SG90servo
Tested : Servo controlled by GPIO PWM

Emergency stop wire a push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.(this is optional)
"""

import sys
import time
from RpiMotorLib import rpiservolib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Initialize servo (name, freq, y_one, y_two)
myservotest = rpiservolib.SG90servo("servoone", 50, 3, 11)
# Initialize emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17,\
stop_callable=myservotest.servo_stop, bouncetime=200, verbose=True)

def main():
    """main function loop"""

    # Arm emergency stop before tests
    estop.enable()

    # == Test 1: servo_move_step ==
    # (servo_pin, start, end, stepdelay, stepsize, initdelay, verbose)
    print("Test 1: test method servo_move_step")
    input("Press <Enter> to continue Test 1a")
    myservotest.servo_move_step(26, 10, 180, .1, 5, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test 1b")
    myservotest.servo_move_step(26, 170, 10, .5, 20, 1, True)
    time.sleep(1)
    input("Press <Enter> to continue Test 1c")
    myservotest.servo_move_step(26, 10, 50, 1, 1, 1, True)
    time.sleep(1)

    # == Test 2: convert degree to duty cycle ==
    print("Test 2: test method convert_from_degree")
    input("Press <Enter> to continue Test 2")
    testdegree = float(input("What degree do you want?\t"))
    print(f"duty cycle percent = {myservotest.convert_from_degree(testdegree)}")

    # == Test 3: servo_sweep ==
    # (servo_pin, center, minduty, maxduty, delay, verbose, initdelay, sweeplen)
    print("Test 3: test method servo_sweep")
    input("Press <Enter> to continue Test 3a")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 3, 11, .5, True, .05, 10)
    input("Press <Enter> to continue Test 3b")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 11, .5, True, 2, 20)
    input("Press <Enter> to continue Test 3c")
    time.sleep(1)
    myservotest.servo_sweep(26, 7.5, 7.5, 3, .5, True, .05)

    # == Test 4: servo_move ==
    # (servo_pin, position, delay, verbose, initdelay)
    print("Test 4: test method servo_move")
    input("Press <Enter> to continue Test 4a")
    time.sleep(1)
    myservotest.servo_move(26, 12, .5, True, 0)
    input("Press <Enter> to continue Test 4b")
    time.sleep(1)
    myservotest.servo_move(26, 2, .5, True, 0)
    input("Press <Enter> to continue Test 4c")
    time.sleep(1)
    myservotest.servo_move(26, 7.5, .5, True, 0)
    time.sleep(1)

    # Disarm emergency stop after tests
    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    main()
    sys.exit()

# ===================== END ===============================
