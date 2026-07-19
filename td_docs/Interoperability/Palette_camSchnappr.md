---
url: https://docs.derivative.ca/Palette:camSchnappr
category: Interoperability
title: Palette:camSchnappr
---

# Palette:camSchnappr

## Summary

camSchnappr is a interactive mapping application entirely inspired by MAPAMOK, created by Kyle McDonald at the YCAM Interlab. With Kyle publishing the source code for MAPAMOK, we had a chance to look at it and convert it into TouchDesigner. For the original tool and source have a look [here](https://github.com/YCAMInterlab/ProCamToolkit/wiki/mapamok-%28English%29):

Kyle describes the significance of the tool as the use of OpenCV's cameraCalibrate to calibrate a projector via a model of the to be mapped structure instead of using a checkerboard. With TouchDesigner’s integration of Python, we were able to implement the same functionality into a standalone tool which lets you map complex structures in a small amount of time.

See also [Projection Mapping](../Learn/Projection_Mapping.md "Projection Mapping"), [Palette:kantanMapper](Palette_kantanMapper.md "Palette:kantanMapper"), [Vioso](Vioso.md "Vioso"), [Scalable Display TOP](../TOPs/Scalable_Display_TOP.md "Scalable Display TOP"), [projectorBlend](Palette_projectorBlend.md "Palette:projectorBlend")

[Palette:camSchnappr Ext](https://docs.derivative.ca/index.php?title=Palette:camSchnappr_Ext&action=edit&redlink=1 "Palette:camSchnappr Ext \(page does not exist\)")

What it does

If you have a physical 3D structure plus a virtual 3D model of that structure, you will be able to project a rendered virtual model onto that physical structure perfectly-aligned. You will be selecting points on your 3D Model and align them with the real world positions as you see them on the projector output. In order to support multiple projectors, the output of blend-masks from multiple camSchnapprs is now supported.

Using your 6 or more alignment points, CamSchnappr will compute the position, rotation, scale and viewing angle of a specified TouchDesigner Camera component used for the rendering. Internally, an openCV function called `calibrateCamera` will be run and the “intrinsics and extrinsics” of the camera will be calculated and stored in the Camera component.

What you need
  * TouchDesigner
  * a projector. **Note:** Make sure your projector has all digital transformations like keystone or zoom reset.
  * a physical structure to project on
  * a 3D Model of the to-be-mapped structure

## Getting Started

camSchnappr is located in the Palette in 'Mapping' folder. To begin, open the [Palette](../Learn/Palette.md "Palette") and drag `camSchnappr` from Palette>Mapping onto your network pane.

## Parameters - camSchnappr Page
- Project `Project` - Specify a [Camera COMP](../Glossary/Camera_COMP.md "Camera COMP") that will be used as the camera to be calibrated. By default the internal Camera COMP called "project" is being used. When dropping a new Camera COMP onto this parameter, a selection of parameters will be created.
- Geo SOP `Geosop` - Assign the [SOP](../SOPs/SOP.md "SOP") which holds the geometry you are calibrating. _Do not specify a SOP that is a [Material SOP](../SOPs/Material_SOP.md "Material SOP") or is from a branch with a Material SOP in it as this would break the blending. Instead reference the Texture via the Color Map Parameter._
- Use Point Group `Usepointgroup` - Enable if the source geometry contains point groups that should be used as calibration points. This is useful when dealing with large models where you can't select points but want to use a predetermined set of points.
- Geo Group `Geogroup` - The available point groups that can be selected as a source for predetermined calibration points.
- Calibration Error `Calibrationerror` - Displays the calibration Error returned from OpenCV after cv2.calibrateCamera has been executed. That is, the total sum of squared distances between the observed feature points _imagePoints_ and the projected (using the current estimates for camera parameters and the poses) object points _objectPoints_.
- Open Main Window `Openmain` - Open the camSchnappr editing window.
- Close Main Window `Closemain` - Close the camSchnappr editing window.
- Output Monitor `Monitor` - Assign which Monitor the output window will open on. This should be your projector.
- Output is Part of Canvas `Outputcanvas` - Enable if the projector output is part of a canvas. The main output might be a single window which is split to multiple projectors.
- Projector Resolution `Projectorres` - The resolution of the individual projector in the output canvas.
- Grid Position `Gridpos` - The pixel position of the individual projector in the output canvas from bottom left.
- Open Output `Open` - Open the output window.
- Close Output `Close` - Close the output window.
- Open Output on Primary (framed) `Openmainedit` - Open the output as a framed window on the main monitor. This can be useful to select and move points on the projection when they are not easily identifiable.
- Show Guides `Guides` - Show the guides on the output monitor.
- Guides Color `Guidescolor` - Control the color of the guides on the output.
- Guides Thickness `Guidesthickness` - Control the thickness of the guides on the output.
- Reverse Geo Vertex `Reversevertex` - Reverse both U and V for the Hull.
- Color Geo Randomly `Colorrandom` - Color each primitive of the geometry by random. This can be useful when schnapping complex objects.
- Color Map `Colormap` - Assign a TOP which is used as texture in the editing viewport and the output.
- Texture Alpha `Texturealpha` - Control the texture alpha.
- Show Wireframe `Wireframe` - Show or hide the geometrie's wireframe.
- Wireframe Line Width `Wirewidth` - Control the wireframe strength of the geometry in the output window.
- Clear `Clear` - Clear the calibration data including any selected points.
- Backlight Dimmer `Blightdimmer` - Control the backlight amount of the output window.
- Wireframe Color `Wirecolor` - ⊞ - Set the wireframe color of the geometry in the output window.
  * Wireframe Color `Wirecolorr` -
  * Wireframe Color `Wirecolorg` -
  * Wireframe Color `Wirecolorb` -
- Backlight Color `Blightcolor` - ⊞ - Set the background color of the output window.
  * Backlight Color `Blightcolorr` -
  * Backlight Color `Blightcolorg` -
  * Backlight Color `Blightcolorb` -
- Alt-key Multiplier `Altmodifier` - Control the offset of a selected point when moving it with the Alt+Arrow Keys in the output window.

## Parameters - Auto Blend Page

The Autoblend feature uses [Light COMPs](../Glossary/Light_COMP.md "Light COMP") to retrieve overlapping areas by comapring uvs from the lights projection area. Further it uses the Blend, Gamma and Luminance Parameters to adjust the blend region after the principles outlined in Paul Bourke's Paper: <http://paulbourke.net/miscellaneous/edgeblend/>
- camSchnappr Cameras `Camschnapprcams` - Specify all other camSchnappr [Camera COMPs](../Glossary/Camera_COMP.md "Camera COMP") in order to calculate the blend-mask for the projector.
- Blend `Blend` - Adjust the power of the blend function.
- Gamma Red `Gammared` - Adjust the gamma for the red channel.
- Gamma Green `Gammagreen` - Adjust the gamma for the green channel.
- Gamma Blue `Gammablue` - Adjust the gamma for the blue channel.
- Luminance `Luminance` - Adjust the luminance for the blend function.

## Parameters - openCV Page
- Near `Near` - This control allows you to designate the near clipping plane. Geometry closer from the lens than this distance will not be visible.
- Far `Far` - This control allows you to designate the far clipping planes. Geometry further away from the lens than this distance will not be visible.
- FOV `Fov` - Specify the initial FOV (field of view) estimation for the camera matrix given to the `cv2.calibrateCamera` function.
- Intrinsic Guess `Intrinsic` - The initial cameraMatrix passed to `cv2.calibrateCamera` contains valid initial values of focal length and principal point that are optimized further. Otherwise, the principal point is initially set to the image center ( imageSize is used), and focal distances are computed in a least-squares fashion. It sets the flag `cv2.CALIB_USE_INTRINSIC_GUESS`
- Fix Aspect Ratio `Fixaspect` - This considers only the vertical focal length as a free parameter. This should always be enabled unless you have an unusual projector with non-square pixels. It sets the flag `cv2.CALIB_FIX_ASPECT_RATIO`
- Zero Tangent Distance `Zerotangentdist` - Tangential distortion is set to zero. It's enabled by default because most projectors have very little tangential distortion. It sets the flag `cv2.CALIB_ZERO_TANGENT_DIST`
- Fix Principal Point `Fixprincipal` - The principal point is not changed during the optimization. You should enable this if you have a high quality lens with zero lens shift. It sets the flag `cv2.CALIB_FIX_PRINCIPAL_POINT`
- Fix Focal Length `Fixfocal` -
- Fix K1 `Fixk1` - The corresponding radial distortion coefficient is not changed during the optimization. For extremely wide fisheye lenses or lenses with radial distortion try enabling these. It sets the flag `cv2.CALIB_FIX_K1`
- Fix K2 `Fixk2` - The corresponding radial distortion coefficient is not changed during the optimization. For extremely wide fisheye lenses or lenses with radial distortion try enabling these. It sets the flag `cv2.CALIB_FIX_K2`
- Fix K3 `Fixk3` - The corresponding radial distortion coefficient is not changed during the optimization. For extremely wide fisheye lenses or lenses with radial distortion try enabling these. It sets the flag `cv2.CALIB_FIX_K3`
- Max Iterations `Maxiterations` - Specify the number of iterations the algorithm should terminate after.
- Precision `Precision` - Specify the value of accuracy at which, when reaching it, the algorithm should terminate.

## Parameters - ArcBall Page

The ArcBall parameters give control over the transform multipliers of the Main Window's arcBall camera. When using geometries with large dimensions, it can be necessary to adjust the Translate, Dolly and Rotate Multipliers to efficiently make use of the ArcBall Viewport.
- Translate Multiplier `Transmult` - Control the Translate Multiplier of the ArcBall camera.
- Dolly Multiplier `Dolmult` - Control the Dolly Multiplier of the Arcball camera.
- Rotate Multiplier `Rotmult` - Control the Rotate Multiplier of the Arcball camera.

## Parameters - OSC Page

camSchnappr now allows you to control it from a mobile device using [TouchOSC](https://hexler.net/products/touchosc) Download the TouchOSC layouts for IPad [File:camSchnappr.touchosc](https://docs.derivative.ca/File:CamSchnappr.touchosc "File:CamSchnappr.touchosc") or IPhone [File:camSchnapprIPhone.touchosc](https://docs.derivative.ca/File:CamSchnapprIPhone.touchosc "File:CamSchnapprIPhone.touchosc"). Make sure to turn on Touch Messages (/z) in the TouchOSC options as some of the interactions require this message to be send through.
- Active `Active` - Activate OSC access to camSchnappr via TouchOSC.
- Port `Port` - Set the portnumber specified in TouchOSC here. MAke sure in TouchOSC incoming and outgoing ports are set to the same value.

## Parameters - About Page
- Help `Help` - Opens this page.
- Version `Version` - Current version of this COMP.

.tox Save Build `Toxsavebuild` - TouchDesigner build this component was saved in.

The Viewport

Open the viewport by clicking the Open Main Window parameter.
[![CamSchnapprMainWindow.jpg](https://docs.derivative.ca/images/thumb/b/be/CamSchnapprMainWindow.jpg/480px-CamSchnapprMainWindow.jpg)](https://docs.derivative.ca/File:CamSchnapprMainWindow.jpg)
You can interact with the viewport as follows:
  *     *       * NEW***:
  * left-mouse click and drag to tumble
  * middle-mouse click and drag to zoom
  * right-mouse click and drag to pan
  * h to home the geometry
  * create control points by ctrl+left-mouse clicking on the geometry
  * make control points active by ctrl+left-mouse clicking on blue spheres
  * delete control points by ctrl+right-mouse clicking onto spheres
  * tab to cycle through selected points

When you select points a little flag with the point number will be displayed.

The Mapping Viewport

Once you selected the correct output Monitor via the Output Monitor parameter, click the Open Output parameter.
[![CamSchnapprOutputGuides.jpg](https://docs.derivative.ca/images/thumb/e/ed/CamSchnapprOutputGuides.jpg/480px-CamSchnapprOutputGuides.jpg)](https://docs.derivative.ca/File:CamSchnapprOutputGuides.jpg)
The interface is quite simple:
  * a red crosshair indicates your current cursor position on the screen
  * a dark yellow crosshair indicates an inactive point previously selected to be mapped in the main viewport
  * a yellow crosshair indicates an active point previously selected to be mapped in the main viewport

You can drag points to their real-world position on the screen or use the arrow keys on the keyboard. For faster movement, use alt+arrowkey to move points.

You can also Shift+Left-click onto the viewport to move points directly to their corresponding real-world position.

Tab will cycle through the available points.

Using the keyboard arrow keys, you can move the points 1 pixel at a time.

Using Alt+Arrow keyboard keys will move the point by the Alt-Multiplier Parameter amount (by default 10 pixel).

Workflow
  * Create a simple render setup with the model of the object you want to map onto.
  * select the camSchnappr Camera COMP.
  * Optional: Drag your Camera COMP onto the Project Parameter of camSchnappr.
  * Drag the SOP containing the geometry of the to be mapped object onto the Geo SOP parameter.
  * Select the number of the output your Projector is connected to via the Output Monitor parameter.
  * Open the Main Window of camSchnappr by clicking the Open Main Window parameter.
  * Open the mapping Viewport by clicking the Open Output parameter, if somehow the output now overlays your main viewport, just hit escape and select a different Monitor Output number via the Output Monitor parameter.
  * In the main viewport align the geometry to the camera so it’s similar to what the projector sees.
  * Select a point in the main viewport and move it in the mapper viewport to the corresponding position on the real world object. You can also hold the Shift key and click in the mapper viewport onto the corresponding real world position.
  * Repeat the last step for at least 6 points total.
  * After you have aligned 6 points, the camera should be calibrated and you should see the projection mapped onto the object.
  * If everything is correct you can close the mapping output and the camSchnappr viewport by clicking the Close Output and Close camSchnappr parameter. The Camera Calibration values are saved inside your camSchnappr Project Camera COMP as 2 Table DATs.
  * If you used an externa Camera COMP as a project, you can now also delete camSchnappr.

OSC Controls

camSchnappr can be controlled using following osc channels:
  * /1/selectPointNext [0|1] - selects the next controlpoint
  * /1/selectPointPrev [0|1] - selects the prev control point
  * /1/pointCoarse [float] [float] - move the currently selected controlpoint by u/v amount.
  * /1/pointFine [float] [float] - move the currently selected controlpoint by a fraction of u/v amount.
  * /1/pointFine/z [0|1] - if `1` start fine movement, if `0` finish fine movement
  * /1/left [0|1] - if `1` move selected point by 1 pixel left.
  * /1/right [0|1] - if `1` move selected point by 1 pixel right.
  * /1/up [0|1] - if `1` move selected point by 1 pixel up.
  * /1/down [0|1] - if `1` move selected point by 1 pixel down.
  * /1/altleft [0|1] - if `1` move selected point by 10 pixels left.
  * /1/altright [0|1] - if `1` move selected point by 10 pixels right.
  * /1/altup [0|1] - if `1` move selected point by 10 pixels up.
  * /1/altdown [0|1] - if `1` move selected point by 10 pixels down.
  * /1/openCloseOutput [0|1] - open / close the main poutput.
  * /1/selectCamSchnappr [0|1] - select the next camSchnappr in your setup.
  * /1/selectCamSchnapprPrev [0|1] - select the previous camSchnappr in your setup.

## Operator Outputs

  * Output 0 - When using multiple camSchnappr cameras, this output will be the blendmask between them.

Palette
---
[Palette ](../Learn/Palette.md "Palette")• [Palette:arcBallCamera ](https://docs.derivative.ca/Palette:arcBallCamera "Palette:arcBallCamera")• [Palette:arcBallGeometry ](https://docs.derivative.ca/Palette:arcBallGeometry "Palette:arcBallGeometry")• [Palette:audioAnalysis ](https://docs.derivative.ca/Palette:audioAnalysis "Palette:audioAnalysis")• [Palette:audioSet ](https://docs.derivative.ca/Palette:audioSet "Palette:audioSet")• [Palette:autoMediaPlayer ](https://docs.derivative.ca/Palette:autoMediaPlayer "Palette:autoMediaPlayer")• [Palette:battery ](https://docs.derivative.ca/Palette:battery "Palette:battery")• [Palette:bitwigClip ](https://docs.derivative.ca/Palette:bitwigClip "Palette:bitwigClip")• [Palette:bitwigClipSlot ](https://docs.derivative.ca/Palette:bitwigClipSlot "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](https://docs.derivative.ca/Palette:bitwigDeviceRemotes "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](https://docs.derivative.ca/Palette:bitwigMain "Palette:bitwigMain")• [Palette:bitwigNote ](https://docs.derivative.ca/Palette:bitwigNote "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](https://docs.derivative.ca/Palette:bitwigProjectRemotes "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](https://docs.derivative.ca/Palette:bitwigRemotesDevice "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](https://docs.derivative.ca/Palette:bitwigRemotesProject "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](https://docs.derivative.ca/Palette:bitwigRemotesTrack "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](https://docs.derivative.ca/Palette:bitwigSelect "Palette:bitwigSelect")• [Palette:bitwigSong ](https://docs.derivative.ca/Palette:bitwigSong "Palette:bitwigSong")• [Palette:bitwigTrack ](https://docs.derivative.ca/Palette:bitwigTrack "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](https://docs.derivative.ca/Palette:bitwigTrackRemotes "Palette:bitwigTrackRemotes")• [Palette:blendModes ](https://docs.derivative.ca/Palette:blendModes "Palette:blendModes")• [Palette:bloom ](https://docs.derivative.ca/Palette:bloom "Palette:bloom")• [Palette:camera ](https://docs.derivative.ca/Palette:camera "Palette:camera")• [Palette:cameraBrowser ](https://docs.derivative.ca/Palette:cameraBrowser "Palette:cameraBrowser")• [Palette:cameraViewport ](https://docs.derivative.ca/Palette:cameraViewport "Palette:cameraViewport")• Palette:camSchnappr • [Palette:changeColor ](https://docs.derivative.ca/Palette:changeColor "Palette:changeColor")• [Palette:changeToColor ](https://docs.derivative.ca/Palette:changeToColor "Palette:changeToColor")• [Palette:checker ](https://docs.derivative.ca/Palette:checker "Palette:checker")• [Palette:chromaKey ](https://docs.derivative.ca/Palette:chromaKey "Palette:chromaKey")• [Palette:colorThreshold ](https://docs.derivative.ca/Palette:colorThreshold "Palette:colorThreshold")• [Palette:compareComp ](https://docs.derivative.ca/Palette:compareComp "Palette:compareComp")• [Palette:convolve ](https://docs.derivative.ca/Palette:convolve "Palette:convolve")• [Palette:cornerPinPOP ](https://docs.derivative.ca/Palette:cornerPinPOP "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](https://docs.derivative.ca/Palette:cornerPinSOP "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](https://docs.derivative.ca/Palette:cppParsTemplateGen "Palette:cppParsTemplateGen")• [Palette:customAttributes ](https://docs.derivative.ca/Palette:customAttributes "Palette:customAttributes")• [Palette:debugControl ](https://docs.derivative.ca/Palette:debugControl "Palette:debugControl")• [Palette:dent ](https://docs.derivative.ca/Palette:dent "Palette:dent")• [Palette:depthExtract ](https://docs.derivative.ca/Palette:depthExtract "Palette:depthExtract")• [Palette:depthProjection ](https://docs.derivative.ca/Palette:depthProjection "Palette:depthProjection")• [Palette:dilate ](https://docs.derivative.ca/Palette:dilate "Palette:dilate")• [Palette:domeViewer ](https://docs.derivative.ca/Palette:domeViewer "Palette:domeViewer")• [Palette:encoder ](https://docs.derivative.ca/Palette:encoder "Palette:encoder")• [Palette:equalizer ](https://docs.derivative.ca/Palette:equalizer "Palette:equalizer")• [Palette:feedback ](https://docs.derivative.ca/Palette:feedback "Palette:feedback")• [Palette:feedbackEdge ](https://docs.derivative.ca/Palette:feedbackEdge "Palette:feedbackEdge")• [Palette:firmata ](Palette_firmata.md "Palette:firmata")• [Palette:gal ](https://docs.derivative.ca/Palette:gal "Palette:gal")• [Palette:geoPanel ](https://docs.derivative.ca/Palette:geoPanel "Palette:geoPanel")• [Palette:gestureCapture ](https://docs.derivative.ca/Palette:gestureCapture "Palette:gestureCapture")• [Palette:graphPlot ](https://docs.derivative.ca/Palette:graphPlot "Palette:graphPlot")• [Palette:histogram ](https://docs.derivative.ca/Palette:histogram "Palette:histogram")• [Palette:hsvBlur ](https://docs.derivative.ca/Palette:hsvBlur "Palette:hsvBlur")• [Palette:imageSearch ](https://docs.derivative.ca/Palette:imageSearch "Palette:imageSearch")• [Palette:julia ](https://docs.derivative.ca/Palette:julia "Palette:julia")• [Palette:kantanMapper ](Palette_kantanMapper.md "Palette:kantanMapper")• [Palette:kinectCalibration ](https://docs.derivative.ca/Palette:kinectCalibration "Palette:kinectCalibration")• [Palette:kinectPointcloud ](https://docs.derivative.ca/Palette:kinectPointcloud "Palette:kinectPointcloud")• [Palette:leapPaint ](https://docs.derivative.ca/Palette:leapPaint "Palette:leapPaint")• [Palette:lightTunnel ](https://docs.derivative.ca/Palette:lightTunnel "Palette:lightTunnel")• [Palette:logger ](https://docs.derivative.ca/Palette:logger "Palette:logger")• [Palette:mandelbrot ](https://docs.derivative.ca/Palette:mandelbrot "Palette:mandelbrot")• [Palette:materialDesignIcons ](https://docs.derivative.ca/Palette:materialDesignIcons "Palette:materialDesignIcons")• [Palette:mesh ](https://docs.derivative.ca/Palette:mesh "Palette:mesh")• [Palette:monochrome ](https://docs.derivative.ca/Palette:monochrome "Palette:monochrome")• [Palette:motionSense ](https://docs.derivative.ca/Palette:motionSense "Palette:motionSense")• [Palette:movieEngine ](https://docs.derivative.ca/Palette:movieEngine "Palette:movieEngine")• [Palette:moviePlayer ](https://docs.derivative.ca/Palette:moviePlayer "Palette:moviePlayer")• [Palette:moviePlaylist ](https://docs.derivative.ca/Palette:moviePlaylist "Palette:moviePlaylist")• [Palette:multiLevel ](https://docs.derivative.ca/Palette:multiLevel "Palette:multiLevel")• [Palette:multiMix ](https://docs.derivative.ca/Palette:multiMix "Palette:multiMix")• [Palette:noise ](https://docs.derivative.ca/Palette:noise "Palette:noise")• [Palette:onScreenKeyboard ](https://docs.derivative.ca/Palette:onScreenKeyboard "Palette:onScreenKeyboard")• [Palette:operatorPath ](https://docs.derivative.ca/Palette:operatorPath "Palette:operatorPath")• [Palette:opticalFlow ](https://docs.derivative.ca/Palette:opticalFlow "Palette:opticalFlow")• [Palette:particlesGpu ](https://docs.derivative.ca/Palette:particlesGpu "Palette:particlesGpu")• [Palette:pixelate ](https://docs.derivative.ca/Palette:pixelate "Palette:pixelate")• [Palette:pixelRelocator ](https://docs.derivative.ca/Palette:pixelRelocator "Palette:pixelRelocator")• [Palette:pointGenerator ](https://docs.derivative.ca/Palette:pointGenerator "Palette:pointGenerator")• [Palette:pointillize ](https://docs.derivative.ca/Palette:pointillize "Palette:pointillize")• [Palette:pointMerge ](https://docs.derivative.ca/Palette:pointMerge "Palette:pointMerge")• [Palette:pointRender ](https://docs.derivative.ca/Palette:pointRender "Palette:pointRender")• [Palette:pointRepack ](https://docs.derivative.ca/Palette:pointRepack "Palette:pointRepack")• [Palette:pointTransform ](https://docs.derivative.ca/Palette:pointTransform "Palette:pointTransform")• [Palette:pointWeight ](https://docs.derivative.ca/Palette:pointWeight "Palette:pointWeight")• [Palette:popDialog ](https://docs.derivative.ca/Palette:popDialog "Palette:popDialog")• [Palette:probe ](https://docs.derivative.ca/Palette:probe "Palette:probe")• [Palette:projectorBlend ](Palette_projectorBlend.md "Palette:projectorBlend")• [Palette:pushPins ](https://docs.derivative.ca/Palette:pushPins "Palette:pushPins")• [Palette:puzzle ](https://docs.derivative.ca/Palette:puzzle "Palette:puzzle")• [Palette:quadReproject ](https://docs.derivative.ca/Palette:quadReproject "Palette:quadReproject")• [Palette:radialBlur ](https://docs.derivative.ca/Palette:radialBlur "Palette:radialBlur")• [Palette:recorder ](https://docs.derivative.ca/Palette:recorder "Palette:recorder")• [Palette:remotePanel ](https://docs.derivative.ca/Palette:remotePanel "Palette:remotePanel")• [Palette:rgbaBlur ](https://docs.derivative.ca/Palette:rgbaBlur "Palette:rgbaBlur")• [Palette:rgbaDelay ](https://docs.derivative.ca/Palette:rgbaDelay "Palette:rgbaDelay")• [Palette:rgbContrast ](https://docs.derivative.ca/Palette:rgbContrast "Palette:rgbContrast")• [Palette:sceneChanger ](https://docs.derivative.ca/Palette:sceneChanger "Palette:sceneChanger")• [Palette:search ](https://docs.derivative.ca/Palette:search "Palette:search")• [Palette:searchReplace ](https://docs.derivative.ca/Palette:searchReplace "Palette:searchReplace")• [Palette:sharpen ](https://docs.derivative.ca/Palette:sharpen "Palette:sharpen")• [Palette:sickEngine ](https://docs.derivative.ca/Palette:sickEngine "Palette:sickEngine")• [Palette:signalingClient ](https://docs.derivative.ca/Palette:signalingClient "Palette:signalingClient")• [Palette:signalingServer ](https://docs.derivative.ca/Palette:signalingServer "Palette:signalingServer")• [Palette:softenAlpha ](https://docs.derivative.ca/Palette:softenAlpha "Palette:softenAlpha")• [Palette:solarize ](https://docs.derivative.ca/Palette:solarize "Palette:solarize")• [Palette:sopRender ](https://docs.derivative.ca/Palette:sopRender "Palette:sopRender")• [Palette:splitter ](https://docs.derivative.ca/Palette:splitter "Palette:splitter")• [Palette:stitcher ](https://docs.derivative.ca/Palette:stitcher "Palette:stitcher")• [Palette:stoner ](Palette_stoner.md "Palette:stoner")• [Palette:superFormula ](https://docs.derivative.ca/Palette:superFormula "Palette:superFormula")• [Palette:SVG ](https://docs.derivative.ca/Palette:SVG "Palette:SVG")• [Palette:sweetSpot ](https://docs.derivative.ca/Palette:sweetSpot "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](https://docs.derivative.ca/Palette:sweetSpotPreviz "Palette:sweetSpotPreviz")• [Palette:synchroCache ](https://docs.derivative.ca/Palette:synchroCache "Palette:synchroCache")• [Palette:synchroClient ](https://docs.derivative.ca/Palette:synchroClient "Palette:synchroClient")• [Palette:synchroFrameIn ](https://docs.derivative.ca/Palette:synchroFrameIn "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](https://docs.derivative.ca/Palette:synchroFrameOut "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](https://docs.derivative.ca/Palette:synchroNDIIn "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](https://docs.derivative.ca/Palette:synchroSDIIn "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](https://docs.derivative.ca/Palette:synchroVideoOut "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](https://docs.derivative.ca/Palette:tdBitwigPackage "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](https://docs.derivative.ca/Palette:tdPyEnvManager "Palette:tdPyEnvManager")• [Palette:TDVR ](https://docs.derivative.ca/Palette:TDVR "Palette:TDVR")• [Palette:testGrid ](https://docs.derivative.ca/Palette:testGrid "Palette:testGrid")• [Palette:threadManagerClient ](https://docs.derivative.ca/Palette:threadManagerClient "Palette:threadManagerClient")• [Palette:threadsMonitor ](https://docs.derivative.ca/Palette:threadsMonitor "Palette:threadsMonitor")• [Palette:transitMap ](https://docs.derivative.ca/Palette:transitMap "Palette:transitMap")• [Palette:twirl ](https://docs.derivative.ca/Palette:twirl "Palette:twirl")• [Palette:vectorScope ](https://docs.derivative.ca/Palette:vectorScope "Palette:vectorScope")• [Palette:virtualFile ](https://docs.derivative.ca/Palette:virtualFile "Palette:virtualFile")• [Palette:waveformMonitor ](https://docs.derivative.ca/Palette:waveformMonitor "Palette:waveformMonitor")• [Palette:webBrowser ](Palette_webBrowser.md "Palette:webBrowser")• [Palette:webRTC ](https://docs.derivative.ca/Palette:webRTC "Palette:webRTC")• [Palette:webRTCPanel ](https://docs.derivative.ca/Palette:webRTCPanel "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](https://docs.derivative.ca/Palette:webRTCPanelRcv "Palette:webRTCPanelRcv")• [Palette:xyScope ](https://docs.derivative.ca/Palette:xyScope "Palette:xyScope")• [Thread Manager ](https://docs.derivative.ca/Thread_Manager "Thread Manager")

A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

MATs or Materials are an [Operator Family](../Glossary/Operator_Family.md "Operator Family") that applies a [Shader](../Glossary/Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](../Glossary/Network_Path.md "Network Path"), which determine the output of the operator.

A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](../POPs/Group_POP.md "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](../Glossary/Designer_Mode.md "Designer Mode"), or (2) a user-created [Panel](../Glossary/Panel.md "Panel") inside a [Window Component](../Glossary/Window_COMP.md "Window COMP"). The user-created windows can span [Multiple Monitors](../Glossary/Multiple_Monitors.md "Multiple Monitors") borderless, or be floating windows with borders, or popups.

The width and height of an image in pixels. Most TOPs, like the [Movie File In TOP](../TOPs/Movie_File_In_TOP.md "Movie File In TOP") can set the image resolution. See [Aspect Ratio](../Glossary/TOP_Generator_Common_Page.md "TOP Generator Common Page") for the width/height ratio of an image, taking into account non-square pixels.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](../Glossary/Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

TouchDesigner Component file, the file type used to save a [Component](../Glossary/Component.md "Component") of your TouchDesigner project.
