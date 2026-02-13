---
url: https://docs.derivative.ca/Blob_Track_CHOP
category: CHOPs
title: Blob_Track_CHOP
---

# Blob Track CHOP
## Summary

The Blob Track CHOP allows tracking blobs in 2D point data.
Input data should be have two channels named _tx_ and _ty_ describing the 2D points in cartesian coordinates. See the [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") examples.
Good sources for input scans are the [Hokuyo CHOP](https://docs.derivative.ca/Hokuyo_CHOP "Hokuyo CHOP") (in Cartesian coordinate mode) and the [Leuze ROD4 CHOP](https://docs.derivative.ca/Leuze_ROD4_CHOP "Leuze ROD4 CHOP"). These devices naturally output a radial scan from the device as the center point, where each point represents (angle, distance). Outputting each scan point in Cartesian coordinate mode gives an (x,y) for each point which is the format required for the Blob Track CHOP.
But any set of (x,y) points in the two channels will be analyzed. The tracker looks for consecutive points close to each other, and handles the case where one blob passes behind another blob giving the hidden blob a linear motion for a specifiable amount of time while it occluded before it removes the blob from the set of blobs being output.
See also [Blob Track TOP](https://docs.derivative.ca/Blob_Track_TOP "Blob Track TOP")
[blobtrackCHOP_Class](https://docs.derivative.ca/BlobtrackCHOP_Class "BlobtrackCHOP Class")

## Parameters - Tracker Page
- Active `active` - While on, the CHOP receives information from the input. While off, no processing occurs. Existing blobs will remain.
- Search Mode `searchmode` - ⊞ - Controls how searching for blobs is done across all the points.
  * All `all` - All the points are compared against each other to find blobs. This mode is slower but more robust for data that has the points randomly assorted in the CHOP.
  * Consecutive Points `consecutive` - Points are only compared against points in neighbouring samples of the CHOP data to find blobs. This is much faster but the data much be setup such that points that are close to each other in space are next to each other in the CHOP samples. Data coming from devices such as the [Hokuyo CHOP](https://docs.derivative.ca/Hokuyo_CHOP "Hokuyo CHOP") and [Leuze ROD4 CHOP](https://docs.derivative.ca/Leuze_ROD4_CHOP "Leuze ROD4 CHOP") output data in this format.

- Max Blobs `maxblobs` - The maximum number of blobs that can be tracked.
- Max Point Distance in Blob `maxpointdistance` - Two measured points from the input are considered to be part of the same blob if they are this distance or closer to each other.
- Max Blob Movement `maxblobmovement` - This controls the maximum distance a blob can move between successive frames and still be considered the same 'blob'.
- Area of Interest `areaofinterest` - ⊞ - Limits the area in which blobs are tracked. Points outside the area of interest are ignored.
  * Off `off` - No limitations, blobs tracked throughout the scanned area.
  * Rectangle `rectangle` - Blobs only tracked within specified rectangle.
  * Circle `circle` - Blobs only tracked within specified circle (or ellipse).

- Center `center` - ⊞ - The center of the area of interest.
  * Center `centerx` -
  * Center `centery` -

- Size `size` - ⊞ - The size of the area of interest.
  * Size `sizew` -
  * Size `sizeh` -

- Rotate `rotate` - Rotate the area of interest.
- Allow Movement Outside Area `allowmovementoutside` - When this is on, blobs detected within the Area of Interest can move outside of that area and still be tracked. When this is off blobs that move outside the area of interest will stop being tracked.

## Parameters - Blobs Page
- Output Centroid `outputcentroid` - Include the centroid of detected blobs as part of the output channels.
- Output Velocity `outputvelocity` - Include the velocity of detected blobs as part of the output channels.
- Min Points per Blob `minblobpoints` - Minimum number of points that must be near each other to form a blob. Use to help filter out false positives.
- Blob Init Time (s) `blobinittime` - Amount of time a blob must be detected to be considered trustworthy. Use to help filter out false positives. A blob will only be output if it's been detected for at least time amount of time.
- Lost Blob Timeout (s) `lostblobtimeout` - The amount of time before a blob that has been lost is removed from the output.
- Blob Movement Prediction Type `predicttype` - ⊞ - With prediction enabled, blobs from the last frame have their new position predicted before being matched to the current frame.
  * Off `off` - Blobs are matched against the blob positions from the last frame.
  * Simple Forward Predict `simple` - Prediction uses constant velocity assumption; blobs are moved the same distance that they moved last frame.
  * Kalman Filter Predict `kalman` - Prediction uses [kalman filtering](https://en.wikipedia.org/wiki/Kalman_filter), with a constant velocity model, to move the blobs forward from last frame.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
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
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Blob Track CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Blob Track CHOP Info Channels
  * num_blobs -

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
