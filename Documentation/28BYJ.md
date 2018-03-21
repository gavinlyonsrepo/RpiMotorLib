28BYJ-48 Stepper motor + ULN2003 driver board
---------------------------------------

![ScreenShot motor](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/screenshot/28BYJ.jpg)


Hardware
------------------------------------

[DataSheet Motor](http://robocraft.ru/files/datasheet/28BYJ-48.pdf)
[DataSheet Motor 2](https://www.bitsbox.co.uk/data/motor/Stepper.pdf)

A stepper motor can move in accurate, fixed angle increments known as steps.
The advantage of steppers over DC motors is that you can achieve much higher 
precision and control over the movement. The downside of using steppers is that they are a bit more complex to 
control than servos and DC motors.

The 28BYJ-48 is a small, cheap, 5 volt, geared stepping motor. 
These stepping motors are widely used to control things like automated blinds, 
A/C units and are mass produced.

The motor has 4 coils of wire that are powered in a sequence to make the magnetic motor shaft spin. 
When using the full-step method, 2 of the 4 coils are powered at each step. 
The 28BYH-48 datasheet specifies that the preferred method for driving this stepper is using the half-step method, 
where we first power coil 1 only, then coil 1 and 2 together, then coil 2 only and so on…With 4 coils, 
this means 8 different signals, like so 


 ![ScreenShot motor diagram](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/screenshot/figure.jpg)


In addition to full step and half step there is also wave drive method.
Where one coil at a time is powered (like a wave) 
All three methods are available in this library.
Full gives the most torque. Half gives less torque but more accuracy 
and wave drive is best for low power applications. half step mode is recommend 
for most projects.

Half-step mode: 8 step control signal sequence 
5.625 degrees per step / 64 steps per one revolution of the internal motor shaft
Full  Step mode and wave drive: 4 step control signal sequence 11.25 degrees per step 
/ 32 steps per one revolution of the internal motor shaft

Gear ratio	Manufacturer specifies 64:1. 
These means that in the recommended half-step mode we will have:
64 steps per motor rotation x 64 gear ratio = 4096 steps per full revolution (approximately). 
So It takes 4096/8 =  512 steps for motor to rotate one revolution due to gear division

for full step 32 X 64 = 2048 , 2048/4 = 512 steps  also

The delay time setting between steps, recommend set to 0.001 second for half-step and 0.01 second
for full and wave. But you can set it to whatever works for you. It was noted in testing
that .001 is too low for full and wave to function.

The ULN2003 stepper motor driver board allows you to easily control the 28BYJ-48 stepper motor.
One side of the board side has a 5 wire socket where the cable from the stepper motor hooks up 
and 4 LEDs to indicate which coil is currently powered.

![ScreenShot motor diagram](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/screenshot/figure2.jpg)

Connect the ULN2003 driver IN1, IN2, IN3 and IN4 to 4 GPIO pins on raspberry pi.
These GPIO pins will be in a list of 4 in the software where [IN1 , IN2 , IN3 ,IN4] = [GPIO0 , GPIO1, GPIO2 , GPIO3]
Connect the positive lead from a decent 5V power source “+” pin of the ULN2003 driver and the ground to the “-” pin.
Make sure that the “on/off” jumper next to the “-” pin is on. 
If you power from raspberry pi connect the grounds together.
It is ok to power one motor from pi 5v rail. 
 
This detailed video  explains more

[video](https://www.youtube.com/watch?v=B86nqDRskVU)

Software
--------------------------------------------

The library file has a single class which controls the motor with one 
function.

The class is called BYJMotor and the function is called 
, motorRun- moves stepper motor based on 6 inputs.


motorRun(GPIOPins, wait, steps, counterclockwise, verbose, steptype)

(1) GpioPins, type=list of ints 4 long, help="list of
 4 GPIO pins to connect to motor controller
 These are the four GPIO pins we will
 use to drive the stepper motor, in the order
 they are plugged into the controller board. So,
 GPIOPins[0] is plugged into Pin 1 on the stepper motor.
 [18, 23, 24, 25]
         
(2) wait, type=float, default=0.001, help=Time to wait
(in seconds) between steps.
         
(3) steps, type=int, default=512, help=Number of steps to take.
Default is one revolution.
         
(4) ccwise (counterclockwise), type=bool default=False
help="Turn stepper counterclockwise"

 (5) verbose, type=bool  type=bool default=False
 help="Write pin actions and provide verbose output",
 
 (6) steptype, type=string , default=half help= type of drive to
 step motor 3 options full step half step or wave drive
 where full = fullstep , half = half step , wave = wave drive.

        
 example: to run A stepper motor connected to GPIO pins 18, 23, 24, 25
 (18-IN1 23-IN2 24-IN3, 25-IN4)
 for step delay of .01 second for 100 steps in clockwise direction,
 verbose output off , in half step mode

    
```sh

import time 
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib
    
GpioPins = [18, 23, 24, 25]
# Declare an named instance of class pass a name
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne")
time.sleep(0.5)

# call the function pass
mymotortest.motorRun(GpioPins , .01, 100, False, False, "half")

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
```

If verbose is set to True various information on pin output and status is outputted to screen

 ![ScreenShot motor diagram](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/screenshot/verbose_output_run.jpg)