Bipolar Nema 11 Stepper motor controlled by MC1508 Motor controller module.
---------------------------------------

![ScreenShot motor](https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/images/nema11.jpg)
![ScreenShot controller](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/MX15083.jpg)


Hardware
------------------------------------

The MX1508 Dual H-bridge is basic, cheap & small device ideal for small and low voltage motors.
It can control two DC motors or one stepper. Motor voltage 2-10 volts. Continuous current 1.5 Amps, peak current 2.5 Amps
and Logic voltage of 1.8-7 volts. There is no input for logic voltage it is derived from the motor power.
Module pinout


| Pin Label | Function | Notes|
| ------ | ------ | ------ |
| '+' | Motor voltage | PSU for the motors (2V to 10V) |
| '-' |Ground | Connect all GNDs to common rail (RPI , Motor PSU and Module) |
| In1-In4 |Input |inputs  connected to RPI GPIO * 4 |
| Motor A | Output 1 for channels A| One of the two outputs to connect the motor coil 1|
| Motor B | Output 2 for channels B| One of the two outputs to connect the motor coil 2 |

HW Connection (for stepper motor) for the test file(see software section below) are as follows,
(you can pick any GPIO pin you want).


1. '+' to motor PSU (2-10 volts) tested at 5
2. '-' to GND connect all GND's to a common rail together with PSU and RPI
3. IN1 = 20 GPIO
4. IN2 = 21 GPIO
5. IN3 = 19 GPIO
6. IN4 = 26 GPIO
7. Motor B Coil Number 1 Stepper motor  black wire A(Nema 11)
8. Motor B Coil Number 1 Stepper motor  green wire C(Nema 11)
9. Motor A Coil Number 2 Stepper motor  red wire B(Nema 11)
10. Motor A Coil Number 2 Stepper motor  blue wire D(Nema 11)


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
main function. The test file in the test folder is called MC150X_Nema_Test.py

When initializing the class pass a name and motor type.
NB **Set motor type to Nema for this component** 
The class is called BYJMotor.

`BYJMotor(name, motor_type)`

| ID  | Name   | Type   | Help | 
|-----|---------|----------|----------|
| (1) | name   | type=string, default="BYJMotorX" | motor_id    |
| (2) | motor_type | type=string, default="28BYJ"     | Used by class to calculate degree in verbose output two options currently Nema and 28BYJ. Set to Nema for this component |

The 1st method  is called motor_run- moves stepper motor based on 7 inputs.

`motor_run(GPIOPins, wait, steps, counterclockwise, verbose, steptype, initdelay)`

| ID  | Name  | Type | Help |
|-----|------|-------|------|
| (1) | GpioPins,                  | List of ints 4 long,         | 4 GPIO pins to connect to motor controller,  GPIOPins[0] is plugged into Pin A11 on the stepper motor. [A11, B11, A12,B12]  |
| (2) | wait,                      | float, default=0.001,        | Time to wait(in seconds) between steps.                       |
| (3) | steps,                     | int, default=512,            | Number of step control signal sequence to take.                 |
| (4) | ccwise (counterclockwise), | bool default=False           | Turn stepper counterclockwise                       |
| (5) | verbose,                   | bool default=False | Write pin actions and provide verbose output                   |
| (6) | steptype,                  | string , default="half"        | Type of drive to step motor 3 options <br> "full" = fullstep <br> "half" = half step <br> "wave" = wave drive.         |
| (7) | initdelay,                 | float, default=1mS,          | Initial delay after GPIO pins initialized but before motor is moved, gives time for GPIO to initialize.                 |


The second method is called to stop the motor when the motor is moving.
motor_stop(), if you wish to stop motor before end of its run. You can also stop with keyboard interrupt.

Example: 

There is a detailed example code is in the **MC150X_Nema_Test.py** file in test subfolder of  rpiMotorLib repository. 

To run this test file type **python3 MC150X_Nema_Test.py** in a terminal.

If verbose is set to True various information on pin output and status is outputted to screen at end of a run


