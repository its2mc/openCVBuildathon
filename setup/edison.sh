sudo opkg update && 
sudo opkg install opencv python-opencv build-essential wget && 
wget https://bootstrap.pypa.io/get-pip.py &&
sudo python get-pip.py &&
echo "Please ignore the errors on twisted installation\n"&&
pip install numpy autobahn twisted 
