---
url: https://docs.derivative.ca/Palette:stoner
category: Interoperability
title: Palette:stoner
---

# Palette:stoner
Stoner is a grid-warping and upscale 'keystoner' tool. It has two levels of warping. First is a 4-point corner-pin. Within that is a mesh warper where for each point of the mesh you can adjust position and curvature using bezier handles. Stoner has 2 outputs:
  * the final warped image and
  * a displacement map which can be used in conjunction with the [Remap TOP](https://docs.derivative.ca/Remap_TOP "Remap TOP")

On the Stoner custom parameter page you can also specify a custom COMP (usually a [Base COMP](https://docs.derivative.ca/Base_COMP "Base COMP") will be perfect) where the displacement data and the displacement map are stored.
**Note:** Stoner is intended to be used to create the displacement map and then to be removed from the file with only the necessary data inside the COMP defined in the "Project" custom parameter staying behind. This will increase performance quite a lot and let you use one centralized Stoner instead of many.
See also [Projection Mapping](https://docs.derivative.ca/Projection_Mapping "Projection Mapping").

##  Getting Started
You can find Stoner in the [Palette](https://docs.derivative.ca/Palette "Palette") under the folder Derivative>Mapping.
Drag and drop the component from the [Palette](https://docs.derivative.ca/Palette "Palette") into your network.
Connect a TOP to the input of the Stoner component.
Open the Stoner interface by clicking the "Open Stoner Window" custom parameter on the node's Stoner parameter page.
##  General Interface Controls
[![default UI with Keystone Mode selected](https://docs.derivative.ca/images/5/56/FullUIKeystone.png)](https://docs.derivative.ca/File:FullUIKeystone.png "default UI with Keystone Mode selected")
You can re-size the interface by dragging any of the windows edges.
Switch between Modes via the Mode Buttons or by hitting keys:      g - for grid-warp mode     k - for keystone mode
Undo and redo can be accessed via Ctrl+z and Ctrl+y.
Zoom in and out of the viewer by using the mouse wheel.
Drag the grid in the viewer by click and drag via the middle mouse button.
Hit "h" to reset the viewer.
Changing the Rows and Columns by number will reset the grid.
##  Grid Warp
[![UI in Grid Warp Mode](https://docs.derivative.ca/images/c/c8/FullUIGridwarp.png)](https://docs.derivative.ca/File:FullUIGridwarp.png "UI in Grid Warp Mode")
The grid can be warped using Bezier or Linear mode.
Select Points to move by clicking on them in the viewer.
You can select multiple points by holding down the Ctrl key.
You can select a whole row or column by holding down "Ctrl+r" or "Ctrl+c".
Add a row or column by switching into "Add Row" or "Add Column" Mode and selecting the point of creation in the viewer. A red line will indicate where a new row or column is created. Selecting a point also enables deleting the row or the column this point belongs to by clicking "Delete Row" or "Delete Column"
[![adding a row](https://docs.derivative.ca/images/1/17/AddRow.png)](https://docs.derivative.ca/File:AddRow.png "adding a row")
Move points by dragging them with the mouse. Alternatively, use the arrow keys to move selected points and hold the "Ctrl" key to increase step size.
Selecting points will reveal additional Bezier control handles. Hitting the "l" key will toggle between locked and unlocked state.
[![changing handles in unlocked mode](https://docs.derivative.ca/images/7/7b/GridWarpHandlesUnlocked.png)](https://docs.derivative.ca/File:GridWarpHandlesUnlocked.png "changing handles in unlocked mode")
##  Keystone
The Image can be mapped Perspectively or in Bilinear mode.
Select Points to move by clicking on them in the viewer. Alternatively, use the arrow keys to move selected points and hold the "Ctrl" key to increase step size.
Reset selected Keystone points by clicking "Reset Selected"
