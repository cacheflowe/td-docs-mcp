---
url: https://docs.derivative.ca/Leap_Motion_CHOP
category: CHOPs
title: Leap_Motion_CHOP
---

# Leap Motion CHOP
## Summary

The Leap Motion CHOP reads hand, finger, tool and gesture data from the [Leap Motion](https://docs.derivative.ca/Leap_Motion "Leap Motion") controller. It outputs hand, finger and tool positions, rotations and 'tracking' channels that indicate if these values are currently being detected and updated. Currently only 1 Leap Motion device can be connected at a time.
To connect with the device you will need to install the Ultraleap Tracking Software. For best performance, it is recommended to use the latest version Gemini drivers for Windows (v5.13.2 or greater) or MacOS (v5.14.0 or greater) that are available here: <https://developer.leapmotion.com/tracking-software-download>. Legacy version 2 or version 4 Orion drivers are also supported. See the API parameter details below for more information.
In addition to installing the driver, TouchDesigner must also be told where to find the tracking library. Installation instructions vary depending on the operating system:
**On Windows:** You can use the Library Folder parameter to point to the location of the LeapC.dll (Orion/Gemini) or Leap.dll (Version 2/3) files on your system. The file is installed as part of the LeapSDK and the location may vary depending on the version and options selected during installation.
**On MacOS:** The library folder should point to the location of the Ultraleap tracking app. By default this is '/Applications/Ultraleap Hand Tracking.app' TouchDesigner will automatically find the library files inside the application's contents folder.
**Tip:** If using Gemini V5, the Leap Motion will only work in one orientation. By default the hands enter from the bottom of the camera view, though this can be changed in setting to invert the direction. This is an important distinction between Gemini V5 and the older V2/V4 APIs which could work in either orientation.
**Note:** TouchDesigner does not include a license to use the Leap Motion hardware or software. Make sure to check with the [UltraLeap website](https://www.ultraleap.com/) regarding any applicable licenses that you may need for your project.
See also [Leap Motion](https://docs.derivative.ca/Leap_Motion "Leap Motion"), [Leap Motion TOP](https://docs.derivative.ca/Leap_Motion_TOP "Leap Motion TOP")
[leapmotionCHOP_Class](https://docs.derivative.ca/LeapmotionCHOP_Class "LeapmotionCHOP Class")

## Parameters - Setup Page
- Active `active` - When 'On' data is captured from the Leap Motion sensor.
- API `api` - ⊞ - Select between Leap Motion V2 or V4/V5 SDKs for tracking. V5 offers the fastest and most stable tracking, V2 offers some legacy features like gestures.
  * Version 2 Tracking `default` - Legacy tracking that includes gesture and tool tracking. Download [(Windows: Orion Beta 3.2.1, MacOS: 2.3.1) ](https://developer.leapmotion.com/releases)
  * Orion (v4) / Gemini (v5) `on` - Gemini offers the best performance with improved stability and faster hand recognition to start tracking. Download [Gemini (Windows 5.13.2 or greater, MacOS 5.14 or greater) ](https://developer.leapmotion.com/tracking-software-download/). Legacy version 4 Orion tracking is available on Windows only. Download [Orion 4.1.0](https://developer.leapmotion.com/releases).

- Library Folder `libfolder` - This parameter is used on Windows only to point to the location of the library file (.dll) that corresponds to the selected API version. The dll file can be found in the driver kit downloaded from the Ultraleap website inside the 'LeapSDK/lib/x64' folder. For V4 and V5 the file is called 'LeapC.dll', for version 2 it is called 'Leap.dll'.
For Gemini V5, first install the tracking software, then set this parameter to C:\Program Files\Ultraleap\LeapSDK\lib\x64 where it will find the LeapC.dll file.
- HMD Mode `hmd` - ⊞ - Switches the device to **H** ead **M** ounted **D** isplay mode.
  * Default `default` -
  * On `on` -
  * Off `off` -

- Debug Channels `debugchannels` - If set, the following channels will be included:
  * `connected` - 1 if the Leap Motion sensor is connected, 0 otherwise.
  * `sequence_id` - Unique id corresponding to the current frame.

- Status Channels `statuschannels` - If set, the following channels will be included:
  * `hands` - Number of hands detected by the sensor.
  * `fingers` - Number of fingers detected by the sensor.
  * `tools` - Number of tools detected by the sensor.
  * `gestures` - Number of gestures detected by the sensor.
  * `[hand / finger / tool / circle / swipe / keytap / screeptap]:tracking` - 1 if the data for the hand, finger, tool or gesture is actively being tracked, 0 otherwise.

- Named Hands `namedhands` - This names the hand channels as either right (r) or left (l) hands.
- Hands `hands` - Number of hands. The following channels will be included for each detected hand:
  * `hand*:t[xyz]` - Coordinates of the hand relative to the sensor.
  * `hand*:r[xyz]` - Rotation of the detected hand.

- Left Hands `lefthands` - When using 'Named Hands', specify how many left hands will be tracked.
- Right Hands `righthands` - When using 'Named Hands', specify how many right hands will be tracked.
- Hand Velocity `handvelocity` - If set, the following channels will be included for each hand, in addition to any others:
  * `hand*:v[xyz]` - Velocity of the detected hand.

- Hand Sphere `handsphere` - This is only available when using API = Version 2 Tracking. It adds the following channels to tracking hands:
  * `hand*/sphere:t[xyz]` - Position of the detected hand sphere.
  * `hand*/sphere:radius` - Radius size of the detected hand sphere.

- Pinch Strength `pinchstrength` - Pinch is defined as the distance between the thumb and first finger.
  * `hand*:pinch` - How much pinch is detected between the thumb and first finger.

- Grab Strength `grabstrength` - Grab is defined as how close a hand is to being a fist.
  * `hand*:grab` - How much grab is detected, strength is 0 for a flat hand and 1 for a fist.

- Named Fingers `namedfingers` - Instead of simply using a finger index number for each finger tracked, when On this names the finger channels as thumb, index, middle, ring, and pinky.
- Fingers per Hand `fingersperhand` - When not using 'Named Fingers', specify how many fingers to track per hand.
- Finger Rotation `fingerrotation` - Track the rotation for all fingers.
  * `hand*/finger*:r[xyz]` - The rotation of the finger.

- Finger Size `fingersize` - If set, the following channels will be included for each finger, in addition to any others:
  * `hand*/finger*:length` - Length of the detected finger.
  * `hand*/finger*:width` - Width of the detected finger.

- Finger Extended `fingerextended` - Track how straight the fingers are, a finger is considered extended when it is straight as if pointing.
  * `hand*/finger*:extended` - How straight the finger is.

- Finger Joints `fingerjoints` - Tracks the position of every joint of every finger.
  * `hand*/finger*/joint_mcp:t[xyz]` - The mcp joint position of the finger.
  * `hand*/finger*/joint_pip:t[xyz]` - The pip joint position of the finger.
  * `hand*/finger*/joint_dip:t[xyz]` - The dip joint position of the finger.
  * `hand*/finger*/joint_tip:t[xyz]` - The finger tip position.

- Tools `tools` - Number of tools. The following channels will be included for each detected tool:
  * `tool*:t[xyz]` - Coordinates of the tool relative to the sensor.
  * `tool*:length` - Length of the detected tool.
  * `tool*:width` - Width of the detected tool.

- Circle Gestures `circlegestures` - Number of circle gestures. The following channels will be included for each detected [Circle Gesture](http://developer.leapmotion.com/documentation/Languages/C++/Guides/Leap_Overview.html#circle):
  * `circle*:handindex` - Index of the hand associated with the gesture. See Notes.
  * `circle*:t[xyz]` - Coordinates of the center of the Circle Gesture relative to the sensor.
  * `circle*:radius` - Radius of the circle in the gesture.
  * `circle*:progress` - Number of cycles done in the gesture.

- Swipe Gestures `swipegestures` - Number of swipe gestures. The following channels will be included for each detected [Swipe Gesture](http://developer.leapmotion.com/documentation/Languages/C++/Guides/Leap_Overview.html#swipe):
  * `swipe*:handindex` - Index of the hand associated with the gesture. See Notes.
  * `swipe*:fingerindex` - Index of the finger associated with the gesture. See Notes.
  * `swipe*:t[xyz]` - Coordinates of the Swipe Gesture relative to the sensor.
  * `swipe*:start[xyz]` - Coordinates of the start of the Swipe Gesture relative to the sensor.
  * `swipe*:speed` - Speed of the swipe.

- Key Tap Gestures `keytapgestures` - Number of key tap gestures. The following channels will be included for each detected [Key Tap Gesture](http://developer.leapmotion.com/documentation/Languages/C++/Guides/Leap_Overview.html#key-taps):
  * `keytap*:handindex` - Index of the hand associated with the gesture. See Notes.
  * `keytap*:fingerindex` - Index of the finger associated with the gesture. See Notes.
  * `keytap*:t[xyz]` - Coordinates of the Key Tap Gesture relative to the sensor.

- Screen Tap Gestures `screentapgestures` - Number of screen tap gestures, which is recognized as a quick forward tapping movement by a tool or finger. The following channels will be included for each detected screen tap gesture:
  * `screentap*:handindex` - Index of the hand associated with the gesture. See Notes.
  * `screentap*:fingerindex` - Index of the finger associated with the gesture. See Notes.
  * `screentap*:t[xyz]` - Coordinates of the Screen Tap Gesture relative to the sensor.

**NOTES:** Rotation order is `Rx Ry Rz`. All vectors are given in the following [coordinate system](http://developer.leapmotion.com/documentation/Languages/C++/Guides/Leap_Overview.html#coordinate-system).
For gestures, if `handindex` is 1, then channels with the prefix `hand1` contain the data for the hand associated with the gesture. If `handindex` is -1 it means there are no channels available for the hand associated with the gesture. The same follows for `fingerindex`.
Data for all indexed prefixes (`hand*`, `hand/finger*`, etc.) will continue to correspond to the same hand/finger/tool/gesture as long as the Leap Motion sensor is detecting it.
Limits for hands/fingers/tools/gestures will filter data from the Leap Motion sensor if there are more than the specified limit detected.

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
Extra Information for the Leap Motion CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Leap Motion CHOP Info Channels
  * installed -

  * connected -

  * hmd_policy_request -

  * hmd_policy_actual -

  * sequence_id -

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
