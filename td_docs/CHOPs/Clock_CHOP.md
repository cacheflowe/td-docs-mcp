---
url: https://docs.derivative.ca/Clock_CHOP
category: CHOPs
title: Clock_CHOP
---

# Clock CHOP
## Summary

The Clock CHOP generates channels that reflect the time of year, month, week, day, hour, minute, second and millisecond. It also has a moon cycle channel. It provides the date as separate channels and in different units. It presents the time in two ways:
  * It generates **0-1 ramps** that reflect the time of year, month, week, day, hour, minute, second and millisecond.
  * It generates **integers that reflects the day-of month** etc. In this form the year channel is 4 for 2004, etc.
  * It generates a countdown to a specific date.

There are sunrise/sunset features, and you can override the day-of-year by inputting 1-6 channels into the CHOP.
[clockCHOP_Class](https://docs.derivative.ca/ClockCHOP_Class "ClockCHOP Class")

## Parameters - Clock Page
- Output `output` - ⊞ - Fractions or Units affects the channel data that is output from the Clock CHOP. Fraction gives convenient 0-1 ramps and Units give integers, like 0-23 for the hours of a day. For example, use Fractions and the day, hour and minute channels to drive a wall clock.
  * Units `units` - Generates **integers that reflect the day-of month** etc. In this form the year channel is 4 for 2004, etc.
  * Fractions `fractions` - Generates **0-1 ramps** that reflect the time of year, month, week, day, hour, minute, second and millisecond.
  * Countdown `countdown` - Runs in a **Countdown** mode. The first input should contain channels name year, month, day, hour, min, sec and msec. Any missing values are assumed to be midnight January 1st of specified year. The second input is entirely optional, missing values are taken from current time. For year values, 25 means 2025, etc.

- Hour Format `hourformat` - ⊞ - 12 hour or 24 hour - Causes the hour channel to cycle through 12 or 24 hours. Also affects the AM/PM channel.
  * 12 hour `12` -
  * 24 hour `24` -

- Hour Adjust `houradjust` - After the Clock CHOP reads the current time, it adds Hour Adjust to pretend the current time is different than the actual current time.
- Start Reference `startref` - ⊞ - The date/time that corresponds to year 0, day 1, hour 0, minute 0. It can be relative to Jan 1, 2000 or to the time that the TouchDesigner process started.
  * Since Jan 1 2000 `jan1` -
  * Since Program Start `program` -

- Millisecond `msec` - If Output is Units, it is the current millisecond, starting at 0 at the start of a second, going up to 999 at the end of a second. If Output is Fraction, it is the current fraction of a millisecond.
- Second `sec` - If Output is Units, it is the current second, starting at 0 for on-the-hour, going up to 59. If Output is Fraction, it is the current fraction of a second (45 seconds past the minute gives .75).
- Minute `min` - If Output is Units, it is the current minute, starting at 0 for on-the-hour, going up to 59. If Output is Fraction, it is the current fraction of a minute (45 seconds past the minute gives .75).
- Hour `hour` - If Output is Units, it is the current hour, starting at 0 for midnight and affected by AM/PM. If Output is Fraction, it is the current fraction of an hour (15 minutes past the hour gives .25), taking into account the current minute and second.
- AM/PM `ampm` - 0 if before noon, 1 if after noon.
- Day of Week `wday` - If Output is Units, it is the actual day of the week, starting with 0 for Monday and 6 for Sunday. If Output is Fraction, it is fraction of a day of the current moment, so at 6:30 PM, it is .77, taking into account the hour, minute and second. To get the fraction for the current time in relation to the week, use the week output.
- Day of Month `day` - If Output is Units, it is the actual day of the month, so on March 20, it is 20. If Output is Fraction, this parameter is disabled. To get the fraction for the current time in relation to the month, use the month output.
- Day of Year `yday` - If Output is Units, it is the Day of year, starting with 0 for January 1. If it is Fraction, this parameter is disabled. To get the fraction for the current time in relation to the year, use the year output.
- Week `week` - Week of the year, starting with 0 for the first week and 51 for the last week of the year.
- Month `month` - Month of the year, starting with 1 for January and 12 for December.
- Year `year` - If Output is Units, it is the integer year number relative to the Start Reference, starting at 0, so year 2009 is 9 by default. If Output is Fraction, it is the current fraction of a year, taking into account today's month, day, hour, minute and second.

## Parameters - Solar Page
- Latitude `latitude` - ⊞ - Enter a latitude (hours/min north/south) of your location. (defaults to Toronto, Canada). Fractional hours are permitted. For example: 43.6532 hours and 0 minutes, is identical to 43 hours and 39 minutes. The parameter latitude1 is hours, latitude2 is minutes.
  * `latitude1` -
  * `latitude2` -

- NS `northsouth` - ⊞ - Set if the Latitude value above is in the north or south hemisphere.
  * North `north` -
  * South `south` -

- Longitude `longitude` - ⊞ - Enter a longitude (hours/min east/west) of your location. Fractional hours are permitted. The parameter longitude1 is hours, longitude2 is minutes.
  * `longitude1` -
  * `longitude2` -

- EW `eastwest` - ⊞ - Set if the Longitude value above is in the east or west hemisphere.
  * East `east` -
  * West `west` -

- Moon Phase `moonphase` - Outputs the moon phase (0 to 1. .5 is a full moon, 0 and 1 are at the time of the new moon).
- Sun Phase `sunphase` - (0 to 1, where sunrise=0, sunset = 1, and it reverses down to 0 in time for the sunrise.
- Sunrise `sunrise` - Outputs the sunrise time (0 to 1, midnight=0, twenty-four hours later = 1).
- Sunset `sunset` - Outputs the sunset time (0 to 1, midnight=0, twent.y-four hours later = 1).
- Declination `declination` - (-180 to 180, degrees north/south that the sun is off the equator).

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
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Clock CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
