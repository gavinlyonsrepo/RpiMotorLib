author__ = 'Gavin Lyons'

import time
import RPi.GPIO as GPIO


class BYJMotor(object):

	def __init__(self, name):
		self.name = name
		#This array is used to make the cursor "spin" while the script is running.
		self.curserSpin = ["/","-","|","\\","|"]
		self.spinPosition = 0
		

			
	def motorRun(self,GpioPins = [],wait=.001,steps=500,counterclockwise=False,verbose=False):
	
		#We will be using GPIO pin numbers instead
		#of phyisical pin numbers.
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		for pin in GpioPins:
			GPIO.setup(pin, GPIO.OUT) #Set pin to output
			GPIO.output(pin, False) #Set pin to low ("False")

		#These steps are defined in datasheet at
		#http://www.bitsbox.co.uk/data/motor/Stepper.pdf
		#Each step is a list containing GPIO pins that should be set to High
		StepSequence = list(range(0, 8))
		StepSequence[0] = [GpioPins[0]]
		StepSequence[1] = [GpioPins[0], GpioPins[1]]
		StepSequence[2] = [GpioPins[1]]
		StepSequence[3] = [GpioPins[1], GpioPins[2]]
		StepSequence[4] = [GpioPins[2]]
		StepSequence[5] = [GpioPins[2], GpioPins[3]]
		StepSequence[6] = [GpioPins[3]]
		StepSequence[7] = [GpioPins[3], GpioPins[0]]
		

		#if we want the motor to run in "reverse" we flip the sequence order.
		if counterclockwise:
			StepSequence.reverse()
			

		#Just prints a spinning cursor. Used when --verbose not set to false.
		def PrintCursorSpin():
			print ("%s\r" % self.curserSpin[self.spinPosition], end='', flush=True)
			self.spinPosition += 1
			if self.spinPosition > 4:
				self.spinPosition = 0
				

		#Print status of pins.		
		def PrintStatus(enabledPins):
			if verbose:
				print ("New Step:")
				for pin in GpioPins:
					if pin in enabledPins:
						print ("Enabling Pin %i" % pin)
					else:
						print ("Disabling Pin %i" % pin)
			else:
				PrintCursorSpin()

		#The actual magic loop. Iterate through the pins turning them on and off.
		stepsRemaining = steps
		while stepsRemaining > 0:
			for pinList in StepSequence:
				for pin in GpioPins:
					if pin in pinList:
						GPIO.output(pin, True)
					else:
						GPIO.output(pin, False)
				PrintStatus(pinList)	
				time.sleep(wait)
			stepsRemaining -= 1
		
		# switch off pins at end. 
		for pin in GpioPins:
			GPIO.output(pin, False)

def test(text):
	"""import code"""
	print(text)

if __name__ == '__main__':
    test("main")
else:
    test("Imported {}".format(__name__))
