# Homework 2
## Buttons and LEDs
This program turns lights on when buttons are pressed. There are four LEDs each with a cooresponding button. Pin assignments are:
* LEDs
    * P9_11
    * P9_13
    * P9_15
    * P9_17
* Buttons
    * P9_21
    * P9_23
    * P9_26
    * P9_27

Run the programby first running `chmod +x buttonsAndLEDs.py`. Then run `./buttonsAndLEDs.py`

## Measuring a GPIO Pin with an Oscilliscope

|  | sh | python | c without lseek | c with lseek | toggle1.c | toggle1.py | toggle2.c | toggle2.py |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Minimum Voltage (mV) | 0 | 0 | 0 | 0 |  |  |  |  |
| Maximum Voltage (mV) | 190 | 290 | 290 | 290 |  |  |  |  |
| Period (ms) | 243 | 201 | 200.5 | 200.5 |  |  |  |  |
| Period - 200 (ms) | 43 | 1 | 0.5 | 0.5 |  |  |  |  |
| Processor Usage (%) | 21.1 | 3.3 | 3.3 | 2.6 |  |  |  |  |
| Shortest Period (us) | 42000 | 500 | 350 | 220 | 3.4 | 17.45 | 3.6 | 18.3 |
| Period Stability (ms) | +/- 1 | +/- 0 | +/- 0 | +/- 0 |  |  |  |  |

* 5.) 
* 10.)
* 11.) 
* 12.)

## Security


## Etch-A-Sketch

A modification of the game in `hw01/etchASketch.py`. Now uses buttons to control the movement and clearing. Pin assignments are as follows:
* Up: P9_21
* Down: P9_23
* Right: P9_26
* Left: P9_27
* Clear: P9_30