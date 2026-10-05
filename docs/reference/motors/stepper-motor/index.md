Stepper motors give you a very precise movement of a number of steps. They are used in things like 3D printers, CNC machines, etc.

![Stepper](index.jpg)

## Wiring
Steppers have 4 wires, which may be already attached to the motor, or you may need to plug them in:

![Connect cable](cable-connect.jpg)

The wires come in two pairs.  You need to identify the matching pairs.  These may be marked, or you can use the continuity/buzz or resistance feature of a multimeter to find matching pairs.  You should get a buzz or a 0 resistance for matching pairs:

![Detecting pairs](find-pair.jpg)

We will use the Motor Controller to drive the motor.  Connect one wire pair to M1 and the other to M2:

![Wiring](wiring.png)

The stepper motor uses a lot of power, so connect 4xAA batteries to the power connector on the motor driver.

## Coding 
To use the motor you need to add the extension.

To add the extension, first click on Extensions:

![GS cable](../../../assets/block-extension.png){ width=400 }

Then enter the URL for the extension:

![Extension](extensions.png)

Then click on the extension:

![Extension](extension.png)

You should see the following block:

![Block](motor-block.png)

Enter the following code:

![Code](code.png)

Download the code to the microbit.

The motor should move forwards for 100 steps and then stop.