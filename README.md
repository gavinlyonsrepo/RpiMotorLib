![ScreenShot dcmotor](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/RF310T11400.jpg)
![ScreenShot Nema](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/nema11.jpg)
![ScreenShot L298N](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/L298N.jpg)
![ScreenShot A3967](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/A3967.jpg)
![ScreenShot A4988](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/A4988.jpg)

Overview
--------------------------------------------
* Name: RpiMotorLib
* Title: Raspberry pi motor library. 
* Description: A python 3 library for various motors and servos 
to connect to a raspberry pi.
There are three categories in library.
Stepper motors , Dc Motors and Servos. The following is a list of tested parts

1. Stepper motor
    * Unipolar 28BYJ-48 Stepper motor controlled by ULN2003 driver module
    * Bipolar Nema 11 Stepper motor controlled by L298N H-Bridge Motor controller module.
    * Bipolar Nema 11 Stepper motor controlled by A4988 Stepper Motor Driver Carrier 
    * Bipolar Nema 11 Stepper motor controlled by DRV8825 Stepper Motor Driver Carrier
    * Bipolar Nema 11 Stepper motor controlled by A3967 Stepper Motor Driver Carrier "easy driver version 4.4" 
    
2. DC motors
    * DC brushed motor controlled by L298N Motor controller module.
    * DC brushed motor controlled by a transistor.

3. Servo GPIO PWM
        * Tower pro Digital SG90 micro servo 
        * Hitec HS422 servo
        * Tower pro MG996R Servo

The end user can import this library into their projects 
and then control the components with short snippets of code.
The library is modular so user can just import the section they need.
A lot of this code will work on similar components/modules but has not. 
been tested due to parts lacking or time constraints.
For example:

The A4988 code **may** work with other pololu modules but is **untested** at this point
with any other of the module listed at link.
See this link for list of alternatives for this module 
(and drop-in replacements in many applications) 
[pololu product 1182](https://www.pololu.com/product/1182)

The L298N code should work with a L9110S or similar configured H-bridge modules/circuits

The Servo code should on any servo that I am of aware of.

Many stepper motors should work with the Nema 11 code, nema 17 etc

* Author: Gavin Lyons
* URL: https://github.com/gavinlyonsrepo/RpiMotorLib

Table of contents
---------------------------

  * [Overview](#overview)
  * [Table of contents](#table-of-contents)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Files](#files)
  * [Dependencies](#dependencies)
  * [Features](#features)
  * [To Do](#to-do)
  * [Communication](#communication)
  * [History](#history)
  * [Copyright](#copyright)

Installation
-----------------------------------------------

Make sure that python3 and pip3 have been installed on your machine, then: 

```sh
sudo pip3 install rpimotorlib
```

Usage
-------------------------------------------
Program is a python 3 package. (3.4.2) 

In addition to library files a small script is installed
to display version and help information.

Run the help script by typing 
RpiMotorScriptLib.py -[options]

Options list :

| Option          | Description     |
| --------------- | --------------- |
| -h  | Print help information and exit |
| -v  | Print version information and exit |

To learn how to use the Library in programs.
Go to features section below

Files
-----------------------------------------
rpiMotorLib files are listed below:

| File Path | Description |
| ------ | ------ |
| RPiMotorLib/RpiMotorLib.py |  stepper motor python library file |
| RPiMotorLib/rpiservolib.py | servo python library  file |
| RPiMotorLib/rpi_dc_lib.py  |    DC python motor library  file |
| RPiMotorLib/RpiMotorScriptLib.py | small script with meta data about library |
| documentation/*.md | 6 markdown library documentation files |
| test/*Test.py | 6 python test files |
| /usr/share/doc/RpiMotorLib/README.md | help file |

Dependencies
-----------

RPi.GPIO 0.6.3

A module to control Raspberry Pi GPIO channels

This package provides a class to control the GPIO on a Raspberry Pi.

This should already installed on most Raspberry Pis.

https://pypi.python.org/pypi/RPi.GPIO

Features
----------------------
The library has tested and built on a raspberry pi 3 model b, Raspbian, jessie 8.0 and python 3.4.2

I have created separate help files in documentation folder to learn how to use library :

[Servo GPIO PWM](Documentation/Servo_GPIO.md)

[28BYJ stepper motor ULN2003 ](Documentation/28BYJ.md)

[Nema 11 stepper motor L298N ](Documentation/Nema11L298N.md)

[Nema 11 stepper motor A4988 ](Documentation/Nema11A4988.md)

[Nema 11 stepper motor A3967](Documentation/Nema11A3967Easy.md)

[L298N DC Motor](Documentation/L298N_DC.md)

[Transistor DC Motor](Documentation/Transistor_DC.md)
    
Test files used during development are in test folder of repo.
Example snippets are also available in documentation files


To Do
-----------------------

(1) add and test more components


Communication
-----------------------
If you should find a bug or you have any other query, 
please send a report.
Pull requests, components, suggestions for improvements
and new features welcome.
* Contact: Upstream repo at github site below or glyons66@hotmail.com
* Upstream repository: https://github.com/gavinlyonsrepo/RpiMotorLib


History
------------------
CHANGELOG.md is at repository

Copyright
-------------
Copyright (C) 2018 Gavin Lyons 
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public license published by
the Free Software Foundation, see LICENSE.md in documentation section 
for more details
