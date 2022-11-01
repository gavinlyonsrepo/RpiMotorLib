Servos
----------------------------------

![ScreenShot servo](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/sg90.jpg)


Hardware
------------------------------------

Should Work on any servo with 20mS duty cycle or 50Hz frequency, tested on.

* Tower pro Digital micro servo SG90 

(Check if your servo matches the freq/duty cycle specifications, most should)

[Datasheet SG90,](http://www.micropik.com/PDF/SG90Servo.pdf)

The following data applies to the SG90 servo.

The servo has 3 wires one for gnd(brown) 5v power(red) and signal(orange/yellow).  
It is generally safe to drive a single small servo from the 5 volt rail on Rpi.
However It is possible to damage your Raspberry Pi by drawing 
too much current out of a pin(spikes or low current power supply on the pi). 
It is best to power it from a 5 Volt source other than a Raspberry Pi rail. 
You can still control it from the Raspberry Pi if you use a common ground, 
but just get the power (red wire) from an external source. 
The Pi draws approximately 700 mA from the +5 V supply. You may draw current from the +5 V pins provided 
the sum of that current and the board's 700 mA doesn't exceed the supply you provide to the board. 

From the data sheet , we see these servos expects a frequency of 50 Hz 
on the control line and the position it moves to depends on the pulse width of the signal.
50Hz gives a period of 20mS (Freq = 1/Period)
These servo has a range of 180 degrees.

The Raspberry Pi controls the servo by outputting a PWM signal of varying 
duty cycle on a GPIO pin connected to signal pin of servo.
For the Raspberry Pi we do not have a change pulse width method for PWM, 
but we can change the Duty Cycle. Note that: Duty Cycle = Pulse Width * Frequency

Given a 50 Hz frequency we can calculate the required duty cycle for any pulse width. For example:
We need a 1.5 ms pulse to center the servo, 
or a Duty Cycle = 0.0015 * 50 = 0.075 (i.e 7.5%).
Similarly, 1 ms pulse (- 90 degrees or 0 degrees) 
requires a Duty Cycle = 0.001 * 50 = 5%
2 ms pulse (+ 90 degrees or 180), Duty Cycle = 0.002 * 50 = 10%
Thus the duty cycle range should be from 5 - 10% with the center at 7.5%. 

Every servo is different, so you will need to calibrate it for the best performance.
It was found 7.5 for center , 
11 for max duty percentage or left position (180 degress)
and 2 for min duty percentage or right postion (0 degrees)
Check datasheet for recommend pulse width and calibrate accordingly.

The software includes a method to convert degrees to pulse duty cycle percentage.
for user convenience, this method is also used internally in one of the other methods
If user prefers working in degrees they can pass result to the other methods
which want pulse duty cycle percentage.

This works as follows imagine we have two points on a graph. 
(x1, y1) (x2, y2). 
Where 1 is servo right position 0 degree. 
Where 2 is servo left position  180 degree. 
Where x is degree and y is pulse duty cycle percentage. 
Y 1 and Y2 are calibrated by user = default (2, 12). 

(x1 , y1) = ( 0,2 )  
(x2, y2) =  (180,12).

To get slope of line m = (y2-y1)/(x2-x1).
The equation of the line using the point slope formula = y-y1=m(x-x1) .
We want to find point (x,y)
Where y is required pulse duty cycle percentage and x is the given degree.
For default values this works out as DutyCycle = 1/18* (DesiredAngle) + 2.
So for default values 90 degree or midpoint is 7.0. 

Software
--------------------------------------------

Note: There are two different options for controlling the servo.
When using Rpi_GPIO option you may notice twitching at certain
delays and stepsizes. This is the result of the 
implementation of the RPIO PWM software timing. If the application requires
precise control the user can pick the pigpio library
which uses hardware based timing. The disadvantage being they must install 
another an extra dependencies.

The library file has a single class which controls the servo 
The class is called SG90servo but works for all listed as tested.
The test file is ServoGPIOTest.py.

The class is called SG90servo and their are five methods are 

| ID  | Method  |  Help  | 
| --- | ---------- |  ----- |
| (1) |  servo_sweep |   sets up a continuous sweep from two points |
| (2) |  servo_move |   moves to a specified location in a single sweep   |
| (3) |  convert_from_degree |  converts degrees to duty cycle percentage   |
| (4) |  servo_move_step |  moves servo from two points in timed steps.  |
| (5) |  servo_stop |   this will stop the servo  |

### Import library and intialise the class 

```sh
from RpiMotorLib import rpiservolib 
myservotest  = rpiservolib.SG90servo("servoone", 50, 2, 12)
```

The class takes four parameters on init

| ID  | Name  | Type  | default  | Help   |       
| --- | --- | --- | --- | --- | 
| (1) | name |string | G90servoX | |
| (2) | freq | int  | 50 | control freq of servo in Hz |
| (3) | y_one | float | 2 | pulse min duty cycle % of servo for 0 degrees |
| (4) | y_two | float | 12 | pulse max duty cycle % of servo for 180 degrees |

y_one and y-two are used by methods numbered 3 and 4. 

### 1 - servo_sweep

Method, servo_sweep, 8 inputs, sets up a sweep from two points, 
Center-delay-min-delay-max-delay- and so on until user quits or set-limit reached.

 servo_sweep(servo_pin, center, minduty, maxduty, delay, verbose, initdelay, sweeplen)

| ID  | Name  | Type  | Default  | Help   |       
| --- | --- | --- | --- | --- | 
| (1) | servo_pin | int | 7 | GPIO pin we will contect to signal line of servo |
| (2)  | center | float | 7.5 | The center dutycycle position of servo |
| (3)  | minduty  | float | 3 | The min dutycycle position of servo |
| (4)  | maxduty  | float | 11 | The max dutycycle position of servo |
| (5)  | delay | float | 0.5 | Time to wait (in seconds) between steps. |
| (6)  | verbose | bool | False  | Output actions & details |
| (7)  | initdelay  | float | 50mS | A delay after Gpio setup and before servo moves |
| (8)  | sweeplen | int | 1 million |   is number of times to execute sweep. |

 example:Setup a class instance called servoone with control freq 50mS
 with y_one set to 3 and Y_two to 11. Next call method
 to sweep the servo connected to GPIO pins 7
 for step delay of 0.5 second from minduty position
 2 to maxduty position 12 and center position 6
 with verbose output set to True and initdelay set to 0.01mS , 100 times
 
```sh

import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib 

myservotest  = rpiservolib.SG90servo("servoone", 50, 3, 11)

# call the function pass by value in this case.
myservotest.servo_sweep(7, 6, 2, 12, 0.5, True, 0.01, 100)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
```

### 2 - servo_move

Method servo_move 5 inputs.

 servo_move(servo_pin, position, delay, verbose, initdelay)
 
| ID  | Name  | Type  | Default  | Help   |       
| --- | --- | --- | --- | --- | 
| (1) | servo_pin | int | 7 | GPIO pin we will contect to signal line of servo |
| (2)  | position  | float | 7.5 | The center dutycycle position of servo |
| (3)  | delay | float | 0.5 | Time to wait (in seconds) after move |
| (4)  | verbose | bool | False  | Output actions & details |
| (5)  | init delay  | float | 50mS | A delay after Gpio setup and before servo moves |

 example: to move the servo connected to GPIO pins 7
 for step delay of 1 second to postion 11
 with non-verbose output and initdelay of 10mS
 
```sh
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import rpiservolib 

# initialize an instance of the class passing a name
myservotest = rpiservolib.SG90servo("servoone", 50, 3, 11)

# call the function pass by value in this case.
myservotest.servo_move(7, 11, 1, False, .01)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
```

### 3 convert_from_degree

converts degrees to duty cycle percentage
Input degrees,
returns duty cycle percentage as floats

```sh
from RpiMotorLib import rpiservolib 
myservotest = rpiservolib.SG90servo("servoone", 50, 3, 11)
degree = float(input("What degree do you want?\t"))
print("Duty cycle percent = {} ".format(myservotest.convert_from_degree(degree)))
```

### 4 servo_move_step 

servo_move_step(servo_pin, start, end, stepdelay, stepsize, initdelay, verbose=)

servo_move_step - moves servo from two points in timed steps,
seven inputs. 

| ID  | Name  | Type  | Default  | Help   |       
| --- | --- | --- | --- | --- | 
| (1) | servo_pin | int | n/a | GPIO pin we will contect to signal line of servo |
| (2)  | start | float | 10 | start position of servo in degree |
| (3)  | end  | float | 170 | end position of servo in degrees  |
| (4)  | stepdelay  | float | 1 | Time to wait (in seconds) between steps |
| (5)  | stepsize | int | 1 | The size of steps between start and end in degrees |
| (6)  | initdelay  | float | 50mS | A delay after Gpio setup and before servo moves |
| (7)  | verbose | bool | False  | Output actions & details |

Example: to move a servo on GPIO pin 26 from 10 degrees to 170 
degrees in 3 degree steps every two seconds, with an initial delay 
of one second and verbose output.   

```sh
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import rpiservolib 

# initialize an instance of the class 
myservotest = rpiservolib.SG90servo("servoone", 50, 3, 11) 

myservotest.servo_move_step.servo_move_step(26, 10, 173, 2, 3, 1, True)

```        
