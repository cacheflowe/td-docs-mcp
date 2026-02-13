---
url: https://docs.derivative.ca/Laser_CHOP
category: CHOPs
title: Laser_CHOP
---

# Laser CHOP
## Summary

The Laser CHOP produces channels that can drive a laser projector. It uses the points and lines of a POP, SOP or CHOP and outputs the channels at a specified sample rate, typically 10,000 to 96,000 samples per second. The Laser CHOP gives optimal control over the movement of the reflectors of the laser projector as well as enhanced color control. In particular, it gives better control of lines being straight, end-points being not cut off or over-drawn, and eliminating tails, all adjustable using a set of parameters.
When sending CHOP channels to the Laser CHOP, the CHOP expects `x` and `y` channels and every sample will be interpreted as a point to be drawn. To draw multiple shapes, also specify a channel named `id` to identify each shape. Points with `id = 0` are part of the first shape, points with `id = 1` form the second shape. All other channels will be interpreted as color channels and blanking will be applied to those. This makes it possible to drive lasers that have more than just RGB diodes active.
The channels output from the Laser CHOP can be sent to the [Laser Device CHOP](https://docs.derivative.ca/Laser_Device_CHOP "Laser Device CHOP") in case of controlling a Laser via the [ILDA Protocol](https://en.wikipedia.org/wiki/International_Laser_Display_Association), or the [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP") in case of using one of LaserAnimation Sollinger's [AVB](https://en.wikipedia.org/wiki/Audio_Video_Bridging) capable devices, where the audio is output via the [Audio Device Out CHOP](https://docs.derivative.ca/Audio_Device_Out_CHOP "Audio Device Out CHOP") to a low-latency AVB-ready audio device like those from MOTU, RME, LaserAnimation Sollinger or Apple macOS.
[LaserAnimation Sollinger's AVB2ILDA devices](https://laseranimation.com/en/products/avb-devices) give you access to features for the professional sector. See [Lasers](https://docs.derivative.ca/Lasers "Lasers").
The CHOP was developed with the help of [LaserAnimation Sollinger](https://laseranimation.com/en/) who guided us in speccing and implementing the necessary parameters, especially in regards of the blanking timing settings.
**Tip** : See the [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") for setup and usage examples.
(The Laser CHOP replaces the legacy Scan CHOP.)
**LASERS ARE DANGEROUS - DAMAGE TO YOUR OR THE AUDIENCE'S EYE SIGHT IS A VERY REAL RISK**
  * If you plan to use lasers

  1. Understand all the laws and regulations for laser operation in your area.
  2. Become a certified Laser Safety Officer (this is required by law in some areas). Courses are available from ILDA directly: [ILDA Laser Safety Courses](https://www.ilda.com/LSOcourse.htm)

  * Make sure an emergency stop button is close to you at all times.
  * Do not let anyone enter the laser projection area unless all precautions have been taken to limit the output.
  * Make sure there are no reflective surfaces in the projection area that might cause the beam to reflect unintendedly.

### Corner Points
The Laser CHOP categorizes input points as either corner points or guide points. Prior to the 2025.30000 series of builds, all points were considered corner points.
All input points are corner points by default. To set a point as either a corner or guide point, use a boolean attribute named `LasCorner` for SOP/POP inputs, or a `lascorner` channel for CHOP inputs. `LasCorner = 1` means it is a corner point.
Guide points are simply points that help move the laser along a path or curve, and they will not have abrupt changes in line direction between the two line segments they're a part of. Guide points are only output once and never repeated. Guide points are also useful for point interpolation when stepping is done along the curve.
Corner points essentially define the start/end points of an individual line strip on the laser. Interpolation of color and point position stepping is done between corner points, with guide points used for weighting. Corner points should also be used when there is an abrupt change in the laser direction (eg. right or acute angle) so that appropriate hold points can be added to increase sharpness of the image.
Corner points repeat as a function of their angle and the corner hold parameters. Additionally, for extra per-point control, corner hold look-up factor and hold add can be used through special attributes in SOP/POP inputs, or channels in CHOP inputs:
  * `LasCornerHoldAdd` (SOP or POP) or `lascornerholdadd` (CHOP)
  * `LasCornerHoldLookupFactor` (SOP or POP) or `lascornerholdlookupfactor` (CHOP)

Corner hold repeat is calculated as follows, where H is the hold value calculated from the angle/parameters:
```
NumRepeatPoints = HoldAdd + HoldLookupFactor * H
```

### Blanking
Blanking is the capability of a laser projector to rapidly turn on / off the laser when displaying animations. For example when displaying multiple shapes, the laser needs the ability of blanking to omit the empty spots between the shapes. Blanking is done automatically between shapes but quantity of blanking points is controlled through the set of blanking delay parameters on the Color Page, as well as the Blanking Step Size parameter on the Scanning Page.
As the laser's mirrors are driven by motors, the positional data that is send to the laser is likely to be ahead of the actual mirror position - the mirror must catch up to the data. The Color data though is in time and as a result the effect can be visible tails at points where the laser switches off its color. Adjusting the blanking parameters can help prevent this.
See also: [Laser Device CHOP](https://docs.derivative.ca/Laser_Device_CHOP "Laser Device CHOP"), [Pangolin CHOP](https://docs.derivative.ca/Pangolin_CHOP "Pangolin CHOP"), [Line Smooth POP](https://docs.derivative.ca/Line_Smooth_POP "Line Smooth POP")
[laserCHOP_Class](https://docs.derivative.ca/LaserCHOP_Class "LaserCHOP Class")

## Parameters - Laser Page
- Active `active` - When disabled, the CHOP will zero out all channels.
- Source OP `source` - ⊞ - Select the source operator type for the laser image.
  * SOP `sop` - Use a SOP as the source for the Laser image. Apart from position attributes, the SOP's point color attributes are used to determine the color output.
  * CHOP `chop` - Use a CHOP as the source for the Laser image. Tthe CHOP expects `x` and `y` channels and every sample will be interpreted as a point to be drawn. To draw multiple shapes, also specify a channel named `id` to identify each shape. Points with `id = 0` are part of the first shape, points with `id = 1` form the second shape. All other channels will be interpreted as color channels and blanking will be applied to those. This makes it possible to drive lasers that have more than just RGB diodes active.
  * POP `pop` - Use a POP as the source for the Laser image. Apart from position attributes, the POP's color attributes are used to determine the color output.

- SOP `sop` - Path to the SOP. The SOP's position and color attributes (as well as other miscellaneous attributes such as `LasCorner`) will be used to generate the laser points.
- CHOP `chop` - Path to the CHOP. The input CHOP must have **x** , **y** channels for the point positions. In addition, it also supports **z** , **r** , **g** , **b** , and **id** channels. The **id** channel is used for grouping points together as a single shape. By default when no **id** channel is present, each point is separate and unconnected. Additional and arbitrarily named colour channels may be added for laser projectors that accept more than just r, g, b. Additional channels include: "lascorner", "lascornerholdadd", and "lascornerholdlookupfactor".
- POP `pop` - Path to the POP. The POP's position and color attributes (as well as other miscellaneous attributes such as `LasCorner`) will be used to generate the laser points.
- Output Sample Rate `outputrate` - The sample rate of the Laser CHOP, and the sample rate at which it will output to the laser. With the default 48000 samples per second and a 60fps frame rate, the Laser CHOP can output 800 position and color values per frame.
- Swap Output `swap` - Lets you swap the x and y axis of the output.
- X Scale `xscale` - Control the horizontal scale of the output.
- Y Scale `yscale` - Control the vertical scale of the output.
- Rotate `rotate` - Control the rotation of the output.
- Camera `camera` - Specify the path to a Camera COMP used to draw a SOP from the cameras view.
- Update Method `updatemethod` - ⊞ - Control how the Laser CHOP pulls data from its source.
In most cases you will want to keep this at the default setting "When All Points Drawn".
There is a specific usage case that requires the "Every Frame" update method. Background is that the Laser CHOP might have to draw the input values over multiple frames. For example given a source with 200 sampling values. After applying all blanking and step sizes at a certain sample rate, the Laser might need more than one frame to draw the full image. The effect will be visible by the Laser image flickering. With the default setting, the Laser will grab a new set of samples from its input once it has completed drawing all previous values. With the "Every Frame" update method, the Laser will grab the updated values for the remaining samples after each frame.
  * When All Points Drawn `alldrawn` - The Laser CHOP will read the source data once all points of the previous frame have been drawn.
  * Every Frame `everyframe` - The Laser CHOP will update the input every frame, no matter if it finished drawing the previous frame or not.

- Frame Start Pulse `startpulse` - When enabled, will insert a sample with all colors set to -1 at the beginning of the laser frame.
- Debug Channel `debugchan` - When enabled, an extra channel with point state will be included:
  * -1 : Frame Start Pulse
  * 0 : Color
  * 1 : Corner Hold Point
  * 2 : Start Point Hold Time
  * 3 : Pre Blank On
  * 4 : Post Blank On
  * 5 : Blanking
  * 6 : Pre Blank Off
  * 7 : Post Blank Off

- Corner Attribute Name `cornerattr` - For SOP and POP inputs, optionally change the point attribute name used to specifiy if a point is a corner point. Default is `LasCorner`.
- Corner Hold Add Attribute Name `cornerholdaddattr` - For SOP and POP inputs, optionally change the name of the point attribute used to add a constant value to the corner hold time. Default is `LasCornerHoldAdd`.
- Corner Hold Factor Attribute Name `cornerholdfactorattr` - For SOP and POP inputs, optionally change the name of the point attribute used to apply a lookup factor to the corner point hold. Default is `LasCornerHoldLookupFactor`.

## Parameters - Scanning Page
- Step Size `stepsize` - The distance each x,y can change while outputing color.
- Blanking Step Size `bstepsize` - The distance each x,y can change while not outputing color (blanking).
- Minimum Corner Hold `mincornerhold` - The minimum value of the corner hold of a point. The value of the corner hold of a point is calculated linearly in the range from the minimum to maximum corner hold, based on the steepness of the angle at the point. This angle is calculated with the following three points: the previous point, the point itself, and the next point. Example: when the angle at the point is 180 degrees then the corner hold of the point will be the minimum value.
- Maximum Corner Hold `maxcornerhold` - The maximum value of the corner hold of a point. See Minimum corner Hold for more details. When the angle at the point is 0 degrees, then the corner hold will be the maximum value. If the maximum value is lower than the minimum then the maximum will be clamped upward.
- Corner Hold Lookup CHOP `cornerholdchop` - Reference to a CHOP to use as the custom lookup curve when interpolating from min to max hold. By default (ie. when no CHOP is specified), then it is linearly interpolated.
- Closed Shape Overlap `closedoverlap` - For closed shapes, the number of points (specified in milliseconds) to overlap the start/end, to utilize color interpolation and get a more uniform shape.

## Parameters - Color Page
These parameters let you control how the color channels for the Laser are created. Especially paying attention to the blanking settings which will have to be adjusted matching the capabilities of your laser projector.
- Red Scale `redscale` - Set the intensity of the Red Channel.
- Green Scale `greenscale` - Set the intensity of the Green Channel.
- Blue Scale `bluescale` - Set the intensity of the Blue Channel.
- Pre Blanking On Delay `preblankon` - Set the time in ms the Laser should wait at a position before turning the color output off.
- Post Blanking On Delay `postblankon` - Set the time in ms the Laser should wait at a position after turning the color output off.
- Pre Blanking Off Delay `preblankoff` - Set the time in ms the Laser should wait at a position before turning the color output on.
- Post Blanking Off Delay `postblankoff` - Set the time in ms the Laser should wait at a position after turning the color output on.
- Start-Point Hold Time `starthold` - Set the time in ms the Laser should wait at the first point of a new data frame before continuing on.
- Color Delay `colordelay` - Set the delay in ms of the color channels in the output.
- Interpolate Colors `interpcolors` - When enabled, interpolates colors between points.
- Brightness Curve Lookup CHOP `brightnesscurvechop` - Reference a CHOP to use as a custom look-up for soft-edge blending of closed shapes.

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
Extra Information for the Laser CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
