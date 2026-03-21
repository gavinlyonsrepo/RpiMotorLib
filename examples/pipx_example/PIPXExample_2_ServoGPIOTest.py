#!/home/gavin/.local/pipx/venvs/rpimotorlib/bin/python
"""
Example file for RpiMotorLib - pipx install method 2
Module : rpiservolib.py
Class  : SG90servo

This example shows how to import RpiMotorLib when installed via pipx
using a pipx-specific shebang line instead of sys.path.insert.
Adjust the shebang line above to match your machine and Python version.
See README for more details on pipx installation.

Note: shebang format is:
#!/home/<username>/.local/pipx/venvs/rpimotorlib/bin/python

Alternatively use the generic shebang:
#!/usr/bin/env python3
and run with: pipx run rpimotorlib (if supported) or activate the venv first.
"""

import sys
import time
from RpiMotorLib import rpiservolib


def main():
    """main function loop"""
    # Initialize (name, freq, y_one, y_two)
    myservotest = rpiservolib.SG90servo("servoone", 50, 3, 11)

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
