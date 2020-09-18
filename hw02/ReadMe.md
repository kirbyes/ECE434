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

Run the program by first running `chmod +x buttonsAndLEDs.py`. Then run `./buttonsAndLEDs.py`

## Measuring a GPIO Pin with an Oscilliscope

|  | sh | python | c without lseek | c with lseek | toggle1.c | toggle1.py | toggle2.c | toggle2.py |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Minimum Voltage (V) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maximum Voltage (V) | 3.32 | 3.32 | 3.32 | 3.32 | 3.32 | 3.32 | 3.32 | 3.32 |
| Processor Usage (%) | 21.1 | 3.3 | 3.3 | 2.6 | 100 | 100 | 100 | 100 |
| Shortest Period (us) | 42000 | 500 | 350 | 220 | 3.4 | 17.45 | 3.6 | 18.3 |
| Period Stability (ms) | +/- 1 | +/- 0 | +/- 0 | +/- 0 |  |  |  |  |

### 1.) What's the min and max voltage?

OV - 3.32V

### 2.) What period is it?

243ms

### 3.) How close is to 100ms?

This is 143ms greater than 100ms.

### 4.) Why do they differ?

The input for the togglegpio.sh program is the sleep time, so it is half the period. 
This means that the period should be around 200ms. It is much longer than this because 
it has to echo the value to a file location, which is a lengthy operation.

### 5.) What is the processor usage?

21.1%

### 6.) What is the shortest period you can get?

42 ms

### 7.) How stable is the period?

It only fluctuates a ms around the period with input 0.1.

### 8.) After launching vi, how stable is the period?

It now fluctuates about 20 ms around the period.

### 9.) After cleaning up togglegpio.sh does it impact the period?

Yes, it speeds it up so it is now closer to 200ms.

### 10.) Try using sh instead of bash. Is the period shorter?

Yes, the period is about 10 ms faster.

### 11.) What is the shortest period you can get?

Now the shortest period I can get is 31ms.

## Python

Results are summarized in the table above.

## C

Results are summarized in the table above.

## Security


## Etch-A-Sketch

A modification of the game in `hw01/etchASketch.py`. Now uses buttons to control the movement and clearing. Pin assignments are as follows:
* Up: P9_21
* Down: P9_23
* Right: P9_26
* Left: P9_27
* Clear: P9_30

Run the program by first running `chmod +x etchASketch.py`. Then run `./etchASketch.py`