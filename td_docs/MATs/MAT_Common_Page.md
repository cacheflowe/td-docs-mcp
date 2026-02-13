---
url: https://docs.derivative.ca/MAT_Common_Page
category: MATs
title: MAT_Common_Page
---

# MAT Common Page

##  Overview
The MAT Common Page allows you adjust many rendering settings. These settings are completely independent of the shader being used, so they be applied to any shader. Some MATs may require certain rendering features be enabled or disabled to work correctly, in that case the parameters will be disabled for that MAT type.
##  Parameters
###  Blending
[Blending](https://docs.derivative.ca/Blending "Blending") is summing the color value of the pixel being drawn and the pixel currently present in the Color-Buffer. Blending is typically used to simulate [Transparency](https://docs.derivative.ca/Transparency "Transparency").
The blending equation is:
Final Pixel Value = (Source Blend * Source Color) + (Dest Blend * Destination Color)
Blending (Transparency) `blending` - This toggle enables and disables blending. However see the wiki article [Transparency](https://docs.derivative.ca/Transparency "Transparency").
Source Color `srcblend` - This value is multiplied by the color value of the pixel that is being written to the Color-Buffer (also know as the Source Color).
Destination Color `destblend` - This value is multiplied by the color value of the pixel currently in the Color-Buffer (also known as the Destination Color).
Separate Alpha Function `separatealphafunc` - This toggle enables and disables separate blending options for the alpha values.
Source Alpha `srcblend` - This value is multiplied by the alpha value of the pixel that is being written to the Color-Buffer (also know as the Source Alpha).
Destination Alpha `destblend` - This value is multiplied by the alpha value of the pixel currently in the Color-Buffer (also known as the Destination Alpha).
###  Depth Test
Depth-Testing is comparing the depth value of the pixel being drawn with the pixel currently in the [Frame-Buffer](https://docs.derivative.ca/index.php?title=Frame-Buffer&action=edit&redlink=1 "Frame-Buffer \(page does not exist\)"). A pixel that is determined to be in-front of the pixel currently in the Frame-Buffer will be drawn over it. Pixels that are determined to be behind the pixel currently in the Frame-Buffer will not be drawn. Depth-Testing allows geometry in a 3D scene to occlude geometry behind it, and be occluded by geometry in-front of it regardless of the order the geometry was drawn.
For a more detailed description of Depth-Testing, refer to the [Depth-Test](https://docs.derivative.ca/Depth-Test "Depth-Test") article.
Depth Test `depthtest` - Enables and disables the Depth-Test. If the depth-test is disabled, depths values aren't written to the Depth-Buffer.
Depth Test Function `depthfunc` - The depth value of the pixel being drawn is compared to the depth value currently in the depth-buffer using this function. If the test passes then the pixel is drawn to the Frame-Buffer. If the test fails the pixel is discarded and no changes are made to the Frame-Buffer.
Write Depth Values `depthwriting` - If Write Depth Values is on, pixels that pass the depth-test will write their depth value to the Depth-Buffer. If this isn't on then no changes will be made to the Depth-Buffer, regardless of if the pixels drawn pass or fail the depth-test.
###  Alpha Test
Alpha-testing allows you to choose to draw or not draw a pixel based on its alpha value.
Discard Pixels Based On Alpha `alphatest` - This enables or disables the pixel alpha test.
Keep Pixels with Alpha `alphatest` - This menu works in conjunction with the Alpha Threshold parameter below in determining which pixels to keep based on their alpha value.
Alpha Threshold `alphathreshold` - This value is what the pixel's alpha is compared to to determine if the pixel should be drawn. Pixels with alpha greater than the Alpha Threshold will be drawn. Pixels with alpha less than or equal to the Alpha Threshold will not be drawn.
###  Wire Frame
The wire-frame feature will render the geometry as wire-frame, using the actual primitive type used in the render. What this means is surfaces like Metaballs, NURBs and Beziers will become a wire-frame of the triangles/triangle-strips used to render them (since these types of primitives can't be natively rendered in OpenGL).
Wire Frame `wireframe` - Enables and disables wire-frame rendering with the option of OpenGL Tesselated or Topology based wireframes.
Line Width `wirewidth` - This value is the width that the wires will be. This value is in pixels.
###  Cull Face
The cull face parameter will cull faces from the render output. This can be used as an optimization or sometimes to remove artifacts. See [Back-Face Culling](https://docs.derivative.ca/Back-Face_Culling "Back-Face Culling") for more infomation.
Cull Face `cullface` - Selects which faces to render.
  * Use Render Setting - use the render settings found in the Render or Render Pass TOP.
  * Neither - do not cull any faces, render everything.
  * Back Faces - cull back faces, render front faces.
  * Front Faces - cull front faces, render back faces.
  * Both Faces - cull both faces, render nothing.

###  Polygon Depth Offset
This feature pushes the polygons back into space a tiny fraction. This is useful when you are rendering two polygons directly on-top of each other and are experiencing [Z-Fighting](https://docs.derivative.ca/Z-Fighting "Z-Fighting"). Refer to [Polygon Depth Offset](https://docs.derivative.ca/Polygon_Depth_Offset "Polygon Depth Offset") for more information. This is also an important feature when doing [shadows](https://docs.derivative.ca/Shadows "Shadows").
Polygon Depth Offset `polygonoffset` - Turns on the polygon offset feature.
Offset Factor `polygonoffsetfactor` - Adds an offset to the Z value that depends on how sloped the surface is to the viewer.
Offset Units `polygonoffsetunits` - Adds a constant offset to the Z value.
MATs or Materials are an [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that applies a [Shader](https://docs.derivative.ca/Shader "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.
The term "Frame" is a measurement of time used (1) in the [Timeline](https://docs.derivative.ca/Timeline "Timeline"), (2) as a time-unit in CHOPs, and (3) as a time unit in movie files that are read into [TOPs](https://docs.derivative.ca/TOP "TOP") and written out from TOPs. The frame rate is the frames per second ([FPS](https://docs.derivative.ca/index.php?title=FPS&action=edit&redlink=1 "FPS \(page does not exist\)")).
The connection of an output of one node to the input of another node in a network. In contrast, see [Link](https://docs.derivative.ca/Link "Link").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
A polygon is a type of [Primitive](https://docs.derivative.ca/Primitive "Primitive") that is formed from a set of [Vertices](https://docs.derivative.ca/Vertex "Vertex") in 3D that are implicitly connected together to form a multi-edge shape.
