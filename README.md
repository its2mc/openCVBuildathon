# openCVBuildathon Viewing Framework

## Description

This is a simple framework that allows for developers to quickly test out their python
opencv programs and view the results on a website. The python programs are separated into 3
image.py, camera.py, video.py. Each script captures a image from a separate source i.e. 
image.py captures a static image saved in the res folder, video.py captures a series of images
from a video file saved in the res folder and camera.py captures a series of images from a 
camera connected to the device. 

To view the Output form the different scripts, once you run the server according to the 
instructions below, go to the urls e.g. localhost:5800/image.html or localhost:800/camera.html
or localhost:800/video.html

To add your program, simply insert your image manipulation algorithm in the spaces designated 
as shown below

'''

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
'''

The img variable stores the image that can be manipulated on command from the website.
The python script is basically a websocket server so you can run this remotely on your raspberry pi
or your computer and access from a different server, provided you connect to the ip address of the 
raspberry pi.


 

##Installation and Running (DEBIAN)

1. The prerequisite programs required to run the program are python, pip, opencv, pyopencv, numpy, autobahn(websocket library),
twisted. To simplify the installation process I have made a script to install the various components. After installing
nodejs and npm just run "<i>npm install</i>" followed by "<i>npm run setup-deb</i>" on your command line which should do the rest. This is 
made for the linux operating system, specifically debian based systems
i.e. with apt-get.

2. In your command line typing "<i>npm run server</i>" will start up the web server, although you can start it from a remote pc. 

3. To start the python scripts just run "<i>npm run imageServer</i>" for the image server, "<i>npm run cameraServer</i>" for the camera server and "<i>npm run videoServer</i>" for the video server onto your command line. This will run image.py, video.py, camera.py log
their outputs to image.log, video.log and camera.log respectively. 

##Installation (Windows)

1. To run the programs in windows, you can still run the "<i>npm install</i>" then "<i>npm setup-win</i>" This is assuming that you have already installed
opencv, python, pip, nodejs and npm.

2. In your command line typing "<i>npm server</i>" will start up the web server, although you can start it from a remote pc. 

3. To start all the python scripts just run "<i>npm run-scripts</i>" onto your command line. This will run image.py, video.py, camera.py log
their outputs to image.log, video.log and camera.log respectively. 

##Installation in other systems

1. To add installation scripts for more systems please feel free to contribute.

