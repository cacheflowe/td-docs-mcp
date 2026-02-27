---
url: https://docs.derivative.ca/Primitive
category: Glossary
title: Primitive
---

# Primitive

A Primitive is a surface type like [Polygon](https://docs.derivative.ca/Polygon "Polygon"), [Mesh](https://docs.derivative.ca/Mesh "Mesh"), [Particle](https://docs.derivative.ca/Particle "Particle"), curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like [Sphere](https://docs.derivative.ca/Sphere_SOP "Sphere SOP"), [Tube](https://docs.derivative.ca/Tube_SOP "Tube SOP") and [Metaball](https://docs.derivative.ca/Metaball "Metaball").

Primitives are defined from [Points](https://docs.derivative.ca/Point "Point") plus other data.

See also: [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), [Point](https://docs.derivative.ca/Point "Point"), [Point List](https://docs.derivative.ca/Point_List "Point List"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), [Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class"), [Polygon](https://docs.derivative.ca/Polygon "Polygon"), [Vertex](https://docs.derivative.ca/Vertex "Vertex"), [SOP](https://docs.derivative.ca/SOP "SOP"), [SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class"), [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/Attribute "Attribute").

Every SOP has a Primitive List, which may contain any number of primitives of the following types:

##  Polygons

**Types of Polygons**
  * **Closed or Open**

A polygon can be closed, where the last vertex is connected to the first vertex, or may be open, where the last vertex is not connected to the first vertex. This is determined by the "closed" flag of a polygon.

A closed polygon shares its first and last vertex and is flagged internally as "closed". Thus, if an open polygon has five vertices, it will still have five vertices when closed. The last (closing) vertex is only implied.
[![ClosedOpenPolys.jpg](https://docs.derivative.ca/images/9/9c/ClosedOpenPolys.jpg)](https://docs.derivative.ca/File:ClosedOpenPolys.jpg)
  * **Planar or Non-planar**

Planar polygons are those whose vertices lie in the same plane in 3D space. Non-planar polygons have vertices that do no lie in the same plane in 3D space.
  * **Convex or Concave**

A polygon can be [convex or concave](https://docs.derivative.ca/Convex_and_Concave_Polygons "Convex and Concave Polygons"), as illustrated below:
[![ConvexPolys.jpg](https://docs.derivative.ca/images/4/44/ConvexPolys.jpg)](https://docs.derivative.ca/File:ConvexPolys.jpg)
Convex Polygons
[![ConcavePolys.jpg](https://docs.derivative.ca/images/a/a8/ConcavePolys.jpg)](https://docs.derivative.ca/File:ConcavePolys.jpg)
Concave Polygons

A polygon is convex if any vertical or horizontal axis intersects it at most twice.

See also: [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), [Point](https://docs.derivative.ca/Point "Point"), [Point List](https://docs.derivative.ca/Point_List "Point List"), [Point Class](https://docs.derivative.ca/Point_Class "Point Class"), Primitive, [Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class"), [Vertex](https://docs.derivative.ca/Vertex "Vertex"), [SOP](https://docs.derivative.ca/SOP "SOP"), [SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class"), [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT"), [Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP"), [Point Groups](https://docs.derivative.ca/Point_Group "Point Group"), [Primitive Groups](https://docs.derivative.ca/Primitive_Group "Primitive Group"), [Attributes](https://docs.derivative.ca/index.php?title=Attributes&action=edit&redlink=1 "Attributes \(page does not exist\)").

##  Meshes

Meshes are a collection of edges and vertices that can be represented as having a number of rows and columns based on a UV co-ordinate system. They can be modified into various shapes such as tubes and spheres by changing the point coordinates and/or closing the mesh in U or V, while maintaining their row/column-like topology.
[![MeshExample1.jpg](https://docs.derivative.ca/images/1/1e/MeshExample1.jpg)](https://docs.derivative.ca/File:MeshExample1.jpg)
For example, below right is a mesh modified into a sphere by wrapping the mesh in U. Both primitives have the same m x n point topology, only the point coordinates are different. What looks like individual polygons in the above figure are actually intrinsic parts of the primitive.

A figure that doesn't have an m × n topology cannot be a primitive mesh. The mesh below-left is not a primitive mesh, it does not have an m x n topology. The mesh below-right is a 5x4 primitive mesh.
[![MeshExample2.jpg](https://docs.derivative.ca/images/2/20/MeshExample2.jpg)](https://docs.derivative.ca/File:MeshExample2.jpg)

##  Particles

A particle system is a type of Primitive of a [SOP](https://docs.derivative.ca/SOP "SOP") that consists of a group of discrete particles which change over time. Each particle has its own attributes controlling size, position, velocity, etc. Particles can generate new attributes depending on their age, or they may die. Assigning values discretely to each particle enables realistic modeling of systems involving turbulence such as: smoke, wind, fire, dust, and hair.

###  Particles on the CPU

Any point or set of [points](https://docs.derivative.ca/Point "Point") can be used as the basis for the particles in a particle system. [Grid SOPs](https://docs.derivative.ca/Grid_SOP "Grid SOP") or [Sphere SOPs](https://docs.derivative.ca/Sphere_SOP "Sphere SOP") are often employed for this purpose. A particle system can be created in SOPs by using a [Particle SOP](https://docs.derivative.ca/Particle_SOP "Particle SOP"), particles will be emitted from the points of the geometry connected to the Particle SOP's first input.

Any point or set of points can also be converted into particles using a [Convert SOP](https://docs.derivative.ca/Convert_SOP "Convert SOP").

###  Particles on the GPU

Particles can be simulated on the GPU by treating each pixel in a TOP as a particle, and instancing them through the Instancing pages of a [Geometry COMP](https://docs.derivative.ca/Geometry_COMP "Geometry COMP"). TOPs that facilitate this include the [Point File In TOP](https://docs.derivative.ca/Point_File_In_TOP "Point File In TOP"), [Math TOP](https://docs.derivative.ca/Math_TOP "Math TOP"), [Limit TOP](https://docs.derivative.ca/Limit_TOP "Limit TOP"), [Slope TOP](https://docs.derivative.ca/Slope_TOP "Slope TOP"), [Feedback TOP]], [Reorder TOP](https://docs.derivative.ca/Reorder_TOP "Reorder TOP"). In the Palette are several examples under Point Clouds and particlesGPU.

See also [Point Sprite MAT](https://docs.derivative.ca/Point_Sprite_MAT "Point Sprite MAT").

##  Splines

Touch allows you to create both Bézier and NURBS curves and surfaces using splines. Refer to [Splines](https://docs.derivative.ca/Spline "Spline") article for a complete discussion of these types.

##  Quadrics

See [Quadrics](http://en.wikipedia.org/wiki/Quadric) for a complete definition of these surfaces.

**Types of Quadrics**
  * **Ellipse (Circle)**

These are circles whose X and Y radii are specified independently of each other. Ellipses are stored as primitives rather than as polygons, NURBS , or Bézier curves. They contain their own set of parameters: centre xyz, x-radius, y-radius, and a 3×3 rotation matrix which determines which direction the primitive faces. If both radii are equal, the ellipse is known as a circle.
  * **Ellipsoid (Sphere)**

Ellipsoids are the three-dimensional analogue of an ellipse. They are defined by the parameters centre xyz, x-radius, y-radius, z-radius, and a 3×3 rotation matrix which determines the orientation of the ellipsoid. The ellipsoid is known as a sphere if all three radii are equal.
  * **Tube (Cylinder)**

Tubes are primitive types which resemble cylinders, with the exception that the upper and lower diameter can be changed independently of each other. They also have the ability to have "Caps" - coverings over their end surfaces. Tubes are defined by a centre xyz, a top radius, a bottom radius, a height, and a 3×3 rotation matrix which determines the orientation of the tube. Tubes degenerate into cones if one of the radii is zero.

##  Metaballs

Metaballs can be thought of as force fields whose surface is an implicit function defined at any point where the density of the force field equals a certain threshold. This field can currently be specified as an elliptical or super-quadric shape around a point. When two metaballs overlap in space, their field effects are added together.

See also [Metaball SOP](https://docs.derivative.ca/Metaball_SOP "Metaball SOP")

The field is specified by a weight and a kernel function. The kernel function results in a value of 0 at the outside edge of the metaball and a value of 1 at the center. The kernel function is scaled by the weight to shift the location of the surface closer or further away from the center.

Because the density of the force field can be increased by the proximity of other metaball force fields, metaballs have the unique property that they change their shape to adapt and fuse with surrounding metaballs. This makes them very effective for modeling organic surfaces.

For example, below we have a metaball. The surface of the metaball exists whenever the density of the metaball's field reaches a certain threshold:
[![MetaExample1.jpg](https://docs.derivative.ca/images/9/92/MetaExample1.jpg)](https://docs.derivative.ca/File:MetaExample1.jpg)
When two or more metaball force fields are combined, as in the illustration below, the resulting density of the force fields is added, and the surface extends to include that area where the force fields intersect and create density values with a value of one.

Metaballs are defined by the parameters **Center x/y/z** , **Radius x/y/z** , **Exponent x/y/z** , and a 3×3 rotation matrix which determines the orientation. A metaball is known as a super-quadratic if either exponent is not equal to one.
[![MetaExample2.jpg](https://docs.derivative.ca/images/8/80/MetaExample2.jpg)](https://docs.derivative.ca/File:MetaExample2.jpg)
You can see a metaball's sphere of influence by turning on **Display Hulls** in a [Geometry Viewer](https://docs.derivative.ca/Geometry_Viewer "Geometry Viewer")'s options dialog.

In the SOP editor, a metaball can be selected only by its hull.

##  Pusher Metaballs

It is possible for metaballs to have negative Weights (_Pusher_ Metaballs). This allows holes to be created by effectively subtracting from the surface.

##  What does an Exponent do?

In the instance of metaballs, the XY and Z exponent determines the inflation towards "squarishness" or contraction towards "starishness" as described below:
  * Value > 1 - Results in metaballs that appear more like a "star".
  * Value < 1 - Results in metaballs that appear more "squarish".
  * Value = 1 - Results in metaballs that appear spherical.

In Touch, metaballs are often used as force fields for particle systems. You can create metaballs with a [Metaball SOP](https://docs.derivative.ca/Metaball_SOP "Metaball SOP"), or in the SOP editor.

##  Metaball Model Types

  * **Blinn Kernal** - Always puts a sphere at the blob centre, even if the weight is less than 1.0. The Blinn model is the fastest and most stable of all the models.

[![BlinnMetaball.jpg](https://docs.derivative.ca/images/b/b4/BlinnMetaball.jpg)](https://docs.derivative.ca/File:BlinnMetaball.jpg)

  * **Wyvill and Elendt Kernals** - These models are very similar; only the weight distribution function is different.

[![WyvillMetaball.jpg](https://docs.derivative.ca/images/3/3a/WyvillMetaball.jpg)](https://docs.derivative.ca/File:WyvillMetaball.jpg) [![ElendtMetaball.jpg](https://docs.derivative.ca/images/0/01/ElendtMetaball.jpg)](https://docs.derivative.ca/File:ElendtMetaball.jpg)

  * **Links Kernal** - This is the slowest method, but provides a good compromise between the Blinn and Wyvill methods in terms of weight distribution.

[![LinksMetaball.jpg](https://docs.derivative.ca/images/7/71/LinksMetaball.jpg)](https://docs.derivative.ca/File:LinksMetaball.jpg)
A surface type in [SOPs](https://docs.derivative.ca/SOP "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](https://docs.derivative.ca/Point "Point") and Primitives are part of the [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), which is a part of a [SOP](https://docs.derivative.ca/SOP "SOP").

A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.
