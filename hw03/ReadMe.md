# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5 | TMP101 
|  3 |   | setup.sh
|  2 |   | Documentation | *Well done*
|  5 | Etch-a-Sketch
|  3 |   | setup.sh
|  2 |   | Documentation
| 20 | **Total**

*My comments are in italics. --may*

# Homework 3
## TMP101
The TMP101s are wired up on bus 2. The alert pin for the first TMP101 is connected to P9_12. The alert pin for the second TMP101 is connected to P9_11.
temp.sh will read the value of the alert pins and print out the temperature every second. temp.py will print out the temperature if the alert pin is triggered.
To run temp.py, first run `chmod +x setup.sh` and then `./temp.py`

*chmod isn't needed.  git remembers it from before.*

## Etch-A-Sketch
To run the Etch-A-Sketch first run `chmod +x setup.sh` and then run `./etchASketch.py`. This will display an 8x8 grid on the computer and the 8x8 matrix
Clear the board with the spacebar. 
Move left by turning the right encoder counterclockwise. 
Move right by turning the right encoder clockwise.
Move up by turning the left encoder counterclockwise.
Move down by turning the left enoder clockwise.
