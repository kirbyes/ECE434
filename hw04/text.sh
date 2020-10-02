# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
# Place boris, but add text above 
convert boris2.png -pointsize 24 \
      label:'Eric Kirby' +swap -append \
      $TMP_FILE

#Display the image
sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font
