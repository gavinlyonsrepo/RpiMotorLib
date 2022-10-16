DC motor controlled by DRV8833 Motor controller module.
-------------------------------------------------

![ScreenShot DRV8833](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/DRV8833.jpg)


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

![ScreenShot DRV8833 pinout](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/DRV8833pinout.jpg)

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
It consists of a class called DRV8833NmDc and five methods
The five functions is called: 
1. forward = Drive motor forward,  passed one argument = duty cycle %
2. backward = drive motor backward,  passed one argument = duty cycle %
3. stop = stop motor, passed one argument = duty cycle %
4. brake = brake motor,  passed one argument = duty cycle %
5. cleanup = turn off the 3 GPIO pins and will also run GPIO.cleanup() 
passed a boolean if False just turn off the 2 GPIO useds by motor,
if True run in-built GPIO.cleanup() function.

Example: 

The GPIO pins of pi in this example
in1 = 19
in2 = 13

1. Runs a motor forwards at duty cycle 15 for 3 seconds 
2. Stop
3. Run a motor forwards in steps of 1 from duty cycle 15 to 30
4. Stop
5. Runs a motor backwards at duty cycle 15 for 3 seconds 
6. Stop
7. Run a motor backwards in steps of 1 from duty cycle 15 to 30
8. Stop
9. Run a motor forwards at 50 and test brake
10. cleanup

In event or error or keyboard interrupt call "cleanup function"
NOTE their is no error handling in this class but their is the "cleanup" 
function, Its left to user to catch exceptions and call "cleanup" if they 
want. The cleanup function executes GPIO.cleanup() if passed True

More example code is in the DRV8833_or_ L9110S_DC_Test.py file 
in test subfolder of rpiMotorLib repository.

```sh
import time 
import RPi.GPIO as GPIO
from RpiMotorLib import rpi_dc_lib 

def motorone():
    
    print(" TEST: testing motor 1") 
    # Motorssetup
    MotorOne = rpi_dc_lib.DRV8833NmDc(19 ,13 ,50 ,True, "motor_one")
    
    try:
        print("1. motor forward")
        MotorOne.forward(15)
        input("press key to stop") 
        print("motor stop\n")
        MotorOne.stop(0)
        time.sleep(3)

        print("2. motor forward speed up")
        for i in range(15,30):
            MotorOne.forward(i)
            time.sleep(1)
        MotorOne.stop(0)
        print("motor stoped\n")
        time.sleep(3)
        
        print("3. motor backward")
        MotorOne.backward(15)
        input("press key to stop") 
        MotorOne.stop(0)
        print("motor stopped\n")
        time.sleep(3)

        print("4. motor backward speed up")
        for i in range(15,30):
            MotorOne.backward(i)
            time.sleep(1)
        MotorOne.stop(0)
        print("motor stopped\n")
        time.sleep(3)
      
      
        print("5  brake check")
        MotorOne.forward(50)
        time.sleep(3)
        MotorOne.brake(100)
        print("motor brake\n")
        
    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        MotorOne.cleanup(False)
        
if __name__ == '__main__':
   
    print("START")
    motorone()
    exit()
    
```
