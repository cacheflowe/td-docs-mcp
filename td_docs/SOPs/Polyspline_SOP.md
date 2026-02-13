---
url: https://docs.derivative.ca/Polyspline_SOP
category: SOPs
title: Polyspline_SOP
---

# Polyspline SOP
## Summary

The Polyspline SOP fits a spline curve to a polygon or hull and outputs a polygonal approximation of that spline. You can choose either to create divisions between the original points, or to ignore the position of the original points and divide the shape into segments of equal lengths.
Polyspline can optionally resample the output curve, providing control over the length and number of its segments.
**Tip:** When using this SOP, it is useful to enable Points display in the Viewport options dialog. This way you can see exactly what effect the SOP is having.
[polysplineSOP_Class](https://docs.derivative.ca/PolysplineSOP_Class "PolysplineSOP Class")

## Parameters - Page
- Group `group` - Subset of faces to use. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Spline Type `basis` - ⊞ - Spline type to use. There are seven choices:
  * Bezier `bezier` - Typical Bezier spline.
  * Special Bezier `sbezier` - Variation on Bezier.
  * Special Smooth Bezier `c1bezier` - Variation on Bezier.
  * Degree 2 Bezier `degree2` - Variation on Bezier.
  * BSpline `bspline` - Softer curve does not pass through the original points of the Source.
  * Cardinal `cardinal` - The curve passes through the original points of the Source.
  * Linear `linear` - Straight line segments.

- Close `closure` - ⊞ - Determines if the output spline is open or closed.
  * Off `cnone` - Output spline open.
  * On `calways` - Output spline closed.
  * If polygon does `cifpoly` - Use the closure of the input face. In other words, Closed splines are created if the Source polygons are closed, open splines are created if the Source polygons are open.

- Division Method `divide` - ⊞ - Settings for refining the spline by adding extra divisions.
  * Standard `standard` - Do not resample curve.
  * Even Length Segments `evenlen` - Ensure equal segment lengths.
  * Even X Segments `evenx` - Ensure segments have equal length in X.
  * Even Y Segments `eveny` - Ensure segments have equal length in Y.
  * Even Z Segments `evenz` - Ensure segments have equal length in Z.

- Segment Length `segsize` - The length of the segments in the resampled curve.
Division Method Standard If Even Length Segments are selected, Segment Length sets the length of output segments. The number of output segments is determined by Output Divisions. If Output Divisions is zero, the number of output segments is calculated using the Segment Length parameter, and is determined by how many segments of this size will fit into the overall shape. If Even Length Segments is selected, along with zero Output Divisions and Segment Length of zero, an error message is generated, saying "Invalid number of divisions or segment size".
- Output Divisions `polydivs` - Number of segments in the resampled curve.
If Division Method = Standard is selected, this has no effect. If Even Length Segments is selected, this parameter sets the number of edges that is created. The length of the segments is determined by Segment Length. If Segment Length is 0, the length of the output segments is determined by dividing the over all shape into this number of segments.
If the Output Divisions parameter is set to zero, the value of the Segment Length parameter is used to calculate the number of Output Divisions.
- Sample Divisions `edgedivs` - Number of spline divisions before resampling.
If Division Method = Standard is selected, this is the number of subdivisions for every edge. If Even Length Segments is chosen, it has the subtle effect of determining the accuracy with which the segment lengths can be calculated.
- First CV Count `first` - Number of times to repeat the first control vertex, determining its multiplicity. This determines the number of times to replicate the first vertex of the Source polygon(s). This is most useful when the Source consists of open polygons; extra vertices at the beginning of the line will force the curve to extend to the beginning of the line. For example a value of two will force a Cardinal curve to extend to its first vertex and a value of three will force a Bspline to start at is first vertex.
- Last CV Count `last` - This determines the number of times to repeat the last control vertex, determining its multiplicity. This determines the number of times to replicate the last vertex of the Source polygon(s). This is most useful when the Source consists of open polygons; extra vertices at the end of the line will force the curve to extend to the end of the line.
- CV Tension `tension` - The tension exerted by the points from the Source polygons. The greater the tension, the closer the resulting shape will be to the original shape.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the Polyspline SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
