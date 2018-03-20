Overview
--------------------------------------------
* Name: RpiMotorLib
* Title: raspberry pi motor library. 
* Description: A python 3 library for various motors and servos 
to connect to a raspberry pi. Currently two components in library
    (1) 28BYJ-48 Stepper motor + ULN2003 driver board
    (2) Tower pro Digital micro servo SG90
* Author: Gavin Lyons
* URL: https://github.com/gavinlyonsrepo/RpiMotorLib

Table of contents
---------------------------

  * [Overview](#overview)
  * [Table of contents](#table-of-contents)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Files and setup](#files-and-setup)
  * [Dependencies](#dependencies)
  * [Features](#features)
  * [See Also](#see-also)
  * [Communication](#communication)
  * [History](#history)
  * [Copyright](#copyright)

Installation
-----------------------------------------------

Make sure that python3 and pip3 have been installed on your machine, then: 

```sh
sudo pip3 install rpimotorlib.py
```

Usage
-------------------------------------------
Program is a python 3 package. 

In addition to library files a small place holder script is installed
to display version and help information

Run the help script by typing RpiMotorScirptLib.py
RpiMotorScirptLib.py -[options]

Options list :

| Option          | Description     |
| --------------- | --------------- |
| -h  | Print help information and exit |
| -v  | Print version information and exit |

To learn how to use the Library in programs.
Go to features section below

Files and setup
-----------------------------------------
rpiMotorLib files are listed below:

| File Path | Description |
| ------ | ------ |
| rpiMotorLib.py |  python library file |
| RpiMotorScirptLib.py | python placeholder information script  |
| maintest.py | python test file, not installed in repo |
| /usr/share/doc/tv_viewer/LICENSE.md | copyright |
| /usr/share/doc/tv_viewer/README.md | help file |


Dependencies
-----------

RPi.GPIO 0.6.3
A module to control Raspberry Pi GPIO channels
This package provides a class to control the GPIO on a Raspberry Pi.
This should be pre-installed on most pies.  

https://pypi.python.org/pypi/RPi.GPIO

Features
----------------------


See Also
-----------


Communication
-----------
If you should find a bug or you have any other query, 
please send a report.
Pull requests, suggestions for improvements
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
