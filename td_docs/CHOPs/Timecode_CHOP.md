---
url: https://docs.derivative.ca/Timecode_CHOP
category: CHOPs
title: Timecode_CHOP
---

# Timecode CHOP
## Summary

The Timecode CHOP generates [Timecode](https://docs.derivative.ca/Timecode "Timecode") data (channels, a `.timecode` python object and other python members). Its Mode menu provides a variety of ways to get, set and generate timecode through its parameters, including being driven from a timecode string, a set of channels, or other OPs that have timecode such as video input devices. You can also set timecode with python functions.
The timecode data is output as both channel data in the CHOP, and as a [Timecode object](https://docs.derivative.ca/Timecode_Class "Timecode Class") via its [`.timecode` member](https://docs.derivative.ca/TimecodeCHOP_Class#timecode "TimecodeCHOP Class") in Python.
The timecode can follow the SMPTE standard (ie. non-negative, frames-per-second up to 60, loops at 24 hours), or a more general format (ie. any number of frames per second, negative timecode allowed, loops at 100 hours).
When being driven by channels, an input with channels named `negative`, `hour`, `minute`, `second`, or `frame` can be provided that is added to the Timecode CHOP's output.
See also: [Timecode](https://docs.derivative.ca/Timecode "Timecode"), [Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class") and the OP Snippets for the Timecode CHOP.
[timecodeCHOP_Class](https://docs.derivative.ca/TimecodeCHOP_Class "TimecodeCHOP Class")

## Parameters - Timecode Page
- SMPTE `smpte` - When enabled the generated timecode will follow the [SMPTE timecode](https://en.wikipedia.org/wiki/SMPTE_timecode) standard, meaning no negative timecodes, and the timecode will loop at 24 hours. When disabled, the format will be more general, allowing for negative numbers and a maximum timecode of 100 hours.
- Mode `mode` - ⊞ - The source used for generating the timecode
  * Locked to Timeline `lockedtotimeline` - Generates the timecode from the timeline's time.
  * Specify Index `specifyindex` - Generates the timecode from a single index value.
  * Timecode String `timecodestr` - Generates the timecode from a timecode string following the format: `hh:mm:ss:ff` or `hh:mm:ss.ff`
  * Hour, Minute, Second, Frame Parameters `timecodepar` - Generates the timecode from hour, minute, second, and frame parameters. The parameters will overflow from one to the next, eg. specifying 120 seconds will output timecode as `00:02:00:00`. Fractional values are also allowed.
  * Sequential `sequential` - The timecode increases sequentially over time.
  * Timecode Object `timecodeobj` - Generates the timecode from a [timecode object](https://docs.derivative.ca/Timecode_Class "Timecode Class").
  * CHOP Channels `chop` - Generates the timecode from a CHOP reference with some or all of the channels: negative, hour, minute, second, frame.
  * OP Reference `op` - Generates the timecode from an OP with a timecode Python member, eg. [MoviefileinTOP_Class](https://docs.derivative.ca/MoviefileinTOP_Class "MoviefileinTOP Class").

- Rate `rate` - The timecode FPS. The timecode's max frame value is equal to `rate-1`. If a fractional rate is provided then the rate is rounded up to the nearest whole number and drop-frames will be calculated if enabled on the Drop Frame parameter.
- Drop Frame `dropframe` - ⊞ - Specify how to calculate [drop-frames](https://en.wikipedia.org/wiki/SMPTE_timecode#Drop-frame_timecode). Drop frames are used when the FPS is fractional. FPS cannot increment a fractional amount per frame so FPS is rounded to the next whole number and the accumulation of error is accommodated for by adding drop frames.
  * Off `off` - Drop-frames will not added.
  * Automatic `auto` - Drop-frames will be added to the timecode when the rate is fractional. For special rate values such as 29.97, the defined standard solution is used (ie. 2 frames added every minute, except minutes that are divisible by 10). In other cases, a general solution is used by calculating the accumulated error.

- Index `index` - The index used to generate the timecode. Value is used in conjunction with the specified units.
- Index Unit `indexunit` - ⊞ - The index value units.
  * I `indices` -
  * F `frames` -
  * S `seconds` -

- Timecode String `timecodestr` - A timecode string following the format: `hh:mm:ss:ff` or `hh:mm:ss.ff`
- Frame `frame` - Frame component of the timecode.
- Second `second` - Second component of the timecode.
- Minute `minute` - Minute component of the timecode. Allows for overflow.
- Hour `hour` - Hour component of the timecode.
- Initialize `init` - Used in sequential mode. Initializes the timecode value.
- Start `start` - Used in sequential mode. Starts the timecode sequential increment.
- Play `play` - When enabled, the sequential timecode will step forward.
- Timecode Object `timecodeobj` - A [timecode object](https://docs.derivative.ca/Timecode_Class "Timecode Class").
- CHOP `chop` - A CHOP reference which contains some or all of the following channels: negative, hour, minute, second, frame.
- OP `op` - An OP reference that contains a timecode Python member: eg. [MoviefileinTOP_Class](https://docs.derivative.ca/MoviefileinTOP_Class "MoviefileinTOP Class").
- Custom Length `customlength` - ⊞ - If set to "By Value", then the Length parameter is used. If set to "By Timecode", then the Length Timecode Object is used. If set to "Off", then the default length will be 23:59:59:ff-1 for a SMPTE timecode and 99:59:59:ff-1 otherwise.
  * Off `off` - When selected, will not use a custom length. The length will default to 23:59:59:ff-1 for a SMPTE timecode and 99:59:59:ff-1 otherwise.
  * By Value `value` - When selected, set the custom length from a value using the Length parameter.
  * By Timecode Object `timecodeobj` - When selected, set the custom length from a [timecode object](https://docs.derivative.ca/Timecode_Class "Timecode Class") using the Length Timecode Object parameter.

- Length `length` - Specifies the custom length in either samples, frames, or seconds.
- Length Units `lengthunits` - ⊞ - The unit of the custom length.
  * I `samples` -
  * F `frames` -
  * S `seconds` -

- Length Timecode Object `lengthtimecodeobj` - Specifies the custom length as a [timecode object](https://docs.derivative.ca/Timecode_Class "Timecode Class").
- Extend Left `extendleft` - ⊞ - Set the timecode behavior when exceeding the lower bound of 00:00:00:00 for SMPTE timecode and -99:59:59:ff+1 otherwise.
  * Hold `hold` - If selected, then the timecode will hold its value when exceeding lower bound: 00:00:00:00 for SMPTE timecode and -99:59:59:ff+1 otherwise.
  * Cycle `cycle` - If selected, then the timecode will cycle its value when exceeding lower bound. It will cycle to the length value for SMPTE timecode and 00:00:00:00 otherwise.

- Extend Right `extendright` - ⊞ - Set the timecode behavior when exceeding the upper bound defined by the length parameters.
  * Hold `hold` - If selected, then the timecode will hold its value to the length value.
  * Cycle `cycle` - If selected, then the timecode will cycle to 00:00:00:00 once it reaches length.

## Parameters - Output Page
- Negative Chan `negativechan` - When enabled, outputs the negative channel, which is true when the timecode is negative. Always false when using SMPTE standard.
- Frame Chan `framechan` - When enabled, outputs the frame channel.
- Second Chan `secondchan` - When enabled, outputs the second channel.
- Minute Chan `minutechan` - When enabled, outputs the minute channel.
- Hour Chan `hourchan` - When enabled, outputs the hour channel.
- Total Seconds Chan `totalseconds` - When enabled, outputs the total_seconds channel, which is the timecode converted into seconds.
- Total Frames Chan `totalframes` - When enabled, outputs the total_frames channel, which is the timecode into frames.
- Drop Frame Chan `dropframechan` - When enabled, outputs the drop_frame channel, which is true when the timecode is drop-frame.
- FPS Chan `fpschan` - When enabled, outputs the fps channel.

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

## Operator Inputs
  * Input 0:  - Optional input CHOP with some or all of following channels: negative, hour, minute, second, frame. The input timecode value is added to the Timecode CHOP's output.
