Version control history:
====================

* Version 1.0-1 150318 
	* First version, 28BYJ-48 + servos.
	
* Version 2.0-1 090418
	* Added DC motors driven by L298N + transistor
	* Added Nema stepper driven by motor controller A4988
	* Added Nema stepper driven by motor controller  L298N
	* Added new functions to Servo section.
	
* Version 2.1-2 280518
	* Added Nema stepper driven by motor controller A3967 "Easy Driver"
	* Added Nema stepper driven by motor controller DRV8825 
	* Added new option (sweeplen) to servo_sweep method. Defines a fixed 
	length to the sweep rather than continuous.  

* Version 2.2-3 200618
	* Added support for pigpio library option for servo control

* Version 2.3-4 010718
	* Added DC motors driven by L9110S module
	* Added DC motors driven by DRV8833 module

* Version 2.4-5 121218
	* Minor update
	* Added Support for installation on Windows 10 by changing Setup.py
	* See issue 2 at Github Project URL.
	
* version 2.5-6 310319
	* Minor update, 
	* Correcting the error message in class "A4988Nema"
	,method "resolution_set". The latter half was reporting the "step type"
	instead of "motor type" to user. This error message was only displayed 
	if user initialized class with a unknown motor type(user typo).
	
* version 2.6-7 210519
	* Minor update
	* Addressing concerns raised by issue 4 on github.
	In class "BYJMotor" changed error handling in 
	method  "motor_run" so Verbose reporting is in the "else" code block
	instead of the "finally" code block as sometimes this reporting code
	was throwing exceptions after a keyboard exception was interrupted: 
	For example before the motor started.
	"UnboundLocalError: local variable 'step_sequence' referenced before assignment"
	
* version 2.7-8 050919
	* Added Support for TB6612FNG motor controller both stepper and DC motor
	
* version 3.0-1 150421
	* Pull request number eight merged. 
	* Added Motor-stop method to all stepper motors classes 
	* Added Servo-Stop method to all servo classes
	* Servo pigpio: make pigpio host and port configurable

* version 3.1-2 110521
	* Added an option to hard-wire to logic MS-X resolution pins 
	on some stepper motors where applicable to save GPIO pins 
	* Added support for LV8729 motor controller.
	* Added basic test file for threading example.

* version 3.2-3 151022
	* Minor update.
	* Added pwm.stop command to all DC motor classes, see github issue 21
	* Added check for negative step numbers in the BYJMotor class, see github issue 20

