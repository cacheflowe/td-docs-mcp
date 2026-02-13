---
url: https://docs.derivative.ca/WrnchAI_CHOP
category: CHOPs
title: WrnchAI_CHOP
---

# WrnchAI CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
**Note: Wrnch has be acquired by another company and it is no longer possible to obtain a license to use it anymore. This CHOP has been removed in 2022.20000+ builds.**
Using the [wrnchAI](https://docs.derivative.ca/WrnchAI "WrnchAI") engine to track human motion in any video stream, this CHOP will output channels for Body, Face and Hand positions. Multiple people can be tracked at the same time with low-latency, and the system compatible with all cameras and video feeds. TouchDesigner used the wrnchAI Edge SDK and all computation is done locally in realtime utilizing Nvidia GPUs and the NVIDIA CUDA® Deep Neural Network library ([cuDNN](https://developer.nvidia.com/cudnn)). This can offer skeletal tracking of multiple people at 60fps or higher (90-120fps etc).
```
**Requires a separate license from wrnchAI** to run in TouchDesigner. Requires **Nvidia GPU on Windows OS** and TouchDesigner Pro.
Make sure to install TouchDesigner from the Full Installer, the Lite Installer does not include wrnchAI libraries.

```

#####  Quickstart Guide
Once you have a wrnchAI license (purchased or trial), you will have access to your **wrnchAI licenses** page and the **wrnchAI Edge Releases** page.
  1. Go to your [wrnchAI licenses page](https://devportal.wrnch.ai/licenses). Click on the 'key' icon and copy the **Edge License Key** into the CHOP's 'wrnchAI License' parameter.
  2. Go to [wrnchAI Edge Releases page](https://devportal.wrnch.ai/wrnchai_edge/releases) and download the **wrnchAI Engine for Win10**. The file will be something like `wrnchAI-Engine-1.17.0-GPU-Win10.zip`
  3. Once downloaded, extract the .zip file and locate the **wrnchAI trained models folder** for use in the CHOP's 'Model Folder' parameter. It should be located here: `wrnchAI-engine-GPU-1.17.0-Windows-amd64/bin/wrModels`

The wrnchAI CHOP will take a few moments to initialize and then will be ready for tracking. Initializing is only required when a new Model Folder is introduced, it will not need to re-initialize each time the project is started.
[wrnchaiCHOP_Class](https://docs.derivative.ca/WrnchaiCHOP_Class "WrnchaiCHOP Class")

## Parameters - Setup Page
- wrnchAI License `license` - Add the Edge License Key from your wrnchAI account here. Requires a separate license from [wrnchAI](https://wrnch.ai/).
- Model Folder `modelfolder` - Specify the path the the folder that contains the trained models. See Quickstart Guide above for details.
- GPU Device `gpu` - ⊞ - A menu of available GPU(s) to run wrnchAI on. Selecting 'Default' uses the same GPU TouchDesigner is currently running on.
  * Default `default` - Uses the same GPU that TouchDesigner is currently assigned to.

- TOP `top` - Specify the TOP to process for tracking.
- Body 3D `body3d` - Enable the channels (tx, ty, tz) for body tracking points in 3D space.
- Body 2D `body2d` - Enable the channels (u, v) for body tracking points in 2D.
- Body 3D IK `body3dik` - Enable the IK channels (tx, ty, tz, rx, ry, rz and associated roll channels) for body tracking points in 3D space.
- Face Bounds `facebounds` - Enable the position and bounds channels (u, v, width, height) for faces.
- Face `face` - Enable the position channels (u, v) for all face tracking points.
- Hands Bounds `handsbounds` - Enable the position and bounds channels (u, v, width, height) for hands.
- Hands `hands` - Enable the position channels (u, v) for all hand tracking points.
- Max Players `maxplayers` - Sets the maximum number of people that can be tracked. For each person/player a new set of channels is created prefixed p1, p2, p3, ... etc.
**NOTE** : The parameter slider goes to 10 but higher numbers of players can be tracked by setting a higher Max Player value.
- Aspect Correct UVs `aspectcorrectuv` - Adjusts the values of u and v channels to take the TOP's aspect ratio into account. When using non-square input TOP, turn this on to line up u and v position with the image.

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
Extra Information for the wrnchAI CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific wrnchAI CHOP Info Channels
  * initializing -

  * running -

  * processing_fps -

  * processing_time -

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
