# This work has been done by Phillip Ochola Mak'Anyengo
# as part of the iHub Research OpenCV Buildathon on the
# <date>
# 
# Email: its2uraps@gmail.com
#
# This work uses open source code and open use libraries
# but the application itself is neither open source or 
# allowed for open use. 
# 
# Users who wish to use parts of this
# work MUST contact the authors before use, failure to which
# the user risks being prosecuted.

#Import all the libraries needed
import time
import json
import numpy as np
import base64
import StringIO
import cv2
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

#Websocket Event Handling
class MyServerProtocol(WebSocketServerProtocol):
	def onConnect(self, request): #Message displayed when there is a connection
		print "Connection opened"

	def onOpen(self): #Message displayed when server opened
		print "WebSocket connection open"
		
	def onMessage(self, payload, isBinary): #Code that runs when message is triggered
		message = format(payload.decode('utf8')) #Message decoded as utf8
		
		#To enhance efficiency starting and stopping video views separated
		#However DO NOT FORGET to close a video capture
		if (message == '1'):#Start Video Capture
			print "Starting Video Capture"
			self.cap = cv2.VideoCapture('res/matlab_slowtraffic.mp4')#Replace with your own video link
			
		if (message == '2'):#Stop Video capture
			print "Closing Video Capture"
			self.cap.release()
			
		if (message == '3'):#Multiple Video displaying algorithms can be added below
			#Remember to refer to video capture as self.cap
			#Replace your own code here. Below is a simple example
			
			
			
			ret,frame = self.cap.read()
			
			
			
			
			#The code below sends the captured frame to the Video viewer. DO NOT DELETE
			#the image is passed to the encoder as frame, you can pass any other image matrix
			encode_param=[1,90]
			res, image = cv2.imencode('.jpg',frame,encode_param)
			sample = base64.b64encode(image)
			self.sendMessage(sample, isBinary)
			
		#if (message == '4'): #add extra algorithms like this
				
	def onClose(self, wasClean, code, reason):#Message displayed when there is an error
		print format(reason)


	
#Start Websocket Server
if __name__ == '__main__':
	import sys
	from twisted.internet import reactor

	factory = WebSocketServerFactory("ws://localhost:5557")#Set debug false to save on processing time
	factory.protocol = MyServerProtocol

	reactor.listenTCP(5557, factory)
	reactor.run()
		


	


