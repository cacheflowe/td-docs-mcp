---
url: https://docs.derivative.ca/Attribute
category: Glossary
title: Attribute
---

# Attribute

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a **Point List** which includes the `P` Position attribute, a **Primitive List** and a **Vertex List**. Each of these lists are made of any number of attributes. Each attribute is given a name.

Position (`P`) is the standard point attribute, and built-in optional attributes include [normals](Normals.md "Normals") (`N`), texture coordinates (`Tex`), color (`Color`), etc. A `Color` primitive attibute enables each primitive to have a separate color. A `N` vertex normal attibute enables each vertex to have a separate surface normal vector.

A POP's point list has a length _numPoints_ which is the length of all point attributes, similar for Primitive and Vertex lists.

A **point attribute** can be a **scalar point attribute** which is a single number for each point, or a **vector point attribute** which is 2, 3 or 4 numbers per point, such as the `P` (X Y Z position) attribute which is a **float3** (3-numbers) vector attribute.

A **primitive attribute** is a list of _numPrimitives_ single scalar numbers or 2- 3- or 4-value vectors.

A **vertex attribute** is a list of _numVertives_ scalar numbers or vectors for the total vertices of all primitives of a POP.

Each attribute is a separately-allocated list of numbers, so that when one attribute is created or deleted, nothing else is touched.

See **Attribute Data Types** below. In addition attributes can have a **Qualifier** , such as a float4 being a Color, or a float3 being an XYZ direction, or a float4 being a rotation quaternion.

_For attributes of SOPs see[SOP Attribute](https://docs.derivative.ca/SOP_Attribute "SOP Attribute") as this page is focused on POPs._

###  Attribute Terminolgy

  * **Built-in Attributes** - Attributes that are strictly reserved, like `P`, `PointScale`, `N` and `Tex`.
  * **Common Attributes** - Attributes that are commonly used but not strictly controlled by TouchDesigner, like `PartMass` and `PartVel`.
  * **Read-Only Attributes** - attributes that are pre-computed by TouchDesigner (like normalized point number `_PointU`) that can be used in Math POP. Math Mix, Math Combine POPs and others.
  * **Components of Attributes** - For attributes that are vectors, a flaot3 has 3 "components", and referred to as `P(1)` or `P.y` or `P.i2` (see Swizzling)
  * **Attribute Class** - refers to Point, Primitive and Vertex classes of POP data.
  * **[Array Attribute](Array_Attribute.md "Array Attribute")** - an attribute type that has per-point multiple float or float2 etc
  * Scalar Attribute vs Vector Attribute - single-component, multi-component.

##  Common Attributes

###  Normals (N)[")]

See [Normals](Normals.md "Normals"). A normal is a directional vector associated with a particular geometric entity, commonly perpendicular to it. The normal to a surface at a given point is a vector perpendicular to the surface at that point, and is computed as the cross product of the tangent vectors at that point.

###  Color (Color)[")]

Surface color and alpha specified by RGBA. Values range from 0 to 1. The alpha component `Color.a` controls the transparency of a given element, where 1 is fully opaque, and 0 is fully transparent.

###  Texture Coordinates (Tex)[")]

Items are located spatially by XYZ values. To differentiate texture coordinate space from XYZ space, the labels U and V and sometimes W are used instead of X and Y and Z. ​ In order to place texture maps (images) onto geometry, we must assign texture coordinates to the geometry. A texture map resides in its own (U, V) texture coordinate space. When assigned to the geometry, the (U, V) coordinates determine how to map the image onto the geometry, where U,V of 0,0 uses the bottom left of the texture image, and 1,1 use the top-right. ​ Most generator POPs like [Sphere POP](../POPs/Sphere_POP.md "Sphere POP") and [Plane POP](../POPs/Plane_POP.md "Plane POP") have texture coordinates already assigned to each point or vertex. ​ Texture coordinates can be visualized in the following manner: Texture maps have their own coordinate space. If the texture were a table cloth with a grid pattern, the color at location 3, 4 on the table cloth remains at location 3, 4 even when the cloth is wrapped around an irregularly shaped object. The color at location 3, 4 can be said to be in the table-cloth's coordinate space. ​

##  Order of Attribute Precedence

The order of precedence for attributes from highest to lowest is:
  1. Vertex Attributes
  2. Point Attributes
  3. Primitive Attributes

Attributes with a higher order of precedence override the same attributes with a lower order of precedence. (Only the [Bone Group SOP](../SOPs/Bone_Group_SOP.md "Bone Group SOP") has Detail attributes from skeletons imported externally.)

Point and vertex attributes are interpolated across primitives, allowing more local flexibility than primitive attributes (e.g. `Color`). Vertex attributes deal with the situation where shared points need different values for the attributes at the boundary of primitives, like the longitudinal seam of a polar texture map for example. Primitive colors typically take us less memory point colors, and point colors less than vertex colors.

##  Custom Attributes

Below are the Attributes which are currently reserved for TouchDesigner use.

##  Point Attributes

Point Attributes are Attributes on [Points](Point.md "Point") in a [POP](../POPs/POP.md "POP").
Name  | Type  | Size  | Description  |  SOP to Create  |  SOP where Used  | Notes
---|---|---|---|---|---|---
`P` | float  | 3  | Point position  |  |  |
`Weight` | float  | 1  | Point weight  |  |  |
`N` | vector  | 3  | Surface Normal  |  |  [Normal POP](../POPs/Normal_POP.md "Normal POP"), [Facet POP](../POPs/Facet_POP.md "Facet POP") |
`Tex` | float  | 3  | Texture Coordinates  |  |  [Texture Map POP](../POPs/Texture_Map_POP.md "Texture Map POP") |
`Color (Color.rgb and Color.a)` | float  | 4  | Surface color and alpha  |  |  |
`PartVel` | vector  | 3  | Particle Velocity  |  |  |
`PartMass` | float  | 1  | particle mass  |  |  [Particle POP](../POPs/Particle_POP.md "Particle POP"), [Force Radial POP](../POPs/Force_Radial_POP.md "Force Radial POP") |
`PartDrag` | float  | 1  | Drag  |  |  [Particle POP](../POPs/Particle_POP.md "Particle POP"), [Force Radial POP](../POPs/Force_Radial_POP.md "Force Radial POP") |
`PartLife` | float  | 1  | Life Expectancy  |  |  [Particle POP](../POPs/Particle_POP.md "Particle POP") |
`PartAge` | float  | 1  | Age  |  |  [Particle POP](../POPs/Particle_POP.md "Particle POP") |
`PartId` | float  | 1  | Particle Identifying Tag |  |  [Particle POP](../POPs/Particle_POP.md "Particle POP") |
`PartInitP` | vector  | 3  | Rest Position  |  |  |
`PointScale` | float  | 1  | Scale of point for rendering  |  |  |

##  Vertex Attributes

A Triangle, Quadrelateral or Line Strip is made of a set of [Vertices](Vertex.md "Vertex"), and each Vertex refers to a [Point](Point.md "Point").
Name  | Type  | Size  | Description  |  SOP to Create  |  SOP where Used  | Notes
---|---|---|---|---|---|---
`N` | vector  | 3  | Surface normal  |  [Facet SOP](../SOPs/Facet_SOP.md "Facet SOP"), [Attribute Create SOP](../SOPs/Attribute_Create_SOP.md "Attribute Create SOP") |  |
`uv` | float  | 3  | Texture coordinates  |  [Texture SOP](../SOPs/Texture_SOP.md "Texture SOP") |  |
`Cd` | float  | 4  | Surface color and alpha  |  |  |
`creaseweight` | float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](../SOPs/Subdivide_SOP.md "Subdivide SOP").
`T` | float  | 4  | Tangents  |  [Attribute Create SOP](../SOPs/Attribute_Create_SOP.md "Attribute Create SOP") |  | two 2D vectors = 4 values
`pCapt` | float  | 2  | Capture data  |  |  | contains index and weight for a transform. See [Deforming Geometry (Skinning)](https://docs.derivative.ca/Deforming_Geometry_\(Skinning\) "Deforming Geometry \(Skinning\)")

##  Primitive Attributes

You can use the [Primitive SOP](../SOPs/Primitive_SOP.md "Primitive SOP") or the [SOP to DAT](SOP_to_DAT.md "SOP to DAT") and [DAT to SOP](../SOPs/DAT_to_SOP.md "DAT to SOP") pair to add or modify primitive attributes.
Name  | Type  | Size  | Description  |  SOP to Create  |  SOP where Used  | Notes
---|---|---|---|---|---|---
`N` | vector  | 3  | Surface normal  |  |  |
`Cd` | float  | 4  | Surface color and alpha  |  |  |
`creaseweight` | float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](../SOPs/Subdivide_SOP.md "Subdivide SOP").
`mat` | index  | 1  |  Material |  [Material SOP](../SOPs/Material_SOP.md "Material SOP") |  |
plus Force dir, fedge, fvortex, fspiral xxx

##  Attribute Data Types

There are three different attribute data types. Each is handled slightly differently internally.
Vector Data  | This data type represents a 3D vector in space. When any transforms occur on the detail, this attribute will also be transformed. Examples of a vector attribute are normals (N) or velocity (PartVel).
---|---
Floating Point Data  | This data type represents an array of floating point values. The values are not transformed when the geometry gets transformed. Some examples of this type of attribute are diffuse colors (Cd), and texture co-ordinates (Tex).
A surface type in [POPs](../POPs/POP.md "POP") and [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](Point.md "Point") and Primitives are part of the [Geometry Detail](Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").

A sequence of vertices form a [Polygon](Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](Point_List.md "Point List"), and each [Point](Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

POPs (Point Operators) is a new [Operator Family](Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

Each operator can have a set of text strings that are its "tags". You can set them and search for them within TouchDesigner.

MATs or Materials are an [Operator Family](Operator_Family.md "Operator Family") that applies a [Shader](Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.
