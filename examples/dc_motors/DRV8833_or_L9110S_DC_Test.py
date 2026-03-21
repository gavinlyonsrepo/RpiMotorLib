#!/usr/bin/env python3
"""
test example file for rpiMotorlib
testfile for  DC motor run by DRV8833 or L9110s test

# ====== tests L9110S -DRV8833   ====

my pin-outs L9110S -DRV8833
in1 A-1B - brown = 26
in2 A-1A - blue = 19

in3 B-1B - green = 13
in4 B-1A - black = 21

for L9110S B output = dir , A output = PWM

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.

"""

import sys
import time
from RpiMotorLib import rpi_dc_lib
from RpiMotorLib.rpi_emergency_stop import EmergencyStop

# Motors setup
motor_one = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,True, "motor_one")
motor_two = rpi_dc_lib.DRV8833NmDc(13 ,21 ,50 ,True, "motor_two")

def stop_all():
    """Stop both motors — used as emergency stop callable."""
    motor_one.motor_stop()
    motor_two.motor_stop()

# Emergency stop on GPIO 17
estop = EmergencyStop(gpio_pin=17, stop_callable=stop_all, verbose=True)

def motorone():
    """ Run motor 1 DC tests """
    print(" TEST: testing motor 1")
    # ================ Motors one test  section =============
    try:
        print("1. motor forward")
        motor_one.stop_motor = False
        motor_one.forward(15)
        input("press enter key to stop")
        print("motor stop\n")
        motor_one.stop(0)
        time.sleep(3)

        print("2. motor forward speed up")
        motor_one.stop_motor = False
        for i in range(15,30):
            if motor_one.stop_motor:
                break
            motor_one.forward(i)
            time.sleep(1)
        motor_one.stop(0)
        print("motor stoped\n")
        time.sleep(3)

        print("3. motor backward")
        motor_one.stop_motor = False
        motor_one.backward(15)
        input("press enter key to stop")
        motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("4. motor backward speed up")
        motor_one.stop_motor = False
        for i in range(15,30):
            if motor_one.stop_motor:
                break
            motor_one.backward(i)
            time.sleep(1)
        motor_one.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("5  brake check")
        motor_one.forward(50)
        time.sleep(3)
        motor_one.brake(100)
        print("motor brake\n")

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    except Exception as error: # pylint: disable=broad-except
        print(error)
        print("Unexpected error:")
    finally:
        motor_one.cleanup(False)


def motortwo():
    """ Run motor 2 DC tests """
    print(" TEST: testing motor 2")
    # ================ Motors two test section =============
    try:
        print("1. motor forward")
        motor_two.stop_motor = False
        motor_two.forward(15)
        input("press enter key to stop")
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("2. motor forward speed up")
        motor_two.stop_motor = False
        for i in range(15,30):
            if motor_two.stop_motor:
                break
            motor_two.forward(i)
            time.sleep(1)
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("3. motor backward")
        motor_two.stop_motor = False
        motor_two.backward(15)
        input("press enter key to stop")
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("4. motor backward speed up")
        motor_two.stop_motor = False
        for i in range(15,30):
            if motor_two.stop_motor:
                break
            motor_two.backward(i)
            time.sleep(1)
        motor_two.stop(0)
        print("motor stop\n")
        time.sleep(3)

        print("5  brake check")
        motor_two.stop_motor = False
        motor_two.forward(50)
        time.sleep(3)
        motor_two.brake(100)
        print("motor brake\n")

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    except Exception as error: # pylint: disable=broad-except
        print(error)
        print("Unexpected error:")
    finally:
        motor_two.cleanup(False)

# ===================MAIN===============================
if __name__ == '__main__':

    print("START")
    estop.enable()
    motorone()
    time.sleep(3)
    motortwo()
    estop.cleanup()
    sys.exit()
# =====================END===============================
