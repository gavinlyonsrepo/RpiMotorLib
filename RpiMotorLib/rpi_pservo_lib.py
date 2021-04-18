#!/usr/bin/env python3
"""
# ========================= HEADER ===================================
# title             :rpi_pservo_lib.py
# description       :Part of a RpiMotorLib python 3 library for motors
# and servos to connect to a raspberry pi
# This file is for servos controlled by pigpio PWM
# author            :Gavin Lyons
# web               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.4.2
"""
# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import sys
import time
import pigpio

# ==================== CLASS SECTION ===============================
class StopServoInterrupt(Exception):
    """ Stop the servo """
    pass

class ServoPigpio(object):
    """A Class to control a servo with pigpio library PWM by raspberry pi
    5 methods:
    1. __init__ 2. servo_sweep 3. servo_move 4. convert_from_degree
    5. servo_move_step
    """

    def __init__(self, name="servoY", freq=50, y_one=1000, y_two=2000,
                 pigpio_addr=None, pigpio_port=None):
        """ init method for class
        6 inputs
        (1) name, default=servoY, type=string, help=name of instance
        (2) Freq, type=int, default=50,  help=control freq of servo in Hz
        (3) y_one, type=float, default = 1000 ,
        help=pulse width min in uS of servo % for 0 degrees
        (4) y_two type=float, default = 2000 ,
        help=pulse width max in uS of servo % for 180 degrees
        (5) pigpio_addr, type=string default=None, help=host name where pigpio is running
        (6) pigpio_port, type=int default=None, help=port number where pigpio is running
          """
        self.name = name
        self.freq = freq
        self.y_one = y_one
        self.y_two = y_two
        self.pigpio_addr = pigpio_addr
        self.pigpio_port = pigpio_port
        self.stop_servo = False

    def servo_stop(self):
        """ Stop the servo """
        self.stop_servo = True

    def _get_pi_servo(self):
        """ Function to set make pigpio host and port configurable """
        args = {}

        if self.pigpio_addr is not None:
            args["host"] = self.pigpio_addr

        if self.pigpio_port is not None:
            args["port"] = self.pigpio_port

        return pigpio.pi(**args)

    def servo_sweep(self, servo_pin=7, center=1500, minduty=1000, maxduty=2000,
                    delay=0.5, verbose=False, initdelay=.05, sweeplen=1000000):
        """servo_sweep 8 inputs, moves servo in sweep loop
         (1) servo_pin, type=int help=GPIO pin
         we will contect to signal line of servo
         (2) center, type=float, default=1000,
         help=The center pulsewidth position of servo, uS
         (3) minduty, type=float, default=1000,
         help=The min pulsewidth position of servo , uS
         (4) maxduty, type=float, default=2000,
         help=The max pulsewidth position of servo , uS
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
        pi_servo = self._get_pi_servo()
        if not pi_servo.connected:
            print("RpiMotorLib : failed to connect to pigpio Daemon")
            exit()
        pi_servo.set_mode(servo_pin, pigpio.OUTPUT)
        time.sleep(initdelay)
        # set pin and freq
        pi_servo.set_PWM_frequency(servo_pin, self.freq)
        # set duty cycle
        pi_servo.set_servo_pulsewidth(servo_pin, center)
        if verbose:
            print("Moved to center Pulse width = {}".format(center))
        time.sleep(delay)
        try:
            while sweeplen > 0:
                if self.stop_servo:
                    raise StopServoInterrupt
                else:
                    pi_servo.set_servo_pulsewidth(servo_pin, minduty)
                    if verbose:
                        print("Moved to min Pulse width = {}".format(minduty))
                    time.sleep(delay)
                    pi_servo.set_servo_pulsewidth(servo_pin, maxduty)
                    if verbose:
                        print("Moved to max Pulse width = {}".format(maxduty))
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
                print("Center Pulse width = {}".format(center))
                print("min Pulse width = {}".format(minduty))
                print("max Pulse width = {}".format(maxduty))
                print("Time delay = {}".format(delay))
                print("Init delay = {}".format(initdelay))
                print("Verbose  = {}".format(verbose))
                print("Servo control frequency = {}".format(self.freq))
                print("Number of Sweeps not completed = {}".format(sweeplen))
            if verbose:
                print("RpiMotorLib: Cleaning up")
            pi_servo.set_servo_pulsewidth(servo_pin, 0)
            pi_servo.stop()

    def servo_move(self, servo_pin, position=1500,
                   delay=0.5, verbose=False, initdelay=.05):
        """ servoMove 5 inputs

         servoMove(servo_pin, position, delay, verbose)

         (1) servo_pin, type=int help=GPIO pin
         we will contect to signal line of servo
         (2) position, type=float, default=1500,
         help=The pulsewidth of servo to move to uS
         (3) delay, type=int, default=0.5,
         help=Time to wait (in seconds) before move after setup
         (4) verbose, type=bool  type=bool default=False
          help="Output actions & details",
         (5) initdelay, type=float, default 50mS
         help= A delay after Gpio setup and before servo moves
        """
        self.stop_servo = False
        pi_servo = self._get_pi_servo()
        pi_servo.set_mode(servo_pin, pigpio.OUTPUT)
        time.sleep(initdelay)
        pi_servo.set_PWM_frequency(servo_pin, self.freq)

        try:
            if self.stop_servo:
                raise StopServoInterrupt
            else:
                pi_servo.set_servo_pulsewidth(servo_pin, position)
                time.sleep(delay)
        except KeyboardInterrupt:
            print("CTRL-C: RpiServoLib: Terminating program.")
        except StopServoInterrupt:
            print("Stop Servo Interrupt : RpiMotorLib: ")
        else:
            if verbose:
                print("\nRpiMotorLib, Servo Single Move finished, Details:.\n")
                print("Moved to pulse width = {}".format(position))
                print("servo pin = {}".format(servo_pin))
                print("Time delay = {}".format(delay))
                print("Init delay = {}".format(initdelay))
                print("Verbose  = {}".format(verbose))
        finally:
            if verbose:
                print("RpiMotorLib: Cleaning up")
            pi_servo.set_servo_pulsewidth(servo_pin, 0)
            pi_servo.stop()

    def convert_from_degree(self, degree):
        """ converts degrees to Pulse width , takes in degree
        returns duty cycle float"""
        x_two = 180
        x_one = 0
        slope = (self.y_two-self.y_one)/(x_two-x_one)
        pulse_width = slope*(degree-x_one) + self.y_one
        return pulse_width

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
        (6) initdelay, type=float, default =1
        help= A delay after Gpio setup and before servo moves
        (7) verbose, type=bool  type=bool default=False
         help="Output actions & details",
        """
        if start > end:
            stepsize = (stepsize)*-1
        self.stop_servo = False
        pi_servo = self._get_pi_servo()
        pi_servo.set_mode(servo_pin, pigpio.OUTPUT)
        time.sleep(initdelay)
        pi_servo.set_PWM_frequency(servo_pin, self.freq)
        try:
            start_dc = self.convert_from_degree(start)
            pi_servo.set_servo_pulsewidth(servo_pin, start_dc)
            for i in range(start, end+stepsize, stepsize):
                if self.stop_servo:
                    raise StopServoInterrupt
                else:
                    end_pwm = self.convert_from_degree(i)
                    if verbose:
                        print("Servo moving: {:.5f}  {} ".format(end_pwm, i))
                    pi_servo.set_servo_pulsewidth(servo_pin, end_pwm)
                    time.sleep(stepdelay)
        except KeyboardInterrupt:
            print("CTRL-C: RpiServoLib: Terminating program.")
        except StopServoInterrupt:
            print("Stop Servo Interrupt : RpiMotorLib: ")
        except Exception as error:
            print(sys.exc_info()[0])
            print(error)
            print("RpiServoLib  : Unexpected error:")
        else:
            if verbose:
                print("\nRpiMotorLib, Servo move finished, Details:.\n")
                print("servo pin = {}".format(servo_pin))
                print("stepsize = {}".format(stepsize))
                print("Start = {}".format(start))
                print("End  = {}".format(end))
                print("Step delay = {}".format(stepdelay))
                print("Initial delay = {}".format(initdelay))
                print("Servo control frequency = {}".format(self.freq))
        finally:
            if verbose:
                print("RpiMotorLib: Cleaning up")
            pi_servo.set_servo_pulsewidth(servo_pin, 0)
            pi_servo.stop()


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
