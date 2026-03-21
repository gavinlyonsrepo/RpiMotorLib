"""
RpiMotorLib GPIO abstraction layer.

Backend is selected via (in priority order):
    1. RPIMOTORLIB_GPIO_BACKEND environment variable
    2. ~/.config/rpiMotorLib/config.ini
    3. Auto-detect (tries RPi.GPIO/rpi-lgpio first, then lgpio)

Valid backend values: null | rpigpio | lgpio
"""

import logging
from RpiMotorLib.settings import get_gpio_backend

_log = logging.getLogger(__name__)
_BACKEND = get_gpio_backend()


class _GPIOAdapter:
    """Unified interface over RPi.GPIO / rpi-lgpio."""

    BCM = None
    BOARD = None
    OUT = None
    IN = None
    HIGH = None
    LOW = None
    PUD_UP = None
    PUD_DOWN = None
    RISING = None
    FALLING = None
    BOTH = None

    def __init__(self):
        self._gpio = None
        self._pwm_registry = {}
        self._load()

    def _load(self):
        """Load the configured GPIO backend and mirror its constants."""
        if _BACKEND in ("null", "auto", "rpigpio"):
            try:
                import RPi.GPIO as _gpio  # pylint: disable=import-outside-toplevel
                self._gpio = _gpio
                _log.debug("GPIO backend: RPi.GPIO / rpi-lgpio")
            except ImportError:
                if _BACKEND == "rpigpio":
                    raise ImportError(
                        "RPi.GPIO not found. On Raspberry Pi 5 install rpi-lgpio:\n"
                        "  pip install rpi-lgpio\n"
                        "  # or: sudo apt install python3-rpi-lgpio"
                    ) from None

        if self._gpio is None and _BACKEND in ("null", "auto", "lgpio"):
            try:
                self._gpio = _LgpioCompat()
                _log.debug("GPIO backend: lgpio (native)")
            except ImportError:
                pass

        if self._gpio is None:
            raise ImportError(
                "No GPIO backend available. Install one of:\n"
                "  pip install rpi-lgpio   # recommended (Pi 1-5)\n"
                "  pip install lgpio       # alternative\n"
                "Or set backend in ~/.config/rpiMotorLib/config.ini"
            )

        for attr in ("BCM", "BOARD", "OUT", "IN", "HIGH", "LOW", "PUD_UP", "PUD_DOWN",
                     "RISING", "FALLING", "BOTH"):
            setattr(self, attr, getattr(self._gpio, attr, None))

    def setmode(self, mode):
        """Set the GPIO pin numbering mode (BCM or BOARD)."""
        self._gpio.setmode(mode)

    def setwarnings(self, flag):
        """Enable or disable GPIO warnings."""
        self._gpio.setwarnings(flag)

    def setup(self, pin, direction, pull_up_down=None, initial=None):
        """Set up a GPIO pin as input or output."""
        kwargs = {}
        if pull_up_down is not None:
            kwargs["pull_up_down"] = pull_up_down
        if initial is not None:
            kwargs["initial"] = initial
        self._gpio.setup(pin, direction, **kwargs)

    def output(self, pin, value):
        """Set a GPIO output pin HIGH or LOW."""
        self._gpio.output(pin, value)

    def input(self, pin):
        """Read the value of a GPIO input pin."""
        return self._gpio.input(pin)

    def cleanup(self, pin=None):
        """Release GPIO pin(s). Pass a pin number to release one pin only.
        Stop all PWM instances then release GPIO pin(s).
        Note: rpi-lgpio 0.6 has a known bug where __del__ fires after cleanup
        causing a harmless TypeError traceback. This is fixed in upstream rpi-lgpio.
        See: https://github.com/waveform80/rpi-lgpio/issues """
        for pwm in self._pwm_registry.values():
            try:
                pwm.ChangeDutyCycle(0)
                pwm.stop()
                # type(pwm).__del__ = lambda self: None  # suppress rpi-lgpio __del__ bug
            except Exception:  # pylint: disable=broad-except
                pass
        self._pwm_registry.clear()
        if pin is not None:
            self._gpio.cleanup(pin)
        else:
            self._gpio.cleanup()

    def PWM(self, pin, frequency):
        """Create and return a PWM instance, replacing any existing one on this pin."""
        if pin in self._pwm_registry:
            try:
                self._pwm_registry[pin].ChangeDutyCycle(0)
                self._pwm_registry[pin].stop()
                self._gpio.cleanup(pin)        # ← force release the channel
                self._gpio.setup(pin, self._gpio.OUT)  # ← re-setup for next use
            except Exception:  # pylint: disable=broad-except
                pass
            del self._pwm_registry[pin]
        pwm = self._gpio.PWM(pin, frequency)
        self._pwm_registry[pin] = pwm
        return pwm

    def add_event_detect(self, pin, edge, callback=None, bouncetime=None):
        """Register an edge detection event on a GPIO input pin."""
        kwargs = {}
        if callback is not None:
            kwargs["callback"] = callback
        if bouncetime is not None:
            kwargs["bouncetime"] = bouncetime
        self._gpio.add_event_detect(pin, edge, **kwargs)

    def remove_event_detect(self, pin):
        """Remove edge detection for a GPIO pin."""
        self._gpio.remove_event_detect(pin)


class _LgpioCompat:
    """Minimal RPi.GPIO-compatible shim over native lgpio.

    Only activated when backend is explicitly set to 'lgpio'.
    Implements the subset of the RPi.GPIO API used by RpiMotorLib.
    """

    BCM = 11
    BOARD = 10
    OUT = 0
    IN = 1
    HIGH = 1
    LOW = 0
    PUD_UP = 2
    PUD_DOWN = 1

    def __init__(self):
        import lgpio as lg  # pylint: disable=import-outside-toplevel  # type: ignore
        self._lg = lg
        self._h = lg.gpiochip_open(0)
        self._pwm_handles = {}

    def setmode(self, mode):
        """No-op: lgpio always uses chip-relative pin offsets (equivalent to BCM)."""

    def setwarnings(self, flag):
        """No-op: lgpio does not have a warnings flag."""

    def setup(self, pin, direction, pull_up_down=None, initial=None):
        """Claim a GPIO pin as input or output."""
        if direction == self.OUT:
            self._lg.gpio_claim_output(self._h, pin, 0 if initial is None else initial)
        else:
            flags = 0
            if pull_up_down == self.PUD_UP:
                flags = self._lg.SET_PULL_UP
            elif pull_up_down == self.PUD_DOWN:
                flags = self._lg.SET_PULL_DOWN
            self._lg.gpio_claim_input(self._h, pin, flags)

    def output(self, pin, value):
        """Write a value to a GPIO output pin."""
        self._lg.gpio_write(self._h, pin, value)

    def input(self, pin):
        """Read the value of a GPIO input pin."""
        return self._lg.gpio_read(self._h, pin)

    def cleanup(self, _pin=None):
        """Stop all PWM and close the gpiochip handle.
        Note: lgpio closes the entire chip handle — per-pin cleanup is not
        supported. The _pin argument is accepted for API compatibility only.
        """
        for handle in self._pwm_handles.values():
            try:
                handle.stop()
            except Exception:  # pylint: disable=broad-except
                pass
        self._lg.gpiochip_close(self._h)

    def PWM(self, pin, frequency):
        """Create and return a software PWM instance."""
        pwm = _SoftwarePWM(self._lg, self._h, pin, frequency)
        self._pwm_handles[pin] = pwm
        return pwm


class _SoftwarePWM:
    """Software PWM wrapper around lgpio tx_pwm."""

    def __init__(self, lg, handle, pin, frequency):
        self._lg = lg
        self._h = handle
        self._pin = pin
        self._freq = frequency
        self._duty = 0

    def start(self, duty_cycle):
        """Start PWM at the given duty cycle (0-100)."""
        self._duty = duty_cycle
        self._lg.tx_pwm(self._h, self._pin, self._freq, duty_cycle)

    def ChangeDutyCycle(self, duty_cycle):
        """Change the PWM duty cycle."""
        self._duty = duty_cycle
        self._lg.tx_pwm(self._h, self._pin, self._freq, duty_cycle)

    def ChangeFrequency(self, frequency):
        """Change the PWM frequency."""
        self._freq = frequency
        self._lg.tx_pwm(self._h, self._pin, frequency, self._duty)

    def stop(self):
        """Stop PWM output."""
        self._lg.tx_pwm(self._h, self._pin, self._freq, 0)


# Module-level singleton — this is what all RpiMotorLib modules import
GPIO = _GPIOAdapter()
