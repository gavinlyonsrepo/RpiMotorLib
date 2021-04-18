Bipolar Nema 11 Stepper motor controlled by TB6612FNG Motor controller module.
---------------------------------------

![ScreenShot motor](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/images/nema11.jpg)
![ScreenShot TB6612FNG](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/TB6612FNG.jpg)


Hardware
------------------------------------

This tiny board is an easy way to use Toshiba’s TB6612FNG dual motor driver, 
Which can independently control two bidirectional DC motors or one bipolar stepper motor.
A recommended motor voltage of 4.5 V to 13.5 V and peak current output of 3 A per channel 
(1 A continuous) make this a great motor driver for low-power motors.
This page is for stepper motor configuration.  
The little breakout board gives you direct access to all of the features of the 
TB6612FNG and adds power supply capacitors and reverse battery protection on the 
motor supply. (note: there is no reverse protection on the Vcc connection).
All of the control inputs are internally pulled low. 

The STBY pin and both PWM pins must be driven high for use with a stepper motor.
You can tie them to VCC RPI or use a GPIO. The SW does not facilitate the GPIO 
of these pins. The STBY pin can be used to put it into Standby mode.



Module pinout

![ScreenShot TB6612FNGpinout](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/TB6612FNGpinout.jpg)

| Pin Label | Function | Notes|
| ------ | ------ | ------ |
| VM | Motor voltage | PSU for the motors (2.2V to 13.5V) |
| VCC | Logic voltage |PSU from RPI 3.3V or 5V |
| GND |Ground | Connect all GNDs to common rail (RPI , Motor PSU and Module) |
| STBY | Standby | Allows the H-bridges to work when high (must actively pulled high) connected to RPI GPIO |
| AIN1/BIN1 | Input 1 for channels A/B | inputs  connected to RPI GPIO |
| AIN2/BIN2 | Input 2 for channels A/B| inputs  connected to RPI GPIO |
| PWMA/PWMB | PWM input for channels A/B |inputs connected to RPI GPIO , must be pulled logic high |
| AON1/AON2 | Output channel A | Two outputs to connect the coil of motor |
| BON1/BON2 | Output channel B | Two outputs to connect the coil motor  |

HW Connection (for stepper motor) for the test file(see software section below) are as follows,
(you can pick any GPIO pin you want).

1. VM = motor PSU 
2. VCC = RPI 3.3 or 5 volt
3. GND = GND connect all GND's to a common rail together with PSU and RPI
4. PWA = GPIO or tied to logic high
5. AI1 = 19 GPIO
6. AI2 = 26 GPIO
7. PWB = GPIO or tied to logic high
8. BI1 = 21 GPIO
9. BI2 = 13 GPIO
10. Standby = GPIO or tied to logic high
11. A01 = Coil Number 1 Stepper motor  black wire A(Nema 11)
12. A02 = Coil Number 1 Stepper motor  green wire C(Nema 11)
13. B01 = Coil Number 2 Stepper motor  red wire B(Nema 11)
14. B02 = Coil Number 2 Stepper motor  blue wire D(Nema 11)


Now the stepper motor , This library was tested  
with a typical bipolar NEMA-11 stepper motor with four wires:

![ScreenShot motor pinout ](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/images/nema11pinout.jpg)

It has 200 steps per revolution, and can operate at at 60 RPM. 
It was a step to angle ratio of 1.8 degrees per step. 

The key to successful stepper motor control is identifying the wires - 
that is which one is which. You will need to determine 
the A, B, C and D wires. 
With our example motor these are green, blue, black and red.  

The software class that controls the motor is same used for the
28BYJ-48 ULN2003 component also in library.

There are 3 step modes available.
Full step and half step there is also wave drive method.
Where one coil at a time is powered (like a wave) 
All three methods are available in this library.
Full gives the most torque. Half gives less torque but more accuracy 
and wave drive is best for low power applications. half step mode is recommend 
for most projects.

![screenshot steps](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/images/figure3.jpg)

half-step takes twice as many steps to complete same distance.

Half-step mode: 
360 degrees / 400 steps = 0.9.
8 step control signal sequence.
0.9 degrees per step , 400 steps , 400/8 = 50 step sequence for one revolution.
7.2 degrees per step sequence.

Full Step mode and wave drive: 4
360 degrees/200 steps = 1.8
4 step control signal sequence.
1.8 degrees per step , 200 steps = 200/4 = 50 step sequence for one revolution.
7.2 degrees per step sequence.


Software
--------------------------------------------

Same software as 28BYJ-48  but with 
minor change in class definition for verbose output.

The library file RpiMotorLib.py has a class which controls the motor with one 
main function. The test file in the test folder is called TB6612FNG_Nema_Test.py

When initializing the class pass a name and motor type.
The class is called BYJMotor.

BYJMotor(name, motor_type) 

(1) name ,type=string, default="BYJMotorX" , help= my motor_id

(2) motor_type ,type=string, default="28BYJ", used by class 
to calculate degree in verbose output two options currently
Nema and 28BYJ. NB **Set to Nema for this component** 

The 1st function is called motor_run- moves stepper motor based on 7 inputs.
motor_run(GPIOPins, wait, steps, counterclockwise, verbose, steptype, initdelay)

(1) GpioPins, type=list of ints 4 long, help="list of
 4 GPIO pins to connect to motor controller
 These are the four GPIO pins we will
 use to drive the stepper motor,  So:
 GPIOPins[0] is plugged into Pin A11 on the stepper motor.
  GpioPins = [A11, B11, A12,B12]
         
(2) wait, type=float, default=0.001, help=Time to wait
(in seconds) between steps.
         
(3) steps, type=int, default=512, help=Number of step control signal sequence
 to take. 
         
(4) ccwise (counterclockwise), type=bool default=False
help="Turn stepper counterclockwise"

 (5) verbose, type=bool  type=bool default=False
 help="Write pin actions and provide verbose output",
 
 (6) steptype, type=string , default=half help= type of drive to
 step motor 3 options full step half step or wave drive
 where full = fullstep , half = half step , wave = wave drive.

 (7) initdelay, type=float, default=1mS, help= Intial delay after
GPIO pins initialized but before motor is moved, gives time for GPIO
to initialize. 

The second function is called to stop the motor when the motor is moving.
motor_stop(), if you wish to stop motor before end of its run. You can also stop with keyboard interrupt.

Example: 

There is a detailed example code is in the **TB6612FNG_Nema_Test.py** file in test subfolder of 
rpiMotorLib repository. 

To run this test file type **python3 TB6612FNG_Nema_Test.py** in a terminal.

If verbose is set to True various information on pin output and status is outputted to screen at end of a run

 ![ScreenShot verbose](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/screenshot/Verbose_output_run.jpg)
