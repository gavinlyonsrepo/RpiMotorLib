#!/usr/bin/env python3
"""A python 3 library for various
 motors and servos to connect to a raspberry pi"""
# ========================= HEADER ===================================
# title             :rpiMotorlib.py
# description       :A python 3 library for various motors
# and servos to connect to a raspberry pi
# This file is for stepper motor tested on
# 28BYJ-48 unipolar stepper motor with ULN2003  = BYJMotor class
# Bipolar Nema stepper motor with L298N = BYJMotor class.
# Bipolar Nema Stepper motor TB6612FNG = BYJMotor class
# Bipolar Nema Stepper motor A4988  Driver = A4988Nema class
# Bipolar Nema Stepper motor DRV8825 Driver = A4988Nema class
# Bipolar Nema Stepper motor A3967 Easy Driver = A3967EasyNema class
# Main author       :Gavin Lyons
# Version           :See changelog at url
# url               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.5.3

# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import sys
import time
import RPi.GPIO as GPIO

# ==================== CLASS SECTION ===============================

class StopMotorInterrupt(Exception):
    """ Stop the motor """
    pass

class BYJMotor(object):
    """class to control a 28BYJ-48 stepper motor with ULN2003 controller
    by a raspberry pi"""
    def __init__(self, name="BYJMotorX", motor_type="28BYJ"):
        self.name = name
        self.motor_type = motor_type
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.curser_spin = ["/", "-", "|", "\\", "|"]
        self.spin_position = 0
        self.stop_motor = False

    def print_cursor_spin(self):
        """ Prints a spinning cursor. Used when verbose not set to false.
        NOTE: deprecated version 2.2-3 left in code for reference """
        # print(self.curser_spin[self.spin_position], end="\r", flush=True)
        self.spin_position += 1
        if self.spin_position > 4:
            self.spin_position = 0

    def motor_stop(self):
        """ Stop the motor """
        self.stop_motor = True

    def motor_run(self, gpiopins, wait=.001, steps=512, ccwise=False,
                  verbose=False, steptype="half", initdelay=.001):
        """motor_run,  moves stepper motor based on 7 inputs

         (1) GPIOPins, type=list of ints 4 long, help="list of
         4 GPIO pins to connect to motor controller
         These are the four GPIO pins we will
         use to drive the stepper motor, in the order
         they are plugged into the controller board. So,
         GPIO 18 is plugged into Pin 1 on the stepper motor.
         (2) wait, type=float, default=0.001, help=Time to wait
         (in seconds) between steps.
         (3) steps, type=int, default=512, help=Number of steps sequence's
         to execute. Default is one revolution , 512 (for a 28BYJ-48)
         (4) counterclockwise, type=bool default=False
         help="Turn stepper counterclockwise"
         (5) verbose, type=bool  type=bool default=False
         help="Write pin actions",
         (6) steptype, type=string , default=half help= type of drive to
         step motor 3 options full step half step or wave drive
         where full = fullstep , half = half step , wave = wave drive.
         (7) initdelay, type=float, default=1mS, help= Intial delay after
         GPIO pins initialized but before motor is moved.

        """
        try:
            self.stop_motor = False
            for pin in gpiopins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, False)
            time.sleep(initdelay)

            # select step based on user input
            # Each step_sequence is a list containing GPIO pins that should be set to High
            if steptype == "half":  # half stepping.
                step_sequence = list(range(0, 8))
                step_sequence[0] = [gpiopins[0]]
                step_sequence[1] = [gpiopins[0], gpiopins[1]]
                step_sequence[2] = [gpiopins[1]]
                step_sequence[3] = [gpiopins[1], gpiopins[2]]
                step_sequence[4] = [gpiopins[2]]
                step_sequence[5] = [gpiopins[2], gpiopins[3]]
                step_sequence[6] = [gpiopins[3]]
                step_sequence[7] = [gpiopins[3], gpiopins[0]]
            elif steptype == "full":  # full stepping.
                step_sequence = list(range(0, 4))
                step_sequence[0] = [gpiopins[0], gpiopins[1]]
                step_sequence[1] = [gpiopins[1], gpiopins[2]]
                step_sequence[2] = [gpiopins[2], gpiopins[3]]
                step_sequence[3] = [gpiopins[0], gpiopins[3]]
            elif steptype == "wave":  # wave driving
                step_sequence = list(range(0, 4))
                step_sequence[0] = [gpiopins[0]]
                step_sequence[1] = [gpiopins[1]]
                step_sequence[2] = [gpiopins[2]]
                step_sequence[3] = [gpiopins[3]]
            else:
                print("Error: unknown step type ; half, full or wave")
                quit()

            #  To run motor in reverse we flip the sequence order.
            if ccwise:
                step_sequence.reverse()

            def display_degree():
                """ display the degree value at end of run if verbose"""
                if self.motor_type == "28BYJ":
                    degree = 1.422222
                    print("Size of turn in degrees = {}".format(round(steps/degree, 2)))
                elif self.motor_type == "Nema":
                    degree = 7.2
                    print("Size of turn in degrees = {}".format(round(steps*degree, 2)))
                else:
                    # Unknown Motor type
                    print("Size of turn in degrees = N/A Motor: {}".format(self.motor_type))

            def print_status(enabled_pins):
                """   Print status of pins."""
                if verbose:
                    print("Next Step: Step sequence remaining : {} ".format(steps_remaining))
                    for pin_print in gpiopins:
                        if pin_print in enabled_pins:
                            print("GPIO pin on {}".format(pin_print))
                        else:
                            print("GPIO pin off {}".format(pin_print))
                else:
                    self.print_cursor_spin()

            # Iterate through the pins turning them on and off.
            steps_remaining = steps
            while steps_remaining > 0:
                for pin_list in step_sequence:
                    for pin in gpiopins:
                        if self.stop_motor:
                            raise StopMotorInterrupt
                        else:
                            if pin in pin_list:
                                GPIO.output(pin, True)
                            else:
                                GPIO.output(pin, False)
                    print_status(pin_list)
                    time.sleep(wait)
                steps_remaining -= 1

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib: ")
        except StopMotorInterrupt:
            print("Stop Motor Interrupt : RpiMotorLib: ")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")
        else:
            # print report status if everything went well
            if verbose:
                print("\nRpiMotorLib, Motor Run finished, Details:.\n")
                print("Motor type = {}".format(self.motor_type))
                print("Initial delay = {}".format(initdelay))
                print("GPIO pins = {}".format(gpiopins))
                print("Wait time = {}".format(wait))
                print("Number of step sequences = {}".format(steps))
                print("Size of step sequence = {}".format(len(step_sequence)))
                print("Number of steps = {}".format(steps*len(step_sequence)))
                display_degree()
                print("Counter clockwise = {}".format(ccwise))
                print("Verbose  = {}".format(verbose))
                print("Steptype = {}".format(steptype))
        finally:
            # switch off pins at end
            for pin in gpiopins:
                GPIO.output(pin, False)



class A4988Nema(object):
    """ Class to control a Nema bi-polar stepper motor with a A4988 also tested with DRV8825"""
    def __init__(self, direction_pin, step_pin, mode_pins, motor_type="A4988"):
        """ class init method 3 inputs
        (1) direction type=int , help=GPIO pin connected to DIR pin of IC
        (2) step_pin type=int , help=GPIO pin connected to STEP of IC
        (3) mode_pins type=tuple of 3 ints, help=GPIO pins connected to
        Microstep Resolution pins MS1-MS3 of IC
        (4) motor_type type=string, help=Type of motor two options: A4988 or DRV8825
        """
        self.motor_type = motor_type
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.mode_pins = mode_pins
        self.stop_motor = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def motor_stop(self):
        """ Stop the motor """
        self.stop_motor = True

    def resolution_set(self, steptype):
        """ method to calculate step resolution
        based on motor type and steptype"""
        if self.motor_type == "A4988":
            resolution = {'Full': (0, 0, 0),
                          'Half': (1, 0, 0),
                          '1/4': (0, 1, 0),
                          '1/8': (1, 1, 0),
                          '1/16': (1, 1, 1)}
        elif self.motor_type == "DRV8825":
            resolution = {'Full': (0, 0, 0),
                          'Half': (1, 0, 0),
                          '1/4': (0, 1, 0),
                          '1/8': (1, 1, 0),
                          '1/16': (0, 0, 1),
                          '1/32': (1, 0, 1)}
        else:
            print("Error invalid motor_type: {}".format(self.motor_type))
            quit()

        # error check stepmode
        if steptype in resolution:
            pass
        else:
            print("Error invalid steptype: {}".format(steptype))
            quit()

        GPIO.output(self.mode_pins, resolution[steptype])

    def motor_go(self, clockwise=False, steptype="Full",
                 steps=200, stepdelay=.005, verbose=False, initdelay=.05):
        """ motor_go,  moves stepper motor based on 6 inputs

         (1) clockwise, type=bool default=False
         help="Turn stepper counterclockwise"
         (2) steptype, type=string , default=Full help= type of drive to
         step motor 5 options
            (Full, Half, 1/4, 1/8, 1/16) 1/32 for DRV8825 only
         (3) steps, type=int, default=200, help=Number of steps sequence's
         to execute. Default is one revolution , 200 in Full mode.
         (4) stepdelay, type=float, default=0.05, help=Time to wait
         (in seconds) between steps.
         (5) verbose, type=bool  type=bool default=False
         help="Write pin actions",
         (6) initdelay, type=float, default=1mS, help= Intial delay after
         GPIO pins initialized but before motor is moved.

        """
        self.stop_motor = False
        # setup GPIO
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.output(self.direction_pin, clockwise)
        GPIO.setup(self.mode_pins, GPIO.OUT)
        try:
            # dict resolution
            self.resolution_set(steptype)
            time.sleep(initdelay)

            for i in range(steps):
                if self.stop_motor:
                    raise StopMotorInterrupt
                else:
                    GPIO.output(self.step_pin, True)
                    time.sleep(stepdelay)
                    GPIO.output(self.step_pin, False)
                    time.sleep(stepdelay)
                    if verbose:
                        print("Steps count {}".format(i+1), end="\r", flush=True)

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib:")
        except StopMotorInterrupt:
            print("Stop Motor Interrupt : RpiMotorLib: ")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")
        else:
            # print report status
            if verbose:
                print("\nRpiMotorLib, Motor Run finished, Details:.\n")
                print("Motor type = {}".format(self.motor_type))
                print("Clockwise = {}".format(clockwise))
                print("Step Type = {}".format(steptype))
                print("Number of steps = {}".format(steps))
                print("Step Delay = {}".format(stepdelay))
                print("Intial delay = {}".format(initdelay))
                print("Size of turn in degrees = {}"
                      .format(degree_calc(steps, steptype)))
        finally:
            # cleanup
            GPIO.output(self.step_pin, False)
            GPIO.output(self.direction_pin, False)
            for pin in self.mode_pins:
                GPIO.output(pin, False)


class A3967EasyNema(object):
    """ Class to control a Nema bi-polar stepper motor with A3967 Easy driver
    motor controller """

    def __init__(self, direction_pin, step_pin, mode_pins):
        """ class init method 3 inputs
        (1) direction type=int , help=GPIO pin connected to DIR pin of IC
        (2) step_pin type=int , help=GPIO pin connected to STEP of IC
        (3) mode_pins type=tuple of 2 ints, help=GPIO pins connected to
        Microstep Resolution pins MS1-MS2 of IC"""

        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.mode_pins = mode_pins
        self.stop_motor = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def motor_stop(self):
        """ Stop the motor """
        self.stop_motor = True

    def motor_move(self, stepdelay=.05, steps=200, clockwise=False,
                   verbose=False, steptype="Full", initdelay=.1):
        """ motor_move,  moves stepper motor based on 6 inputs
         (1) stepdelay type=float, default=0.05, help=Time to wait
         (in seconds) between steps.
         (2) steps, type=int, default=200, help=Number of steps sequence's
         to execute. Default is 200 ,
         (3) clockwise, type=bool default=False
         help="Turn stepper counterclockwise"
         (4) verbose, type=bool  type=bool default=False
         help="Write pin actions",
         (5) steptype, type=string , default=Full help= type of drive to
         step motor 4 options
            (Full, Half, 1/4, 1/8)
         (6) initdelay, type=float, default=1mS, help= Intial delay after
         GPIO pins initialized but before motor is moved.
        """

        def ms_steps_pins():
            """ Method to handle MS pins setup """
            # dict resolution
            resolution = {'Full': (0, 0),
                          'Half': (1, 0),
                          '1/4': (0, 1),
                          '1/8': (1, 1)}
            # error check stepmode input
            if steptype in resolution:
                pass
            else:
                print("Error invalid steptype: {}".format(steptype))
                quit()

            GPIO.output(self.mode_pins, resolution[steptype])

        # setup GPIO
        self.stop_motor = False
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.output(self.direction_pin, clockwise)
        GPIO.setup(self.mode_pins, GPIO.OUT)

        ms_steps_pins()
        time.sleep(initdelay)

        try:
            for i in range(steps):
                if self.stop_motor:
                    raise StopMotorInterrupt
                else:
                    GPIO.output(self.step_pin, False)
                    time.sleep(stepdelay)
                    GPIO.output(self.step_pin, True)
                    time.sleep(stepdelay)
                    if verbose:
                        print("Steps count {}".format(i+1), end="\r", flush=True)

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib:")
        except StopMotorInterrupt:
            print("Stop Motor Interrupt : RpiMotorLib: ")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")
        else:
            # print report status
            if verbose:
                print("\nRpiMotorLib, Motor Run finished, Details:.\n")
                print("Clockwise = {}".format(clockwise))
                print("Step Type = {}".format(steptype))
                print("Number of steps = {}".format(steps))
                print("Step Delay = {}".format(stepdelay))
                print("Intial delay = {}".format(initdelay))
                print("Size of turn in degrees = {}"
                      .format(degree_calc(steps, steptype)))
        finally:
            # cleanup
            GPIO.output(self.step_pin, False)
            GPIO.output(self.direction_pin, False)
            for pin in self.mode_pins:
                GPIO.output(pin, False)


def degree_calc(steps, steptype):
    """ calculate and returns size of turn in degree
    , passed number of steps and steptype"""
    degree_value = {'Full': 1.8,
                    'Half': 0.9,
                    '1/4': .45,
                    '1/8': .225,
                    '1/16': 0.1125,
                    '1/32': 0.05625}
    degree_value = (steps*degree_value[steptype])
    return degree_value


def importtest(text):
    """ testing import """
    # print(text)
    text = " "

# ===================== MAIN ===============================


if __name__ == '__main__':
    importtest("main")
else:
    importtest("Imported {}".format(__name__))


# ===================== END ===============================
