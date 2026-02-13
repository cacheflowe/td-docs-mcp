---
url: https://docs.derivative.ca/RealSense_CHOP
category: CHOPs
title: RealSense_CHOP
---

# RealSense CHOP
## Summary

**DEPRECATED:** Skeleton tracking features no longer licensable by Cubemos. [RealSense](https://docs.derivative.ca/RealSense "RealSense") is a tracking device from Intel. The RealSense CHOP references a [RealSense TOP](https://docs.derivative.ca/RealSense_TOP "RealSense TOP") camera and fetches tracking data from it. The RealSense CHOP supports skeleton tracking through the [Cubemos Skeleton Tracking API](https://www.intelrealsense.com/skeleton-tracking/). [Cubemos](https://docs.derivative.ca/Cubemos "Cubemos") is Windows only. A Cubemos license is required to use the skeleton tracking.
#### Skeleton Tracking Setup
The RealSense CHOP supports skeleton tracking through the [Cubemos RealSense Skeleton Tracking API](https://www.intelrealsense.com/skeleton-tracking/). The Cubemos API requires a license to use in TouchDesigner. A full license can be purchased [here](https://www.intelrealsense.com/skeleton-tracking); a trial license is also available. Installing their SDK is required to setup the license file. After installation of the SDK, the license can be setup with the `post_installation.bat` script in the `C:/Program Files/Cubemos/SkeletonTracking/scripts` folder. A model file (`.cubemos`) is also required for the skeleton tracking, two of which are packaged with the Cubemos Skeleton Tracking SDK, located in their `Cubemos/SkeletonTracking/models/skeleton-tracking` folder.
**NOTE:** The [librealsense SDK v2.50.0](https://github.com/IntelRealSense/librealsense/releases) does not look like it will be updated for Apple Silicon, so it is not an option to add to these builds.
See also: [RealSense](https://docs.derivative.ca/RealSense "RealSense"), [RealSense TOP](https://docs.derivative.ca/RealSense_TOP "RealSense TOP")
[realsenseCHOP_Class](https://docs.derivative.ca/RealsenseCHOP_Class "RealsenseCHOP Class")

## Parameters - Setup Page
- Active `active` - When enabled, actively fetches skeleton tracking data from a RealSense TOP.
- RealSense TOP `top` - The RealSense TOP camera to fetch skeleton data from.
- Skeletons `skeletons` - When enabled, displays the skeleton channels.
- Max Players `maxplayers` - Specify the max number of players tracked.
- Image Position Pixels `pos` - When enabled, will display positions of each landmark in image pixels as x/y channels.
- Image Positions Normalized `norm` - When enabled, will display normalized position values of each landmark as u/v channels.
- Confidence `confidence` - When enabled, will display the confidence value of each landmark. When the confidence channel value is 0 the landmark is untracked.

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
Extra Information for the RealSense CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
