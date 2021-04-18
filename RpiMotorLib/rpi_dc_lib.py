#!/usr/bin/env python3
"""
 title             :rpi_dc_lib.py

 description       :Part of a RpiMotorLib python 3 library for motors
 and servos to connect to a raspberry pi
 This file is for DC Motors. direct current.

 TEST MATRIX :
 DC motor via L298n motor controller  = L298NMDc class
 DC motor via L9110S and DRV8833 motor controller = DRV8833 class.
 DC motor via TB6612FNG motor controller = TB6612FNGDc class.
 DC motor via a transistor = TranDc class.

 author            :Gavin Lyons
 web               :https://github.com/gavinlyonsrepo/RpiMotorLib
 mail              :glyons66@hotmail.com
 python_version    :3.5.3
 """

# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import time
import RPi.GPIO as GPIO

# ==================== CLASS SECTION ===============================


class L298NMDc():
    """ Class to control DC motor via L298n motor controller
    6 methods 1. __init__ 2. forward
    3.backward 4.stop 5 .brake 6.cleanup"""

    def __init__(self, pin_one, pin_two,
                 pwm_pin, freq=50, verbose=False, name="DCMotorX"):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected to IN1 or IN3
        (2) Pin two type=int, GPIO pin connected to IN2 or IN4
        (3) pwm_pin type=int, GPIO pin connected to EnA or ENB
        (4) freq in Hz default 50
        (5) verbose, type=bool  type=bool default=False
         help="Write pin actions"
        (6) name, type=string, name attribute
        """
        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two
        self.pwm_pin = pwm_pin
        self.freq = freq
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)

        self.my_pwm = GPIO.PWM(self.pwm_pin, self.freq)
        self.last_pwm = 0
        self.my_pwm.start(self.last_pwm)
        if self.verbose:
            print(" Motor initialized named: {} ".format(self.name))
            print(" Pin one In1 or In3:  {}".format(self.pin_one))
            print(" Pin two In2 or in4:  {}".format(self.pin_two))
            print(" Pin pwm enA or enB:  {}".format(self.pwm_pin))
            print(" Frequency: {} ".format(self.freq))

    def forward(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print("Moving Motor Forward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def backward(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print("Moving Motor Backward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def stop(self, duty_cycle=0):
        """ Stop motor"""
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print("Stoping Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print("Braking Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        if self.verbose:
            print("rpi_dc_lib.py : Cleaning up")
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)
        if clean_up:
            GPIO.cleanup()


class DRV8833NmDc():
    """ Class to control DC motor via L9110S and DRV8833 motor controller
    6 methods 1. __init__ 2. forward
    3.backward 4.stop 5.brake 6.cleanup"""

    def __init__(self, pin_one, pin_two,
                 freq=50, verbose=False, name="DCMotorY"):
        """ init method
        (1) pin_one, type=int,  GPIO pin  direction pin connected to IN1 or IN3
        (2) Pin two type=int, GPIO pin PWM speed pin connected to IN2 or IN4
        (3) freq in Hz default 50
        (4) verbose, type=bool  type=bool default=False
         help="Write pin actions"
        (5) name, type=string, name attribute
        """
        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two
        self.freq = freq
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)

        self.my_pwm = GPIO.PWM(self.pin_two, self.freq)
        self.last_pwm = 0
        self.my_pwm.start(self.last_pwm)
        if self.verbose:
            print(" Motor initialized named: {} ".format(self.name))
            print(" Direction pin In1 or In3:  {}".format(self.pin_one))
            print(" PWM speed pin In2 or in4:  {}".format(self.pin_two))
            print(" Frequency: {} ".format(self.freq))

    def forward(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        GPIO.output(self.pin_one, True)
        if self.verbose:
            print("Moving Motor Forward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def backward(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        GPIO.output(self.pin_one, False)
        if self.verbose:
            print("Moving Motor Backward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def stop(self, duty_cycle=0):
        """ Stop motor"""
        GPIO.output(self.pin_one, False)
        self.my_pwm.ChangeDutyCycle(duty_cycle)
        if self.verbose:
            print("Stoping Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        GPIO.output(self.pin_one, True)
        if self.verbose:
            print("Braking Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        if self.verbose:
            print("rpi_dc_lib.py : Cleaning up")
        GPIO.output(self.pin_one, False)
        self.my_pwm.ChangeDutyCycle(0)
        GPIO.output(self.pin_two, False)
        if clean_up:
            GPIO.cleanup()


class TranDc():
    """ Class to control DC motor via a transistor """
    def __init__(self, pin, freq=50, verbose=False):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected base of transistor
        (2) PWM freq in Hz default 50
        (3) verbose, type=bool  type=bool default=False
         help="Write pin actions"
        """
        self.pin = pin
        self.freq = freq
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

        self.motor_pwm = GPIO.PWM(self.pin, self.freq)
        self.motor_pwm.start(0)

    def dc_motor_run(self, speed=10, step_delay=1):
        """ controls speed of motor passed speed and step_delay
        speed is PWm duty cycle in percentage, delay is in seconds """
        self.motor_pwm.ChangeDutyCycle(speed)
        time.sleep(step_delay)
        if self.verbose:
            print("Speed PWM duty cycle percentage {}".format(speed))

    def dc_clean_up(self):
        """ docstring """
        self.motor_pwm.ChangeDutyCycle(0)
        self.motor_pwm.stop()
        GPIO.output(self.pin, False)


class TB6612FNGDc():
    """ Class to control DC motor via TB6612FNGDC motor controller
    6 methods 1. __init__ 2. forward
    3.backward 4.stop 5 .brake 6.cleanup 7.standby"""

    def __init__(self, pin_one, pin_two,
                 pwm_pin, freq=50, verbose=False, name="DCMotorX"):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected to AI1 or BI1
        (2) Pin two type=int, GPIO pin connected to AI2 or BI2
        (3) pwm_pin type=int, GPIO pin connected to PWA or PWB
        (4) freq in Hz default 50
        (5) verbose, type=bool  type=bool default=False
         help="Write pin actions"
        (6) name, type=string, name attribute
        """
        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two
        self.pwm_pin = pwm_pin
        self.freq = freq
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)

        self.my_pwm = GPIO.PWM(self.pwm_pin, self.freq)
        self.last_pwm = 0
        self.my_pwm.start(self.last_pwm)
        if self.verbose:
            print(" Motor initialized named: {} ".format(self.name))
            print(" Pin one AI1 or BI1:  {}".format(self.pin_one))
            print(" Pin two AI2 or BI2:  {}".format(self.pin_two))
            print(" Pin pwm PWA or PWB:  {}".format(self.pwm_pin))
            print(" Frequency: {} ".format(self.freq))


    def standby(standby_pin, standby_on=True):
        """Enables/disables the  standby mode of TB661FNG controller"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        if standby_on:
            GPIO.setup(standby_pin, GPIO.OUT)
            GPIO.output(standby_pin, True)
        else:
            GPIO.output(standby_pin, False)

    def forward(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print("Moving Motor Forward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def backward(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print("Moving Motor Backward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def stop(self, duty_cycle=0):
        """ Stop motor"""
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print("Stoping Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print("Braking Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        if self.verbose:
            print("rpi_dc_lib.py : Cleaning up : {}".format(self.name))
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)
        if clean_up:
            GPIO.cleanup()




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
