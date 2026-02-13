---
url: https://docs.derivative.ca/Perform_CHOP
category: CHOPs
title: Perform_CHOP
---

# Perform CHOP
## Summary

The Perform CHOP outputs many channels like frames-per-second, describing the current state of the TouchDesigner process. As channels they can be manipulated into user interfaces and calculations to adjust real-time self-tuning of the process.
It outputs the "cook time" of the prior frame that was drawn, which is a reflection of how many frames TouchDesigner cooked in the prior second. The `cook`
**Tip** : Put a Trail CHOP after the Perform CHOP to watch its progress.
channel, when sent to a Trail CHOP shows which frames were cooked and which were skipped, useful in optimizing your work to reach a desired frame rate.
The Built-in Variables found on Dialogs -> Variables -> Built-in include more useful data on your running system. See also the Built-in Variables section of the [Variables](https://docs.derivative.ca/Variables "Variables") page.
[performCHOP_Class](https://docs.derivative.ca/PerformCHOP_Class "PerformCHOP Class")

## Parameters - Perform Page
This is a listing of the channels output from the Perform CHOP.
- Frames per Second `fps` - The number of frames rendered in the last second.
- Frame Time `msec` - Amount of time each frame takes to cook in msec.
- Cook `cook` - Is equal to 1 when a frame is cooked and equal to 0 when a frame is skipped. It is often useful to view this channel in a [Trail CHOP](https://docs.derivative.ca/Trail_CHOP "Trail CHOP") to see when frames are skipped (dropped).
- Dropped Frames `droppedframes` - The number of frames dropped between the last frame and the current frame.
- Movie Read Ahead Misses `mvreadahead` - How many times the movie read ahead failed to maintain the number of specified Read Ahead frames.
- GPU Mem Used (MB) `gpumemused` - Amount of GPU memory used (in megabytes).
- Total GPU Mem (MB) `totalgpumem` - Total amount of GPU memory available on the system (in megabytes).
- Total Active OPs `activeops` - How many OPs are actively cooking.
- Total Deactivated OP Calls `deactivatedops` - Number of calls to cook a component that has its [Cooking Flag](https://docs.derivative.ca/Cooking_Flag "Cooking Flag") turned off.
- Total OPs `totalops` - Total number of OPs in the [.toe](https://docs.derivative.ca/.toe ".toe") file.
- CPU Mem Used (MB) `cpumemused` - Amount of CPU memory used (in megabytes).
- Cook State `cookstate` - Monitors which frames actually cooked. Pass the Perform CHOP to a Trail CHOP to properly see the trail of frames that did and did not cook. (It appears as always 1 because the viewer is displaying only the current frame and not frames it missed.)
- Cook Realtime `cookrealtime` - Monitors the state of the realtime flag, determining if TouchDesigner is running in realtime mode or not.
- Cookrate `cookrate` - The global target cook rate (frames per second) of the project. This is the frames per second of the root component, `root.time.rate`, typically `60`, though due to frames taking too long to cook, the actual frames per second may be lower.
- Time Slice Step `timeslicestep` - The number of frames that TouchDesigner stepped forward for the current cook. It's the length of the [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") in frames. It will be equal to 1 when the system is taking `1000/root.time.rate` msec or less to complete one frame (16.666 msec for a rate of 60).
- Time Slice Milliseconds `timeslicemsec` - The length of the current [Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)") in milliseconds.
- Perform Mode `performmode` - Monitors the state of [Perform Mode](https://docs.derivative.ca/Perform_Mode "Perform Mode").
- Perform Window Focus `performfocus` - Monitors if the Perform Window currently has focus or not.
- GPU Temperature (Slow) `gputemp` - Monitors the temperature of the system's GPUs, only works for NVIDIA GPUs.
- AC Line Status `aclinestatus` - Indicates if the laptop's AC Charger is plugged in and active. 1 if AC line is detected, 0 otherwise.
- Battery Charging `batterycharging` - Indicates if the battery is being charged. 1 if charging, 0 otherwise.
- Battery Life `batterylife` - Indicated charge remaining in battery, 1 is battery full, 0 is battery empty.
- Battery Time `batterytime` - Estimated time remaining in battery charge. Only works if AC Line is disconnected and battery is not being charged.
- Active Expressions `activeexpressions` - The number of active python expressions found in the project.
- Optimized Expressions `optimizedexpression` - The number of python expression that have been optimized, see [Optimized Python Expressions](https://docs.derivative.ca/Optimized_Python_Expressions "Optimized Python Expressions").
- Expressions Using Cache `cachedexpressions` - The number of python expression that have been cached, see [Optimized Python Expressions](https://docs.derivative.ca/Optimized_Python_Expressions "Optimized Python Expressions").

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
Extra Information for the Perform CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
