---
url: https://docs.derivative.ca/Palette:firmata
category: Interoperability
title: Palette:firmata
---

# Palette:firmata

## Summary

Firmata is an [Arduino](Arduino.md "Arduino") sketch allowing for configuration and control of the Arduino using messages formatted as MIDI.

More information on the firmata protocol can be found here: <https://github.com/firmata/protocol>

See also <https://jmarsico.github.io/rsma2019/tutorials/td_arduino/>

[Palette:firmata Ext](https://docs.derivative.ca/Palette:firmata_Ext "Palette:firmata Ext")

Getting Started
  * Install the latest Arduino IDE on your computer and connect your Arduino board.
  * In the Arduino IDE, under `File`, select `Examples>Firmata>Standard Firmata` and upload it to your board.
  * Close the IDE and select the port your Arduino is conencted to on the firmata COMP's `Port` parameter.
  * Toggle the `Active` parameter. The component will attempt to communicate with the Arduino and create all necessary parameters for pin-modes and pin-values.
  * Via the now available `Pin Modes` and `Pin Values` pages, setup and control your Arduino.
  * The CHOP output form the component contains all pin values.

## Parameters - Firmata Page
- Firmata Type `Firmatatype` - When connecting to an Arduino, will display the name of the sketch uploaded to the Arduino.
- Firmata Version `Firmataversion` - When connecting to an Arduino, will display the version of Firmata uploaded to the Arduino.
- Active `Active` - Toggle on to start communicating with the Arduino.
- Port `Port` - Select the COM Port the Arduino is connected to.
- Baud Rate `Baudrate` - Set the Baud Rate of the selected COM Port.
- Reset `Reset` - Reset the firmata Component to it's original empty state.
- Query Version `Queryver` - Query the Firmata version uploaded to the Arduino.
- Query Board Capabilities `Querycap` - Query the supported modes and resolution of all pins.
- Query Pin States `Querystates` - Query the pins' current mode and state (different than value).
- Query Analog Mapping `Queryanalog` - Ask for the mapping of analog to pin numbers.
- Report All Analog Pins `Reportanalog` - Toggle on to report all analog pin values.
- Report All Digital Ports `Reportdigital` - Toggle on to report all digital pin values.
- Sampling Interval `Samplinginterval` - Set the interval at which analog input is sampled (default = 19ms).

## Parameters - Pin Modes Page

This will contain as many menu parameters as available pins on the Arduino with the available modes for each pin respectively. Possible modes can be:
  * DIGITAL_INPUT
  * DIGITAL_OUTPUT
  * ANALOG_INPUT
  * PWM
  * SERVO
  * SHIFT
  * I2C
  * ONEWIRE
  * STEPPER
  * ENCODER
  * SERIAL
  * INPUT_PULLUP
- Pin 2 `Modepin2` - Select the operating mode for this pin.

## Parameters - Pin Values Page

This page will contain a number of Pin Values either to set the values or display the reported values. If reporting values, the respective parameters will be in read-only mode. For digital pins, enabling reporting is only possible on a per-port basis with pins being grouped in up to 8 pin blocks.
- Enable Reporting `Reportport0` - Enable Reporting for this Pin or Port.
- Pin 2 `Valpin2` - Get or set the current value of the pin.

## Parameters - Servo Page
- Min Pulse `Minpulse` - The Servo's minimum pulse length for the minimum angle.
- Max Pulse `Maxpulse` - The Servo's maximum pulse length for the maximum angle.

## Parameters - About Page
- Help `Help` - Opens this page.
- Version `Version` - The current version of the component.

.tox Save Build `Toxsavebuild` - THe TouchDesigner build this component was saved with.

## Operator Outputs

  * Output 0 - A CHOP containing all pin values.
