Servos
----------------------------------

![ScreenShot servo](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/sg90.jpg)
![ScreenShot servo1](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/hs422.jpg)
![ScreenShot servo2](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/screenshot/mg996.jpg)

Hardware
------------------------------------

Should Work on any servo with 20mS duty cycle or 50Hz frequency
Tested on:
	(1) Tower pro Digital micro servo SG90 
	(2) Hitec HS422 servo
	(3) Tower pro MG996R Servo

(Check if your servo matches the freq/duty cycle specifications)

[Datasheet SG90](http://www.micropik.com/PDF/SG90Servo.pdf)
[Datasheet Hs422](https://cdn.sparkfun.com/datasheets/Robotics/hs422-31422S.pdf)
[Datasheet MG996R](http://www.datasheetcafe.com/mg996r-datasheet-digital-servo/)

The servo has 3 wires one for gnd(brown) 5v power(red) and signal(orange/yellow).  
I have verified that it is safe to drive a single servo from the 5 volt rail on Rpi.
However It is possible to damage your Raspberry Pi by drawing 
too much current out of a pin(spikes or low current power supply on the pi). 
It is best to power it from a 5 Volt source other than a Raspberry Pi rail. 
You can still control it from the Raspberry Pi if you use a common ground, 
but just get the power (red wire) from an external source. 
The Pi draws approximately 700 mA from the +5 V supply. You may draw current from the +5 V pins provided 
the sum of that current and the board's 700 mA doesn't exceed the supply you provide to the board. 

From the data sheet, we see these servos expects a frequency of 50 Hz 
on the control line and the position it moves to depends on the pulse width of the signal.
50Hz gives a period of 20mS (Freq = 1/Period)

These servo has a range of 180 degrees.

The Raspberry Pi controls the servo by outputting a PWM signal of varying 
duty cycle on a GPIO pin connected to signal pin of servo.

For the Raspberry Pi we do not have a change pulse width method for PWM, 
but we can change the Duty Cycle. Note that:

Duty Cycle = Pulse Width * Frequency

Given a 50 Hz frequency we can calculate the required duty cycle for any pulse width. For example:

We need a 1.5 ms pulse to center the servo, 
or a Duty Cycle = 0.0015 * 50 = 0.075 (i.e 7.5%).
Similarly, 1 ms pulse (- 90 degrees or 0 degrees) 
requires a Duty Cycle = 0.001 * 50 = 5%
2 ms pulse (+ 90 degrees or 180), Duty Cycle = 0.002 * 50 = 10%

Thus the duty cycle range should be from 5 - 10% with the center at 7.5%. 

Every servo is different, so you will need to calibrate it for the best performance.
I found 7.5 for center , 
11 for max duty percentage or left position (180 degress)
and 2 for min duty percentage or right postion (0 degrees)
Check datasheet for recommend pulse width and calibrate accordingly.

 
Software
--------------------------------------------

The library file has a single class which controls the servo with two different 
functions. The class is called SG90servo but works for all listed as tested.

The class is called SG90servo and the functions are 

(1) servo_sweep - sets up a continuous sweep from two points
Center-wait-min-wait-max- and so on until user quits

(2) servo_move - moves to a specified location


### 1 - servo_sweep

function, servo_sweep, 6 inputs
sets up a continuous sweep from two points, 
Center-delay-min-delay-max-delay- and so on until user quits

 servo_sweep(servo_pin, center, minduty, maxduty, delay, verbose)

 (1) servo_pin, type=int help=GPIO pin
 we will contect to signal line of servo
 
 (2) center, type=float, default=7.5,
 help=The center dutycycle position of servo
 
 (3) minduty, type=float, default=3,
 help=The min dutycycle position of servo
 
 (4) maxduty, type=float, default=11,
 help=The max dutycycle position of servo
 
 (5) delay, type=float, default=0.5,
 help=Time to wait (in seconds) between steps.
 
 (6) verbose, type=bool  type=bool default=False
  help="Output actions & details",


 example (Version 1.1): to sweep the servo connected to GPIO pins 7
 for step delay of .5 second from minduty position
 2 to maxduty position 12 and  center position 6
 with verbose output set to True
 
```sh

import time 
import RPi.GPIO as GPIO

# This code snippet is for Version 1.1 

# import the library
from RpiMotorLib import RpiMotorLib 

# initialize an instance of the class passing a name
myservotest  = RpiMotorLib.SG90servo("servoone")
time.sleep(0.5)

# call the function pass by value in this case.
myservotest.servo_sweep(7, 6, 2, 12, .5, True)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
```

### 2 - servo_move


function servo_move 4 inputs

 servo_move(servo_pin, position, delay, verbose)

 (1) servo_pin, type=int help=GPIO pin
 we will contect to signal line of servo
 
 (2) position, type=float, default=7.5,
 help=The  dutycycle position of servo to move to
 
 (3) delay, type=float, default=0.5,
 help=Time to wait (in seconds) between steps.
 
 (4) verbose, type=bool  type=bool default=False
  help="Output actions & details",


 example(Version 1.1): to move the servo connected to GPIO pins 7
 for step delay of 1 second to postion 11
 with non-verbose output
 
```sh
import time 
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

# This code snippet is for Version 1.1 

# initialize an instance of the class passing a name
myservotest = RpiMotorLib.SG90servo("servoone")
time.sleep(0.5)

# call the function pass by value in this case.
myservotest.servo_move(7, 11, 1, False)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
```

