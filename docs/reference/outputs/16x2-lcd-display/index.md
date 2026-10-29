The 16x2 LCD Display can be used to display two lines of 16 characters.

Use it to display short messages!

![Numeric LED](index.jpg)

## Wiring
Use the I2C cable to connect the sensor.  This has 4 wires in 2 pairs: orange-yellow and red-black:

![Code](../../../assets/i2c-cable.jpg)

Wire up as follows, using the Edge Connector or Motor Controller board:

|16x2 LCD Display  | Edge Connector | Motor Controller |
| :--------------- | :------------- | :--------------- |
|Red               | 5V             | Vin              |
|Black             | GND            | G                |
|Yellow            | SCL            | C                |
|Orange            | SDA            | D                |

Note that the LCD display needs arounf 4.5 - 5V to work well, but the Microbit only gives 3.3V.  So we need to ensure we add additional power.

On the edge connector wire it like this, using the 5V "Husky Lens" pins to connect the display and an additional 5V power from a USB input (this can come from a USB port on your computer or a USB power bank):

![Wiring](wiring-edge.png)

On the motor controller wire it like this, using the servo connector GND and VIN pins, and a power input such as 3AA batteries:

![Wiring](wiring-motor.png)


## Coding

You will need to add an extension to get additional blocks for the display.  Click on the extensions block:

![Extension block](../../../assets/block-extensions.png)

Then search for "lcd":

![Search extension](extensions-search.png)

Then click on the **i2cLD1602** extension:

![LCD extension](lcd-extension.png)

You should see a new block appear:

![LCD block](lcd-block.png)

Enter this code in **on start** and **forever** blocks:

![Code](code1.png)

Download the code to the microbit.

The code will show "Hello" on the top line and a random number on the bottom line.  The random number changes every half second:

![Hello](hello.jpg){ width=600 }

Note that if the message is not displaying clearly, you can adjust the blue screw on the back of the display to control the contrast.  The backlight jumper needs to be present for the backlight to be on:

![Adjust contrast](adjust.jpg){ width=600 }

