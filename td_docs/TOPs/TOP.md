---
url: https://docs.derivative.ca/TOP
category: TOPs
title: TOP
---

# TOP

## Summary

[![OP TOP.png](https://docs.derivative.ca/images/a/a9/OP_TOP.png)](https://docs.derivative.ca/File:OP_TOP.png)
See also [Category:TOPs](https://docs.derivative.ca/Category:TOPs "Category:TOPs") for a full list of articles related to TOPs.

**Texture Operators** , also known as **TOPs** , are image operators that provide real-time, GPU-based compositing and image manipulation. All calculations for TOPs are performed on the system's GPU. TOPs can be used for preparing textures, compositing streams images and movies, building control panel elements, manipulation of 32-bit floating point data, and almost any other image task you might have. TOPs support many formats, including floating-point image formats for working with high-dynamic range (HDR) images.

All renders and composites occur offscreen with TOPs. Data can be scaled to any resolution, limited only by the amount of graphics RAM and the maximum resolution of the graphics card.

TOPs that are being used to hold point cloud data, where R G B holds 32-bit X Y Z data can be viewed as a 3D set of points by right-clicking on the viewer and selecting View as Points.

**NOTE:** TouchDesigner Non-Commercial is limited to 1280x1280 resolution.

[TOP Class](TOP_Class.md "TOP Class")

##  Sweet 16 TOPs

The following 16 TOPs are commonly used, we recommend familiarizing yourself with them.
TOP | Purpose | Related TOP
---|---|---
[Movie File In](Movie_File_In_TOP.md "Movie File In TOP") | Read movies, still images, or a sequence of still images. |  [Video Device In](Video_Device_In_TOP.md "Video Device In TOP"), [Movie File Out](Movie_File_Out_TOP.md "Movie File Out TOP")
[Ramp](Ramp_TOP.md "Ramp TOP") | Create vertical, horizontal, radial, and circular ramps. |  [Constant](Constant_TOP.md "Constant TOP"), [Noise](Noise_TOP.md "Noise TOP")
[Level](Level_TOP.md "Level TOP") | Adjust contrast, brightness, gamma, black level, color range, opacity. |  [Luma Level](Luma_Level_TOP.md "Luma Level TOP")
[Transform](Transform_TOP.md "Transform TOP") | Translate, scale, rotate, multi-repeat tile, background fill. |  [Flip](Flip_TOP.md "Flip TOP")
[Over](Over_TOP.md "Over TOP") | Place and shift one image over another based on the alpha of one image. |  [Cross](Cross_TOP.md "Cross TOP"), [Multiply](Multiply_TOP.md "Multiply TOP")
[Text](Text_TOP.md "Text TOP") | Text generation with variety of fonts. |
[Blur](Blur_TOP.md "Blur TOP") | Blur. |  [Luma Blur](Luma_Blur_TOP.md "Luma Blur TOP")
[Composite](Composite_TOP.md "Composite TOP") | Combine multiple images with variety of operations like under, difference. |
[Render](Render_TOP.md "Render TOP") | Render 3D objects, lights and camera into an image. |
[CHOP to](CHOP_to_TOP.md "CHOP to TOP") | Convert CHOP channels into scanlines of an image. |
[Resolution](Resolution_TOP.md "Resolution TOP") | Change the resolution of an image and smooth-filter down. | all TOPs alter resolution
[Crop](Crop_TOP.md "Crop TOP") | Crop image to smaller resolution. |  [Corner Pin](Corner_Pin_TOP.md "Corner Pin TOP"), [Fit](Fit_TOP.md "Fit TOP")
[Select](Select_TOP.md "Select TOP") | Selects an image from the same network or a different network. |  [Switch](Switch_TOP.md "Switch TOP")
[Reorder](Reorder_TOP.md "Reorder TOP") | Re-order the channels of an image. |  [Channel Mix](Channel_Mix_TOP.md "Channel Mix TOP")
[Cache](Cache_TOP.md "Cache TOP") | Hold a static or dynamic sequence of images and output one of them. |  [Feedback](Feedback_TOP.md "Feedback TOP")
[Displace](Displace_TOP.md "Displace TOP") | Use red-blue of one image to warp another image. |  [Time Machine](Time_Machine_TOP.md "Time Machine TOP")
All TOPs are documented in the [Category:TOPs](https://docs.derivative.ca/Category:TOPs "Category:TOPs").

##  TOP Flags

The lower right corner contains only 2 flags, the TOP’s [Display Flag](../Glossary/Display_Flag.md "Display Flag") and [Viewer Active Flag](https://docs.derivative.ca/Viewer_Active_Flag "Viewer Active Flag"). Turning on the display flag displays the TOP as a background in the current [Network Pane](../Glossary/Network_Editor.md "Network Editor"). Turning on multiple TOP Display Flags will display a tiled sequence of multiple TOP outputs as the background of the network pane.

[![TOPDisplaySingle.jpg](https://docs.derivative.ca/images/d/da/TOPDisplaySingle.jpg)](https://docs.derivative.ca/File:TOPDisplaySingle.jpg) [![TOPDisplayMulti.jpg](https://docs.derivative.ca/images/6/69/TOPDisplayMulti.jpg)](https://docs.derivative.ca/File:TOPDisplayMulti.jpg)

##  TOP Viewers

All TOP operators have interactive [Node Viewers](../Glossary/Node_Viewer.md "Node Viewer"). To interact with it, turn on the TOP's [Viewer Active Flag](https://docs.derivative.ca/Viewer_Active_Flag "Viewer Active Flag") to make the viewer active.
[![TOPviewer.jpg](https://docs.derivative.ca/images/b/bb/TOPviewer.jpg)](https://docs.derivative.ca/File:TOPviewer.jpg)
A gray checkerboard background will be displayed in images where an alpha channel is present. This can be turned off by opening [Preferences](https://docs.derivative.ca/Dialogs:Preferences_Dialog "Dialogs:Preferences Dialog") in the **Edit** menu. In preferences you can choose to use checkerboard or black as you alpha background.

Use [LMB](../Glossary/Mouse_Click.md "Mouse Click") to move the image around. Use [MMB](../Glossary/Mouse_Click.md "Mouse Click") to zoom in and out of the image. Re-center the image by using the home shortcut "**h** ".

Clicking the [RMB](../Glossary/Mouse_Click.md "Mouse Click") will open the viewer options menu. Keyboard shortcuts are listed beside each entry in the menu.
[![TOPviewermenu.png](https://docs.derivative.ca/images/c/c1/TOPviewermenu.png)](https://docs.derivative.ca/File:TOPviewermenu.png)
**Home** - Re-centers and scales the image to fit in the viewer.

**Display Pixel Values** - Displays pixel information over the image. The [Timeline](../Glossary/Timeline.md "Timeline") should be playing forward for the values to properly update.

The following is displayed:
  * cursor uv coordinates
  * cursor xy pixel coordinates
  * RGB values 0-255
  * RGB values 0-1

**Display Field Guide** - Displays a 24x24 field guide over the image. The guide also displays the action safe zone and title safe zone for the image.

**Display Mode** - The display mode options give the option of viewing certain channels of the image.

The following display modes are available:
  * Color - Display all RGB channles.
  * Red/Green/Blue/Alpha - Display the Red/Green/Blue/Alpha channel respectively.
  * Mono - Display the image in monochrome.
  * Normalize Split - Displays each channel in the image at the same time normalized from 0-1. Excellent for viewing floating point and point cloud data.

**View as Points** - Displays the data in the TOP as 3D points for each pixel assuming red = x, green = y, and blue = z. Useful for viewing point cloud data.
[![PointCloudViews.png](https://docs.derivative.ca/images/thumb/c/cc/PointCloudViews.png/800px-PointCloudViews.png)](https://docs.derivative.ca/File:PointCloudViews.png)
Point cloud data displayed 3 modes: 1) Color 2) Normalized Split 3) View as Points

  * [![TOP operators](https://docs.derivative.ca/images/thumb/5/55/Opcreate_TOP.jpg/95px-Opcreate_TOP.jpg.png)](https://docs.derivative.ca/File:Opcreate_TOP.jpg "TOP operators")
TOP operators
  * [![A TOP network](https://docs.derivative.ca/images/thumb/c/c3/TOPexample.jpg/144px-TOPexample.jpg)](https://docs.derivative.ca/File:TOPexample.jpg "A TOP network")
A TOP network
  * [![TOP viewer options](https://docs.derivative.ca/images/thumb/b/bb/TOPviewer.jpg/144px-TOPviewer.jpg)](https://docs.derivative.ca/File:TOPviewer.jpg "TOP viewer options")
[TOP viewer options](TOP_Viewer.md "TOP Viewer")
  * [![Composite with Feedback](https://docs.derivative.ca/images/7/7a/TOPexample2.jpg)](https://docs.derivative.ca/File:TOPexample2.jpg "Composite with Feedback")
Composite with Feedback

##  Using TOPs

  * 2D image data, everything processed on GPU, generators and filters, real-time compositing
  * Import: Movie File In TOP, Video Device In TOP
  * Export: right-click menu, Movie File Out TOP, Export Movie Dialog

##  See also

[Category:TOPs](https://docs.derivative.ca/Category:TOPs "Category:TOPs")

[Mipmapping](https://docs.derivative.ca/Mipmapping "Mipmapping") and [Texture Filtering](https://docs.derivative.ca/Texture_Filtering "Texture Filtering")

[TOP Generator Common Page](../Glossary/TOP_Generator_Common_Page.md "TOP Generator Common Page") and [TOP Filter Common Page](https://docs.derivative.ca/TOP_Filter_Common_Page "TOP Filter Common Page")

[Pixel Formats](https://docs.derivative.ca/Pixel_Formats "Pixel Formats")
