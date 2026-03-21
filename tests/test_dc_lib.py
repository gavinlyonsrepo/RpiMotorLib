# tests/test_dc_lib.py
"""
Unit tests for rpi_dc_lib.py DC motor classes.
GPIO is mocked — no hardware required.
"""
from unittest.mock import MagicMock, patch
import pytest


@pytest.fixture(autouse=True)
def mock_gpio(monkeypatch):
    """Replace the GPIO adapter singleton with a MagicMock before every test."""
    fake = MagicMock()
    fake.BCM = 11
    fake.OUT = 0
    fake.IN = 1
    fake.HIGH = 1
    fake.LOW = 0
    fake_pwm = MagicMock()
    fake.PWM.return_value = fake_pwm
    monkeypatch.setattr("RpiMotorLib.gpio_adapter.GPIO", fake)
    monkeypatch.setattr("RpiMotorLib.rpi_dc_lib.GPIO", fake)
    return fake, fake_pwm


# ── L298NMDc ──────────────────────────────────────────────────────────────


class TestL298NMDc:

    def test_init_sets_up_pins(self, mock_gpio):
        fake, _ = mock_gpio
        from RpiMotorLib.rpi_dc_lib import L298NMDc
        motor = L298NMDc(pin_one=17, pin_two=27, pwm_pin=22, freq=50)
        fake.setmode.assert_called_once_with(fake.BCM)
        assert fake.setup.call_count == 3
        fake.PWM.assert_called_once_with(22, 50)

    def test_forward(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import L298NMDc
        motor = L298NMDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.forward(75)
        fake.output.assert_any_call(17, True)
        fake.output.assert_any_call(27, False)
        fake_pwm.ChangeDutyCycle.assert_called_with(75)

    def test_backward(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import L298NMDc
        motor = L298NMDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.backward(40)
        fake.output.assert_any_call(17, False)
        fake.output.assert_any_call(27, True)
        fake_pwm.ChangeDutyCycle.assert_called_with(40)

    def test_stop(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import L298NMDc
        motor = L298NMDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.stop()
        fake.output.assert_any_call(17, False)
        fake.output.assert_any_call(27, False)

    def test_brake(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import L298NMDc
        motor = L298NMDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.brake()
        fake.output.assert_any_call(17, True)
        fake.output.assert_any_call(27, True)

    def test_cleanup_stops_pwm(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import L298NMDc
        motor = L298NMDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.cleanup(clean_up=True)
        fake_pwm.stop.assert_called_once()
        fake.cleanup.assert_called_once()

    def test_duty_cycle_not_updated_if_unchanged(self, mock_gpio):
        """ChangeDutyCycle should not be called if duty cycle hasn't changed."""
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import L298NMDc
        motor = L298NMDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.forward(50)   # first call — sets last_pwm to 50
        fake_pwm.ChangeDutyCycle.reset_mock()
        motor.forward(50)   # same duty cycle — should not call ChangeDutyCycle
        fake_pwm.ChangeDutyCycle.assert_not_called()


# ── DRV8833NmDc ───────────────────────────────────────────────────────────


class TestDRV8833NmDc:

    def test_init_sets_up_pins(self, mock_gpio):
        fake, _ = mock_gpio
        from RpiMotorLib.rpi_dc_lib import DRV8833NmDc
        motor = DRV8833NmDc(pin_one=17, pin_two=27, freq=50)
        assert fake.setup.call_count == 2
        fake.PWM.assert_called_once_with(27, 50)

    def test_forward(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import DRV8833NmDc
        motor = DRV8833NmDc(pin_one=17, pin_two=27)
        motor.forward(60)
        fake.output.assert_any_call(17, True)
        fake_pwm.ChangeDutyCycle.assert_called_with(60)

    def test_backward(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import DRV8833NmDc
        motor = DRV8833NmDc(pin_one=17, pin_two=27)
        motor.backward(60)
        fake.output.assert_any_call(17, False)
        fake_pwm.ChangeDutyCycle.assert_called_with(60)


# ── TranDc ────────────────────────────────────────────────────────────────


class TestTranDc:

    def test_init(self, mock_gpio):
        fake, _ = mock_gpio
        from RpiMotorLib.rpi_dc_lib import TranDc
        motor = TranDc(pin=18, freq=50)
        fake.setup.assert_called_once_with(18, fake.OUT)
        fake.PWM.assert_called_once_with(18, 50)

    def test_cleanup(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import TranDc
        motor = TranDc(pin=18)
        motor.dc_clean_up()
        fake_pwm.stop.assert_called_once()
        fake.output.assert_called_with(18, False)


# ── TB6612FNGDc ───────────────────────────────────────────────────────────


class TestTB6612FNGDc:

    def test_init_sets_up_pins(self, mock_gpio):
        fake, _ = mock_gpio
        from RpiMotorLib.rpi_dc_lib import TB6612FNGDc
        motor = TB6612FNGDc(pin_one=17, pin_two=27, pwm_pin=22)
        assert fake.setup.call_count == 3
        fake.PWM.assert_called_once_with(22, 50)

    def test_forward(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import TB6612FNGDc
        motor = TB6612FNGDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.forward(50)
        fake.output.assert_any_call(17, True)
        fake.output.assert_any_call(27, False)

    def test_cleanup(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpi_dc_lib import TB6612FNGDc
        motor = TB6612FNGDc(pin_one=17, pin_two=27, pwm_pin=22)
        motor.cleanup(clean_up=True)
        fake_pwm.stop.assert_called_once()
        fake.cleanup.assert_called_once()
