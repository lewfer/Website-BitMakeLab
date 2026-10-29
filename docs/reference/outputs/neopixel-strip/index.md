Neopixels come as strips of LEDs.  Each LED can be individually set to a different colour.

Use a neopixel to make a colourful light show, visualise some data and much more!

![Neopixel](index.jpg)

## Wiring
Use a GVS cable to connect the neopixel. This has 3 wires, blue, red and black:

![Cable](../../../assets/gvs-cable.jpg)

Wire up as follows, using the Edge Connector or Motor Controller board:

|Neopixel          | Microbit             | 
| :--------------- | :------------------- | 
|3-pin connector   | P12 3-pin connector  | 

Make sure you connect the cable the right way round, with the black wire connecting to the black pin on both ends.

On the edge connector it should look like this:

![Wiring](wiring.png)

You don't have to use pin P12.  You can use any <a href="../../../assets/pins-short.png" target="_blank">digital pin</a>.  Just remember to adjust your code accordingly.

## Coding

You will need to add an extension to get additional blocks for the neopixel.  Click on the extensions block:

![Extension block](../../../assets/block-extensions.png)

Then search for "neopixel":

![Search extension](extensions-search.png)

Then click on the **neopixel** extension:

![Neopixel Extension](neopixel-extension.png)

You should see a new block appear:

![OLED block](neopixel-block.png)

Enter this code in **on start** and **forever** blocks:

![Code](code1.png)

Download the code to the microbit.

The on start block sets up a strip of 5 neopixels and shows a rainbow of colours on each one.  The forever block then rotates the pixels, so they move around the strip every 1/2 second.

![Rotate](rotate.gif){ width=600 }

The values in the show rainbow block relate to the range of colours, or **hue**, to show. You can use values from 0 to 360.  This relates to the HSL (Hue Saturation Lightness) model for defining colours.  Take a look at the link below.  Slide the H slider (H for Hue) from 0 to 360 to see the colours corresponding to each value.

[HSL Colours](https://www.w3schools.com/colors/colors_hsl.asp){target=_blank}

