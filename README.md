RpiMotorLib, A Raspberry pi python motor library
--------------------------------------------------

![ScreenShot dcmotor](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/RF310T11400.jpg)
![ScreenShot Nema](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/nema11.jpg)
![ScreenShot L298N](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/L298N.jpg)
![ScreenShot A4988](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/A4988.jpg)

Table of contents
---------------------------

  * [Table of contents](#table-of-contents)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Files](#files)
  * [Dependencies](#dependencies)
  * [Components](#components)
  * [Notes](#notes)

Overview
--------------------------------------------
* Name: RpiMotorLib
* Title: Raspberry pi motor library.
* Description: 

A python 3 library for various common motor controllers and servos to connect to a raspberry pi.
These components are some of the most widely used by community.
There are three categories in library.
Stepper motors, DC Motors and Servos.
The end user can import this library into their projects 
and then control the components with short snippets of code.
The library is modular so user can just import/use the section they need.

* Main Author: Gavin Lyons , [website.](https://gavinlyonsrepo.github.io/).
* Project URL: [URL LINK](https://github.com/gavinlyonsrepo/RpiMotorLib)
* History: CHANGELOG.md is at repository in documentation.
* Copyright: Copyright (C) 2018 Gavin Lyons. See LICENSE.md in documentation.
* Pull requests,bug reports, suggestions for new components and features welcome. 

Installation
-----------------------------------------------

The library was initially tested and built on a raspberry pi 3 model b,
Raspbian jessie 8.0 and python 3.4.2.
It was also tested for Python (3.5.3) and Raspbian stretch 9.
Also for Windows 10 users See issue number 2 at project Github URL.

Make sure that python 3 and pip have been installed on your machine, then:

```sh
sudo pip install rpimotorlib
```

Files
-----------------------------------------
rpiMotorLib files are listed below:

| File Path | Description |
| ------ | ------ |
| RPiMotorLib/RpiMotorLib.py |  stepper motor python library file |
| RPiMotorLib/rpiservolib.py | servo python library RPi.GPIO  PWM file |
| RPiMotorLib/rpi_pservo_lib.py | servo python library pigpio PWM file |
| RPiMotorLib/rpi_dc_lib.py  |    DC python motor library  file |
| documentation/*.md | 14 markdown library documentation files |
| test/*Test.py | 12 python test files |
| /usr/share/doc/RpiMotorLib/README.md | This help file |
| RPiMotorLib/RpiMotorScriptLib.py | small script with meta data about library |

A small script is installed to display version and help information.
Run the information script by typing.
RpiMotorScriptLib.py -[options]

| Option          | Description     |
| --------------- | --------------- |
| -h  | Print help information and exit |
| -v  | Print version information and exit |


Dependencies
-----------

1. RPi.GPIO 0.6.3  [Rpi.GPIO pypi page](https://pypi.python.org/pypi/RPi.GPIO)

A module to control Raspberry Pi GPIO channels.
This package provides a class to control the GPIO on a Raspberry Pi.
This should already be installed on most Raspberry Pis.

2. pigpio 1.60-1 [Homepage](http://abyz.co.uk/rpi/pigpio/)

This Dependency is *Optional*, it is currently 
only used in one of the two servo control options.
pigpio is a library for the Raspberry which allows 
control of the General Purpose Input Outputs (GPIO).

Components
----------------------

Şeparate help files are in documentation folder to learn how to use library.
Click on the relevant URL link in tables below.
Test files used during development are in test folder of repo.
Example snippets are also available in some of the documentation files.
There is a libre office spreadsheet file in the Documentation folder called Matrix, 
which shows which class is used for which controller, 
or consult the docstring of the appropriate python file.

1. Stepper motors

| Motor | Motor controller| Help File URL link |
| ----- | ----- | ----- |
| Unipolar 28BYJ-48 | ULN2003 driver module | [ URL ](Documentation/28BYJ.md)| 
| Bipolar Nema 11 | TB6612FNG Dual Driver Carrier | [ URL ](Documentation/Nema11TB6612FNG.md) |
| Bipolar Nema 11 | L298N H-Bridge controller module | [ URL ](Documentation/Nema11L298N.md) |
| Bipolar Nema 11 | A4988 Stepper Driver Carrier | [ URL ](Documentation/Nema11A4988.md)|
| Bipolar Nema 11 | DRV8825 Stepper Driver Carrier | [ URL ](Documentation/Nema11DRV8825.md) |
| Bipolar Nema 11 | A3967 Stepper Driver aka "easy driver v4.4" | [ URL ](Documentation/Nema11A3967Easy.md)|

Note: NEMA 11 bipolar stepper motors where used in tests but most other bipolar 4-pin motors of similar type 
should work as well.
    
2. DC motors

| Motor | Motor controller| Help File URL link |
| ----- | ----- | ----- |
| DC Brushed Motor | L298N Motor controller module. | [ URL ](Documentation/L298N_DC.md) |
| DC Brushed Motor | L9110S Motor controller module. | [ URL ](Documentation/L9110S_DC.md) |
| DC Brushed Motor | DV8833 Motor controller module. | [ URL ](Documentation/DRV8833_DC.md) |
| DC Brushed Motor | TB6612FNG Dual Motor Driver Carrier| [ URL ](Documentation/TB6612FNG_DC.md) |
| DC Brushed Motor | A transistor. | [ URL ](Documentation/Transistor_DC.md) |

3. Servos

| Servo | Link |
| ----- | ----- |
| Servo software timing | [  RPi.GPIO module PWM ](Documentation/Servo_RPI_GPIO.md) |
| Servo hardware timing | [  pigpio library module PWM ](Documentation/Servo_pigpio.md) |

Note: There are two different options for controlling the servo.
When using Rpi_GPIO option you may notice twitching at certain
delays and stepsizes. This is the result of the 
implementation of the RPIO PWM software timing. If the application requires
precise control the user can pick the pigpio library
which uses hardware based timing. The disadvantage being they must install 
a dependency.
 
