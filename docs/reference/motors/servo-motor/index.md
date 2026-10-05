Servo motors generally are designed to move to any angle between 0 and 180 degrees.

Use them where reasonably precise positioning of the motor is required, for example to control a lever or operate a robot arm.

![Servo](index.jpg)

![Angles](angles.png)

## Wiring
Servo motors have 3 wires connected together in a single cable:

![Wire](wire.jpg)

The middle red wire is for power.  The brown wire is for GND.  The orange (or sometimes yellow) wire is for the signal.

Connect the cable to the special connectors, marked S1, S2 etc, on the Motor Controller:

![Wiring](wiring2.jpg)

Make sure to connect the orange/yellow wire to the green pin and the brown wire to the black pin.

## Coding
To use the servo motor you need to add the extension.

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

The motor should move between 3 angles: 90 degrees, 160 degrees and 20 degrees.

Note that although most servo motors claim to run between 0 and 180 degrees, many don't work well or may even lock up at the far ends of the range.  So generally it makes sense to limit the angles to between 20 and 160 degrees.

