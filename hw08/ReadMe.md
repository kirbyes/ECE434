# Homework 8
## Blinking an LED
`make start` will start the PRU and `make stop` will stop the PRU.

![LED](led.png)
Figure 1: Toggling P9_31 as fast as possible using ARM GPIO

## PWM Generator
![PRU Fast](pruFast.png)
Figure 2: Toggling P9_31 as fast as possile using the PRU

![PRU 50](pru50.png)
Figure 3: Toggling P9_31 at 50 MHz using the PRU

## Controlling the PWM Frequency
Bits 0-3 of __R30 are being used. Thes correspond to P9_31, P9_29, P9_30, and P9_28.

![PWM Initial](pwmInitial.png)
Figure 4: Using the given code to toggle the 4 PWM channels

![PWM Fast](pwmFast.png)
Figure 5: Toggling the 4 PWM channels as fast as possible

## Reading an Input at Regular Intervals
![Input Output](inputOutput.png)
Figure 6: With an input a of a square wave with a frequency of 12 MHz using a function generator, this is the output.

## Analog Wave Generator
![Sawtooth](sawtooth.png)
Figure 7: Sawtooth Output

![Triangle](triangle.png)
Figure 8: Triangle Output

![Sine](sine.png)
Figure 9: Sine Output