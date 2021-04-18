#!/usr/bin/env python3
"""
# ========================= HEADER ===================================
# title             :rpiservolib.py
# description       :Part of a RpiMotorLib python 3 library for motors
# and servos to connect to a raspberry pi
# This file is for servos controlled by GPIO PWM
# author            :Gavin Lyons
# web               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.4.2
"""
# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import sys
import time
import RPi.GPIO as GPIO

# ==================== CLASS SECTION ===============================

class StopServoInterrupt(Exception):
    """ Stop the servo """
    pass


class SG90servo(object):
    """class to control a servo with GPIO PWM by raspberry pi"""

    def __init__(self, name="SG90servoX", freq=50, y_one=2, y_two=12):
        """ init method for class
        4 inputs
        (1) name, default=SG90servoX, type=string, help=name of instance
        (2) Freq, type=int, default=50,  help=control freq of servo in Hz
        (3) y_one, type=float, default = 2 ,help=pulse min duty cycle of servo % for 0 degrees
        (4) y_two type=float, default = 12, help=pulse max duty cycle of servo % for 180 degrees
          """
        self.name = name
        self.freq = freq
        self.y_one = y_one
        self.y_two = y_two
        self.stop_servo = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def servo_stop(self):
        """ Stop the servo """
        self.stop_servo = True

    def servo_sweep(self, servo_pin=7, center=7.5, minduty=3,
                    maxduty=11, delay=0.5, verbose=False, initdelay=.05, sweeplen=1000000):
        """servo_sweep 8 inputs, moves servo in sweep loop

         (1) servo_pin, type=int help=GPIO pin
         we will contect to signal line of servo
         (2) center, type=float, default=7.5,
         help=The center dutycycle position of servo
         (3) minduty, type=float, default=3,
         help=The min dutycycle position of servo
         (4) maxduty, type=float, default=11,
         help=The max dutycycle position of servo
         (5) delay, type=float, default=0.5,
         help=Time to wait (in seconds) between steps.
         (6) verbose, type=bool  type=bool default=False
          help="Output actions & details",
         (7) initdelay, type=float, default 50mS
         help= A delay after Gpio setup and before servo moves
         (8)  sweeplen, type=integer , default one million
         help=  is number of times to execute sweep.
        """
        if verbose:
            print("RpiMotorLib: Servo Sweep running")
        self.stop_servo = False
        GPIO.setup(servo_pin, GPIO.OUT)
        time.sleep(initdelay)
        # set pin and freq
        pwm_servo = GPIO.PWM(servo_pin, self.freq)
        # set duty cycle
        pwm_servo.start(center)
        if verbose:
            print("Moved to center position = {}".format(center))
        time.sleep(delay)
        try:
            while sweeplen > 0:
                if self.stop_servo:
                    raise StopServoInterrupt
                else:
                    pwm_servo.ChangeDutyCycle(minduty)
                    if verbose:
                        print("Moved to min position = {}".format(minduty))
                    time.sleep(delay)
                    pwm_servo.ChangeDutyCycle(maxduty)
                    if verbose:
                        print("Moved to max position = {}".format(maxduty))
                        print("Number of loops left = {}".format(sweeplen))
                    sweeplen -= 1
                    time.sleep(delay)

        except KeyboardInterrupt:
            print("CTRL-C: RpiMotorLib: Terminating program.")
        except StopServoInterrupt:
            print("Stop Servo Interrupt : RpiMotorLib: ")
        finally:
            if verbose:
                print("\nRpiMotorLib, Servo Sweep finished, Details:.\n")
                print("servo pin = {}".format(servo_pin))
                print("Center position = {}".format(center))
                print("min position = {}".format(minduty))
                print("max position = {}".format(maxduty))
                print("Time delay = {}".format(delay))
                print("Init delay = {}".format(delay))
                print("Verbose  = {}".format(verbose))
                print("Servo control frequency = {}".format(self.freq))
                print("Number of Sweeps not completed = {}".format(sweeplen))
            if verbose:
                print("RpiMotorLib: Cleaning up")
            pwm_servo.stop()
            GPIO.output(servo_pin, False)

    def servo_move(self, servo_pin, position=7.5,
                   delay=0.5, verbose=False, initdelay=.05):
        """ servoMove 5 inputs

         servosweep(servo_pin, position, delay, verbose)

         (1) servo_pin, type=int help=GPIO pin
         we will contect to signal line of servo
         (2) position, type=float, default=7.5,
         help=The  dutycycle position of servo to move to
         (3) delay, type=int, default=0.5,
         help=Time to wait (in seconds) after move
         (4) verbose, type=bool  type=bool default=False
          help="Output actions & details",
         (5) initdelay, type=float, default 50mS
         help= A delay after Gpio setup and before servo moves

         example: to move the servo connected to GPIO pins 7
         for step delay of .5 second to postion 11
         with non-verbose output
         servoMove(7, 11, .5, False)
        """
        self.stop_servo = False
        GPIO.setup(servo_pin, GPIO.OUT)
        time.sleep(initdelay)
        pwm_servo = GPIO.PWM(servo_pin, self.freq)
        try:
            if self.stop_servo:
                raise StopServoInterrupt
            else:
                pwm_servo.start(position)
                time.sleep(delay)
        except KeyboardInterrupt:
            print("CTRL-C: RpiServoLib: Terminating program.")
        except StopServoInterrupt:
            print("Stop Servo Interrupt : RpiMotorLib: ")
        else:
            if verbose:
                print("\nRpiMotorLib, Servo Single Move finished, Details:.\n")
                print("Moved to position = {}".format(position))
                print("servo pin = {}".format(servo_pin))
                print("Time delay = {}".format(delay))
                print("Init delay = {}".format(initdelay))
                print("Verbose  = {}".format(verbose))
        finally:
            if verbose:
                print("RpiMotorLib: Cleaning up")
            pwm_servo.stop()
            GPIO.output(servo_pin, False)

    def convert_from_degree(self, degree):
        """ converts degrees to duty cycle percentage , takes in degree
        returns duty cycle float"""
        x_two = 180
        x_one = 0
        slope = (self.y_two-self.y_one)/(x_two-x_one)
        duty_cycle = slope*(degree-x_one) + self.y_one
        return duty_cycle

    def servo_move_step(self, servo_pin, start=10, end=170, stepdelay=1,
                        stepsize=1, initdelay=1, verbose=False):
        """
        servo move in step , moves servo in delayed steps
        between two points , seven inputs

        (1) servo_pin, type=int help=GPIO pin
        we will contect to signal line of servo
        (2) start, type=float, default=10,
        help=start position of servo in degrees
        (3) end, type=float, default=170,
        help=start position of servo in degrees
        (4) stepdelay, type=float, default=1,
        help=Time to wait (in seconds) between steps.
        (5) stepsize, type=int, default=1.
        help=teh size of steps between start and end in degrees
        (6) initdelay, type=float, default 50mS
        help= A delay after Gpio setup and before servo moves
        (7) verbose, type=bool  type=bool default=False
         help="Output actions & details",

        Example: to move a servo on GPIO pin 26 from 10 degrees to 180
        degrees in 20 degree steps every two seconds, with an initial delay
        of one second and verbose output.

        servo_move_step(26, 10, 180, 2, 20, 1, True)
        """
        if start > end:
            stepsize = (stepsize)*-1

        GPIO.setup(servo_pin, GPIO.OUT)
        self.stop_servo = False
        time.sleep(initdelay)
        pwm_servo = GPIO.PWM(servo_pin, self.freq)
        try:
            start_dc = self.convert_from_degree(start)
            pwm_servo.start(start_dc)
            for i in range(start, end+stepsize, stepsize):
                if self.stop_servo:
                    raise StopServoInterrupt
                else:
                    end_pwm = self.convert_from_degree(i)
                    if verbose:
                        print("Servo moving: {:.5f}  {} ".format(end_pwm, i))
                    pwm_servo.ChangeDutyCycle(end_pwm)
                    time.sleep(stepdelay)
        except KeyboardInterrupt:
            print("CTRL-C: RpiMotorLib: Terminating program.")
        except StopServoInterrupt:
            print("Stop Servo Interrupt : RpiMotorLib: ")
        except Exception as error:
            print(sys.exc_info()[0])
            print(error)
            print("RpiMotorLib  : Unexpected error:")
        else:
            if verbose:
                print("\nRpiMotorLib, Servo move finished, Details:.\n")
                print("servo pin = {}".format(servo_pin))
                print("stepsize = {}".format(stepsize))
                print("Start = {}".format(start))
                print("End = {}".format(end))
                print("Step delay = {}".format(stepdelay))
                print("Initial delay = {}".format(initdelay))
                print("Servo control frequency = {}".format(self.freq))
        finally:
            if verbose:
                print("RpiMotorLib: Cleaning up")
            pwm_servo.stop()
            GPIO.output(servo_pin, False)


def importtest(text):
    """import print test statement"""
    pass
    # print(text)

# ===================== MAIN ===============================


if __name__ == '__main__':
    importtest("main")
else:
    importtest("Imported {}".format(__name__))


# ===================== END ===============================
