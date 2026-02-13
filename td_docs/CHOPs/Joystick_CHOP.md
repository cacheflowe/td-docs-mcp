---
url: https://docs.derivative.ca/Joystick_CHOP
category: CHOPs
title: Joystick_CHOP
---

# Joystick CHOP
## Summary

The Joystick CHOP outputs values for all 6 possible axes on any game controller (joysticks, game controllers, driving wheels, etc.), as well as up to 32 button, 2 sliders and 4 POV Hats.
It handles game controllers connected to the gameport or USB ports, including the [3D Connexion](http://www.3dconnexion.com/) mouse. You can have several devices attached, and any number of Joystick CHOPs in a project per device.
Before you use the game controller on your computer, calibrate them using Start -> Settings -> Control Panel -> Gaming Options -> Properties.
The main two outputs, the X-axis and Y-axis are output through channels called xaxis and yaxis. The other four axes are output through channels with similar names.
The range of the values for each channel is 0 to 1. For any axis, a value 0.5 is considered "centered". A value of 0 is given if the axis doesn't exist.
For any button, a value of 0 means the button is up or doesn't exist. A value of 1 means the button is pressed.
POV Hats behave like an X and Y axis. A POV axis only has 3 values though, 0, 0.5 and 1.
[joystickCHOP_Class](https://docs.derivative.ca/JoystickCHOP_Class "JoystickCHOP Class")

## Parameters - Control Page
- Active `active` - While on, the CHOP receives information from joysticks and gamepads. While Off, no updating occurs.
- Joystick Source `source` - This menu will list up to 4 game controllers currently attached to the computer presented to the operating system as Player 1 through Player 4. The selected game controller is the one the CHOP reads data from. If set to 'Default', the CHOP will adopt the first game controller it finds.
- Axis Range `axisrange` - ⊞ - Select between and axis range of 0 to 1 or -1 to 1.
  * [-1, 1] `negoneone` -
  * [0, 1] `zeroone` -

- X Axis `xaxis` - The name of the channel that records the X-axis position of the game controller.
- Y Axis `yaxis` - The name of the channel that records the Y-axis position of the game controller.
- Invert Y Axis `yaxisinvert` - Inverts the Y axis.
- Z Axis `zaxis` - The name of the channel that records the Z-axis position of the game controller.
- X Rotation `xrot` - The names of the channels that record the X-rotation axis position of the game controller.
- Y Rotation `yrot` - The names of the channels that record the Y-rotation axis position of the game controller.
- Invert Y Rotation `yrotinvert` - Invert the rotation direction around the Y axis.
- Z Rotation `zrot` - The names of the channels that record the Z-rotation axis position of the game controller.
- Slider 1 `slider0` - The name of the channel that records the position of the first slider on the game controller.
- Slider 2 `slider1` - The name of the channel that records the position of the second slider on the game controller.
- Button Array `buttonarray` - The names of the channels for the buttons on the game controller. This CHOP can handle up to 32 buttons.
- POV Hat Array `povarrray` - The names of the channels for the POV Hats. This CHOP can handle up to 4 POV Hats. The channels a POV hat is split up into are _POVHatName_ _X and _POVHatName_ _Y.
- POV Hat State Array `povstatearray` -
- Connected `connected` - Creates a channel that reports the state of connection of the controller.
- Axis Dead Zone `axisdeadzone` - This value defines how much of the area in the center of the joystick is considered 'dead zone'. When a joystick axis is in this dead zone it is considered to be centered. This value applies to all normal axes and rotation axes. This value is a percentage that defaults to 7%.

## Parameters - Channel Page
This sets the [Sample Rate](https://docs.derivative.ca/CHOP_Channel_Page#Sample_Rate "CHOP Channel Page") and the [Extend Conditions](https://docs.derivative.ca/CHOP_Channel_Page#Extend_Conditions "CHOP Channel Page").
- Sample Rate `rate` - The sample rate of the channels, in samples per second.
- Extend Left `left` - ⊞ - The left extend conditions (before range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope before the start of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Extend Right `right` - ⊞ - The right extend conditions (after range).
  * Hold `hold` - Hold the current value of the channel.
  * Slope `slope` - Continue the slope after the end of the channel.
  * Cycle `cycle` - Cycle the channel repeatedly.
  * Mirror `mirror` - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value `default` - Use the constant value specified in the Default Value parameter.

- Default Value `defval` - The value used for the Default Value extend condition.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page.
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).

## Info CHOP Channels
Extra Information for the Joystick CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common CHOP Info Channels
  * start - Start of the CHOP interval in samples.

  * length - Number of samples in the CHOP.

  * sample_rate - The samplerate of the channels in frames per second.

  * num_channels - Number of channels in the CHOP.

  * time_slice - 1 if CHOP is Time Slice enabled, 0 otherwise.

  * export_sernum - A count of how often the export connections have been updated.

###
## Common Operator Info Channels
  * total_cooks - Number of times the operator has cooked since the process started.

  * cook_time - Duration of the last cook in milliseconds.

  * cook_frame - Frame number when this operator was last cooked relative to the component timeline.

  * cook_abs_frame - Frame number when this operator was last cooked relative to the absolute time.

  * cook_start_time - Time in milliseconds at which the operator started cooking in the frame it was cooked.

  * cook_end_time - Time in milliseconds at which the operator finished cooking in the frame it was cooked.

  * cooked_this_frame - 1 if operator was cooked this frame.

  * warnings - Number of warnings in this operator if any.

  * errors - Number of errors in this operator if any.
