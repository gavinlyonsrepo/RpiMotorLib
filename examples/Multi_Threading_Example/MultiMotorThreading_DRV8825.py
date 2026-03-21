#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : A4988Nema
Tested : Two DRV8825 Nema stepper motors running simultaneously via threading

Pinout used:
    Motor 1: DIRECTION-GPIO 23, STEP-GPIO 24, M0-GPIO 25, M1-GPIO 16, M2-GPIO 20
    Motor 2: DIRECTION-GPIO 19, STEP-GPIO 13, M0-GPIO 26, M1-GPIO 27, M2-GPIO 22
    Note: pass (-1,-1,-1) for mode pins to hardwire MS resolution and save GPIO pins.

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import concurrent.futures
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Motor 1 GPIO pins
GPIO_PINS_1 = (25, 16, 20)  # Microstep Resolution M0-M1-M2
DIRECTION_1 = 23            # Direction -> GPIO pin
STEP_1 = 24                 # Step -> GPIO pin

# Motor 2 GPIO pins
GPIO_PINS_2 = (26, 27, 22)  # Microstep Resolution M0-M1-M2
DIRECTION_2 = 19            # Direction -> GPIO pin
STEP_2 = 13                 # Step -> GPIO pin

# Declare two named instances of class
mymotortest_one = RpiMotorLib.A4988Nema(DIRECTION_1, STEP_1, GPIO_PINS_1, "DRV8825")
mymotortest_two = RpiMotorLib.A4988Nema(DIRECTION_2, STEP_2, GPIO_PINS_2, "DRV8825")


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
    # motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        _f1 = executor.submit(mymotortest_one.motor_go,
                             True, "Full", 800, .005, False, .05)
        _f2 = executor.submit(mymotortest_two.motor_go,
                             False, "Full", 1600, .005, False, .05)

    estop.cleanup()


# ===================== MAIN ===============================

if __name__ == '__main__':
    print("START")
    main()
    print("END")
    sys.exit()

# ===================== END ===============================
