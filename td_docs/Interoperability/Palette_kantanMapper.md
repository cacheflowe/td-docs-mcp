---
url: https://docs.derivative.ca/Palette:kantanMapper
category: Interoperability
title: Palette:kantanMapper
---

# Palette:kantanMapper

簡単 (kantan) - japanese for easy, simple - **Kantan Mapper 2** is a new projection mapping and masking toolkit for TouchDesigner. The user defines 2D polygons and bezier outlines in the field of view of a projector, then fills each shape with a selected image (TOP) with tools to warp how the image fits into the shape.

##  Summary

Kantan Mapper is an interface overlaid on-top of an actual projection to enable the drawing, creation and placement of various shapes onto real life objects and the possibility to assign TOP Image Nodes to these shapes and masks.

See also [Projection Mapping](https://docs.derivative.ca/Projection_Mapping "Projection Mapping"), [Vioso](https://docs.derivative.ca/Vioso "Vioso"), [Scalable Displays](https://docs.derivative.ca/Scalable_Display_TOP "Scalable Display TOP"), [camSchnappr](https://docs.derivative.ca/Palette:camSchnappr "Palette:camSchnappr"), [projectorBlend](https://docs.derivative.ca/Palette:projectorBlend "Palette:projectorBlend").

##  Getting Started

Kantan Mapper 2 is located in the Palette in 'Mapping' folder. To begin, open the [Palette](https://docs.derivative.ca/Palette "Palette") and drag `kantanMapper` from Palette>Mapping onto your network pane.

##  Parameters - Kantan Page

Help `Help` - Opens this page.

Open Kantan Window `Open` - Opens the Kantan Mapper Interface.

Close Kantan Window `Close` - Closes the Kantan Mapper Interface.

##  General Usage

After dragging kantanMapper from Palette>Tools onto your network pane, click the "Open Kantan Window" parameter pulse button to open the KantanMapper editing interface.
[![MottoKantanFullInterface.png](https://docs.derivative.ca/images/9/96/MottoKantanFullInterface.png)](https://docs.derivative.ca/File:MottoKantanFullInterface.png)

###  Create a Shape

To create a shape select either the [![Kantan-CreateRectangle.png](https://docs.derivative.ca/images/9/94/Kantan-CreateRectangle.png)](https://docs.derivative.ca/File:Kantan-CreateRectangle.png) Create Quad or the [![Kantan-CreateFreeform.png](https://docs.derivative.ca/images/d/d8/Kantan-CreateFreeform.png)](https://docs.derivative.ca/File:Kantan-CreateFreeform.png) Create Freeform tool.
[![Kantan-CreateQuadAni.gif](https://docs.derivative.ca/images/d/d9/Kantan-CreateQuadAni.gif)](https://docs.derivative.ca/File:Kantan-CreateQuadAni.gif)
For quads click on the startpoint on the editing canvas and drag to the opposite endpoint of the quad.
[![Kantan-CreateFreeAni.gif](https://docs.derivative.ca/images/1/1d/Kantan-CreateFreeAni.gif)](https://docs.derivative.ca/File:Kantan-CreateFreeAni.gif)
For freeform shapes, click on the canvas to create a key and drag out the edges. To close a shape, click back on the first key created.

###  Transform a Shape

With the Select Shape Tool selected, select a shape on the canvas. You can drag the shape to reposition or use the outer handles to scale and rotate the shape.
[![Kantan-TransformAni.gif](https://docs.derivative.ca/images/3/39/Kantan-TransformAni.gif)](https://docs.derivative.ca/File:Kantan-TransformAni.gif)

###  Modifying a Shape

With the Select Keys and Handles Tool selected, pick a shape on the canvas if a shape is not yet selected and move the keys or handles.
[![Kantan-MofifyShape.gif](https://docs.derivative.ca/images/8/8c/Kantan-MofifyShape.gif)](https://docs.derivative.ca/File:Kantan-MofifyShape.gif)

###  Assigning a Texture

Drag a TOP onto the Texture field in the Shape Settings section.
[![Kantan-AssignTexture.gif](https://docs.derivative.ca/images/b/b2/Kantan-AssignTexture.gif)](https://docs.derivative.ca/File:Kantan-AssignTexture.gif)

###  Duplicate Shapes

Select a shape and hold the Alt key when transforming the shape to create a copy.
[![Kantan-DuplicateShape.gif](https://docs.derivative.ca/images/7/7c/Kantan-DuplicateShape.gif)](https://docs.derivative.ca/File:Kantan-DuplicateShape.gif)

###  Editing Textures

With a shape selected, click the Edit Texture Button to bring up the Texture Editor. Here, specify the area of the texture to apply to the shape or apply the shape as a mask to the texture.v
[![Kantan-TextureAni.gif](https://docs.derivative.ca/images/7/7d/Kantan-TextureAni.gif)](https://docs.derivative.ca/File:Kantan-TextureAni.gif)

##  User Interface

###  Project Settings

Resolution - Specify the output Resolution of the full Canvas. This should match the resolution of the projector(s) used for this project.

Window Options - Will open the [Window COMP](https://docs.derivative.ca/Window_COMP "Window COMP") parameters for the output screen.

Toogle Output - Will open/close the output window as set-up in the Window Options.

Bg Mask - Specify a background mask by either dragging a TOP into the field or typing in the absolute path to the TOP. The button behind the field is used to enable or disable the mask.

Bg Level - Control the level of the background mask when enabled.

###  Shapes Tree

[![Kantan-TreeBrowser.png](https://docs.derivative.ca/images/4/43/Kantan-TreeBrowser.png)](https://docs.derivative.ca/File:Kantan-TreeBrowser.png)
The Shapes Tree Viewer is a list of shapes (quads and freeform) as well as groups in a collapsible display.

Every row representing a shape or group can be hidden by clicking the eyeball icon [![Kantan-Eyeball.png](https://docs.derivative.ca/images/e/e7/Kantan-Eyeball.png)](https://docs.derivative.ca/File:Kantan-Eyeball.png) in the last column of the tree.

Shapes and groups can be reordered by dragging them.

Shapes and groups can be nested by dragging them onto other groups.

New Groups can be created with the "Add Group" button [![Kantan-AddGroup.png](https://docs.derivative.ca/images/2/20/Kantan-AddGroup.png)](https://docs.derivative.ca/File:Kantan-AddGroup.png) on the top-left of the Shape Tree.

###  Editing Tools

The Editing Tools section of the UI holds the controls for selecting, creating and transforming shapes in KantanMapper.
[![Kantan-EditingTools.png](https://docs.derivative.ca/images/1/1c/Kantan-EditingTools.png)](https://docs.derivative.ca/File:Kantan-EditingTools.png)
Select Shape Tool [![Kantan-SelectShape.png](https://docs.derivative.ca/images/5/5a/Kantan-SelectShape.png)](https://docs.derivative.ca/File:Kantan-SelectShape.png) can select Shapes and exposes the shape transform handles for translation, scale and rotate.

Select Key & Handle Tool [![Kantan-SelectKeys.png](https://docs.derivative.ca/images/d/d9/Kantan-SelectKeys.png)](https://docs.derivative.ca/File:Kantan-SelectKeys.png) enables the selection and transform of a shapes keys and handles.

To add a quad use the Create Quad Tool [![Kantan-CreateRectangle.png](https://docs.derivative.ca/images/9/94/Kantan-CreateRectangle.png)](https://docs.derivative.ca/File:Kantan-CreateRectangle.png). After selecting the tool click and drag on the canvas to create a quad shape.

To add a freeform shape use the Create Freeform Tool [![Kantan-CreateFreeform.png](https://docs.derivative.ca/images/d/d8/Kantan-CreateFreeform.png)](https://docs.derivative.ca/File:Kantan-CreateFreeform.png). After selecting the tool, click and drag on the canvas to create a key and it's handles. repeat and finish the shape by clicking on the first key created.

If a shape is selected and the "Select Key & Handle" tool is active, shape specific tools become available:

Common to all shapes is the key and handle selector [![Kantan-KeyHandleTransform.png](https://docs.derivative.ca/images/b/bf/Kantan-KeyHandleTransform.png)](https://docs.derivative.ca/File:Kantan-KeyHandleTransform.png). Keys and Handles can be translated when selected. A red line shows

For Quads:
  * [![Kantan-Gridwarp.png](https://docs.derivative.ca/images/a/af/Kantan-Gridwarp.png)](https://docs.derivative.ca/File:Kantan-Gridwarp.png) enables the gridwarp mode of the selected quad. This enables the transformation of grid points and handles. Also rows and columns can be removed by selecting them and clicking the keyboard delete key.
  * [![Kantan-AddRow.png](https://docs.derivative.ca/images/8/80/Kantan-AddRow.png)](https://docs.derivative.ca/File:Kantan-AddRow.png) add a row to the gridwarp mesh by selecting the insert point on the grid directly.
  * [![Kantan-AddCol.png](https://docs.derivative.ca/images/d/d3/Kantan-AddCol.png)](https://docs.derivative.ca/File:Kantan-AddCol.png) add a column to the gridwarp mesh by selecting the insert point on the grid directly.

For Freeform Shapes:
  * [![Kantan-AddKey.png](https://docs.derivative.ca/images/3/3d/Kantan-AddKey.png)](https://docs.derivative.ca/File:Kantan-AddKey.png) enables adding keys inline the selected shape.
  * [![Kantan-ConvertKey.png](https://docs.derivative.ca/images/f/f9/Kantan-ConvertKey.png)](https://docs.derivative.ca/File:Kantan-ConvertKey.png) collapses the handles of a bezier key when selecting the key and enables resizing of the handles by dragging them from the key.

###  Shape Settings

[![Kantan-ShapeSettings.png](https://docs.derivative.ca/images/7/70/Kantan-ShapeSettings.png)](https://docs.derivative.ca/File:Kantan-ShapeSettings.png)
Name - Change the name of the shape as shown in the Shapes Tree.

Color - Change the color of the shape. The color is shown if no texture is assigned to the shape or the texture is disabled.

Texture - Assign a texture to the shape by dragging a TOP onto the field and enabling it by clicking the [![Kantan-Disable.png](https://docs.derivative.ca/images/1/1d/Kantan-Disable.png)](https://docs.derivative.ca/File:Kantan-Disable.png) button behind it.

Orientation - Change the orientation of the assigned texture or flip it.

Edit Texture - Open the Texture Editor.

Softedge - Apply softedge to the shape. While softedge on the quad is done via a basic shader, the softedge on the freeform is a bit more of an experiment using the [Extrude SOP](https://docs.derivative.ca/Extrude_SOP "Extrude SOP") and [Skin SOP](https://docs.derivative.ca/Skin_SOP "Skin SOP"). To see it's inner workings, navigate to .../kantanMapper/project/allShapes/item*.

Lock Handle - Locks and unlocks the gridwarp handles of the quad and the key handles of the freeform shape.

###  Transform Tools

Transformation can be applied to single or multiple shapes. When using the fields or buttons, the middle mouse wheel can be used to increase or decrease the current value.
[![Kantan-TransformTools.png](https://docs.derivative.ca/images/b/bb/Kantan-TransformTools.png)](https://docs.derivative.ca/File:Kantan-TransformTools.png)
Scale - Change the scale of the selected shapes around the selected pivot.

Rotate - Change the rotation of the selected shapes around the selected pivot.

Translate - Move the selected shapes in tx and ty.

Pivot - Pick the pivot to apply the transform around.

Free Pivot - If "Free" is selected in Pivot, change the position of the pivot point.

###  Shape Tools

The available Tools depend on the selected shape.

####  Quad

[![Kantan-RectangleTools.png](https://docs.derivative.ca/images/1/13/Kantan-RectangleTools.png)](https://docs.derivative.ca/File:Kantan-RectangleTools.png) Rows / Cols - Change the number of rows and columns in the quad. **Warning:** this will reset the Gridwarp. To remove a row or column without loosing the previously applied deform, select the row or column when in grid warp mode.
Warping - Change the warping mode of the quad. Options are:
  * Bezier: The grid can be warped with keys and handles.
  * Linear: only the grid points can be transformed and are connected linearly.

Mapping - Choose how a texture is mapped onto the quad:
  * Perspective
  * Bilinear

Reset Keystone - Reset the transformation on the corner points of the quad.

Reset Warp - Reset the transformation on all grid points of the quad.

####  Freeform

[![Kantan-FreeformTools.png](https://docs.derivative.ca/images/e/ee/Kantan-FreeformTools.png)](https://docs.derivative.ca/File:Kantan-FreeformTools.png)
Detail - change the resolution of the edges between keys on the freeform shape.

##  Texture Editor
