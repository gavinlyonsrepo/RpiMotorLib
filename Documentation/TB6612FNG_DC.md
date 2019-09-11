DC motor controlled by a TB6612FNG Dual Motor Driver Carrier
-------------------------------------------------

![ScreenShot dcmotor](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/RF310T11400.jpg)
![ScreenShot TB6612FNG](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/TB6612FNG.jpg)


Hardware
--------------------------------------------

The TB6612FNG is an easy and affordable way to control motors. 
The TB6612FNG is capable of driving two DC motors at up to 1A of constant current. 
Inside the IC, you'll find two standard H-bridges on a chip allowing you 
to not only control the direction and speed of your motors but also stop and brake.
This guide will cover how to use the TB6612FNG breakout board. 

This tiny board is an easy way to use Toshiba’s TB6612FNG dual motor driver, 
which can independently control two bidirectional DC motors or one bipolar stepper motor.
A recommended motor voltage of 4.5 V to 13.5 V and peak current output of 3 A per channel 
(1 A continuous) make this a great motor driver for low-power motors.

The MOSFET-based H-bridges are much more efficient than the BJT-based H-bridges 
used in older drivers such as the L298N,  
The little breakout board gives you direct access to all of the features of the 
TB6612FNG and adds power supply capacitors and reverse battery protection on the 
motor supply. (note: there is no reverse protection on the Vcc connection).

All of the control inputs are internally pulled low. 
Each of the two motor channels has two direction control pins and a speed control pin 
that accepts a PWM input with a frequency of up to 100 kHz. 
The STBY pin must be driven high to take the driver out of standby mode.


Module pinout

![ScreenShot TB6612FNGpinout](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/TB6612FNGpinout.jpg)


| Pin Label | Function | Notes|
| ------ | ------ | ------ |
| VM | Motor voltage | PSU for the motors (2.2V to 13.5V) |
| VCC | Logic voltage |PSU from RPI 3.3V or 5V |
| GND |Ground | Connect all GNDs to common rail (RPI , Motor PSU and Module) |
| STBY | Standby | Allows the H-bridges to work when high (must actively pulled high) connected to RPI GPIO |
| AIN1/BIN1 | Input 1 for channels A/B | inputs direction, connected to RPI GPIO |
| AIN2/BIN2 |  Input 2 for channels A/B| inputs direction, connected to RPI GPIO |
| PWMA/PWMB | PWM input for channels A/B |inputs speed, connected to RPI GPIO |
| AON1/BON1 | Output 1 for channels A/B| One of the two outputs to connect the motor |
| AON2/BON2 | Output 2 for channels A/B| One of the two outputs to connect the motor  |

HW Connection (for two DC motors) for the test file(see software section below) are as follows,
(you can pick any GPIO pin you want).

1. VM to motor PSU 
2. VCC to RPI 3.3 or 5 volt
3. GND to GND connect all GND's to a common rail together with PSU and RPI
4. PWA = 17 GPIO
5. AI1 = 22 GPIO
6. AI2 = 27 GPIO
7. PWB = 18 GPIO
8. BI1 = 23 GPIO
9. BI2 = 24 GPIO
10. Standby = 25 GPIO
11. A01 DC motor 1 +
12. A02 DC motor 1 -
13. B01 DC motor 2 +
14. B02 DC motor 2 -


Software
-------------------------------------------

The file rpi_dc_lib.py contains code for this component.
It consists of a class called TB6612FNGDc and six methods.
The Six functions are called: 
1. forward = Drive motor forward,  passed one argument = duty cycle %
2. backward = drive motor backward,  passed one argument = duty cycle %
3. stop = stop motor, passed one argument = duty cycle %
4. brake = brake motor,  passed one argument = duty cycle %
5. cleanup = turn off the 3 GPIO pins and will also run GPIO.cleanup() 
passed a boolean if False just turn off the 3 GPIO used by motor driver,
if True run in-built GPIO.cleanup() function.
6. Standby = Turns standby line on module high or low, Must be high to run
set low when finished. Passed an integer with standby pin and a boolean.
If true , standby high. Alternative to using this method is too just tie line to logic high.

Example: 

There is a detailed example code is in the TB6612FNGDCtest.py file in test subfolder of 
rpiMotorLib repository. 

To run this test file type **python3 TB6612FNG_DCMot_Test.py** in a terminal.


In event of error or keyboard interrupt call "cleanup function"
NOTE their is no error handling in this class but their is the "cleanup" 
function, Its left to user to catch exceptions and call "cleanup" if they 
want. The cleanup function executes GPIO.cleanup() if passed True.if passed false it just
sets the pins in play low. The standby function is independent of the class object
and is set on and off by user. One class object is declared for each motor.



