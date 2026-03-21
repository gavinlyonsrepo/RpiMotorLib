#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : BYJMotor
Tested : Two 28BYJ-48 stepper motors running simultaneously via threading

Pinout used:
    Motor 1: IN1-GPIO 18, IN2-GPIO 23, IN3-GPIO 24, IN4-GPIO 25
    Motor 2: IN1-GPIO 6,  IN2-GPIO 13, IN3-GPIO 19, IN4-GPIO 26

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import concurrent.futures
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# GPIO pins
GPIO_PINS_1 = [18, 23, 24, 25]
GPIO_PINS_2 = [6, 13, 19, 26]

# Declare two named instances of class
mymotortest_one = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
mymotortest_two = RpiMotorLib.BYJMotor("MyMotorTwo", "28BYJ")


def stop_all():
    """Stop both motors — used as emergency stop callable."""
    mymotortest_one.motor_stop()
    mymotortest_two.motor_stop()


# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=stop_all, verbose=True)


def main():
    """main function loop"""
    estop.enable()

    # Run two motors simultaneously using threading
    # motor_run(GPIOPins, stepdelay, steps, ccwise, verbose, steptype, initdelay)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        _f1 = executor.submit(mymotortest_one.motor_run,
                             GPIO_PINS_1, .05, 128, False, False, "half", .05)
        _f2 = executor.submit(mymotortest_two.motor_run,
                             GPIO_PINS_2, .05, 128, False, False, "half", .05)

    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("START")
    main()
    print("END")
    sys.exit()

# ===================== END ===============================
