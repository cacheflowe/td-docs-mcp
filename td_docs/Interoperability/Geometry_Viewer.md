---
url: https://docs.derivative.ca/Geometry_Viewer
category: Interoperability
title: Geometry_Viewer
---

# Geometry Viewer

The Geometry Viewer lets you view and manipulate 3D objects in the [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP"), [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP"), [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") and all other 3D [Node Viewers](https://docs.derivative.ca/Node_Viewer "Node Viewer"), plus in Geometry Viewer [Panes](https://docs.derivative.ca/Pane "Pane") (alt+3 in any pane).

Through the [right-click](https://docs.derivative.ca/RMB_Menu "RMB Menu") menu you can get at viewing options like wireframe (w) and the Display Options (d) like point numbers, normals, grids, axes and more. You can also change your navigation modes.

**TIP:** It has its own lighting for viewing your 3D scene that is separate from the the light objects you create. To duplicate the default lighting in a geometry viewer, create two [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP") objects. Translate one to (30, 30, 100) and set its Light Color to (0.9, 0.9, 0.9). Translate the other to (-100, 0, 30) and set its Light Color to (0.3, 0.3, 0.3).

##  Display Options

Right-click on the viewer to open the view options menu. (You must be in **View** state if using the Geometry Viewer in a pane.)
[![](https://docs.derivative.ca/images/thumb/c/c3/GeoViewMenu2.png/300px-GeoViewMenu2.png)](https://docs.derivative.ca/File:GeoViewMenu2.png)
[](https://docs.derivative.ca/File:GeoViewMenu2.png "Enlarge")

Right-clicking brings up the geo view options menu
  * [Camera Navigation Modes](#Camera_Navigation_Modes) - change how the mouse controls the camera movement.
  * [3D SpaceMouse Navigation Modes](#3D_SpaceMouse_Navigation_Modes) - change how a SpaceMouse device controls the camera movement.
  * Adaptive Homing - when adaptive homing is enabled, the camera will automatically adjust to frame the current contents. Manually adjusting the camera position with the mouse will temporarily override the adaptive homing behaviour. Adaptive homing can be re-engaged by calling one of the Home or Frame options below.
  * [Display Options](https://docs.derivative.ca/Display_Options "Display Options") - opens a dialog of display options for the geometry viewer. Here you can turn on/off the display of points, normals, uv coordinates etc.
  * Toggle Hilite Dot Per Point - displays an overlay dot for each point in the scene (POPs only).
  * Display Attribute Text - display attribute data or indices as text overlayed on the geometry (POPs only).
  * Display Attribute Vector - display multi-dimension attribute data as vector arrows overlayed on the geometry (POPs only). If the selected attribute is less than 3 dimensions, the missing dimensions will be assumed to be 0. Attribute values are normalized so that vectors with smaller magnitudes will appear as smaller arrows.
  * Display Attribute Dots - display single dimension attributes as a colored dot with a ring of blue proportional to the magnitude of the value. The smallest value in the scene appears as a solid red dot and the largest as a solid blue dot.
  * Display Attribute Colors - display multi-dimension attribute data as a colored dot (POPs only). The attribute is not normalized to preserve the color value. This means attributes greater than one will appear solid white and negative values will appear black.
  * Home All - resets the view's orientation down the z-axis and ensures the view includes all geometry.
  * Home Selected - resets the view's orientation down the z-axis and ensures the view includes all selected geometry.
  * Frame All - moves the view to include all geometry without changing the view's orientation.
  * Frame Selected - moves the view to include all selected geometry without changing the view's orientation.
  * Frame C-Plane - moves the view to include the construction plane without changing the view's orientation.
  * Toggle Shaded/Wireframe - toggles the rendering of geometry between shaded and wireframe.
  * Toggle Ortho/Perspective - toggles the view between orthographic view and perspective view.
  * Select Viewport -
  * Perspective Viewport - changes the viewport to a perspective view.
  * Top Viewport - changes the viewport to a top view.
  * Front Viewport - changes the viewport to a front view.
  * Right Viewport - changes the viewport to a side view.
  * Help - open this help page.

##  Camera Navigation Modes

The geometry viewer has 4 Camera Navigation Modes selectable from the right-click menu in the viewer. For the first 3 modes the camera dolly always moves towards the cursor position, each of these modes differ in the the way they set a pivot. The pivot determines the point in 3D space that the camera tumbles (rotates) around as well as the speed of camera movement i.e. if the pivot point is far away, the camera will move further for each movement of the mouse. The last mode, Camera Mode, moves and pivots from the perspective of the camera and is more similar to the movement possible using a real-world camera (ie pan, tilt, dolly, track, crane), or in a game engine such as Unreal.
[![CameraNavigationModes.png](https://docs.derivative.ca/images/6/6a/CameraNavigationModes.png)](https://docs.derivative.ca/File:CameraNavigationModes.png)
**Viewport Mode**

This standard control scheme always uses the center of the view for the pivot for tumble. Dolly will always move in and out towards the position of the cursor.
  * [LMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - tumble around pivot
  * [MMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - dolly using MMB-drag or scroll wheel
  * [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - move left or right (track) and up or down (crane)

**Cursor Mode**

If the cursor is placed on a piece of geometry, that specific point on the geometry will become the new pivot and will determine the center of rotation for tumbling and the speed of camera movements i.e. if you hold the cursor over a distant piece of geometry and scroll the mouse wheel, it will move quickly towards that point, whereas if you hold it over a closer piece of geometry it would move more slowly. If the cursor is not over a piece of geometry, it uses the center of the view for a pivot at the same distance as the previous pivot (like viewport mode above).
  * [LMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - tumble around pivot
  * [MMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - move towards or away from the pivot (dolly) using MMB-drag or scroll wheel
  * [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - move left or right (track) and up or down (crane) perpendicular to the camera direction

**Object Mode**

The pivot is the center of all geometry in the viewer, or just the selected geometry if the viewer supports selection (see Geometry [Pane](https://docs.derivative.ca/Pane "Pane")). If no geometry is present, the origin 0,0,0 is used as the pivot.
  * [LMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - tumble around pivot
  * [MMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - dolly using MMB-drag or scroll wheel
  * [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - move left or right (track) and up or down (crane)

**Camera Mode**

The controls are from the perspective of the camera and the pivot is the camera's position. This is most like camera moves that are possible with a real-world camera, or in a first-person game engine such as Unreal.
  * [LMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - look up and down (tilt), or left and right (pan)
  * [MMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - move the camera forward or back in the XZ plane (dolly), or look left and right (pan)
  * [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") - move left or right (track) and up or down (crane). **NOTE:** reversed from other modes above since movement is based on the camera's perspective.

**Connection Problems** : If you are having trouble with the Spacemouse on macOS, there is a setting under “Privacy & Security” called ‘Input Monitoring’ which could block input from certain devices. It’s worth checking that TouchDesigner is not listed there. Or do an OSX update, which may prompt you to to re-validate the 3Dxware permissions.

##  3D SpaceMouse Navigation Modes

The camera in the geometry viewer can also be controlled using a [3DConnexion SpaceMouse](https://3dconnexion.com/ca/spacemouse/). The SpaceMouse supports full 3D movement in 6 axes (XYZ Translation and XYZ Rotation) and works independently of the mouse cursor. The Geometry viewer supports 3 different navigation modes for the SpaceMouse that are independent from the regular mouse-driven navigation modes. The mode can be selected by right-clicking on the active viewer and choosing a mode from the menu.

**Object Mode**

Object Mode is the default navigation mode and acts like the SpaceMouse is directly manipulating the geometry in the viewer. For example, nudging the SpaceMouse right will move the geometry to the right in the viewer and tilting the SpaceMouse forward will rotate the geometry away from the camera. Note that the geometry is not actually moving in the scene, but rather the camera is moving around the object in way that makes it feel like you are moving the geometry directly.

**Camera Mode**

In Camera Mode, the SpaceMouse controls the camera's position and orientation directly rather than the objects. For example, nudging the SpaceMouse forward will move the camera forwards in the scene and twisting the SpaceMouse to the right will turn the camera to the right. This mode generally feels like the reverse of the Object Mode.

**Target Camera Mode**

This mode is somewhat of a hybrid of the other two camera modes. Twisting the SpaceMouse will rotate (tumble) the camera around the center of the geometry, while pushing the SpaceMouse will directly move the camera.


##  In Node Viewers

[Node Viewers](https://docs.derivative.ca/Node_Viewer "Node Viewer") of 3D object type Components and SOPs are also geometry viewers. These geometry viewers do not include all the toolbars of a Geometry Viewer in a pane, however you can access many viewer options using the right-click menu over the viewer while in [Viewer Active](https://docs.derivative.ca/Viewer_Active "Viewer Active") mode.
[![Geometry Component.jpg](https://docs.derivative.ca/images/0/04/Geometry_Component.jpg)](https://docs.derivative.ca/File:Geometry_Component.jpg)

##  In Panes

Any [Pane](https://docs.derivative.ca/Pane "Pane") can be set to Geometry Viewer using the pane type menu or by using the shortcut alt+3.
[![Pane Type Menu Geo Viewer.jpg](https://docs.derivative.ca/images/a/ac/Pane_Type_Menu_Geo_Viewer.jpg)](https://docs.derivative.ca/File:Pane_Type_Menu_Geo_Viewer.jpg)
[![Geometry Viewer.png](https://docs.derivative.ca/images/2/2b/Geometry_Viewer.png)](https://docs.derivative.ca/File:Geometry_Viewer.png)


###  Using the Geometry Viewer Pane

###

Camera and Geometry Picking

[![GeometryViewerMenuBar.png](https://docs.derivative.ca/images/0/0b/GeometryViewerMenuBar.png)](https://docs.derivative.ca/File:GeometryViewerMenuBar.png)
  * **Camera** - [![MenuCamera.png](https://docs.derivative.ca/images/b/b8/MenuCamera.png)](https://docs.derivative.ca/File:MenuCamera.png) - Select any camera to view the scene through. You can also manually type in the path to the desire camera in the field to the right.

  * **Lock Camera** - [![MenuLock.png](https://docs.derivative.ca/images/c/cf/MenuLock.png)](https://docs.derivative.ca/File:MenuLock.png) - When this lock button is on, the position of the camera being viewed through is locked to the view in the viewer. So tumbling, zooming, or repositioning the view will update the camera's position to keep in sync with the view.

  * **Save View to** - [![MenuSaveViewto.png](https://docs.derivative.ca/images/2/25/MenuSaveViewto.png)](https://docs.derivative.ca/File:MenuSaveViewto.png) - This takes the current view in the viewer and saves it out to whichever camera is selected from the menu. This updates the camera's position so it is in sync with the current view.

  * **Pick** - [![MenuPick.png](https://docs.derivative.ca/images/3/32/MenuPick.png)](https://docs.derivative.ca/File:MenuPick.png) - This menu lets you select any [Object Component](https://docs.derivative.ca/Object_Component "Object Component") in the scene. The field to the right can be used for [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") to select multiple objects quickly.



###

Viewer States

[![GeometryViewerStateBar.png](https://docs.derivative.ca/images/f/f7/GeometryViewerStateBar.png)](https://docs.derivative.ca/File:GeometryViewerStateBar.png)
The Geometry Viewer state bar lets you switch viewer states. Click one of the buttons to switch states, or hold down the state's keyboard shortcut for temporarily switching states. For example, if working in **View** state, you can temporarily go into **Select & Transform** state by holding down the "s" key. While holding "s" key, select or transform some geometry, then release the key and you will be back in **View** state.
  * **View** - [![StateMove.png](https://docs.derivative.ca/images/2/24/StateMove.png)](https://docs.derivative.ca/File:StateMove.png) - Tumble, pan, and zoom throughout 3D space.
  * **Select & Transform** - [![StateSelect.png](https://docs.derivative.ca/images/3/31/StateSelect.png)](https://docs.derivative.ca/File:StateSelect.png) - Select and transform geometry.
  * **Construction Plane** - [![StateCplane.png](https://docs.derivative.ca/images/f/f2/StateCplane.png)](https://docs.derivative.ca/File:StateCplane.png) - Display and position the construction plane
  * **Bones** - [![StateBone.png](https://docs.derivative.ca/images/e/e9/StateBone.png)](https://docs.derivative.ca/File:StateBone.png) - Create bones.



###

Viewer Tools

[![GeometryViewerOptionsBar.png](https://docs.derivative.ca/images/b/b0/GeometryViewerOptionsBar.png)](https://docs.derivative.ca/File:GeometryViewerOptionsBar.png)
  * **Display Options** - [![OptionsDisplayOptions.png](https://docs.derivative.ca/images/8/85/OptionsDisplayOptions.png)](https://docs.derivative.ca/File:OptionsDisplayOptions.png) - Opens the [Display Options](https://docs.derivative.ca/Display_Options "Display Options") dialog.
  * **Home Button** - [![OptionsHome.png](https://docs.derivative.ca/images/0/04/OptionsHome.png)](https://docs.derivative.ca/File:OptionsHome.png) - Homes the view to one of the following views; Front, Right, Top, Y-axis, or X-axis.
  * **Camera Perspective** - [![OptionsPerspective.png](https://docs.derivative.ca/images/7/73/OptionsPerspective.png)](https://docs.derivative.ca/File:OptionsPerspective.png) - Switches the view between perspective and orthographic cameras.
  * **Construction Plane** - [![StateCplane.png](https://docs.derivative.ca/images/f/f2/StateCplane.png)](https://docs.derivative.ca/File:StateCplane.png) - When in Construction Plane state toggle the view of the Construction Plane on and off.
  * **Shading Options** - [![OptionsShading.png](https://docs.derivative.ca/images/2/2c/OptionsShading.png)](https://docs.derivative.ca/File:OptionsShading.png) - Switch geometry display between wireframe or shaded modes.
  * **Selected Geo Info** - [![OptionsSelectedInfo.png](https://docs.derivative.ca/images/1/1f/OptionsSelectedInfo.png)](https://docs.derivative.ca/File:OptionsSelectedInfo.png) - Displays information for the selected geometry.
  * **Viewport Options** - [![OptionsView.png](https://docs.derivative.ca/images/0/0a/OptionsView.png)](https://docs.derivative.ca/File:OptionsView.png) - Select from different viewport layouts.
  * **Snapshot** - [![OptionsSnapshot.png](https://docs.derivative.ca/images/5/59/OptionsSnapshot.png)](https://docs.derivative.ca/File:OptionsSnapshot.png) - Click with the [LMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") to take a snapshot of the viewport. Click with the [RMB](https://docs.derivative.ca/Mouse_Click "Mouse Click") to open snapshot options.
  * **Background TOP** - [![OptionsBGTOP.png](https://docs.derivative.ca/images/3/31/OptionsBGTOP.png)](https://docs.derivative.ca/File:OptionsBGTOP.png) - Enter the path to a [TOP](https://docs.derivative.ca/TOP "TOP") to load an image in the background of the viewport.
  * **Background Scale** - [![OptionsScale.png](https://docs.derivative.ca/images/7/76/OptionsScale.png)](https://docs.derivative.ca/File:OptionsScale.png) - Adjust the scale of the image loaded in the Background TOP.
  * **Snap Options** - [![OptionsSnap.png](https://docs.derivative.ca/images/9/93/OptionsSnap.png)](https://docs.derivative.ca/File:OptionsSnap.png) - Ajusts the viewport's snap options and priority.

A 3D viewport for viewing and manipulating 3D scenes or objects interactively. A geometry viewer can be found in [Panes](https://docs.derivative.ca/Pane "Pane") (alt+3 in any pane) or the [Node Viewers](https://docs.derivative.ca/Node_Viewer "Node Viewer") of all Geometry Object components.

In the [Node Viewer](https://docs.derivative.ca/Node_Viewer "Node Viewer") of a Geometry COMP or any POP, the Adaptive Homing option will continually keep in-view the 3D geometry being displayed, even when the geometry changes shape, size and animated position.

Privacy of TouchDesigner Components (`.tox` files) or Projects (`.toe` files) is the protection of networks that enables them to be used but not be visible or editable.

A work area in TouchDesigner's layout that includes the [Network Editor](https://docs.derivative.ca/Network_Editor "Network Editor") and 7 other pane types used for different tasks. The TouchDesigner interface can consist of a single pane, or be split into multiple panes.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
