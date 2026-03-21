DC motor controlled by DRV8833 Motor controller module.
-------------------------------------------------

![ScreenShot DRV8833](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/extra/images/DRV8833.jpg)


Hardware
--------------------------------------------
[Ebay listing](https://www.ebay.ca/itm/DRV8833-2-Channel-DC-Motor-Driver-Module-1-5A-for-Arduino-/311651296778)
[Datasheet DRV8833](http://www.ti.com/lit/ds/symlink/drv8833.pdf)

This DRV8833 based DC motor controller board allows users to attach an external power
source to power DC motors that require a little bit more current. 
Plug in an external power source up to 10.8VDC with a max current of 1.5A per channel. 
The IC onboard contains two h-bridges allowing the control of two independent DC motors or one 4 wire bipolar stepper motor. 
The design of this module also guarantees protection against overcurrent, short circuit, overheating and under voltage lockout. 
It also comes with a low power sleep mode.  
This module comes with straight headers that you will need to solder on the module. 
The pin IN1 and IN2 control the outputs OUT1 and OUT2 (1st channel). 
IN3 and IN4 control the outputs OUT3 and OUT4 (2nd channel). 
Pin EEP is for output protection and ULT is your sleep mode pin (sleep mode active when logic level low). 
Vcc and GND are power and ground. Remember to also connect the raspberry Gnd to other gnds.
INx pins connect to GPIO pins on RPi OUTx pins connect to Dc motors.
Also Decoupling the motor power supply with a capacitor(see datasheet for value)

![ScreenShot DRV8833 pinout](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/extra/images/DRV8833pinout.jpg)

Input voltage:3V-10V
Single H-Bridge output current:1.5A(It can drive two DC motor)
Features:

1. ULT PIN:mode set.Low level is sleep mode
2. OUT1,OUT2:1-channel H-bridge controlled by IN1/IN2
3. OUT3,OUT4:2-channel H-bridge controlled by IN3/IN4
4. EEP PIN:Output protection.
5. VCC:3-10V
6. GND

This library was tested on a RF-310T-11400 DC motor.

Software
-------------------------------------------
The file rpi_dc_lib.py contains code for this component
It consists of a class called DRV8833NmDc and six methods
The methods are called: 
1. forward = Drive motor forward,  passed one argument = duty cycle %
2. backward = drive motor backward,  passed one argument = duty cycle %
3. stop = stop motor, Intended for normal motor control flow
   passed one argument = duty cycle %
4. brake = brake motor,  passed one argument = duty cycle %
5. cleanup = stop PWM and turn off GPIO pins used by motor.
   Passed a boolean: if False just stop and zero the motor pins,
   if True also run GPIO.cleanup() for all pins.
6. motor_stop = Intended for emergency/interrupt situations — immediately kills output
   immediately stop motor output and set stop flag.
   Does not destroy the PWM object — motor can be restarted.
   Call cleanup() for full teardown at end of program.

Example code is in the DRV8833_or_ L9110S_DC_Test.py file 

