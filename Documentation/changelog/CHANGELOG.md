Version control history:
====================

* Version 1.0-1 150318 
	* First version, 28BYJ-48 + servos.
	
* Version 1.1-2 220318
	* Code re-factor python standard and optimization's.
	
* Version 2.0-1 090418
	* added DC motors driven by L298N + transistor
	* added Nema stepper driven by motor controller A4988
	* added Nema stepper driven by motor controller  L298N
	* Added new functions to Servo section.
	
* Version 2.1-2 280518
	* Added Nema stepper driven by motor controller A3967 "Easy Driver"
	* Added Nema stepper driven by motor controller DRV8825 
	* Added new option (sweeplen) to servo_sweep method. Defines a fixed 
	length to the sweep rather than continuous.  

* Version 2.2-3 200618
	* Added support for pigpio library option for servo control
