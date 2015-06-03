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
		
	def onMessage(self, payload, isBinary):#Code that runs when message is triggered
		message = format(payload.decode('utf8')) #Message decoded as utf8
		
		if (message == '1'):#Multiple Image displaying algorithms can be added below
			#Replace your own code here. Below is a simple example
			img = cv2.imread('res/facetest.jpg')
			
			#The code below sends the image to the Image viewer. DO NOT DELETE
			#the image is passed to the encoder as img, you can pass any other image matrix
			encode_param=[1,90]
			res, image = cv2.imencode('.jpg',img,encode_param)
			sample = base64.b64encode(image)
			self.sendMessage(sample, isBinary)
			
		#if (message == '2'): #add extra algorithm like this
				
    def onClose(self, wasClean, code, reason):#Message displayed when there is an error
        print format(reason)


	
#Start Websocket Server
if __name__ == '__main__':
    import sys
    from twisted.internet import reactor

    factory = WebSocketServerFactory("ws://localhost:555", debug=False)#Set debug false to save on processing time
    factory.protocol = MyServerProtocol

    reactor.listenTCP(555, factory)
    reactor.run()
		

	


