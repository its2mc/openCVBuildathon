sudo apt-get update && 
sudo apt-get install -y libopencv-dev python-opencv python-dev cmake build-essential python-setuptools wget libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev&& 
wget https://bootstrap.pypa.io/get-pip.py &&
sudo python get-pip.py &&
echo "Please ignore the errors on twisted installation\n"&&
sudo pip install numpy autobahn twisted 
