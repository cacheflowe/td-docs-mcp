---
url: https://docs.derivative.ca/TOP_Viewer
category: TOPs
title: TOP_Viewer
---

# TOP Viewer
All [TOP](https://docs.derivative.ca/TOP "TOP") operators have interactive [Node Viewers](https://docs.derivative.ca/Node_Viewer "Node Viewer"). To interact with it, turn on the TOP's [Viewer Active Flag](https://docs.derivative.ca/Viewer_Active_Flag "Viewer Active Flag") to make the viewer active.
[![TOPviewer.jpg](https://docs.derivative.ca/images/b/bb/TOPviewer.jpg)](https://docs.derivative.ca/File:TOPviewer.jpg)
A gray checkerboard background will be displayed in images where an alpha channel is present. This can be turned off by opening [Preferences](https://docs.derivative.ca/Dialogs:Preferences_Dialog "Dialogs:Preferences Dialog") in the **Edit** menu. In preferences you can choose to use checkerboard or black as you alpha background.
Use [LMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") to move the image around. Use [MMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") to zoom in and out of the image. Re-center the image by using the home shortcut "**h** ".
Clicking the [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") will open the viewer options menu. Keyboard shortcuts are listed beside each entry in the menu.
[![TOPviewermenu.png](https://docs.derivative.ca/images/c/c1/TOPviewermenu.png)](https://docs.derivative.ca/File:TOPviewermenu.png)
**Home** - Re-centers and scales the image to fit in the viewer.
**Display Pixel Values** - Displays pixel information over the image. The [Timeline](https://docs.derivative.ca/Timeline "Timeline") should be playing forward for the values to properly update.
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
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
