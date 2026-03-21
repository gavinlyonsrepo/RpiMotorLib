# tests/test_emergency_stop.py
"""
Unit tests for rpi_emergency_stop.py EmergencyStop class.
GPIO is mocked — no hardware required.
"""
from unittest.mock import MagicMock, call
import pytest


@pytest.fixture(autouse=True)
def mock_gpio(monkeypatch):
    """Replace GPIO adapter with a MagicMock before every test."""
    fake = MagicMock()
    fake.BCM = 11
    fake.IN = 1
    fake.PUD_DOWN = 1
    fake.RISING = 31
    monkeypatch.setattr("RpiMotorLib.gpio_adapter.GPIO", fake)
    monkeypatch.setattr("RpiMotorLib.rpi_emergency_stop.GPIO", fake)
    return fake


class TestEmergencyStop:

    def test_init_sets_up_pin(self, mock_gpio):
        """Init should configure the GPIO pin as input with pull-down."""
        fake = mock_gpio
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        stop_fn = MagicMock()
        estop = EmergencyStop(gpio_pin=17, stop_callable=stop_fn)
        fake.setmode.assert_called_once_with(fake.BCM)
        fake.setup.assert_called_once_with(17, fake.IN, pull_up_down=fake.PUD_DOWN)

    def test_init_stores_callable(self, mock_gpio):
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        stop_fn = MagicMock()
        estop = EmergencyStop(gpio_pin=17, stop_callable=stop_fn)
        assert estop.stop_callable is stop_fn
        assert estop.gpio_pin == 17
        assert estop._enabled is False

    def test_enable_adds_event_detect(self, mock_gpio):
        """enable() should register a rising edge callback."""
        fake = mock_gpio
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        stop_fn = MagicMock()
        estop = EmergencyStop(gpio_pin=17, stop_callable=stop_fn)
        estop.enable()
        fake.add_event_detect.assert_called_once_with(
            17, fake.RISING,
            callback=estop._callback,
            bouncetime=200
        )
        assert estop._enabled is True

    def test_enable_idempotent(self, mock_gpio):
        """Calling enable() twice should only register the callback once."""
        fake = mock_gpio
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        estop = EmergencyStop(gpio_pin=17, stop_callable=MagicMock())
        estop.enable()
        estop.enable()
        assert fake.add_event_detect.call_count == 1

    def test_disable_removes_event_detect(self, mock_gpio):
        """disable() should remove the event detect."""
        fake = mock_gpio
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        estop = EmergencyStop(gpio_pin=17, stop_callable=MagicMock())
        estop.enable()
        estop.disable()
        fake.remove_event_detect.assert_called_once_with(17)
        assert estop._enabled is False

    def test_disable_when_not_enabled(self, mock_gpio):
        """disable() on an unarmed stop should not call remove_event_detect."""
        fake = mock_gpio
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        estop = EmergencyStop(gpio_pin=17, stop_callable=MagicMock())
        estop.disable()
        fake.remove_event_detect.assert_not_called()

    def test_callback_calls_stop(self, mock_gpio):
        """Callback should call the stop callable when triggered."""
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        stop_fn = MagicMock()
        estop = EmergencyStop(gpio_pin=17, stop_callable=stop_fn)
        estop._callback(channel=17)
        stop_fn.assert_called_once()

    def test_cleanup_disables_and_releases_pin(self, mock_gpio):
        """cleanup() should disarm and release the GPIO pin."""
        fake = mock_gpio
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        estop = EmergencyStop(gpio_pin=17, stop_callable=MagicMock())
        estop.enable()
        estop.cleanup()
        fake.remove_event_detect.assert_called_once_with(17)
        fake.cleanup.assert_called_once_with(17)
        assert estop._enabled is False

    def test_works_with_motor_stop(self, mock_gpio):
        """Should work with any callable — motor stop, servo stop, lambda."""
        from RpiMotorLib.rpi_emergency_stop import EmergencyStop
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        estop = EmergencyStop(gpio_pin=17, stop_callable=motor.motor_stop)
        estop.enable()
        # Simulate button press
        estop._callback(channel=17)
        assert motor.stop_motor is True
