#!/usr/bin/env python3
"""A python 3 library for various
 motors and servos to connect to a raspberry pi"""
# ========================= HEADER ===================================
# title             :rpiMotorlib.py
# description       :A python 3 library for various motors
# and servos to connect to a raspberry pi
# author            :Gavin Lyons
# date              :15/03/2018
# version           :1.0-1
# web               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.6.0

# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import time
import RPi.GPIO as GPIO

# ==================== CLASS SECTION ===============================


class BYJMotor(object):
    """class to control a 28BYJ-48 stepper motor with ULN2003 controller
    by a raspberry pi"""
    def __init__(self, name="BYJMotorX"):
        self.name = name
        # This array is used to make the cursor "spin"
        # while the script is running.
        self.curserSpin = ["/", "-", "|", "\\", "|"]
        self.spinPosition = 0
        # We will be using GPIO pin numbers instead
        # of phyisical pin numbers.
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def motorRun(self, GpioPins, wait=.001, steps=512, ccwise=False, verbose=False, steptype="half"):
        """function motorRun, 6 inputs , moves stepper motor based on inputs

         motorRun(GPIOPins, wait, steps, counterclockwise, verbose, steptype)

         (1) GPIOPins, type=list of ints 4 long, help="list of
         4 GPIO pins to connect to motor controller
         These are the four GPIO pins we will
         use to drive the stepper motor, in the order
         they are plugged into the controller board. So,
         GPIO 18 is plugged into Pin 1 on the stepper motor.
         (2) wait, type=float, default=0.001, help=Time to wait
         (in seconds) between steps.
         (3) steps, type=int, default=512, help=Number of steps to take.
         Default is one revolution.
         (4) counterclockwise, type=bool default=False
         help="Turn stepper counterclockwise"
         (5) verbose, type=bool  type=bool default=False
         help="Write pin actions",
         (6) steptype, type=string , default=half help= type of drive to
         step motor 3 options full step half step or wave drive
         where full = fullstep , half = half step , wave = wave drive.

         example: to run A stepper motor connected to GPIO pins 18, 23, 24, 25
         for step delay of .01 second for 10 steps in clockwise direction,
         verbose output off , in half step mode
         motorRun([18, 23, 24, 25], .01, 10, False, False, "half")
        """

        for pin in GpioPins:
            GPIO.setup(pin, GPIO.OUT)  # Set pin to output
            GPIO.output(pin, False)  # Set pin to low ("False")

        # select step based on user input
        # Each step is a list containing GPIO pins that should be set to High

        if steptype == "half":  # half stepping.
            StepSequence = list(range(0, 8))
            StepSequence[0] = [GpioPins[0]]
            StepSequence[1] = [GpioPins[0], GpioPins[1]]
            StepSequence[2] = [GpioPins[1]]
            StepSequence[3] = [GpioPins[1], GpioPins[2]]
            StepSequence[4] = [GpioPins[2]]
            StepSequence[5] = [GpioPins[2], GpioPins[3]]
            StepSequence[6] = [GpioPins[3]]
            StepSequence[7] = [GpioPins[3], GpioPins[0]]
        elif steptype == "full":  # full stepping.
            StepSequence = list(range(0, 4))
            StepSequence[0] = [GpioPins[0], GpioPins[1]]
            StepSequence[1] = [GpioPins[1], GpioPins[2]]
            StepSequence[2] = [GpioPins[2], GpioPins[3]]
            StepSequence[3] = [GpioPins[0], GpioPins[3]]
        elif steptype == "wave":  # wave driving
            StepSequence = list(range(0, 4))
            StepSequence[0] = [GpioPins[0]]
            StepSequence[1] = [GpioPins[1]]
            StepSequence[2] = [GpioPins[2]]
            StepSequence[3] = [GpioPins[3]]
        else:
            print("Error: unknown step type ; half full or wave")
            quit()

        #  To run motor in reverse we flip the sequence order.
        if ccwise:
            StepSequence.reverse()

        # Prints a spinning cursor. Used when verbose not set to false.
        def PrintCursorSpin():
            print("%s\r" % self.curserSpin[self.spinPosition], end='', flush=True)
            self.spinPosition += 1
            if self.spinPosition > 4:
                self.spinPosition = 0

        # Print status of pins.
        def PrintStatus(enabledPins):
            if verbose:
                print("New Step:")
                for pin in GpioPins:
                    if pin in enabledPins:
                        print("Enabling Pin %i" % pin)
                    else:
                        print("Disabling Pin %i" % pin)
            else:
                PrintCursorSpin()

        # Iterate through the pins turning them on and off.
        stepsRemaining = steps
        while stepsRemaining > 0:
            for pinList in StepSequence:
                for pin in GpioPins:
                    if pin in pinList:
                        GPIO.output(pin, True)
                    else:
                        GPIO.output(pin, False)
                PrintStatus(pinList)
                time.sleep(wait)
            stepsRemaining -= 1

        # switch off pins at end. and print report status
        for pin in GpioPins:
            GPIO.output(pin, False)
        if verbose:
            print("\nRpiMotorLib, Motor Run finished, Details:.\n")
            print("GPIO pins = {}".format(GpioPins))
            print("Wait time = {}".format(wait))
            print("Number of steps = {}".format(steps))
            print("Counter clockwise = {}".format(ccwise))
            print("Verbose  = {}".format(verbose))
            print("Steptype = {}".format(steptype))


class SG90servo(object):
    """class to control a Tower pro micro servo SG90 by raspberry pi"""
    def __init__(self, name="SG90servoX"):
        self.name = name
        # We will be using GPIO pin numbers instead
        # of phyisical pin numbers.
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def servoSweep(self, servo_pin=7, center=7.5, minduty=3, maxduty=11, delay=0.5, verbose=False):
        """function servoSweep, 6 inputs

         servosweep(servo_pin, center, minduty, maxduty, delay, verbose)

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

         example: to sweep the servo connected to GPIO pins 7
         for step delay of .5 second from minduty postion
         2 to maxduty 12 center position 6
         with verbose output
         servoSweep(7, 6, 3, 11, .5, True)
        """
        print("RpiMotorLib: Servo Sweep running , press ctrl+c to quit")
        GPIO.setup(servo_pin, GPIO.OUT)
        pwm_servo = GPIO.PWM(servo_pin, 50)
        pwm_servo.start(center)
        if verbose:
                    print("Moved to center position = {}".format(center))
        time.sleep(delay)
        try:
            while True:
                pwm_servo.ChangeDutyCycle(minduty)
                if verbose:
                    print("Moved to min position = {}".format(minduty))
                time.sleep(delay)
                pwm_servo.ChangeDutyCycle(maxduty)
                if verbose:
                    print("Moved to max position = {}".format(maxduty))
                time.sleep(delay)

        except KeyboardInterrupt:
            print("CTRL-C: RpiMotorLib: Terminating program.")
        finally:
            print("RpiMotorLib: Cleaning up")
            if verbose:
                print("\nRpiMotorLib, Servo Sweep finished, Details:.\n")
                print("servo pin = {}".format(servo_pin))
                print("Center position = {}".format(center))
                print("min position = {}".format(minduty))
                print("max position = {}".format(maxduty))
                print("Time delay = {}".format(delay))
                print("Verbose  = {}".format(verbose))

            pwm_servo.stop()
            GPIO.output(servo_pin, False)
            time.sleep(0.05)

    def servoMove(self, servo_pin, position=7.5, delay=0.5, verbose=False):
        """function servoMove 4 inputs

         servosweep(servo_pin, position, delay, verbose)

         (1) servo_pin, type=int help=GPIO pin
         we will contect to signal line of servo
         (2) position, type=float, default=7.5,
         help=The  dutycycle position of servo to move to
         (3) delay, type=int, default=0.5,
         help=Time to wait (in seconds) between steps.
         (4) verbose, type=bool  type=bool default=False
          help="Output actions & details",

         example: to move the servo connected to GPIO pins 7
         for step delay of .5 second to postion 11
         with non-verbose output
         servoMove(7, 11, .5, False)
        """
        GPIO.setup(servo_pin, GPIO.OUT)
        pwm_servo = GPIO.PWM(servo_pin, 50)
        pwm_servo.start(position)
        time.sleep(delay)
        if verbose:
            print("RpiMotorLib: Cleaning up")
            print("\nRpiMotorLib, Servo Single Move finished, Details:.\n")
            print("Moved to position = {}".format(position))
            print("servo pin = {}".format(servo_pin))
            print("Time delay = {}".format(delay))
            print("Verbose  = {}".format(verbose))
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
