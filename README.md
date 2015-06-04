# openCVBuildathon Viewing Framework

##Installation

1. First clone the repo to your edison board from the commandline

2. Make sure all the python pip dependencies have been installed </br>
 a. numpy : pip install numpy (pip install numpy -U "if numpy is already installed")</br>
 b. autobahn : pip install autobahn (pip install autobahn -U "if autobahn is already installed")</br>
 c. twisted : pip install twisted (pip install twisted -U "if twisted is already installed")</br>
	
3. Make sure the nodejs npm dependencies have been installed
	a. express : npm install -g express --update
	
4. Run the streaming server using this command : node stream.js > output.txt &
This will run the code in the background while any output will be written to output.txt.

###Running image Viewer
5. Edit the image.html document in the static folder. Change the localUrl variable to the edison device ip address
with respect to your computer.
6. Save and exit. Edit the image.py file in the main folder. You can choose to replace your own code as instructed
on the document, or you can choose to run the sample as it is.
7. To run the script you can run "python image.py"

###Running Video Viewer
5. Edit the video.html document in the static folder. Change the localUrl variable to the edison device ip address
with respect to your computer.
6. Save and exit. Edit the video.py file in the main folder. You can choose to replace your own code as instructed
on the document, or you can choose to run the sample as it is.
7. To run the script you can run "python video.py"

###Running Camera Viewer
5. Edit the camera.html document in the static folder. Change the localUrl variable to the edison device ip address
with respect to your computer.
6. Save and exit. Edit the camera.py file in the main folder. You can choose to replace your own code as instructed
on the document, or you can choose to run the sample as it is.
7. To run the script you can run "python camera.py"