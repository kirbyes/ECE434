# Spotify Box
# ECE434 - Embedded Linux Final Project

This project uses Mopidy, Mopidy-Spotify, and Mopidy-Touchscreen to create an interface to listen to Spotify through a BeagleBone Black. It is
mostly just modifications of the mopidy-touchscreen to use the BeagleBone Black and its gpio including an LCD screen through SPI1 and buttons.

More information about this project can be found at [ELinux](https://elinux.org/ECE434_Spotify_Box) and [hackster.io]().

# Installation

1. Clone this git repository  
`git clone https://github.com/kirbyes/ECE434.git`  
  
2. Run install.sh. This only needs to be run the first time that you are running the program.  
`chmod +x install.sh`  
`./install.sh`  

3. Edit the config file with your Spotify credentials.  
`cd ~/.config/mopidy`  
`nano mopidy.conf`  
Copy the mopidy.conf file from this repository and paste it into yours  
Add your own credentials to the lines. To get the client_id and the client_secret visit [Spotify Credentials](https://mopidy.com/ext/spotify/)  
`username = `  
`password = `  
`client_id = `  
`client_secret = `  
  
3. Change directory to the spotify-box folder and install our revised version of mopidy-touchscreen.  
`cd spotify-box`  
`sudo python setup.py install`  
`cd ..`  
  
3. Run setup.sh. This needs to be run everytime before you want to run the program.  
`chmod +x setup.sh`  
`./setup.sh`  
  
4. Run the program.  
`sudo mopidy`  
