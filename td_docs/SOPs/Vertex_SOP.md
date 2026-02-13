---
url: https://docs.derivative.ca/Vertex_SOP
category: SOPs
title: Vertex_SOP
---

# Vertex SOP
## Summary

The Vertex SOP allows you to edit/create attributes on a per-vertex (rather than per-point) basis. It is similar to the [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP") in this respect. It supports two inputs, and will inherit the first input source by default. If the second input have less primitives than the first input, it will cycle through the primitives and match the vertices. If the primitive in the first input has more vertices than the matching primitive in the second input, the extra vertices are ignored.
There are currently three vertex attributes supported:
  * Diffuse Color
  * Alpha
  * Texture Coordinates

When the attribute is defined, it can only occur on either points or vertices, but not both. Thus, if the input geometry has a point attribute for diffuse color, the attribute will automatically be "elevated" to be a vertex attribute (if diffuse colors are added in the Vertex SOP).
The SOP processes every vertex of every primitive. For each vertex processed, there are variables which allow you to know the:
  * Vertex number of the primitive being processed
  * The number of vertices in the primitive being processed
  * The point which is referenced by the vertex
  * The primitive which contains the vertex
  * The total number of points
  * The total number of primitives

There are also local variables to find out the values of some point attributes (i.e. position, normal - if they exist), in addition to vertex attributes. To access the attributes of the second input source, append a 2 to the variable.
[vertexSOP_Class](https://docs.derivative.ca/VertexSOP_Class "VertexSOP Class")

## Parameters - Vertex Page
- Group `group` - If there are input groups, specifying a group name in this field will cause this `SOP` to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Color `doclr` - ⊞ - Select between keeping the color, adding new color, or using no color for vertex color attributes from incoming geometry.
  * Keep Color `off` -
  * Add Color `on` -
  * No Color `remove` -

- Color `diff` - ⊞ - If you select 'Add Color' from the menu above, Cd color vertex attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are: `me.inputColor[0]` for red, `me.inputColor[1]` for green, `me.inputColor[2]` for blue, and `me.inputColor[3]` for alpha. If you select 'No Color' from the menu above, the Cd color vertex attribute will be removed from the SOP.
  * Color `diffr` -
  * Color `diffg` -
  * Color `diffb` -

- Alpha `alpha` - Control the alpha attribute in the same manner as the rgb colors above. Alpha is Cd[3] and comes from input via `me.inputColor[3]`
- Texture `douvw` - ⊞ - Select between keeping the texture coordinates, adding new texture coordinates, or using no texture coordinates for the vertex texture attributes from incoming geometry.
  * Keep Texture `off` -
  * Add Texture `on` -
  * No Texture `remove` -

- Texture `map` - ⊞ - If you select 'Add Texture' from the menu above, uv texture coordinate vertex attributes will be added/modified in the SOP. Enter expressions here to control the values of the vertex texture coordinates here. The attributes to modify are: `me.inputTexture[0]`, `me.inputTexture[1]` and `me.inputTexture[2]`. If you select 'No Texture' from the menu above, the uv texture coordinates vertex attribute will be removed from the SOP.
  * Texture `mapu` -
  * Texture `mapv` -
  * Texture `mapw` -

- Crease `docrease` - ⊞ - Select between keeping the crease, adding new crease, or using no crease for creaseweight attribute from incoming geometry.
The `Crease Weight` attribute can be used to set individual edge crease weights for sub-division surfaces (see [Subdivide SOP](https://docs.derivative.ca/Subdivide_SOP "Subdivide SOP") ). This vertex attribute defines the weight for the edge which goes from that vertex to the next vertex in the polygon. For example, with a triangle (which has vertices 0, 1, 2), the attribute for vertex 1 defines the crease weight for the edge (1, 2). The attribute for vertex 2 defines the crease weight for edge (2, 0). The crease weight should be greater than 0. The larger the value for crease weights, the sharper the edge will be when sub-divided.
Crease attributes can be visualized by passing them into a [Subdivide SOP](https://docs.derivative.ca/Subdivide_SOP "Subdivide SOP").
  * Keep Crease `off` -
  * Add Crease `on` -
  * No Crease `remove` -

- Crease `crease` - If you select 'Add Crease' from the menu above, enter expressions here to control the values of the creaseweights here. The attribute to modify is: me.inputVertex.creaseWeight[0]. Values for the weight of the vertex can range from 0.0001 to infinity.

## Parameters - Attributes Page
- Custom Attribute `attr` - Sequence of custom attributes to be added to the geometry created.
- Name `attr0name` - Creates a custom attribute with this name.
- Type `attr0type` - ⊞ - The type of attribute created can be selected from this menu.
  * float `float` -
  * vec2 `vec2` -
  * vec3 `vec3` -
  * vec4 `vec4` -
  * int `int` -
  * ivec2 `ivec2` -
  * ivec3 `ivec3` -
  * ivec4 `ivec4` -

- Value `attr0value` - ⊞ - Set the values of the Custom Attrib using these parameters.
  * Value `attr0value1` -
  * Value `attr0value2` -
  * Value `attr0value3` -
  * Value `attr0value4` -

## Examples
###
Texture Offsets
You can have set of images in a TOP, and apply all of them in one material to different parts of an object. This allows you to have a pre-rendered animation clip with the clip playing at different speeds and time offsets on different surfaces.
You can adjust the material frame time by the first vertex/point texture W component (texture coordinated are U (horizontal), V (vertical) and W (one of a set of texture images). A texture (W) value of -1 moves back in time 1 frame. This lets you apply different frames to many polygons simultaneously using the Vertex SOP, or [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP").

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Vertex SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
