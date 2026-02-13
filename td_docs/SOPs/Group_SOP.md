---
url: https://docs.derivative.ca/Group_SOP
category: SOPs
title: Group_SOP
---

# Group SOP
## Summary

The Group SOP generates groups of points or primitives according to various criteria and allows you to act upon these groups. Elements can occur in more than one group. Groups are used in many parts of the SOP Editor to specify which portion(s) of input geometry you wish a SOP to act upon.
You can also create ordered groups. To do so, check the Ordered button.
[groupSOP_Class](https://docs.derivative.ca/GroupSOP_Class "GroupSOP Class")

## Parameters - Group Page
- Group Name `crname` - The name of the group to be created. The default name is set to match the name of the SOP.
- Entity `entity` - ⊞ - Primitives or Points.
  * Primitives `primitive` -
  * Points `point` -

- Geometry Type `geotype` - ⊞ - Select the geometry type group. The selection will only pertain to the geometry type specified. e.g. If you only wanted to group polygons.
  * All Types `all` - All geometry will be selected.
  * Bezier Curve `bezierc` -
  * Bezier Surface `bezier` -
  * Circle `circle` -
  * Mesh `mesh` -
  * Metaball `meta` -
  * NURBS Curve `nurbc` -
  * NURBS Surface `nurb` -
  * Particles `part` -
  * Polygon `poly` -
  * Sphere `sphere` -
  * Tube `tube` -
  * Triangle Strip `tristrip` -
  * Triangle Fan `trifan` -

## Parameters - Create Page
- Use Number `usenumber` - Allows selection of grouping of entities by number. When the Enable button is Active, the selection options become active and can be used to select entities. The fields available are listed below.
- Create Ordered `ordered` - When selected, elements in the group are traversed in the order they are selected; otherwise they are traversed in creation order.
- Operation `groupop` - ⊞ - When the Number Enable button is checked, this option groups entities based on a defined Pattern or by a Range.
  * Group by Pattern `grppattern` - Select a pattern in the Pattern field below.
  * Group by Range `grprange` - Select a Range using the Start/End and Select_of_ fields below.
  * Group by Expression `grpexpression` - Select a range using the Filter Expression field below.

- Pattern `pattern` - Activated when Operation is set to Group by Pattern. In this field, enter the range of primitives to select. The required syntax is "S.P", where S is the index of the parent surface, and P the profile index on that surface. You can mix primitives with profiles in the list. A mixed group is automatically ordered.
For Example:
  * `0.4 2 4 2.5 3.7` selects three profiles and two primitives,
  * `0-100:2` selects every other number from 0 to 100,
  * `0-10:2,3` selects every two of three,
  * `0.0-6` selects six profiles on primitive 0,
  * `0.*` selects all profiles on primitive 0,
  * `!4` selects every primitive or point except the fourth,
  * `9-0` selects first ten (in reverse if ordered flag is on),
  * `!0.*` selects all profiles except those on primitive 0,
  * `*` selects all primitives or points, and no profiles.

See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching") for details.
- Transfer Selection to Pattern `transfer` - This allows you to define the range of points / primitives visually by selecting them in the Viewport with the Select state. Clicking this button transfers the selected points/primitives into the Pattern field as a compacted range (e.g. `1-23 40 67-100`). This eliminates the need for typing the point or primitive numbers manually.
**Note:** Point and primitive selections can be dumped directly into Group fields without use of the Group SOP. Do this by selecting the points or primitives in the Viewport with the Select state. Then the pop-up N menu beside the Group field of the SOP you want to cook should display the selection in the input SOP (e.g. "grid1's Primitive Selection"). Ranges are automatically compacted.
- Start / End `range` - ⊞ - Activated when Operation is set to Group by Range. Select the start and end of the primitive/point number selection.
  * `rangestart` -
  * `rangeend` -

- Select _ of _ `select` - ⊞ - Activated when Operation is set to Group by Range. Select every nth occurrence of every mth entity in the above Start/End range.
**For Example:** entering 1 and 2 selects 1 out of every 2 entities.
  * `select1` -
  * `select2` -

- Filter Expression `filter` - The Filter Expression provided is evaluated for every point/primitive. Wherever it is true, the entity is added. All the local variables of point and primitive are present, though only accessable when the right type of group is being created.

- Use Bounds `usebounds` - This option is used for selecting entities based on bounding volumes: Bounding Box, or Bounding Sphere. When Active, the selection options become active and can be used to select entities. The fields available are listed below. The bounding volume can be seen in the viewport as guide geometry.
- Bounding Type `boundtype` - ⊞ - Selects the type of bounding volume to use
  * Bounding Box `usebbox` - Entities contained within the box are selected.
  * Bounding Sphere `usebsphere` - Entities contained within the sphere are selected.
  * Bounding Object (points only) `usebobject` - Points contained within the Object are selected. Make sure the object consists of well formed polygons. If using an irregular mesh, convert to polygons with a Convert SOP, then use a Divide SOP to convex sides to 3.

- Size `size` - ⊞ - Dimensions of either the Bounding Box or Bounding Sphere in X, Y and Z.
  * X `sizex` -
  * Y `sizey` -
  * Z `sizez` -

- Center `t` - ⊞ - The X, Y, and Z coordinates of the center of the bounding volume.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Use Normal `usenormal` - This option is used for selecting entities based on the angle of the entity normals. When the Active, the selection options become active and can be used to select entities. The fields available are listed below.
The primary axis and the spread angle from the defined axis define a range of angles. If any entity normals lie within this range, then the associated entity is selected.
**For Example:** if you want to select the polygons that are very steep in a polygon mountain terrain on the XZ axis. You would set the Direction to be 0, 1, 0 and the spread angle to around 75. This selects all the polygons with normals that lie flat to fairly sloped. You will have grouped all of the polygons that lie flat up to polys that are at a 75 angle from the axis. You are left with all of the polygons that are 76 or greater.
- Direction `dir` - ⊞ - The default values of 0, 1, 0 create a normal vector straight up in Y, which is perpendicular to the XZ plane, which becomes the primary axis. The 1, 0, 0 points the normal in positive X, giving a normal axis perpendicular to the YZ. The plane may be positioned at an angle by using values typed in (1, 1, 0 gives a 45 angle plane) or interactively by using the direction vector jack. Values between 0 and 1 should be used.
  * X `dirx` -
  * Y `diry` -
  * Z `dirz` -

- Spread Angle `angle` - The value entered in this field generates an angle of deviation from the primary axis. This can be visualized as a cone where the radius of the base of the cone is defined by the Spread Angle and the axis of the cone is determined by the Direction axis. Viewing the primitive normals in the viewport, you can see that any primitives with normals that have an angle that lies in the range of angles defined by the cone will be selected and grouped.
- Backface from `camera` - This menu allows you to select an object. Typically, a camera object would be chosen. The primitives which are backface when viewed from the object specified will be grouped or selected.
- Use Edges `useedges` - Allows you to group primitives by edges.
- Edge Angle `doangle` - Enables the Edge Angle parameter.
- Edge Angle `edgeangle` - Specifies an angle between edges in which to group. Works only for primitive groups.
- Edge Depth `dodepth` - Enables the Edge Depth parameter.
- Edge Depth `edgestep` - Enter the depth of the edge (only for point groups).
- Point Number `point` - Enter the specific point numbers (only for point groups).
- Unshared Edges `unshared` - When selecting points, this option selects the points of a ploygonal mesh which appear on the boundary (i.e. those which are not shared) for inclusion in the group, and orders them. In addition to polygonal meshes, this option also finds the boundaries of geo Hulls and open faces.
- Create Boundary Groups `boundarygroups` - When selecting points with the Unshared Edges parameter, this option becomes available. Enabling it creates new groups of the form: <name>__< n> , (two underscores) where the < name> is the Group Name specified in the Create page. Numbers < n> begin at zero, and increment as more groups are created.
These groups contain the points on each boundary of the surface. For example, if you have a grid with a hole in the middle of it, two new point groups are created - one containing the points for the outer boundary and one with the points from the hole. These new point groups are also ordered.

## Parameters - Combine Page
This page of parameters lets you modify the The number of primitives or points in one of the input groups by combining groups through different operations.
- Group = `grpequal` - Specify the group whose members you wish to edit. This can be one of the input groups or a new group created in this SOP specified in the Group Name parameter on the Group page.
- Not `not1` - When Off, include the members of the group specified in Group 1 parameter below. When On, include all members that are not part of the group specified in Group 1 parameter below.
- Group 1 `grp1` - Select one of the input groups to start with, noting the setting of the Not (not1) parameter above.
- Operation `op1` - ⊞ - Select the operation used to combine the group specified in Group 1 parameter with the group specified in Group 2 parameter.
  * None `none` - No operation is performed between the groups.
  * Union (Or) `or` - A OR B
  * Intersect (And) `and` - A AND B
  * Exclusive Or `xor` - !A OR !B
  * Subtraction `sub` - A minus B

- Not `not2` - When Off, include the members of the group specified in Group 2 parameter below. When On, include all members that are not part of the group specified in Group 2 parameter below.
- Group 2 `grp2` - Select one of the input groups to combine with the group above, noting the setting of the Not (not2) parameter above.
- Operation `op2` - ⊞ - Select the operation used to combine the group specified in Group 2 parameter with the group specified in Group 3 parameter.
  * None `none` -
  * Union (Or) `or` -
  * Intersect (And) `and` -
  * Exclusive Or `xor` -
  * Subtraction `sub` -

- Not `not3` - When Off, include the members of the group specified in Group 3 parameter below. When On, include all members that are not part of the group specified in Group 3 parameter below.
- Group 3 `grp3` - Select one of the input groups to combine with the group combination above, noting the setting of the Not (not3) parameter above.
- Operation `op3` - ⊞ - Select the operation used to combine the group specified in Group 3 parameter with the group specified in Group 4 parameter.
  * None `none` -
  * Union (Or) `or` -
  * Intersect (And) `and` -
  * Exclusive Or `xor` -
  * Subtraction `sub` -

- Not `not4` - When Off, include the members of the group specified in Group 4 parameter below. When On, include all members that are not part of the group specified in Group 4 parameter below.
- Group 4 `grp4` - Select one of the input groups to combine with the group combination above, noting the setting of the Not (not4) parameter above.

## Parameters - Edit Page
This folder allows you to edit existing groups.
- Convert Type `cnvtype` - ⊞ - Converts a group from a point group to a primitive group, and vice versa.
  * Primitive to Point Group `toprim` -
  * Point to Primitive Group `topoint` -

- Group `convertg` - Name of the group to convert.
- Convert Name `cnvtname` - New group name.
- Preserve Original `preserve` - When checked, preserves original geometry.

- Group `oldname` - Allows you to rename an existing group to something else.
- New Name `newname` - Allows you to rename an existing group to something else.

- Group `destroyname` - Allows you to delete an existing point or primitive group.

## Operator Inputs
  * Input 0:  -
  * Input 1:  -

## Info CHOP Channels
Extra Information for the Group SOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
