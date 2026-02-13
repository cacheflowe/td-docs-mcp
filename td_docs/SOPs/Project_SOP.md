---
url: https://docs.derivative.ca/Project_SOP
category: SOPs
title: Project_SOP
---

# Project SOP
## Summary

The Project SOP creates curves on surface (also known as trim or profile curves) by projecting a 3D face onto a spline surface, much like a light casts a 2D shadow onto a 3D surface. There are two projection methods: along a vector, or by mapping the face directly onto the parametric space of the surface.
You will usually need a [Trim SOP](https://docs.derivative.ca/Trim_SOP "Trim SOP"), [Bridge SOP](https://docs.derivative.ca/Bridge_SOP "Bridge SOP"), or [Profile SOP](https://docs.derivative.ca/Profile_SOP "Profile SOP") after a Project SOP. For example, in the case of a Trim SOP we might have:
[![TouchGeometry146.gif](https://docs.derivative.ca/images/4/41/TouchGeometry146.gif)](https://docs.derivative.ca/File:TouchGeometry146.gif)
Use a Trim SOP to cut a hole in the projected surface (as shown above).
Use a Bridge SOP to skin the profile curve to another profile curve.
Use a Profile SOP to extract the curve on surface or remap its position.
If you end up with a profile curve that is not visible, it may still exist. Confirm a profile curve's existence by clicking on the SOP's info pop-up (using middle-mouse button).
###
Additional Operations for Profile Curves
To delete a projected curve, use a [Delete SOP](https://docs.derivative.ca/Delete_SOP "Delete SOP"), and enter the profile number (e.g. 1.4 returns the fifth profile on the second primitive (counting starts at 0) ). You can visualise the number of the profiles by enabling the Profile Number icon in the Viewport Display options.
You can group the profile curves with a [Group SOP](https://docs.derivative.ca/Group_SOP "Group SOP"). Do this by typing the profile numbers in the Pattern field. You can use all regular expressions.
You can apply parametric affine transformations to the profile by using a [Primitive SOP](https://docs.derivative.ca/Primitive_SOP "Primitive SOP"). You can also use the Primitive SOP to open, close, reverse, and cycle the profile curves.
**Note:** When applying transformations to a profile in the Primitive SOP, you can only rotate about the Z axis because the projected curve is a planar curve that lives in the domain of the surface. Therefore it wouldn't make any sense to allow rotations in X or Y for profiles.
[projectSOP_Class](https://docs.derivative.ca/ProjectSOP_Class "ProjectSOP Class")

## Parameters - Page
- Face Group `facegroup` - The group of faces to be projected onto the spline surfaces. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Surface Group `surfgroup` - The group of surfaces to project faces onto. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Cycle Type `cycle` - ⊞ - Select the method use to project the 3D faces onto the 3D spline surfaces.
  * All on Each Surface in Sequence `allseq` - If projected parametrically, the spatial relationship between the faces will be preserved. For example, if the text "hello" is projected parametrically and in sequence, the letters will appear on the surface naturally, side by side. Sequence is not applicable if projecting along a vector.
  * All on Each Surface Overlapping `allover` - If projected parametrically, the spatial relationship between the faces is not preserved, so they will appear overlapped in the area of the domain chosen for projection. Overlapping is not applicable if projecting along a vector.
  * One per Surface `oneeach` - Each face is projected onto a surface in the order in which the face and the surface appear in the input or in their respective groups.
  * Cycled `cycled` - This is the same as One Per Surface, above, but starts the faces again if there are surfaces left.

## Parameters - Method Page
- Method `method` - ⊞ - Select between projecting along a vector or parametrically using the parameters below.
  * Along Vector `vector` - The face is projected along a 3D vector and its image on the surface is converted into a curve on the surface. One spatial curve may generate several profiles depending on its position relative to the surface, the shape of the surface, and the chosen projection side. If the projected face does not intersect the surface at all, no profile curve will be generated.
  * Parametrically `parametric` - The spatial size of the faces is mapped directly onto the domain of the spline surface. The resulting projection is sensitive to the parameterization of the surface and is likely to appear distorted. It is, however, the fastest of the two projection types and tends to behave well on surfaces with regular shapes and chord-length parameterizations.

- Axis `axis` - ⊞ - The axis along which the four corners of the feature are projected onto the base. When adding the feature from the outside as a Vector paste.
  * X `xaxis` - Cartesian axis X, Y, or Z.
  * Y `yaxis` - Cartesian axis X, Y, or Z.
  * Z `zaxis` - Cartesian axis X, Y, or Z.
  * Face Normal `fnorm` - Projection axis occurs along each face's normal. Thus, each face could potentially have a different projection direction than the others. The option also works well for non-planar faces.
  * Minimum Distance `mindist` - Projects the entire 3D face along the vectors of minimum distance to the surface. The projection resolution is given by the Divisions per Span value.
  * User Defined: `other` - Enables the Vector fields immediately below to specify the X, Y, and Z components of the vector.

**Note:** When the **Minimum Distance** option is selected, the **Side** button becomes disabled because it's irrelevant for this projection type.
- Vector `vector` - ⊞ - The X, Y, and Z components of the projection vector if none of the main axes is chosen in the Axis parameter above.
  * `vector1` -
  * `vector2` -
  * `vector3` -

- Side `projside` - ⊞ - Select which sides of the geometry to project on, closest or farthest.
  * Closest `closest` - Will project the face onto the closest part of the surface in either direction of projection vector. For example, if a curve being projected onto a tube is inside the tube, it will yield two profiles, one on each side of the tube; if the curve is outside the tube, it will project onto the side closest to it.
  * Farthest `farthest` - The reverse of Closest. In the example above, Farthest would also yield two images if the curve is inside the tube, but it will choose the farthest side if the curve is outside the tube.

- Divisions per Span `sdivs` - The number of points to be computed on the spatial face between successive spans. A span is the line connecting two consecutive CVs on a polygon, or the arc between two breakpoints on a spline curve. The projection tends to become more accurate as the number of divisions increases.
- Ray Tolerance `rtolerance` - Controls the precision of the ray intersection with the surface. The ray is cast along the projection vector from every point of the 3-D curve.
- Fit Tolerance `ftolerance` - Controls the 2-D fitting precision and is typically less than 0.01.
- Max UV Gap (%) `uvgap` - This specifies what percentage of the size of the surface domain is acceptable for two separate profiles to be joined into a single curve.
- Order `order` - The spline order of the resulting profile curve. The type of curve (Bzier or NURBS) is inherited from the spatial curve. The order, however, is not inherited because the spline order provides useful control over the quality of the fit. If the spatial face is a polygon, the profile will be a NURBS curve.
- Preserve Sharp Corners `csharp` - Controls the precision with which sharp corners in the projection curve are interpolated. It should be on when the projection has areas of high changes in curvature.
- Super Accurate Projection `accurate` - Use a very accurate yet expensive algebraic pruning algorithm to determine the intersection of the vector with the surface.
- U from `ufrom` - ⊞ - Specifies which of the spatial coordinates - X, Y, or Z - must be mapped to the U parametric direction of the surface.
  * X Coordinate `uvx` -
  * Y Coordinate `uvy` -
  * Z Coordinate `uvz` -

- V from `vfrom` - ⊞ - Specifies which of the spatial coordinates - X, Y, or Z - must be mapped to the V parametric direction of the surface.
  * X Coordinate `uvx` -
  * Y Coordinate `uvy` -
  * Z Coordinate `uvz` -

- Map Profile to Range: `userange` - This option is on by default. It causes the profile to be scaled and translated to fit within the surface's domain ranges described below. If this option is off, the profile's coordinates are mapped onto the surface domain without any transformation; consequently, the profile will not be visible if its points are not inside the domain of the target surface.
Typically, the projected face should not be mapped to the U/V range if it was previously extracted from the same surface using the [Profile SOP](https://docs.derivative.ca/Profile_SOP "Profile SOP") with the Parametrically to XY option selected. The extraction and re-projection tandem can be very useful in achieving the modeling goals currently attainable only with 3D curves. Such tasks include the ability to edit the points of a profile, joining, stitching, or filleting profiles together, carving or refining profiles, etc. By extracting a profile parametrically to XY, Touch creates a 3D face that is identical to the 2D profile but has an additional (constant) Z component.
The resulting 3D curve can be modeled using all the 3D tools available. Finally, the modeled 3D face can be reapplied onto the surface parametrically, making sure that the range mapping option is off.
- U Range `urange` - ⊞ - Indicates in percentages what part of the U surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the U parametric direction. The range is not restricted to the 0-1 interval.
  * `urange1` -
  * `urange2` -

- V Range `vrange` - ⊞ - Indicates in percentages what part of the V surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the V parametric direction. The range is not restricted to the 0-1 interval.
  * `vrange1` -
  * `vrange2` -

- Mapping Type `maptype` - ⊞ - Select how to reposition and scale an existing profile to fit within the specified domain range.
  * Uniform `unif` - Mapping converts the spatial coordinates of the projection faces to (U,V) points in the domain of the surface without taking into account the parameterization of the surface.
  * Chord Length `chordlen` - Mapping takes into account the surface parameterization and attempts to compute a projection best suited to the spatial and parametric determinants of the model.

If the face is not mapped to range, it's vertices will be transferred to the profile without any transformation. Use this technique together with the parametric extraction in the Profile SOP to edit the points of a profile generated by a SOP other than Project: extract, edit the points, then project again.

Tips
###
NURBS Scalp Patch for Hair
The: Along Vector > Axis > Minimum Distance option is extremely useful, say in the following situation: You have a NURBS surface of a head, and you want to obtain a NURBS patch by projecting a hairline onto the head's surface. You could:
Template the NURBS head.
Enter a [Model SOP](https://docs.derivative.ca/Model_SOP "Model SOP").
Enable the Snap to Template option in the Model Editor (Snap options).
Draw a NURBS curve along the surface of the head where you want the hairline. Then, with the Project SOP, you select the Minimum Distance option, and you have a profile curve with which you can trim the surface of the head to obtain the patch.
Thus having obtained a NURBS patch for the scalp, you could use it as the base for hair.

## Example
  1. Place a [Circle SOP](https://docs.derivative.ca/Circle_SOP "Circle SOP") - Type: `NURBS`, Radius: `0.3, 0.3`; then place a [Tube SOP](https://docs.derivative.ca/Tube_SOP "Tube SOP") - Type: `NURBS`.
  2. Connect them into a Project SOP - Circle to Input1; Tube to Input2.
  3. Append a [Trim SOP](https://docs.derivative.ca/Trim_SOP "Trim SOP") to the Project SOP - it trims the surface according to the projection provided by the Project SOP. You need to append a Trim SOP to a Project SOP in order to realise this trimming action.
  4. Enable the template flags on the Circle and Tube SOPs; make the Project SOP the display SOP.

[![TouchGeometry36.gif](https://docs.derivative.ca/images/a/aa/TouchGeometry36.gif)](https://docs.derivative.ca/File:TouchGeometry36.gif)

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Project SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
