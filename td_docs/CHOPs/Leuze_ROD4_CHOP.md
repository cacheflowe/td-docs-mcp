---
url: https://docs.derivative.ca/Leuze_ROD4_CHOP
category: CHOPs
title: Leuze_ROD4_CHOP
---

# Leuze ROD4 CHOP
## Summary

**NOTE**
**License:** Only available in [TouchDesigner Educational](https://docs.derivative.ca/TouchDesigner_Educational "TouchDesigner Educational"), [TouchDesigner Commercial](https://docs.derivative.ca/TouchDesigner_Commercial "TouchDesigner Commercial") and [TouchDesigner Pro](https://docs.derivative.ca/TouchDesigner_Pro "TouchDesigner Pro").
The Leuze ROD4 CHOP connects to the [Leuze ROD4](https://www.leuze.com/en-int/products/switching-sensors/area-scanners?p=1) laser scanner via TCP/IP. Blob Tracking mode allows for turning the measured distances into blobs for use as an interaction surface. It should work with any of the ROD4 scanners currently available.
The 'object detection' mode available on some of the models is not currently supported.
The Leuze can be used with the [Blob Track CHOP](https://docs.derivative.ca/Blob_Track_CHOP "Blob Track CHOP") to detect objects in its field. See the OP Snippet for Blob Track.
[leuzerod4CHOP_Class](https://docs.derivative.ca/Leuzerod4CHOP_Class "Leuzerod4CHOP Class")

## Parameters - ROD4 Page
- Active `active` - While on, the CHOP receives information from the scanner. While off, the network connection is disconnected and no updating occurs.
- Network Address `netaddress` - The IP address of the ROD4 scanner.
- Network Port `port` - The network port of the scanner.
- ROD4 Protocol `rod4porotocol` - ⊞ - Selects which protocol to use. This must match the protocol the scanner was set to use in the RODplussoft setup utility for the device. You may still get some sort of data if the wrong protocol is selected, but the data will be random and incorrect.
  * Binary ROD4 compatible `binary` -
  * ROD4plus ASCII-Remote `ascii` -

- Input Coordinate `inputcoordinate` - ⊞ - Available when using ROD4plus ASCII-Remote protocol, specifies whether to use Polar or Cartesian input coordinates. This must match the coordinate the scanner was set to use in the RODplussoft setup utility for the device.
  * Polar `polar` -
  * Cartesian `cartesian` -

- Output Mode `outputmode` - ⊞ - Select Raw Data or Blob Tracking mode for output channels. The parameters below are only available in Blob Tracking mode.
  * Raw Data `rawdata` - A CHOP of 529 samples long that will contain the raw X/Y position in meters of every measured point from the scanner.
  * Blob Tracking `blobtracking` - The raw data will be analyzed for points that are close together which will be turned into blobs and assigned unique IDs.

- Max Blobs `maxblobs` - The maximum number of blobs that can be tracked.
- Max Point Distance in Blob `maxpointdistance` - Two measured points from the scanner are considered to be part of the same blob if they are this distance or closer to each other. Distance is specified in meters.
- Max Blob Movement `maxblobmovement` - Specified in meters. This controls the maximum distance a blob can move between successive frames and still be considered the same 'blob'.
- Area of Interest `areaofinterest` - ⊞ - Limits the area in which blobs are tracked.
  * Off `off` - No limitations, blobs tracked throughout the scanned area.
  * Distance Based `distancebased` - Blobs only tracked within specified distance from the scanner.
  * Bounding Box `boundingbox` - Blobs only tracked within specified bounding box.

- Max Distance `maxdistance` - Maximum distance in which blobs are tracked when Area of Interest parameter is set to Distance Based.
- Lower Left Corner `lowerleft` - ⊞ - Specifies the lower left corner of the bounding box used when Area of Interest parameter is set to Bounding Box.
  * `lowerleft1` -
  * `lowerleft2` -

- Upper Right Corner `upperright` - ⊞ - Specifies the upper right corner of the bounding box used when Area of Interest parameter is set to Bounding Box.
  * `upperright1` -
  * `upperright2` -

- Allow Movement Outside Area `allowmovementoutside` - When this is on, blobs detected within the Area of Interest can move outside of that area and still be tracked. When this is off blobs that move outside the area of interest will stop being tracked.
- Bounding Box Mask TOP `boundingboxmask` - Specify a TOP to use as a mask for the bounding box when Area of Interest parameter is set to Bounding Box. Any pixel with a non-zero value will be treated as part of the area of interest, any pixel that is (0,0,0) will be treated as not in the area of interest. Regardless of resolution/aspect ratio of the TOP, the TOP will be stretched to fix the bounding box specified. This TOP should **not** be cooking every frame as that will make the ROD4 CHOP very slow.
- Rotate Incoming Coordinates `rotate` - Rotates all incoming coordinates where the tx and ty values are rotated around a perpendicular z-axis.

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
Extra Information for the Leuze ROD4 CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
