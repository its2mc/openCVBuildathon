#This pilot project aims to marry opencv methods with hardware controlled by the edison.
#This pilot toggles an LED between on and off states every time a face is detected.

import numpy as np
import cv2
#import mraa  #this is the i/o library for intel edison/galileo
import RPi.GPIO as gpio
import time
import sys
import signal

# Setup LED variables
gpio.setmode(gpio.BOARD)  # use P1 header pin numbering convention
gpio.setwarnings(False)   # don't want to hear about how pins are already in use

ledPin = 2
gpio.setup(ledPin,gpio.OUT)

#ledPin = mraa.Gpio(2) 
#ledPin.dir(mraa.DIR_OUT)

#Setup Opencv Cascade algorithms
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Capture video 
cap = cv2.VideoCapture(0)
faceNo = 0
trigger = 0

def toggleLED():
	global trigger
	if trigger == 0:
		trigger = 1
	elif trigger == 1:
		trigger = 0
	gpio.output(ledPin,trigger) #turn off or on according to the trigger
	#ledPin.write(trigger)
	
def exit(signum, frame):
	# restore the original signal handler as otherwise evil things will happen
	# in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
	signal.signal(signal.SIGINT, original_sigint)
	
	print "Exiting Gracefully"
	cap.release()
	sys.exit(1)
	# restore the exit gracefully handler here    
	signal.signal(signal.SIGINT, exit)
	
# store the original SIGINT handler
original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit)

print "Starting Loop"

while(1):

	# Take each frame
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	
	for (x,y,w,h) in faces:
		print "Found Face"
		faceNo = faceNo + 1
		print faceNo
		toggleLED()
	
	k = cv2.waitKey(5) & 0xff
	if k == 27:
		break

cap.release()




