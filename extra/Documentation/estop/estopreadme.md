# Emergency Stop

RpiMotorLib includes an `EmergencyStop` class that allows a push button
wired to any GPIO pin to immediately stop a motor or servo mid-run.

## Wiring

```
VCC  ----  PB Pin 1
GPIO ----  PB Pin 2
```

The button should pull the GPIO pin HIGH when pressed (active high, pull-down resistor).
Default pin is GPIO 17 in all example scripts.

## Basic Usage

```python
from RpiMotorLib.rpi_emergency_stop import EmergencyStop
from RpiMotorLib import RpiMotorLib

# Create motor instance
motor = RpiMotorLib.BYJMotor("MyMotor", "28BYJ")

# Create emergency stop — pass any motor or servo stop method as callable
estop = EmergencyStop(gpio_pin=17, stop_callable=motor.motor_stop, verbose=True)

# Arm before running motor
estop.enable()

# Run motor
motor.motor_run([18, 23, 24, 25], .001, 512, False, True, "half", .05)

# Disarm and release GPIO pin after use
estop.cleanup()
```

## Works with any motor or servo class

The `stop_callable` argument accepts any callable — pass the stop method
of whatever motor or servo instance you are using:

| Device | Stop method |
| ----- | ----- |
| Motors | `motor.motor_stop` |
| servos | `servo.servo_stop` |


## Stopping multiple motors

Pass a custom function as the callable to stop multiple motors at once:

```python
motor_one = RpiMotorLib.BYJMotor("MotorOne", "28BYJ")
motor_two = RpiMotorLib.BYJMotor("MotorTwo", "28BYJ")

def stop_all():
    motor_one.motor_stop()
    motor_two.motor_stop()

estop = EmergencyStop(gpio_pin=17, stop_callable=stop_all, verbose=True)
```

## Parameters

```python
EmergencyStop(gpio_pin, stop_callable, bouncetime=200, verbose=False)
```

| Parameter | Type | Default | Description |
| ----- | ----- | ----- | ----- |
| gpio_pin | int | — | GPIO pin number (BCM) connected to push button |
| stop_callable | callable | — | Function to call when button is pressed |
| bouncetime | int | 200 | Debounce time in milliseconds |
| verbose | bool | False | Print message when button is pressed |

## Methods

| Method | Description |
| ----- | ----- |
| `enable()` | Arm the emergency stop — start listening for button press |
| `disable()` | Disarm — stop listening, does not release GPIO pin |
| `cleanup()` | Disarm and release the GPIO pin |

## Example scripts

All hardware example scripts in the `examples/` folder include emergency stop
support commented in by default. To disable it, comment out the three
`EmergencyStop` lines in the script.


## Known issue — RPi.GPIO edge detection 

`EmergencyStop` requires `add_event_detect` which is broken in RPi.GPIO
on Raspberry Pi running Bookworm due to removal of the sysfs GPIO interface
in recent kernels(~6.6.y_. If you see `RuntimeError: Failed to add edge detection`
replace RPi.GPIO with rpi-lgpio:
```sh
pip install rpimotorlib[rpilgpio]
```
References:
- [Raspberry Pi kernel issue #6037](https://github.com/raspberrypi/linux/issues/6037)

