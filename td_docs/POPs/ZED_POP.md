---
url: https://docs.derivative.ca/ZED_POP
category: POPs
title: ZED_POP
---

# ZED POP
## Summary

**NOTE**
**OS:** This operator is only supported under the **Microsoft Windows** operating system.

The ZED POP uses the [ZED](https://docs.derivative.ca/ZED "ZED") StereoLabs SDK to scan and create geometry meshes (triangles) by moving it around the room or an object of interest. It also has the option to display a live point cloud from the depth image passed to it from the ZED TOP.
After pressing start the ZED POP uses each frame of video to build up the mesh, with the preview of the captured points in the viewer.
To know what ZED SDK we are using, refer to the [ZED](https://docs.derivative.ca/ZED "ZED") page. See also [ZED](https://docs.derivative.ca/ZED "ZED"), [ZED TOP](https://docs.derivative.ca/ZED_TOP "ZED TOP"), [ZED CHOP](https://docs.derivative.ca/ZED_CHOP "ZED CHOP") and [ZED SOP](https://docs.derivative.ca/ZED_SOP "ZED SOP")
[zedPOP_Class](https://docs.derivative.ca/ZedPOP_Class "ZedPOP Class")

## Parameters - Zed Page
- Active `active` - Extra pass to free unused GPU memory.
- ZED TOP `zedtop` - Reference to a ZED TOP.
- Output Mode `outputmode` - ⊞ - Whether to output a mesh or a point cloud.
  * Mesh `mesh` -
  * Point Cloud `pointcloud` -

- Connectivity `connectivity` - ⊞ - Determines whether and how to connect the points.
  * None `none` -
  * Point Primitives `points` -
  * Triangles `triangles` -

- Initialize `initialize` - Clears the extracted geometry and resets spatial mapping.
- Start `startpulse` - Start playback.
- Play `play` - Enable playback.
- Go to Done `donepulse` - Will immediately go to the done state.
- Preview `preview` - ⊞ - Camera preview mode.
  * No Preview `nopreview` -
  * Limited Preview `limited` -
  * Full Preview `limited` -

- Maximum Memory `maxmemory` - Sets the maximum memory used for spatial mapping.
- Resolution `resolution` - Spatial mapping resolution in meters.
- Range `range` - Depth range in meters.
- Normals `normals` - When enabled, the extracted geometry will have normals.
- Color `color` - Output color information as an attribute.
- Filter `filter` - ⊞ - The greater the filtering, the more the resulting mesh is smoothed, small holes are filled, and small blobs of non-connected triangles are deleted.
  * Low `low` -
  * Medium `medium` -
  * High `high` -

- Perspective `perspective` - ⊞ - Camera perspective.
  * Left `left` -
  * Right `right` -

- Rerange from Low High `rerangefromlow` - ⊞ - Range for input values.
  * Rerange from Low High `rerangefromlow` - Re-ranging low values.
  * Rerange from High `rerangefromhigh` - Re-ranging from high value.

- Rerange to Low High `rerangetolow` - ⊞ - Range for output values.
  * Rerange to Low High `rerangetolow` - Re-ranging to low value.
  * Rerange to High `rerangetohigh` - Re-ranging to high value.

- Mirror Image `mirrorimage` - Mirrors the input image.
- Camera `camera` - Specify the camera component.
- Override Camera View `overridecamera` - When on, overrides the View settings from the selected camera object.
- View Angle Method `viewanglemethod` - ⊞ - Sets the method to convert the depth TOP.
  * Horizontal FOV `horfov` -
  * Vertical FOV `vertfov` -
  * Focal Lengths `focallengths` - Determines the camera's focal lengths.

- FOV Angle `fov` - Determines the camera's field of view angle.
- Focal Length (Fx, Fy) `focallengths` - ⊞ -
  * Focal Length (Fx, Fy) `focallengthsx` -
  * Focal Length (Fx, Fy) `focallengthsy` -

- Optical Center (Cx, Cy) `center` - ⊞ - The location of the center of the camera for the depth projection.
  * Optical Center (Cx, Cy) `centerx` -
  * Optical Center (Cx, Cy) `centery` -

- Delete Near Points `deletenear` - Enable removal of points that are close to the camera.
- Near Depth `depthnear` - Depth of the near clipping plane.
- Delete Far Points `deletefar` - Enable removal of points that are far from the camera.
- Far Depth `depthfar` - Depth of the far clipping plane.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Info CHOP Channels
Extra Information for the ZED POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
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
