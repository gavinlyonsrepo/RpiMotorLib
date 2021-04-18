Servos
----------------------------------

![ScreenShot servo](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/images/sg90.jpg)

Hardware
------------------------------------

Should Work on any servo with 20mS duty cycle or 50Hz frequency, tested on.

Tower pro Digital micro servo SG90
Hitec HS422 servo
Tower pro MG996R Servo
(Check if your servo has a range of 0-180 degrees and matches the freq/duty cycle specifications, most should)

Datasheet SG90 Datasheet Hs422 Datasheet MG996R

The following HW description applies to the ultra common SG90 servo.

The servo has 3 wires one for gnd(brown) 5v power(red) and signal(orange/yellow).
I have verified that it is safe to drive a single servo from the 5 volt rail on Rpi. However It is possible to damage your Raspberry Pi by drawing too much current out of a pin(spikes or low current power supply on the pi). It is best to power it from a 5 Volt source other than a Raspberry Pi rail. You can still control it from the Raspberry Pi if you use a common ground, but just get the power (red wire) from an external source. The Pi draws approximately 700 mA from the +5 V supply. You may draw current from the +5 V pins provided the sum of that current and the board's 700 mA doesn't exceed the supply you provide to the board.

From the data sheet , we see these servos expects a frequency of 50 Hz on the control line and the position it moves to depends on the pulse width of the signal. 50Hz gives a period of 20mS (Freq = 1/Period)

These servo has a range of 180 degrees.

The Raspberry Pi controls the servo by outputting a PWM signal of varying duty cycle on a GPIO pin connected to signal pin of servo.

Duty Cycle = Pulse Width * Frequency

Given a 50 Hz frequency we can calculate the required duty cycle for any pulse width.

Excepted values of pulse width for many standard servos are

1.5 ms pulse( to center the servo or 0 or 90 degrees or center postion)
1 ms pulse (- 90 degrees or 0 degrees or "min postion ")
2 ms pulse (+ 90 degrees or 180 or "max postion ")
Note: 1mS = 1000uS The pigpio module uses Pulse width in microseconds So the SW methods take uS as parameters.

However every servo is different, so you will need to calibrate it for the best performance. Check datasheet for recommend pulse width and calibrate accordingly. Some cheap hobby servos can vary widely. The software will only accept values from 500-2500uS or 0 in event of turning "off".

The software includes a method to convert degrees to pulse width in uS. for user convenience, this method is also used internally in one of the other methods If user prefers working in degrees they can pass result to the other methods which want pulse duty cycle percentage.

This method works as follows imagine we have two points on a graph. (x1, y1) (x2, y2). Where 1 is servo right position 0 degree. Where 2 is servo left position 180 degree. Where x is degree and y is pulse width. Y 1 and Y2 are calibrated by user = default (1000, 2000).

(x1 , y1) = ( 0,1000 )
(x2, y2) = (180,2000).

To get slope of line m = (y2-y1)/(x2-x1). The equation of the line using the point slope formula = y-y1=m(x-x1) . We want to find point (x,y) Where y is required pulse width and x is the given degree. For default values this works out as PulseWidth = 5.55555*(DesiredAngle) + 1000.

So for default values 90 degree or midpoint is 1500.


Software for Servo by pigpio library
--------------------------------------------

NB , Remember to start to pigpio daemon every time you want to use it or at
startup. By typing sudo pigpiod in terminal 

The library file rpi_pservo_lib.py has a single class 
which controls the servo. Test file is called ServoPIGPIOTest.py.

The class is called ServoPigpio and it contains four methods:

(1) servo_sweep - sets up a continuous sweep from two points
Center-wait-min-wait-max-wait-min- and so on until user quits or set limit reached.

(2) servo_move - moves to a specified location in a single sweep

(3) convert_from_degree - converts degrees to pulse width 

(4) servo_move_step - moves servo from two points in timed steps.

(5) servo_stop - this will stop the servo if you wish to stop servo before end of its run. 
You can also stop with keyboard interrupt.

### Import library and intialise the class 

```sh
from RpiMotorLib import rpi_pservo_lib
myservotest  = rpi_pservo_lib.ServoPigpio("Sone", 50, 1000, 2000)
```

The class takes four parameters on init
1. name, type=string, default=servoY,  
2. Freq, type=int, default=50, help=control freq of servo in Hz
3. y_one, type=float, default = 1000 ,help=pulse width min in uS of servo % for 0 degrees
4. y_two type=float, default = 2000 , help=pulse width max in uS of servo % for 180 degrees
5. pigpio_addr, type=string default=None, help=host name where pigpio is running
6. pigpio_port, type=int default=None, help=port number where pigpio is running

y_one and y-two are used by methods numbered 3 and 4. 

### 1 - servo_sweep

function, servo_sweep, 8 inputs
sets up asweep from two points, 
Center-delay-min-delay-max-delay- and so on until user quits or set-limit reached.

 servo_sweep(servo_pin, center, minduty, maxduty, delay, verbose, initdelay, sweeplen)

 (1) servo_pin, type=int help=GPIO pin
 we will contect to signal line of servo
 
 (2) center, type=float, default=1500,
 help=The center pulse width position of servo in uS.
 
 (3) minduty, type=float, default=1000,
 help=The min pulse width position of servo in uS.
 
 (4) maxduty, type=float, default=2000,
 help=The max pulse width position of servo in uS.
 
 (5) delay, type=float, default=0.5,
 help=Time to wait (in seconds) between steps.
 
 (6) verbose, type=bool  type=bool default=False
  help="Output actions & details",

 (7) initdelay, type=float, default 50mS
    help= A delay after Gpio setup and before servo moves
    
 (8)  sweeplen, type=integer , default one million
     help=  is number of times to execute sweep.
 
 example:Setup a class instance called servoone with control freq 50mS
 with y_one set to 3 and Y_two to 11. Next call method
 to sweep the servo connected to GPIO pins 7
 for step delay of 0.5 second from pulse width
 1000uS to pulse width position 2000uS and center position 1500uS
 with verbose output set to True and initdelay set to 0.01mS , 100 times
 
```sh

# call the function pass by value in this case.
myservotest.servo_sweep(7, 1500, 1000, 2000, 0.5, True, 0.01, 100)

```

### 2 - servo_move


function servo_move 5 inputs

 servo_move(servo_pin, position, delay, verbose, initdelay)

 (1) servo_pin, type=int help=GPIO pin
 we will contect to signal line of servo
 
 (2) position, type=float, default=7.5,
 help=The  pulse width position of servo to move to, in uS.
 
 (3) delay, type=float, default=0.5,
 help=Time to wait (in seconds) before move and after setup
 
 (4) verbose, type=bool  type=bool default=False
  help="Output actions & details",

 (5) initdelay, type=float, default 50mS
    help= A delay after Gpio setup and before servo moves

 example: to move the servo connected to GPIO pins 7
 for step delay of 1 second to pulse width of 1200uS
 with non-verbose output and initdelay of 10mS
 
```sh
# call the function pass by value in this case.
myservotest.servo_move(7, 1200, 1, False, .01)
```

### 3 convert_from_degree

converts degrees to pulse width uS
Input degrees,
returns pulse width in uS as float

```sh
testdegree = float(input("What degree do you want?\t"))
print("Pulse width micro seconds = {} ".format(myservotest.convert_from_degree(testdegree)))
```

### 4 servo_move_step 

servo_move_step(servo_pin, start, end, stepdelay, stepsize, initdelay, verbose)

servo_move_step - moves servo from two points in timed steps,
seven inputs. 


(1) servo_pin, type=int help=GPIO pin
we will contect to signal line of servo

(2) start, type=float, default=10,
help=start position of servo in degree

(3) end, type=float, default=170,
help=end position of servo in degrees 

(4) stepdelay, type=float, default=1,
help=Time to wait (in seconds) between steps.

(5) stepsize, type=int, default=1.
help=the size of steps between start and end in degrees

(6) initdelay, type=float, default 50mS
help= A delay after Gpio setup and before servo moves

(7) verbose, type=bool  type=bool default=False
 help="Output actions & details",
         
Example: to move a servo on GPIO pin 26 from 10 degrees to 170 
degrees in 3 degree steps every two seconds, with an initial delay 
of one second and verbose output.   

```sh
myservotest.servo_move_step.servo_move_step(26, 10, 173, 2, 3, 1, True)

```        
