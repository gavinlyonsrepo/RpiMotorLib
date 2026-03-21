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
 DC motor via MX1508 motor controller = MC150XDc class.
 DC motor via a transistor = TranDc class.

 stop_motor flag rules:
   False — set in __init__, cleanup, forward(), backward(), dc_motor_run()
   True  — set in motor_stop(), stop(), brake(), standby()

 motor_stop() halts output immediately but does NOT destroy the PWM object,
 so the motor can be reused in subsequent tests without re-initialisation.
 Call cleanup() for full teardown at end of program.

 author            :Gavin Lyons
 web               :https://github.com/gavinlyonsrepo/RpiMotorLib
 """

# ========================== IMPORTS ======================
import time
from RpiMotorLib.gpio_adapter import GPIO

# ==================== CLASS SECTION ===============================


class L298NMDc():
    """ Class to control DC motor via L298n motor controller
    7 methods 1. __init__ 2. forward 3.backward
    4.stop 5.brake 6.cleanup 7.motor_stop"""

    def __init__(self, pin_one, pin_two,
                 pwm_pin, freq=50, verbose=False, name="DCMotorX"):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected to IN1 or IN3
        (2) Pin two type=int, GPIO pin connected to IN2 or IN4
        (3) pwm_pin type=int, GPIO pin connected to EnA or ENB
        (4) freq in Hz default 50
        (5) verbose, type=bool  default=False, help="Write pin actions"
        (6) name, type=string, name attribute
        """
        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two
        self.pwm_pin = pwm_pin
        self.freq = freq
        self.verbose = verbose
        self.stop_motor = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)

        self.my_pwm = GPIO.PWM(self.pwm_pin, self.freq)
        self.last_pwm = 0
        self.my_pwm.start(self.last_pwm)
        if self.verbose:
            print(f" Motor initialized named: {self.name} ")
            print(f" Pin one In1 or In3:  {self.pin_one}")
            print(f" Pin two In2 or in4:  {self.pin_two}")
            print(f" Pin pwm enA or enB:  {self.pwm_pin}")
            print(f" Frequency: {self.freq} ")

    def motor_stop(self):
        """Stop motor output immediately. PWM object kept alive for reuse.
        Call cleanup() for full teardown at end of program."""
        self.stop_motor = True
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)

    def forward(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        self.stop_motor = False
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print(f"Moving Motor Forward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def backward(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        self.stop_motor = False
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print(f"Moving Motor Backward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def stop(self, duty_cycle=0):
        """ Stop motor"""
        self.stop_motor = True
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print(f"Stopping Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        self.stop_motor = True
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print(f"Braking Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        self.stop_motor = False
        if self.verbose:
            print("rpi_dc_lib.py : Cleaning up")
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)
        self.my_pwm.stop()
        if clean_up:
            GPIO.cleanup()


class DRV8833NmDc():
    """ Class to control DC motor via L9110S and DRV8833 motor controller
    7 methods 1. __init__ 2. forward 3.backward
    4.stop 5.brake 6.cleanup 7.motor_stop"""

    def __init__(self, pin_one, pin_two,
                 freq=50, verbose=False, name="DCMotorY"):
        """ init method
        (1) pin_one, type=int,  GPIO pin direction pin connected to IN1 or IN3
        (2) Pin two type=int, GPIO pin PWM speed pin connected to IN2 or IN4
        (3) freq in Hz default 50
        (4) verbose, type=bool  default=False, help="Write pin actions"
        (5) name, type=string, name attribute
        """
        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two
        self.freq = freq
        self.verbose = verbose
        self.stop_motor = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)

        self.my_pwm = GPIO.PWM(self.pin_two, self.freq)
        self.last_pwm = 0
        self.my_pwm.start(self.last_pwm)
        if self.verbose:
            print(f" Motor initialized named: {self.name} ")
            print(f" Direction pin In1 or In3:  {self.pin_one}")
            print(f" PWM speed pin In2 or in4:  {self.pin_two}")
            print(f" Frequency: {self.freq} ")

    def motor_stop(self):
        """Stop motor output immediately. PWM object kept alive for reuse.
        Call cleanup() for full teardown at end of program."""
        self.stop_motor = True
        GPIO.output(self.pin_one, False)
        self.my_pwm.ChangeDutyCycle(0)

    def forward(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        self.stop_motor = False
        GPIO.output(self.pin_one, True)
        if self.verbose:
            print(f"Moving Motor Forward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def backward(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        self.stop_motor = False
        GPIO.output(self.pin_one, False)
        if self.verbose:
            print(f"Moving Motor Backward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def stop(self, duty_cycle=0):
        """ Stop motor"""
        self.stop_motor = True
        GPIO.output(self.pin_one, False)
        self.my_pwm.ChangeDutyCycle(duty_cycle)
        if self.verbose:
            print(f"Stopping Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        self.stop_motor = True
        GPIO.output(self.pin_one, True)
        if self.verbose:
            print(f"Braking Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        self.stop_motor = False
        if self.verbose:
            print("rpi_dc_lib.py : Cleaning up")
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)
        self.my_pwm.stop()
        if clean_up:
            GPIO.cleanup()


class MC150XDc():
    """ Class to control DC motor via MC150X motor controller
    7 methods 1. __init__ 2. forward 3.backward
    4.standby 5.brake 6.cleanup 7.motor_stop"""

    def __init__(self, pin_one, pin_two,
                 freq=50, verbose=False, name="DCMotorY"):
        """ init method
        (1) pin_one type=int, GPIO PWM pin connected to INT1 or INT3
        (2) Pin two type=int, GPIO PWM pin connected to INT2 or INT4
        (3) freq in Hz default 50
        (4) verbose, type=bool  default=False, help="Write pin actions"
        (5) name, type=string, name attribute
        """
        self.name = name
        self.freq = freq
        self.verbose = verbose
        self.pin_one_num = pin_one   # store pin numbers separately
        self.pin_two_num = pin_two   # as self.pin_one/two become PWM objects
        self.stop_motor = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin_one, GPIO.OUT)
        GPIO.setup(pin_two, GPIO.OUT)

        self.pin_one = GPIO.PWM(pin_one, self.freq)
        self.pin_two = GPIO.PWM(pin_two, self.freq)
        self.last_pwm = 0
        self.pin_one.start(self.last_pwm)
        self.pin_two.start(self.last_pwm)
        if self.verbose:
            print(f" Motor initialized named: {self.name} ")
            print(f" Pwm pin 1 InT1 or InT3:  {self.pin_one_num}")
            print(f" PWM pin 2 InT2 or inT4:  {self.pin_two_num}")
            print(f" Frequency: {self.freq} ")

    def motor_stop(self):
        """Stop motor output immediately. PWM object kept alive for reuse.
        Call cleanup() for full teardown at end of program."""
        self.stop_motor = True
        self.pin_one.ChangeDutyCycle(0)
        self.pin_two.ChangeDutyCycle(0)

    def forward(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        self.stop_motor = False
        self.pin_one.ChangeDutyCycle(duty_cycle)
        self.pin_two.ChangeDutyCycle(0)
        if self.verbose:
            print(f"Moving Motor Forward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.last_pwm = duty_cycle

    def backward(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        self.stop_motor = False
        self.pin_two.ChangeDutyCycle(duty_cycle)
        self.pin_one.ChangeDutyCycle(0)
        if self.verbose:
            print(f"Moving Motor Backward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.last_pwm = duty_cycle

    def standby(self, duty_cycle=0):
        """ Standby motor"""
        self.stop_motor = True
        self.pin_one.ChangeDutyCycle(duty_cycle)
        self.pin_two.ChangeDutyCycle(duty_cycle)
        if self.verbose:
            print(f"Standby Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        self.stop_motor = True
        self.pin_one.ChangeDutyCycle(duty_cycle)
        self.pin_two.ChangeDutyCycle(duty_cycle)
        if self.verbose:
            print(f"Brake Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        self.stop_motor = False
        if self.verbose:
            print("rpi_dc_lib.py : Cleaning up")
        self.pin_one.ChangeDutyCycle(0)
        self.pin_two.ChangeDutyCycle(0)
        self.pin_one.stop()
        self.pin_two.stop()
        if clean_up:
            GPIO.cleanup()


class TranDc():
    """ Class to control DC motor via a transistor
    4 methods 1. __init__ 2. motor_stop
    3.dc_motor_run 4.dc_clean_up"""

    def __init__(self, pin, freq=50, verbose=False):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected base of transistor
        (2) PWM freq in Hz default 50
        (3) verbose, type=bool  default=False, help="Write pin actions"
        """
        self.pin = pin
        self.freq = freq
        self.verbose = verbose
        self.stop_motor = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

        self.motor_pwm = GPIO.PWM(self.pin, self.freq)
        self.motor_pwm.start(0)

    def motor_stop(self):
        """Stop motor output immediately. PWM object kept alive for reuse.
        Call dc_clean_up() for full teardown at end of program."""
        self.stop_motor = True
        self.motor_pwm.ChangeDutyCycle(0)

    def dc_motor_run(self, speed=10, step_delay=1):
        """ controls speed of motor passed speed and step_delay
        speed is PWM duty cycle in percentage, delay is in seconds """
        self.stop_motor = False
        self.motor_pwm.ChangeDutyCycle(speed)
        time.sleep(step_delay)
        if self.verbose:
            print(f"Speed PWM duty cycle percentage {speed}")

    def dc_clean_up(self):
        """ Stop PWM and release GPIO pins """
        self.stop_motor = False
        self.motor_pwm.ChangeDutyCycle(0)
        self.motor_pwm.stop()
        GPIO.output(self.pin, False)


class TB6612FNGDc():
    """ Class to control DC motor via TB6612FNGDC motor controller
    8 methods 1. __init__ 2. forward 3.backward
    4.stop 5.brake 6.cleanup 7.standby 8.motor_stop"""

    def __init__(self, pin_one, pin_two,
                 pwm_pin, freq=50, verbose=False, name="DCMotorX"):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected to AI1 or BI1
        (2) Pin two type=int, GPIO pin connected to AI2 or BI2
        (3) pwm_pin type=int, GPIO pin connected to PWA or PWB
        (4) freq in Hz default 50
        (5) verbose, type=bool  default=False, help="Write pin actions"
        (6) name, type=string, name attribute
        """
        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two
        self.pwm_pin = pwm_pin
        self.freq = freq
        self.verbose = verbose
        self.stop_motor = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)

        self.my_pwm = GPIO.PWM(self.pwm_pin, self.freq)
        self.last_pwm = 0
        self.my_pwm.start(self.last_pwm)
        if self.verbose:
            print(f" Motor initialized named: {self.name} ")
            print(f" Pin one AI1 or BI1:  {self.pin_one}")
            print(f" Pin two AI2 or BI2:  {self.pin_two}")
            print(f" Pin pwm PWA or PWB:  {self.pwm_pin}")
            print(f" Frequency: {self.freq} ")

    def motor_stop(self):
        """Stop motor output immediately. PWM object kept alive for reuse.
        Call cleanup() for full teardown at end of program."""
        self.stop_motor = True
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)

    def standby(self, standby_pin, standby_on=True):
        """Enables/disables the standby mode of TB661FNG controller"""
        self.stop_motor = True
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        if standby_on:
            GPIO.setup(standby_pin, GPIO.OUT)
            GPIO.output(standby_pin, True)
        else:
            GPIO.output(standby_pin, False)

    def forward(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        self.stop_motor = False
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print(f"Moving Motor Forward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def backward(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        self.stop_motor = False
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print(f"Moving Motor Backward : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def stop(self, duty_cycle=0):
        """ Stop motor"""
        self.stop_motor = True
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print(f"Stopping Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        self.stop_motor = True
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print(f"Braking Motor : Duty Cycle = {duty_cycle}")
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        self.stop_motor = False
        if self.verbose:
            print(f"rpi_dc_lib.py : Cleaning up : {self.name}")
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)
        self.my_pwm.stop()
        if clean_up:
            GPIO.cleanup()


def importtest(text):
    """Import print test statement."""
    _ = text  # acknowledged, intentionally unused


# ===================== MAIN ===============================

if __name__ == '__main__':
    importtest("main")
else:
    importtest(f"Imported {__name__}")

# ===================== END ===============================
