Bipolar Nema11 Stepper motor with DRV8825  Driver Carrier 
--------------------------------------------  

![ScreenShot Nema](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/nema11.jpg)
![ScreenShot DRV8825](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/DRV8825.jpg)

Hardware
------------------------------------

Nema 11 Stepper Motor:

see [A4988 Nema Section](Nema11A4988.md) 


DRV8825:

Info.

[DRV8825 at pololu](https://www.pololu.com/product/2133)

[DRV8825 Datasheet](https://www.pololu.com/file/0J590/drv8825.pdf)


The DRV8825 is a very common and inexpensive stepper motor controller,
designed by pololu.With a heatsink the device can handle up to 1.5 amps per coil.

Pinout of the DRV8825 module:

![ScreenShot DRV8825 pinout](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/DRV8825pinout2.jpg)

We see the following pins:

* VMOT – The motor DC supply voltage (positive). The maximum voltage is 35 volts.
* GND – The motor supply voltage ground.
* 2B, 2A – The connections to coil 2 of the bipolar stepper motor.
* 1A, 1B – The connections to coil 1 of the bipolar stepper motor.
* GND – The logic supply ground.
* FLT - Logic low when in fault condition (overtemp, overcurrent)
* ENABLE – Logic high to disable device outputs and indexer operation, logic  low to enable. Internal pulldown.
* MS0, MS1, MS2 – These three connections determine the microstepping mode of the DRV8825 module. By setting the logic levels here you can set the motor to Full, Half, Quarter, Eighth, Sixteenth or 1/32 steps. 
* RESET – Active-low reset input initializes the indexer logic and disables the H-bridge outputs. Internal pulldown.
* SLEEP – Logic high to enable device, logic low to enter low-power sleep Internal pulldown.
* STEP – This is how you drive the motor from an external microcontroller or square wave oscillator. Each pulse sent here steps the motor by whatever number of steps or microsteps that has been set by MSX settings. The faster you pulse this the faster the motor will travel.
* DIR – The direction control A high input here drives the motor clockwise, a low will drive it counterclockwise.

DRV8825 wiring diagram:

![ScreenShot DRV8825 wiring diagram](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/DRV8825pinout.jpg)


Make sure to observe the motor connections, described in Motor section above
the DRV8825 is conveniently laid out to match the 4-pin connector 
that is common on several bipolar motors 
but you should check your motor connections to be sure they are correct.

Connect 5 GPIO pins to MS0, MS1, MS2, STEP and DIR.
If you do not wish to use GPIO for MS_X pins 
and hard wire MS-X to logic levels.
You can also pass in (-1, -1, -1) to software. 
Do this if your project only uses one type of resolution and you wish to save GPIO pins.
Connect pi gnd to DRV8825 at GND. 
Connect Reset and sleep together and to pi 5V.
Connect up capacitor and Motor leads.

The capacitor  is essential to decouple the power supply. Any value from 47uf up will suffice, 
try and mount the capacitor as close to the DRV8825 VMOT and GND pins as possible.
Advisable to carry out a DRV8825 Current Adjustment before using motor see info links at top of section.

Also do not disconnect motor when in operation, as it will damage controller. 
It is also possible and valid to connect up the DRV8825 in another alternative minimal wiring type as per A4988 section
see first info links at top of section bottom of page.

There are 6 step modes for DRV8825, 
Six different step resolutions: full-step, half-step, 1/4-step, 1/8-step, 1/16-step, and 1/32-step

| MicroStep| Step increment degrees | Steps for 1 revolution(360) |
| ------ | ------ |  ------ |
| Full | 1.8 |  200 |
| Half | 0.9 |  400 |
| 1/4 | 0.45 |  800 |
| 1/8 | 0.225 |  1600 |
| 1/16 | 0.1125 |  3200 |
| 1/32 | 0.05625 |  6400 |

Microstep Resolution Truth Table.
 
| MS1 | MS2 | MS3 |  Resolution |
| --- | --- | --- | --- |
| Low | Low |Low | Full step | 
| High | Low | Low | Half step |
| Low | High | Low | 1/4 |
| High | High | Low | 1/8 |
| Low | Low | High | 1/16 |
| High | Low | High | 1/32 |
| Low | High | High | 1/32 |
| High | High | High | 1/32 |


Software
--------------------------------------------

The library file RpiMotorLib.py contains the class which controls 
the motor. The class is called A4988Nema. This class handles both A4988 
and Drv8825. The only difference from a user POV is when you instantiate 
the class the user passes the motor type and also user can now use 
1/32 microstep for DRV8825. The test file is called DRV8825_Nema_Test.py

See for more details [A4988 software Section](Nema11A4988.md) 


Example: Should do a 180 degree turn.
To run A stepper motor clockwise in Full mode for 100 steps.
 for step delay of .01 second. 
 verbose output off , with 50mS init delay.
 
```sh

 
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib
    
#define GPIO pins
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "DRV8825")


# call the function, pass the arguments
mymotortest.motor_go(False, "Full" , 100, .01, False, .05)

```
