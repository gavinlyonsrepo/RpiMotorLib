# tests/test_stepper_lib.py
"""
Unit tests for RpiMotorLib.py stepper motor classes.
GPIO is mocked — no hardware required.
"""
from unittest.mock import MagicMock, call, patch
import pytest


@pytest.fixture(autouse=True)
def mock_gpio(monkeypatch):
    """Replace the GPIO adapter singleton with a MagicMock before every test."""
    fake = MagicMock()
    fake.BCM = 11
    fake.OUT = 0
    fake.HIGH = 1
    fake.LOW = 0
    monkeypatch.setattr("RpiMotorLib.gpio_adapter.GPIO", fake)
    monkeypatch.setattr("RpiMotorLib.RpiMotorLib.GPIO", fake)
    return fake


# ── BYJMotor ──────────────────────────────────────────────────────────────


class TestBYJMotor:

    def test_init_defaults(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        assert motor.name == "BYJMotorX"
        assert motor.motor_type == "28BYJ"
        assert motor.stop_motor is False

    def test_init_custom(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor(name="MyMotor", motor_type="Nema")
        assert motor.name == "MyMotor"
        assert motor.motor_type == "Nema"

    def test_motor_stop_sets_flag(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        assert motor.stop_motor is False
        motor.motor_stop()
        assert motor.stop_motor is True

    def test_motor_run_negative_steps_exits(self, mock_gpio):
        """motor_run should call quit() if steps < 0."""
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        with pytest.raises(SystemExit):
            motor.motor_run(gpiopins=[17, 18, 19, 20], steps=-1)

    def test_motor_run_invalid_steptype_exits(self, mock_gpio):
        """motor_run should call quit() on unknown steptype."""
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        with pytest.raises(SystemExit):
            motor.motor_run(gpiopins=[17, 18, 19, 20], steps=1, steptype="invalid")

    def test_motor_run_half_step(self, mock_gpio):
        """motor_run half step should set up all 4 GPIO pins."""
        fake = mock_gpio
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        motor.motor_run(gpiopins=[17, 18, 19, 20], steps=1,
                        steptype="half", wait=0, initdelay=0)
        for pin in [17, 18, 19, 20]:
            fake.setup.assert_any_call(pin, fake.OUT)

    def test_motor_run_full_step(self, mock_gpio):
        """motor_run full step should set up all 4 GPIO pins."""
        fake = mock_gpio
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        motor.motor_run(gpiopins=[17, 18, 19, 20], steps=1,
                        steptype="full", wait=0, initdelay=0)
        for pin in [17, 18, 19, 20]:
            fake.setup.assert_any_call(pin, fake.OUT)

    def test_motor_run_wave_step(self, mock_gpio):
        """motor_run wave step should set up all 4 GPIO pins."""
        fake = mock_gpio
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        motor.motor_run(gpiopins=[17, 18, 19, 20], steps=1,
                        steptype="wave", wait=0, initdelay=0)
        for pin in [17, 18, 19, 20]:
            fake.setup.assert_any_call(pin, fake.OUT)

    def test_motor_run_pins_off_after_run(self, mock_gpio):
        """All pins should be set LOW in the finally block."""
        fake = mock_gpio
        from RpiMotorLib.RpiMotorLib import BYJMotor
        motor = BYJMotor()
        motor.motor_run(gpiopins=[17, 18, 19, 20], steps=1,
                        wait=0, initdelay=0)
        for pin in [17, 18, 19, 20]:
            fake.output.assert_any_call(pin, False)


# ── A4988Nema ─────────────────────────────────────────────────────────────


class TestA4988Nema:

    def test_init_with_mode_pins(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(14, 15, 18), motor_type="A4988")
        assert motor.direction_pin == 20
        assert motor.step_pin == 21
        assert motor.mode_pins == (14, 15, 18)
        assert motor.motor_type == "A4988"
        assert motor.stop_motor is False

    def test_init_without_mode_pins(self, mock_gpio):
        """mode_pins=(-1,-1,-1) should set self.mode_pins to False."""
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1))
        assert motor.mode_pins is False

    def test_motor_stop_sets_flag(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1))
        motor.motor_stop()
        assert motor.stop_motor is True

    def test_motor_go_sets_up_pins(self, mock_gpio):
        fake = mock_gpio
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1))
        motor.motor_go(steps=1, stepdelay=0, initdelay=0)
        fake.setup.assert_any_call(20, fake.OUT)
        fake.setup.assert_any_call(21, fake.OUT)

    def test_motor_go_invalid_steptype_exits(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1))
        with pytest.raises(SystemExit):
            motor.motor_go(steptype="invalid", steps=1,
                           stepdelay=0, initdelay=0)

    def test_motor_go_invalid_motor_type_exits(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1), motor_type="UNKNOWN")
        with pytest.raises(SystemExit):
            motor.motor_go(steps=1, stepdelay=0, initdelay=0)

    def test_motor_go_pins_off_after_run(self, mock_gpio):
        """step and direction pins should be set LOW in finally block."""
        fake = mock_gpio
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1))
        motor.motor_go(steps=1, stepdelay=0, initdelay=0)
        fake.output.assert_any_call(21, False)
        fake.output.assert_any_call(20, False)

    def test_drv8825_motor_type(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1), motor_type="DRV8825")
        assert motor.motor_type == "DRV8825"
        # Should not raise
        motor.motor_go(steptype="Full", steps=1, stepdelay=0, initdelay=0)

    def test_lv8729_motor_type(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A4988Nema
        motor = A4988Nema(direction_pin=20, step_pin=21,
                          mode_pins=(-1, -1, -1), motor_type="LV8729")
        assert motor.motor_type == "LV8729"
        motor.motor_go(steptype="Full", steps=1, stepdelay=0, initdelay=0)


# ── A3967EasyNema ─────────────────────────────────────────────────────────


class TestA3967EasyNema:

    def test_init_with_mode_pins(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A3967EasyNema
        motor = A3967EasyNema(direction_pin=20, step_pin=21,
                              mode_pins=(14, 15))
        assert motor.direction_pin == 20
        assert motor.step_pin == 21
        assert motor.mode_pins == (14, 15)

    def test_init_without_mode_pins(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A3967EasyNema
        motor = A3967EasyNema(direction_pin=20, step_pin=21,
                              mode_pins=(-1, -1))
        assert motor.mode_pins is False

    def test_motor_stop_sets_flag(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A3967EasyNema
        motor = A3967EasyNema(direction_pin=20, step_pin=21,
                              mode_pins=(-1, -1))
        motor.motor_stop()
        assert motor.stop_motor is True

    def test_motor_move_invalid_steptype_exits(self, mock_gpio):
        from RpiMotorLib.RpiMotorLib import A3967EasyNema
        motor = A3967EasyNema(direction_pin=20, step_pin=21,
                              mode_pins=(-1, -1))
        with pytest.raises(SystemExit):
            motor.motor_move(steptype="invalid", steps=1,
                             stepdelay=0, initdelay=0)

    def test_motor_move_pins_off_after_run(self, mock_gpio):
        fake = mock_gpio
        from RpiMotorLib.RpiMotorLib import A3967EasyNema
        motor = A3967EasyNema(direction_pin=20, step_pin=21,
                              mode_pins=(-1, -1))
        motor.motor_move(steps=1, stepdelay=0, initdelay=0)
        fake.output.assert_any_call(21, False)
        fake.output.assert_any_call(20, False)


# ── degree_calc ───────────────────────────────────────────────────────────


class TestDegreeCalc:

    def test_full_step(self):
        from RpiMotorLib.RpiMotorLib import degree_calc
        assert degree_calc(200, "Full") == pytest.approx(360.0)

    def test_half_step(self):
        from RpiMotorLib.RpiMotorLib import degree_calc
        assert degree_calc(200, "Half") == pytest.approx(180.0)

    def test_quarter_step(self):
        from RpiMotorLib.RpiMotorLib import degree_calc
        assert degree_calc(200, "1/4") == pytest.approx(90.0)
