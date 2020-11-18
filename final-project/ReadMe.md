# Spotify Box
# ECE434 - Embedded Linux Final Project

This project uses Mopidy, Mopidy-Spotify, and Mopidy-Touchscreen to create an interface to listen to Spotify through a BeagleBone Black.

More information about this project can be found at [ELinux](https://elinux.org/ECE434_Spotify_Box) and [hackster.io]().

# Instillation

1. Clone this git repository 
`git clone https://github.com/kirbyes/ECE434.git`

2. Run install.sh. This only needs to be run the first time that you are running the program.
`chmod +x install.sh`
`./install.sh`

3. Edit the config file with your 

3. Change directory to the spotify-box folder and install our revised version of mopidy-touchscreen.
`cd spotify-box`
`sudo python setup.py install`
`cd ..`

3. Run setup.sh. This needs to be run everytime before you want to run the program.
`chmod +x setup.sh`
`./setup.sh`

4. Run the program.
`sudo mopidy`