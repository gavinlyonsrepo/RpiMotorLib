[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/paypalme/whitelight976) [![CI](https://github.com/gavinlyonsrepo/RpiMotorLib/actions/workflows/ci.yml/badge.svg)](https://github.com/gavinlyonsrepo/RpiMotorLib/actions/workflows/ci.yml) [![PyPI version](https://img.shields.io/pypi/v/rpimotorlib.svg)](https://pypi.org/project/rpimotorlib/)

# RpiMotorLib

![ScreenShot dcmotor](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/extra/images/RF310T11400.jpg)
![ScreenShot Nema](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/extra/images/nema11.jpg)
![ScreenShot L298N](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/extra/images/L298N.jpg)
![ScreenShot A4988](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/extra/images/A4988.jpg)

## Table of contents

  * [Table of contents](#table-of-contents)
  * [Overview](#overview)
  * [Installation](#installation)
    * [From PyPi with pip or pipx](#from-pypi-with-pip-or-pipx)
    * [From Github](#from-github)
  * [Hardware](#hardware)
    * [Stepper motors](#stepper-motors)
    * [DC motors](#dc-motors)
    * [Servos](#servos)
  * [Software](#software)
    * [File System](#file-system)
    * [Dependencies](#dependencies)
  * [Notes and issues](#notes-and-issues)
    * [Servo trace back issue](#servo-trace-back-issue)
    * [Two Motors simultaneously](#two-motors-simultaneously)
    * [GPIO cleanup method](#gpio-cleanup-method)
    * [Emergency Stop](#emergency-stop)
    * [pipx](#pipx)
  * [See Also](#see-also)

## Overview

* Name: RpiMotorLib
* Version: 4.0.0
* Title: Raspberry Pi motor library.
* Description:

A Python 3 library to drive motor controllers and servos with a Raspberry Pi.

These components supported are some of the most widely used by the maker community.
There are three categories in the library: Stepper motors, DC Motors and Servos.
The end user can import this library into their projects
and then control the components with short snippets of code.
The library is modular so the user can just import/use the section they need.

* Project URL: [URL LINK](https://github.com/gavinlyonsrepo/RpiMotorLib)

* Tested on Toolchains:
    1. RPI 3 model B. Raspbian 12 Bookworm, 64 bit. Python 3.11.2.
    2. RPI 5 model B. Raspbian 12 Bookworm, 64 bit. Python 3.11.2.

## Installation

Latest version 4.0.0

**Raspberry Pi compatibility:**

Before the Raspberry pi 5 rpimotorlib used RPi.GPIO as low level
dependency. but it wont work on Raspberry 5 and will not be upgraded
so we switched to rpi-lgpio which works on all in Version 4.0.0.
Using a gpio_adpater, we maintained backwards compatibility
and capability to use RPi.GPIO.

| Raspberry Pi | Supported | Recommended GPIO library |
| ----- | ----- | ----- |
| Pi 1 / 2 / 3 / 4 | ✅ | `rpi-lgpio` (recommended) or `RPi.GPIO` (legacy) |
| Pi 5 | ✅ | `rpi-lgpio` required — `RPi.GPIO` does not support Pi 5 |

`rpi-lgpio` is a drop-in replacement for `RPi.GPIO` that works on **all**
Raspberry Pi models including Pi 5. It is the recommended GPIO library for
all new installations regardless of Pi model.

### From PyPi with pip or pipx

The Python Package Index (PyPI) is a repository of software for the Python
programming language. Install using *pip* or *pipx* to the location or
environment of your choice. Recommend set up a
[virtual environment](extra/Documentation/venv_help/venv_help_readme.md)
or use pipx. NB see notes section for more on pipx.
Package name = rpimotorlib [Link](https://pypi.org/project/rpimotorlib/).

**Recommended install (all Pi models including Pi 5):**
```sh
pip install rpimotorlib[rpilgpio]
```

**Legacy install (Pi 1-4 with existing RPi.GPIO):**
```sh
pip install rpimotorlib[legacy]
```

> **Warning:** Do not install `rpilgpio` and `legacy` extras together —
> both provide the `RPi.GPIO` namespace and will conflict.

**Optional extras:**

| Extra | Description |
| ----- | ----- |
| `rpilgpio` | Installs rpi-lgpio — recommended for all Pi models including Pi 5 |
| `legacy` | Installs RPi.GPIO — Pi 1-4 only, not supported on Pi 5 |
| `pigpio` | Installs pigpio — optional hardware PWM servo, Pi 1-4 only |
| `dev` | Installs pytest, pytest-cov, pylint — for development |

### From Github

Clone and install via pip:

```sh
git clone https://github.com/gavinlyonsrepo/RpiMotorLib.git
cd RpiMotorLib
pip install .[rpilgpio]
```

## Hardware

Supported Components:

### Stepper motors

| Motor tested | Motor controller| Help File URL link |
| ----- | ----- | ----- |
| Unipolar 28BYJ-48 | ULN2003 driver module | [URL](extra/Documentation/28BYJ.md)|
| Bipolar Nema  | TB6612FNG Dual Driver Carrier | [URL](extra/Documentation/Nema11TB6612FNG.md) |
| Bipolar Nema  | L298N H-Bridge controller module | [URL](extra/Documentation/Nema11L298N.md) |
| Bipolar Nema  | A4988 Stepper Driver Carrier | [URL](extra/Documentation/Nema11A4988.md)|
| Bipolar Nema  | DRV8825 Stepper Driver Carrier | [URL](extra/Documentation/Nema11DRV8825.md) |
| Bipolar Nema  | A3967 Stepper Driver aka "easy driver v4.4" | [URL](extra/Documentation/Nema11A3967Easy.md)|
| Bipolar (untested on hw)| LV8729 Stepper Driver Carrier  | [URL](extra/Documentation/Nema11LV8729.md)|
| Bipolar (untested)| DRV8833 Motor controller module | TODO |
| Bipolar (untested)| L9110S Motor controller module | TODO |
| Bipolar Nema | MX1508 Motor controller module | [URL](extra/Documentation/Nema11MX150X.md) |

### DC motors

| Motor | Motor controller| Help File URL link |
| ----- | ----- | ----- |
| DC Brushed Motor | L298N Motor controller module. | [ URL ](extra/Documentation/L298N_DC.md) |
| DC Brushed Motor | L9110S Motor controller module. | [ URL ](extra/Documentation/L9110S_DC.md) |
| DC Brushed Motor | DRV8833 Motor controller module. | [ URL ](extra/Documentation/DRV8833_DC.md) |
| DC Brushed Motor | TB6612FNG Dual motor driver carrier| [ URL ](extra/Documentation/TB6612FNG_DC.md) |
| DC Brushed Motor | MX1508 Motor controller module| [ URL ](extra/Documentation/MX1508_DC.md) |
| DC Brushed Motor | Transistor control | [ URL ](extra/Documentation/Transistor_DC.md) |

### Servos

There are two different options for controlling the servo.
When using the rpi-lgpio/RPi.GPIO option you may notice twitching at certain
delays and step sizes. This is the result of software PWM timing.
If the application requires precise control the user can pick the pigpio library
which uses hardware based timing. The disadvantage is they must install
a dependency (pigpio) and start its daemon.
**Note: pigpio does not support Raspberry Pi 5.**

| Servo | Pi 5 | Link |
| ----- | ----- | ----- |
| Servo software timing | ✅ | [ rpi-lgpio / RPi.GPIO PWM ](extra/Documentation/Servo_RPI_GPIO.md) |
| Servo hardware timing | ❌ | [ pigpio library PWM ](extra/Documentation/Servo_pigpio.md) |

## Software

1. Separate help files are in the documentation folder to learn how to use the library.
   Click on the relevant URL link in the tables in the hardware section.
2. Hardware example scripts are in the `examples/` folder of the repository.
3. There is a "Software matrix" showing which classes are used to drive which components.
   This is in the Software_Matrix.md file in extra/Documentation folder.

### File System

RpiMotorLib files are listed below:

| File Path | Description |
| ------ | ------ |
| RpiMotorLib/RpiMotorLib.py | Stepper motor library file |
| RpiMotorLib/rpiservolib.py | Servo library — software PWM via rpi-lgpio/RPi.GPIO |
| RpiMotorLib/rpi_pservo_lib.py | Servo library — hardware PWM via pigpio (Pi 1-4 only) |
| RpiMotorLib/rpi_dc_lib.py | DC motor library file |
| RpiMotorLib/gpio_adapter.py | GPIO abstraction layer — supports rpi-lgpio, RPi.GPIO, lgpio |
| RpiMotorLib/settings.py | Settings manager — reads ~/.config/rpiMotorLib/config.ini |
| RpiMotorLib/rpi_emergency_stop.py | Emergency stop push button class |
| RpiMotorLib/RpiMotorScriptLib.py | Script to display version and help information |
| extra/Documentation/ | Markdown library documentation files |
| examples/ | Hardware example scripts organised by motor type |
| tests/ | Pytest unit tests with mocked GPIO — run on any machine |

A small script is installed to display version and help information.
Run the information script by typing:

```sh
rpimotorscript -[options]
```

| Option | Description |
| --------------- | --------------- |
| -h  | Print help information and exit |
| -v  | Print version information and exit |

### Dependencies

| Dependency | Required | Pi 5 | Notes |
| ----- | ----- | ----- | ----- |
| rpi-lgpio >= 0.4 | Recommended | ✅ | Drop-in RPi.GPIO replacement, works on all Pi models |
| RPi.GPIO | Legacy alternative | ❌ | Pre-installed on most Pi 1-4 systems |
| pigpio >= 1.78 | Optional | ❌ | Hardware PWM servo only, Pi 1-4 only |

The GPIO backend is selected automatically at runtime in the following priority order:

1. `RPIMOTORLIB_GPIO_BACKEND` environment variable (if set)
2. `~/.config/rpiMotorLib/config.ini` (created automatically on first run)
3. Auto-detect: tries rpi-lgpio/RPi.GPIO first, then lgpio

Valid backend values in config: `null` (auto-detect), `rpigpio`, `lgpio`.

## Notes and issues

### Servo trace back issue

rpi-lgpio 0.6 may produces a harmless `TypeError` traceback
after `GPIO.cleanup()` when PWM has been used. This is a known upstream
bug in rpi-lgpio (see [PR #23](https://github.com/waveform80/rpi-lgpio/pull/23))
and does not affect motor or servo operation. A fix exists in the PR but
has not yet been merged by the upstream maintainer.

### Two Motors simultaneously

Running two stepper motors simultaneously — see github issue #11.
If you want to control two or more steppers simultaneously, there are two
example scripts using threading in `examples/Multi_Threading_Example/`:

1. For Unipolar 28BYJ-48: `MultiMotorThreading_BYJ.py`
2. For Bipolar DRV8825 Stepper: `MultiMotorThreading_DRV8825.py`

### GPIO cleanup method

As of v4.0.0 the library manages GPIO cleanup internally via the GPIO
abstraction layer. User scripts no longer need to call `GPIO.cleanup()`
directly — the motor class `cleanup()` methods and `estop.cleanup()` handle
this correctly for all backends.

For users on older versions experiencing GPIO cleanup issues see github
issues #18 and #21.

### Emergency Stop

All example scripts include support for an motor movement stop push button.

[Emergency Stop README](extra/Documentation/estop/estopreadme.md)

### pipx

[pipx README](extra/Documentation/pipx/pipxreadme.md)

## See Also

1. Partial port to Raspberry Pi PICO SDK C++ at [link.](https://github.com/gavinlyonsrepo/Stepper_Motor_Control_PICO)
