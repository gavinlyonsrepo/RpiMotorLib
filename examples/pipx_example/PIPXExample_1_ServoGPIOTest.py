#!/usr/bin/python3
"""
Example file for RpiMotorLib - pipx install method 1
Module : rpiservolib.py
Class  : SG90servo

This example shows how to import RpiMotorLib when installed via pipx
using sys.path.insert. Adjust the path below to match your machine.
See README for more details on pipx installation.

Note: path format is:
/home/<username>/.local/pipx/venvs/rpimotorlib/lib/python<version>/site-packages/
"""

import sys
import time

# Adjust this path to match your machine and Python version
sys.path.insert(0, '/home/gavin/.local/pipx/venvs/rpimotorlib/lib/python3.11/site-packages/') # pylint: disable=line-too-long

from RpiMotorLib.rpiservolib import SG90servo  # pylint: disable=import-error,wrong-import-position

def main():
    """main function loop"""
    # Initialize (name, freq, y_one, y_two)
    myservotest = SG90servo("servoone", 50, 3, 11)

    # Test 1 — servo_move_step
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


# ===================== MAIN ===============================

if __name__ == '__main__':
    main()
    sys.exit()

# ===================== END ===============================
