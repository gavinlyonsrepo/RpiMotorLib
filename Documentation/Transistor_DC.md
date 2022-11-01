DC motor controlled by Transistor
-------------------------------------------------

![ScreenShot dcmotor](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/RF310T11400.jpg)
![ScreenShot Tran](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/tran.jpg)


Hardware
--------------------------------------------

![ScreenShot sch](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/motor_gpio.jpg)

DC motor controlled by Transistor connected to a GPIO pin and feed a PWM 
signal for speed control. No direction.
Used for fans and applications where direction not needed.   
This video explains setup and theory well.

[youtube Video](https://www.youtube.com/watch?v=W7cV9_W12sM)

This library was tested on a number of motors including the RF-310T-11400
  
Software
-------------------------------------------

The file rpi_dc_lib.py contains code for this component
It consists of a class called TranDc and two methods

Class init:
| ID  | Name   | Type  | Default | Help  |
| ----- | ----- | -- | --- | --- |
| (1) | pin | int |  | GPIO pin connected base of transistor |
| (2) | freq  | int | 50| PWM freq in Hz of control signal |
| (3) | verbose | bool | False |  Write pin actions to console|

The two methods are called 
1. dc_motor_run = Drive motor forward, two args = duty cycle % , step delay in seconds
2. dc_clean_up = switchs GPIO pins off

More example code is in the Transistor_DC test.py file in test subfolder of 
rpiMotorLib repository.

This code will run motor up to max duty cycle % hold it for 
5 seconds and then run it down to zero and then cleanup.

```sh

import time 
import RPi.GPIO as GPIO

# import library
from RpiMotorLib import rpi_dc_lib

step_delay = .05
# intialise class object
MotorOne = rpi_dc_lib.TranDc(TranDc(26 ,200 ,True)

input("Press key to accelerate to 100") 
for speed in range(0,100):
    MotorOne.dc_motor_run(speed, step_delay)
time.sleep(5)
input("Press key to decelerate to 0") 
for speed in range(100,0,-1):
    MotorOne.dc_motor_run(speed, step_delay)
MotorOne.dc_clean_up() 

GPIO.cleanup()
exit()

```



