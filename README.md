

[![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://gavinlyonsrepo.github.io/)  [![Rss](https://img.shields.io/badge/Subscribe-RSS-yellow.svg)](https://gavinlyonsrepo.github.io//feed.xml)  [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/paypalme/whitelight976)

# RpiMotorLib


![ScreenShot dcmotor](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/RF310T11400.jpg)
![ScreenShot Nema](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/nema11.jpg)
![ScreenShot L298N](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/L298N.jpg)
![ScreenShot A4988](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/A4988.jpg)

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
    * [RPI 5](#rpi-5)
    * [Two Motors simultaneously](#two-motors-simultaneously)
    * [GPIO cleanup method](#gpio-cleanup-method)
    * [pipx](#pipx)


## Overview

* Name: RpiMotorLib
* Title: Raspberry pi motor library.
* Description: 

A python 3 library to drive motor controllers and servos with a Raspberry pi.

These components supported are some of the most widely used by maker community.
There are three categories in library. Stepper motors, DC Motors and Servos.
The end user can import this library into their projects 
and then control the components with short snippets of code.
The library is modular so user can just import/use the section they need.

* Project URL: [URL LINK](https://github.com/gavinlyonsrepo/RpiMotorLib)


* Tested on Toolchains: 
    1. RPI 3 model B. Raspbian 10 Buster, 32 bit. Python 3.7.3.
    2. RPI 3 model B. Raspbian 12 Bookworm, 64 bit. Python 3.11.2.

## Installation

Latest version 3.2 (10-2022)

### From PyPi with pip or pipx

The Python Package Index (PyPI) is a repository of software for the Python programming language.
The program is present in python package index, Pypi.
Install using *pip* or *pipx* to the location or environment of your choice.
Package name = rpimotorlib [Link](https://pypi.org/project/rpimotorlib/).

NB see notes section for more on pipx. 

### From Github

Manually install from github
The package is also archived on github and can be manually download and installed 
via python and setup.py. Not recommended.

```sh
curl -sL https://github.com/gavinlyonsrepo/RpiMotorLib/archive/3.3.tar.gz | tar xz
cd RpiMotorLib-3.3
python3 setup.py build 
python3 setup.py install --user
```

## Hardware

Supported Components: 

### Stepper motors

| Motor tested | Motor controller| Help File URL link |
| ----- | ----- | ----- |
| Unipolar 28BYJ-48 | ULN2003 driver module | [URL](Documentation/28BYJ.md)| 
| Bipolar Nema  | TB6612FNG Dual Driver Carrier | [URL](Documentation/Nema11TB6612FNG.md) |
| Bipolar Nema  | L298N H-Bridge controller module | [URL](Documentation/Nema11L298N.md) |
| Bipolar Nema  | A4988 Stepper Driver Carrier | [URL](Documentation/Nema11A4988.md)|
| Bipolar Nema  | DRV8825 Stepper Driver Carrier | [URL](Documentation/Nema11DRV8825.md) |
| Bipolar Nema  | A3967 Stepper Driver aka "easy driver v4.4" | [URL](Documentation/Nema11A3967Easy.md)|
| Bipolar (untested on hw)| LV8729 Stepper Driver Carrier  | [URL](Documentation/Nema11LV8729.md)|
| Bipolar (untested)| DV8833 Motor controller module | TODO |
| Bipolar (untested)| L9110S Motor controller module | TODO |
| Bipolar | MX1508 Motor controller module | [URL](Documentation/Nema11MX1508.md |

### DC motors

| Motor | Motor controller| Help File URL link |
| ----- | ----- | ----- |
| DC Brushed Motor | L298N Motor controller module. | [ URL ](Documentation/L298N_DC.md) |
| DC Brushed Motor | L9110S Motor controller module. | [ URL ](Documentation/L9110S_DC.md) |
| DC Brushed Motor | DV8833 Motor controller module. | [ URL ](Documentation/DRV8833_DC.md) |
| DC Brushed Motor | TB6612FNG Dual motor driver carrier| [ URL ](Documentation/TB6612FNG_DC.md) |
| DC Brushed Motor | MX1508 Motor controller module| [ URL ](Documentation/MC1508_DC.md) |
| DC Brushed Motor | Transistor control | [ URL ](Documentation/Transistor_DC.md) |

### Servos

There are two different options for controlling the servo.
When using Rpi_GPIO option you may notice twitching at certain
delays and stepsizes. This is the result of the 
implementation of the RPIO PWM software timing. If the application requires
precise control the user can pick the pigpio library
which uses hardware based timing. The disadvantage being they must install 
a dependency(pigpio) and start its daemon.


| Servo | Link |
| ----- | ----- |
| Servo software timing | [  RPi.GPIO module PWM ](Documentation/Servo_RPI_GPIO.md) |
| Servo hardware timing | [  pigpio library module PWM ](Documentation/Servo_pigpio.md) |


## Software

1. Separate help files are in documentation folder to learn how to use library.
    Click on the relevant URL link in tables in hardware section.
2. Test files used during development are in test folder of repository.
3. There is a "Software matrix" showing which classes are used to drive which components.
    This is in the Software_Matrix.md file in documentation folder.


### File System


RpiMotorLib files are listed below:

| File Path | Description |
| ------ | ------ |
| RPiMotorLib/RpiMotorLib.py |  stepper motor python library file |
| RPiMotorLib/rpiservolib.py | servo python library RPi.GPIO  PWM file |
| RPiMotorLib/rpi_pservo_lib.py | servo python library pigpio PWM file |
| RPiMotorLib/rpi_dc_lib.py  |    DC python motor library  file |
| documentation/*.md | 15 markdown library documentation files |
| test/*Test.py | 14 python test files |
| /usr/share/doc/RpiMotorLib/README.md | This help file |
| RPiMotorLib/RpiMotorScriptLib.py | small script with meta data about library |

A small script is installed to display version and help information.
Run the information script by typing.
RpiMotorScriptLib.py -[options]

| Option          | Description     |
| --------------- | --------------- |
| -h  | Print help information and exit |
| -v  | Print version information and exit |


### Dependencies


1. RPi.GPIO 0.6.3  [Rpi.GPIO pypi page](https://pypi.python.org/pypi/RPi.GPIO)

A module to control Raspberry Pi GPIO channels.
This package provides a class to control the GPIO on a Raspberry Pi.
This should already be installed on most Raspberry Pis.

2. pigpio 1.64-1 [Homepage](abyz.co.uk/rpi/pigpio/)

This Dependency is *Optional*, it is currently 
only used in one of the two servo control options.
pigpio is a library for the Raspberry which allows 
control of the General Purpose Input Outputs (GPIO).


## Notes and issues

### RPI 5

Will NOT work on raspberry pi 5's at present as  RPi.GPIO does not work anymore due to change's in way raspberry pi 5  handles the peripheral access. See github issue #26

### Two Motors simultaneously

Running two motors simultaneously, See github issue #11

If you want to control two or more steppers simultaneously, there are two basic setup
files for using threading in test/Multi_Threading_Example folder. 

1. For Unipolar 28BYJ-48  MultiMotorThreading_BYJ.py
2. For Bipolar DRV8825 Stepper MultiMotorThreading_DRV8825.py

### GPIO cleanup method

Potential Issue with GPIO.cleanup() method not working* See github issue #18 and #21

Some users are reporting that GPIO.cleanup() does not work.
It does not switch off or "cleanup" GPIO as it should.
This is external function from RPi.GPIO. It is mainly used in the test scripts.
It is also called by the classes in DC motor if the cleanup method is passed argument "true".
If you see this issue simply don't use GPIO.cleanup() or remove GPIO.cleanup 
and clear the GPIO you set manually or use python "del" method to destroy the relevant class object,
to free resources if you need them again.

### pipx

As of pep668, Users on many systems will now get an error if they try and install packages on system
with pip("~environment is externally managed"). One solution is to use pip to install to a virtual environment.

Another is to use package. **PIPX**, which installs packages globally into isolated Virtual Environments.

The first problem I had was getting my test files to "see" this isolated Virtual environment so they could import the modules. In test/pipx
I have created two pipx examples files showing a solution. In example 1 I append the package location to sys.path using sys.path.insert
and in example 2 I simply change the shebang at first line of file(the new shebang is from the pipx installed RpiMotorScriptLib.py file at .local/bin).
I will learn more about pipx and see if there is a better solution.

The second problem after finding the correct path is the dependency RPi.GPIO module is not in the pipx venv. So must be "injected" into the venv.
this is because I did not include RPi.GPIO in the setup.py as it is always there globally(for most users).
I will correct this in next update.

```sh
pipx install rpimotorlib
pipx inject rpimotorlib RPi.GPIO
```

 

