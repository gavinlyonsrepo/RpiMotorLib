DC motor controlled by L298N Motor controller module.
-------------------------------------------------

![ScreenShot dcmotor](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/RF310T11400.jpg)
![ScreenShot L298N](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/L298N.jpg)


Hardware
--------------------------------------------

The L298N H-bridge   
Dual Motor Controller Module 2A allows you to control the speed and direction of two DC motors, 
or control one bipolar stepper motor with ease. 
The L298N H-bridge module can be used with motors 
that have a voltage of between 5 and 35V DC. 

There is also an onboard 5V regulator, 
so if your supply voltage is up to 12V you can also source 5V from the board.

These L298 H-bridge dual motor controller modules 
are inexpensive and widely available.

Module pinouts
Consider the following image - match the numbers against the list below the image:


![ScreenShot L298Npinout](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/298pinout.jpg)

1. DC motor 1 "+" or stepper motor A+
2. DC motor 1 "-" or stepper motor A-
3. 12V jumper - remove this if using a supply voltage greater than 12V DC. This enables power to the onboard 5V regulator
4. Connect your motor supply voltage here, maximum of 35V DC. Remove 12V jumper if >12V DC
5. GND
6. 5V output if 12V jumper in place, 
7. DC motor 1 enable jumper. Leave this in place when using a stepper motor. Connect to PWM output for DC motor speed control.
8. IN1 connect to GPIO on Pi
9. IN2 connect to GPIO on Pi
10. IN3 connect to GPIO on Pi
11. IN4 connect to GPIO on Pi
12. DC motor 2 enable jumper. Leave this in place when using a stepper motor. Connect to PWM output for DC motor speed control.
13. DC motor 2 "+" or stepper motor B+
14. DC motor 2 "-" or stepper motor B-

To control one or two DC motors. First connect each motor to the A and B connections on the L298N  module. 
If you're using two motors for a robot (etc) ensure that the polarity of the motors is the same on both inputs. 
Otherwise you may need to swap them over when you set both motors to forward and one goes backwards!

Next, connect your power supply - the positive to pin 4 on the module and negative/GND to pin 5. 
If you supply is up to 12V you can leave in the 12V jumper (point 3 in the image above) and 5V will be 
available from pin 6 on the module. 
NB!! Don't forget to connect Pis GND to pin 5 on the module as well to complete the circuit. 

Finally, connect the six GPIO pins on your pi  output pins to the driver module. 
IN software code below for two DC motors, So GPIO 19, 13, 20 and 21 will be connected to pins 
IN1, IN2, IN3 and IN4 respectively. Then connect GPIO 26 to module pin enB (remove the jumper first) 
and GPIO 16 to module pin EnB (again, remove the jumper). 

The motor direction is controlled by sending a HIGH or LOW signal to the drive for each motor (or channel). 
For example for motor one, a HIGH to IN1 and a LOW to IN2 will cause it to turn in one direction, 
and  a LOW and HIGH will cause it to turn in the other direction.

However the motors will not turn until a HIGH is set to the enable pin (ENA for motor one, ENB for motor two). 
And they can be turned off with a LOW to the same pin(s). However if you need to control the speed of the motors, 
the PWM signal from the digital pin connected to the enable pin can take care of it.

The PWM signal or duty cycle is a floating point number and a percentage can be set from 0 to 100.

This sofware and L298N should work with any DC Motor between rated 5 and 35 volts.
This library was tested on a RF-310T-11400 DC motor.

  
Software
-------------------------------------------

The file rpi_dc_lib.py contains code for this component
It consists of a class called L298NMDc and five methods
The five functions is called: 
1. forward = Drive motor forward,  passed one argument = duty cycle %
2. backward = drive motor backward,  passed one argument = duty cycle %
3. stop = stop motor, passed one argument = duty cycle %
4. brake = brake motor,  passed one argument = duty cycle %
5. cleanup = turn off the 3 GPIO pins and will also run GPIO.cleanup() 
passed a boolean if False just turn off the 3 GPIO used by motor driver,
if True run in-built GPIO.cleanup() function.

Example: 

The GPIO pins of pi in this example
EnA = 26
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

More example code is in the L298DCtest.py file in test subfolder of 
rpiMotorLib repository.

```sh  
import time
# import library
from RpiMotorLib import rpi_dc_lib

def motorone():
    
    # define instance of the class 
    # (GPIO , GPIO , GPIO , freq , verbose, name) 
    MotorOne = rpi_dc_lib.L298NMDc(19 ,13 ,26 ,50 ,True, "motor_one")
    
    try:
        print("1. motor forward at 15")
        MotorOne.forward(15)
        input("press key to stop") 
        print("motor stop\n")
        MotorOne.stop(0)
        time.sleep(3)

        print("2. motor forward ramp speed up 15 to 30 steps of 1")
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

        print("4. motor backward ramp speed up up 15 to 30 steps of 1")
        for i in range(15,30):
            MotorOne.backward(i)
            time.sleep(1)
        MotorOne.stop(0)
        print("motor stopped\n")
        time.sleep(3)
         
        print("5  brake check")
        MotorOne.forward(50)
        time.sleep(3)
        MotorOne.brake(0)
        print("motor brake\n")
      
    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    else:
        print("No errors")
    finally:
        print("cleaning up")
        MotorOne.cleanup(False)
    
if __name__ == '__main__':
    motorone()
    exit()

```
