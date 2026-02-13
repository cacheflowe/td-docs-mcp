---
url: https://docs.derivative.ca/Primitive_SOP
category: SOPs
title: Primitive_SOP
---

# Primitive SOP
## Summary

The Primitive SOP is like the [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP") but manipulates a [primitive](https://docs.derivative.ca/Primitive "Primitive")'s position, size, orientation, color, alpha, in addition to primitive-specific attributes, such as reversing primitive normals. The Primitive SOP also lets you create custom primitive attributes.
You can also apply parametric affine transformations to a profile by using this SOP. You can also use it to open, close, reverse, and cycle the profile curves.
**Note:** When applying transformations to a profile, you can only rotate about the Z axis because the projected curve is a planar curve that lives in the domain of the surface. Therefore it wouldn't make any sense to allow rotations in X or Y for profiles.
###
Transformation of Primitives vs Profiles
A Bezier surface is a single primitive, as is a NURBS surface, while a polygon mesh can consist of hundreds of individual primitives. Care must be taken to ensure the desired result. Profiles can be translated, rotated, and scaled along with 3D primitives. The Z component of translation and scaling is ignored. The X and Y components would be interpreted as U and V values because they apply to the space in which profiles are defined.

###
Example - Mapping a Texture Inside a Sphere
There are many uses for the Primitive SOP. Normally, if you apply a texture onto a sphere, it is mapped onto the outside surface because the U surface normals point outwards by default. If you wanted to map the texture onto the inside of the sphere instead, you could simply run the sphere geometry through a Primitive SOP, and select Reverse U (i.e. the surface normals) in the Face/Hull page > Vertex menu.
[primitiveSOP_Class](https://docs.derivative.ca/PrimitiveSOP_Class "PrimitiveSOP Class")

## Parameters - Primitive Page
- Source Group `group` - If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. You can specify profile curves within the group by providing a profile pattern (e.g. *.3 specifies the fourth profile in all spline surfaces).
**Tip:** By specifying both a primitive and a profile here (example: 0 0.* ), you can affect a transformation of both the parent surface and a profile curve.
- Template Group `templategrp` - A subset of template points to transform to.

## Parameters - Transform Page
- Do Transformation `doxform` - When checked, allows transformations to occur.
- Rotate to Template `dorot` - ⊞ - A template can be specified using the second input of the Primitive SOP. When set to On, this template can be used to transform each primitive to the location and orientation of the template point. This is similar to what the [Copy SOP](https://docs.derivative.ca/Copy_SOP "Copy SOP") does except that the actual primitives are transformed, not copies made.
  * Off `off` - Don't rotate.
  * On `on` - The primitive gets rotated as if its normal was (0,0,1), and is meant to point the same direction as the template normal.
  * Match Normals `match` - Rotates the primitive so that its real normal lines up with the normal of the template point.

- Transform Order `xord` - ⊞ - Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu.
  * Scale Rotate Translate `srt` -
  * Scale Translate Rotate `str` -
  * Rotate Scale Translate `rst` -
  * Rotate Translate Scale `rts` -
  * Translate Scale Rotate `tsr` -
  * Translate Rotate Scale `trs` -

- Rotate Order `rord` - ⊞ - Sets the order of the rotations within the overall transform order.
  * Rx Ry Rz `xyz` -
  * Rx Rz Ry `xzy` -
  * Ry Rx Rz `yxz` -
  * Ry Rz Rx `yzx` -
  * Rz Rx Ry `zxy` -
  * Rz Ry Rx `zyx` -

- Translate `t` - ⊞ - These three fields move the input geometry in the three axes. Profiles use tx and ty only.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Rotate `r` - ⊞ - These three fields rotate the Source geometry in the three axes. Profiles use rz only.
  * X `rx` -
  * Y `ry` -
  * Z `rz` -

- Scale `s` - ⊞ - These three fields scale the Source geometry in the three axes. Profiles use sx and sy only.
  * X `sx` -
  * Y `sy` -
  * Z `sz` -

- Pivot `p` - ⊞ - The pivot point for the transformations. Profiles use px and py only.
  * X `px` -
  * Y `py` -
  * Z `pz` -

- Lookat Object `lookat` - Selects the object the primitive should point towards. This performs the lookat in object space; if you need to a lookat in world space, use the lookat in the object's Transform page instead.
**Tip:** In order to get multiple sprites to always be perpendicular to the camera, feed them into a Primitive SOP and specify the camera as your **Lookat Object**. Then the sprites should always be perpendicular to the camera.
- Up-Vector `upvector` - ⊞ - Defines the orientation of the primitive along the X, Y, or Z axes.
The Up Vector determines how a primitive orients itself with respect to the target object (specified in Lookat Object). The default value is of 1 in the Y direction. This will produce nice behaviour if you want the object to rotate somewhat in the Z axis as the Lookat Object gets very close and/or passes the target. Scaling the Up Vector will cause the Lookat primitives to remain more upright as they get very close and/or pass the target. The stronger the Up Vector, the more the primitives will want to stay vertical and resist the rotation.
  * X `upvectorx` -
  * Y `upvectory` -
  * Z `upvectorz` -

## Parameters - Attributes Page
- Color `doclr` - ⊞ - If Keep is selected, the color attribute is left unchanged. If Add is selected, this parameter changes the color of input primitives according to diffuse color field. If No is selected, the color attribute is removed.
  * Keep Color `off` -
  * Add Color `on` -
  * No Color `remove` -

- Color `diff` - ⊞ - The color to add.
  * Red `diffr` -
  * Green `diffg` -
  * Blue `diffb` -

- Alpha `alpha` - The alpha value to add.
- Crease `docrease` - ⊞ - If Keep is selected, the crease attribute is left unchanged. If Add is selected, this parameter generates a crease attribute for the primitive. If No is selected, the crease attribute is removed.
  * Keep Crease `off` -
  * Add Crease `on` -
  * No Crease `remove` -

- Crease `crease` - Attribute is used to set edge crease weights for subdivision surfaces (see [Subdivide SOP](https://docs.derivative.ca/Subdivide_SOP "Subdivide SOP")). The Crease Weight attribute for a primitive sets all edges of the polygon to the value specified. On shared edges, the maximum of the two crease weights is used to define the sharpness of the subdivided surface. Crease weights should be larger than 0, with larger values defining sharper edges.
- Custom Attrib `attr` - Sequence of custom attributes to be added to the geometry created.
- Name `attr0name` - Creates a custom attribute with this name.
- Size `attr0size` - ⊞ - The size of the attribute to create. It'll use however many values from the Value parameter as the size is.
  * float `float` -
  * vec2 `vec2` -
  * vec3 `vec3` -
  * vec4 `vec4` -

- Value `attr0value` - ⊞ - The value(s) to assign to the attribute.
  * Value 1 `attr0value1` -
  * Value 1 `attr0value2` -
  * Value 1 `attr0value3` -
  * Value 1 `attr0value4` -

## Parameters - Face/Hull Page
- Preserve Shape U `pshapeu` - These options only become available once a type of clamping or closure has been selected.
**Closure** - Change the closure and clamping of a face or hull.
- Preserve Shape V `pshapev` - These options only become available once a type of clamping or closure has been selected.
**Closure** - Change the closure and clamping of a face or hull. The options are:
- Close U `closeu` - ⊞ - Close the primitive in U / V. Select from: Open, Closed Straight, Close Rounded, and Unroll. When you unroll a closed curve you duplicate the wrapped points (you make them unique) and turn the curve into an open curve. The shape of the curve does not change. Same goes for hulls, only there we unique entire rows and cols. This addresses a problem with texturing wrapped surfaces whereby the texture repeats itself in the wrapped portion of the surface.
  * No change `sameclosure` -
  * Open `open` -
  * Close Straight `closesharp` -
  * Close Rounded `closeround` -
  * Unroll `unroll` -

- Close V `closev` - ⊞ - Close the primitive in U / V. Select from: Open, Closed Straight, Close Rounded, and Unroll. When you unroll a closed curve you duplicate the wrapped points (you make them unique) and turn the curve into an open curve. The shape of the curve does not change. Same goes for hulls, only there we unique entire rows and cols. This addresses a problem with texturing wrapped surfaces whereby the texture repeats itself in the wrapped portion of the surface.
  * No change `sameclosure` -
  * Open `open` -
  * Close Straight `closesharp` -
  * Close Rounded `closeround` -
  * Unroll `unroll` -

- Clamp U `clampu` - ⊞ - Clamp the primitive in U / V. Select from: Clamp, Unclamp.
  * No change `sameclamp` -
  * Clamp `clamp` -
  * Unclamp `unclamp` -

- Clamp V `clampv` - ⊞ - Clamp the primitive in U / V. Select from: Clamp, Unclamp.
  * No change `sameclamp` -
  * Clamp `clamp` -
  * Unclamp `unclamp` -

- Vertex `vtxsort` - ⊞ - Reorder the vertices in a number of ways.
  * No change `samevertex` - Does not affect the ordering of the vertices.
  * Reverse `reverse` - Reverses both U and V for hulls, and just U for faces.
**For example:**
  * Reverse U `reverseu` - Reverses column order of hulls.
  * Reverse V `reversev` - Reverses row order of hulls.
  * Swap U and V `swapuv` - Interchanges rows/columns while preserving topology.
  * Shift `shift` - Cycles the vertices by "U Offset" and "V Offset".
  * Flip Face `flipfacing` -

- U Offset `vtxuoff` - Cycles face or hull columns / rows when the Shift operation is selected.
- V Offset `vtxvoff` - Cycles face or hull columns / rows when the Shift operation is selected.

## Parameters - Meta Page
- Meta-Surface Weight `metaweight` - When selected, allows meta-surface weighting.
- Weight `doweight` - Enter weight of meta-surface here when Meta-surface Weight is selected.

## Parameters - Particles Page
- Particle Render Type `doprender` - When On the Particle Type menu below allows section of particle render type.
- Particle Type `prtype` - ⊞ - Selects how the particles are rendered.
  * Render as Lines `lines` - Each particle will be rendered as a 2-point line, with the length determined based on the particles velocity. If the particle has no velocity it will just be a single pixel in size.
  * Render as Point Sprites `pointprites` - For use with the [Point Sprite MAT](https://docs.derivative.ca/Point_Sprite_MAT "Point Sprite MAT"). Each particle is a square of pixels that always face the camera. The size of the square is determined by parameters in the Point Sprite and the `pscale` vertex/point attribute. The point sprites will have texture coordinates generated for them automatically also ((0,0) in the bottom left and (1,1) in the top right).
  * Render as Point Sprites `pointsprites` -

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Primitive SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
