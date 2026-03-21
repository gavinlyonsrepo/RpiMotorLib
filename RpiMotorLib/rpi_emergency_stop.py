#!/usr/bin/env python3
"""
 title             :rpi_emergency_stop.py
 description       :Part of a RpiMotorLib python 3 library for motors
 and servos to connect to a raspberry pi.
 This file provides a reusable emergency stop button class.
 A push button wired to a GPIO pin can be used to stop any
 motor or servo mid-run by calling its stop method.

 Wiring:
     VCC  --- PB Pin 1
     GPIO --- PB Pin 2
     Button should pull pin HIGH when pressed (active high).

 author            :Gavin Lyons
 web               :https://github.com/gavinlyonsrepo/RpiMotorLib
 python_version    :3.11
"""

# ========================== IMPORTS ======================
from RpiMotorLib.gpio_adapter import GPIO


# ==================== CLASS SECTION ===============================


class EmergencyStop():
    """Class to handle an emergency stop push button for any motor or servo.

    Monitors a GPIO pin for a rising edge (button press) and calls
    the provided stop callable when triggered.

    Methods: __init__, enable, disable, cleanup

    Example usage:
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        from RpiMotorLib.rpiservolib import SG90servo

        servo = SG90servo("myservo")
        estop = EmergencyStop(gpio_pin=17, stop_callable=servo.servo_stop)
        estop.enable()
        servo.servo_sweep(26, 7.5, 3, 11, .5, True, .05, 1000)
        estop.cleanup()
    """

    def __init__(self, gpio_pin, stop_callable, bouncetime=200, verbose=False):
        """Init method.

        (1) gpio_pin, type=int, GPIO pin connected to push button.
            Wire button between this pin and VCC (active high, pull-down).
        (2) stop_callable, type=callable, the stop method of the motor
            or servo instance e.g. mymotor.motor_stop or myservo.servo_stop
        (3) bouncetime, type=int, default=200, debounce time in milliseconds.
        (4) verbose, type=bool, default=False, print button press events.
        """
        self.gpio_pin = gpio_pin
        self.stop_callable = stop_callable
        self.verbose = verbose
        self.bouncetime = bouncetime
        self._enabled = False

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def _callback(self, channel):  # pylint: disable=unused-argument
        """Internal callback fired on rising edge (button press)."""
        if self.verbose:
            print(f"EmergencyStop: button pressed on GPIO {self.gpio_pin} — stopping.")
        self.stop_callable()

    def enable(self):
        """Arm the emergency stop — start listening for button presses."""
        if not self._enabled:
            GPIO.add_event_detect(
                self.gpio_pin,
                GPIO.RISING,
                callback=self._callback,
                bouncetime=self.bouncetime
            )
            self._enabled = True
            if self.verbose:
                print(f"EmergencyStop: armed on GPIO {self.gpio_pin}")

    def disable(self):
        """Disarm the emergency stop — stop listening for button presses."""
        if self._enabled:
            GPIO.remove_event_detect(self.gpio_pin)
            self._enabled = False
            if self.verbose:
                print(f"EmergencyStop: disarmed on GPIO {self.gpio_pin}")

    def cleanup(self):
        """Disarm and release the GPIO pin."""
        self.disable()
        GPIO.cleanup(self.gpio_pin)
