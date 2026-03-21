# tests/test_servo_lib.py
"""
Unit tests for rpiservolib.py and rpi_pservo_lib.py servo classes.
GPIO and pigpio are mocked — no hardware required.
"""
from unittest.mock import MagicMock
import pytest


# ── rpiservolib (GPIO PWM) ────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def mock_gpio(monkeypatch):
    """Replace GPIO adapter with a MagicMock before every test."""
    fake = MagicMock()
    fake.BCM = 11
    fake.OUT = 0
    fake_pwm = MagicMock()
    fake.PWM.return_value = fake_pwm
    monkeypatch.setattr("RpiMotorLib.gpio_adapter.GPIO", fake)
    monkeypatch.setattr("RpiMotorLib.rpiservolib.GPIO", fake)
    return fake, fake_pwm


class TestSG90Servo:

    def test_init_defaults(self, mock_gpio):
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        assert servo.name == "SG90servoX"
        assert servo.freq == 50
        assert servo.y_one == 2
        assert servo.y_two == 12
        assert servo.stop_servo is False

    def test_init_custom(self, mock_gpio):
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo(name="MyServo", freq=100, y_one=3, y_two=11)
        assert servo.name == "MyServo"
        assert servo.freq == 100

    def test_servo_stop_sets_flag(self, mock_gpio):
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        assert servo.stop_servo is False
        servo.servo_stop()
        assert servo.stop_servo is True

    def test_servo_move_sets_up_pin(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        servo.servo_move(servo_pin=7, position=7.5, delay=0, initdelay=0)
        fake.setup.assert_called_once_with(7, fake.OUT)
        fake.PWM.assert_called_once_with(7, 50)

    def test_servo_move_starts_pwm(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        servo.servo_move(servo_pin=7, position=9.0, delay=0, initdelay=0)
        fake_pwm.start.assert_called_once_with(9.0)

    def test_servo_move_cleanup(self, mock_gpio):
        """PWM should be stopped and pin set LOW in finally block."""
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        servo.servo_move(servo_pin=7, delay=0, initdelay=0)
        fake_pwm.stop.assert_called_once()
        fake.output.assert_called_with(7, False)

    def test_servo_sweep_sets_up_pin(self, mock_gpio):
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        # sweeplen=0 so loop doesn't execute
        servo.servo_sweep(servo_pin=7, sweeplen=0, delay=0, initdelay=0)
        fake.setup.assert_called_once_with(7, fake.OUT)
        fake.PWM.assert_called_once_with(7, 50)

    def test_servo_sweep_cleanup(self, mock_gpio):
        """PWM should be stopped and pin set LOW in finally block."""
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        servo.servo_sweep(servo_pin=7, sweeplen=0, delay=0, initdelay=0)
        fake_pwm.stop.assert_called_once()
        fake.output.assert_called_with(7, False)

    def test_convert_from_degree_zero(self, mock_gpio):
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo(y_one=2, y_two=12)
        assert servo.convert_from_degree(0) == pytest.approx(2.0)

    def test_convert_from_degree_180(self, mock_gpio):
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo(y_one=2, y_two=12)
        assert servo.convert_from_degree(180) == pytest.approx(12.0)

    def test_convert_from_degree_90(self, mock_gpio):
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo(y_one=2, y_two=12)
        assert servo.convert_from_degree(90) == pytest.approx(7.0)

    def test_servo_move_step_cleanup(self, mock_gpio):
        """PWM should be stopped and pin set LOW in finally block."""
        fake, fake_pwm = mock_gpio
        from RpiMotorLib.rpiservolib import SG90servo
        servo = SG90servo()
        servo.servo_move_step(servo_pin=7, start=10, end=10,
                              stepdelay=0, initdelay=0)
        fake_pwm.stop.assert_called_once()
        fake.output.assert_called_with(7, False)


# ── rpi_pservo_lib (pigpio PWM) ───────────────────────────────────────────

@pytest.fixture()
def mock_pigpio(monkeypatch):
    """Mock pigpio module and pi instance."""
    fake_pi = MagicMock()
    fake_pi.connected = True
    fake_pigpio = MagicMock()
    fake_pigpio.pi.return_value = fake_pi
    fake_pigpio.OUTPUT = 1
    monkeypatch.setattr("RpiMotorLib.rpi_pservo_lib.pigpio", fake_pigpio)
    return fake_pigpio, fake_pi


class TestServoPigpio:

    def test_init_defaults(self, mock_pigpio):
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio()
        assert servo.name == "servoY"
        assert servo.freq == 50
        assert servo.y_one == 1000
        assert servo.y_two == 2000
        assert servo.pigpio_addr is None
        assert servo.pigpio_port is None
        assert servo.stop_servo is False

    def test_servo_stop_sets_flag(self, mock_pigpio):
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio()
        servo.servo_stop()
        assert servo.stop_servo is True

    def test_get_pi_servo_no_args(self, mock_pigpio):
        fake_pigpio, fake_pi = mock_pigpio
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio()
        result = servo._get_pi_servo()
        fake_pigpio.pi.assert_called_once_with()
        assert result == fake_pi

    def test_get_pi_servo_with_addr(self, mock_pigpio):
        fake_pigpio, _ = mock_pigpio
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio(pigpio_addr="192.168.1.1", pigpio_port=8888)
        servo._get_pi_servo()
        fake_pigpio.pi.assert_called_once_with(host="192.168.1.1", port=8888)

    def test_servo_move_sets_pulsewidth(self, mock_pigpio):
        _, fake_pi = mock_pigpio
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio()
        servo.servo_move(servo_pin=7, position=1500, delay=0, initdelay=0)
        fake_pi.set_servo_pulsewidth.assert_any_call(7, 1500)

    def test_servo_move_cleanup(self, mock_pigpio):
        """pigpio should be stopped in finally block."""
        _, fake_pi = mock_pigpio
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio()
        servo.servo_move(servo_pin=7, delay=0, initdelay=0)
        fake_pi.set_servo_pulsewidth.assert_called_with(7, 0)
        fake_pi.stop.assert_called_once()

    def test_convert_from_degree_zero(self, mock_pigpio):
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio(y_one=1000, y_two=2000)
        assert servo.convert_from_degree(0) == pytest.approx(1000.0)

    def test_convert_from_degree_180(self, mock_pigpio):
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio(y_one=1000, y_two=2000)
        assert servo.convert_from_degree(180) == pytest.approx(2000.0)

    def test_convert_from_degree_90(self, mock_pigpio):
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio(y_one=1000, y_two=2000)
        assert servo.convert_from_degree(90) == pytest.approx(1500.0)

    def test_servo_sweep_cleanup(self, mock_pigpio):
        """pigpio should be stopped in finally block."""
        _, fake_pi = mock_pigpio
        from RpiMotorLib.rpi_pservo_lib import ServoPigpio
        servo = ServoPigpio()
        servo.servo_sweep(servo_pin=7, sweeplen=0, delay=0, initdelay=0)
        fake_pi.set_servo_pulsewidth.assert_called_with(7, 0)
        fake_pi.stop.assert_called_once()
