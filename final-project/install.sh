#!/bin/bash

sudo apt-get update
sudo apt-get install build-essential python-dev python-setuptoolspython-pip python-smbus python-pip python3-pip -y

sudo pip3 install Adafruit_BBIO

sudo apt-get install mopidy
sudo apt-get install pulseaudio

sudo apt-get install mopidy-spotify
sudo pip install Mopidy-Mopify

sudo apt-get install git python-dev python-numpy python-opengl libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf libfreetype6-dev
sudo apt-get install python-pygame

sudo pip install Mopidy-EvtDev
git clone https://github.com/kirbyes/final_project/mopidy_touchscreen.git
