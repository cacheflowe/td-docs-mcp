---
url: https://docs.derivative.ca/Kinect_SOP
category: SOPs
title: Kinect_SOP
---

# Kinect SOP
## Summary

The Kinect SOP uses the Kinect v1 sensor to scan and create geometry.
[kinectSOP_Class](https://docs.derivative.ca/KinectSOP_Class "KinectSOP Class")

## Parameters - Page
- Hardware Version `hwversion` - ⊞ - Only Kinect v1 sensors supported at this time.
  * Version 1 `version1` -

- Sensor `sensor` - Selects which Kinect sensor to use. Only available when using Kinect v1.
- Skeleton `skeleton` - ⊞ - Only used for Kinect 1 devices. Specify whether to track full skeleton or seated skeleton.
  * Full `full` -
  * Seated `seated` -

- Near Depth Mode `neardepthmode` - Only used for Kinect 1 devices. Enables near mode which allows camera to see objects as close as 40cm to the camera (instead of the default 80cm).
- Compute Normals `normals` - Creates normals on the geometry.

## Info CHOP Channels
Extra Information for the Kinect SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common SOP Info Channels
  * num_points - Number of points in this SOP.

  * num_prims - Number of primitives in this SOP.

  * num_particles - Number of particles in this SOP.

  * last_vbo_update_time - Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

  * last_meta_vbo_update_time - Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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
