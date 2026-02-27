---
url: https://docs.derivative.ca/Attribute
category: Glossary
title: Attribute
---

# Attribute

Attributes are data associated with [POP](https://docs.derivative.ca/POP "POP") (or [SOP](https://docs.derivative.ca/SOP "SOP")) geometry. [Points](https://docs.derivative.ca/Point "Point"), [Vertex (Vertices)s](https://docs.derivative.ca/Vertex "Vertex") and [Primitives](https://docs.derivative.ca/Primitive "Primitive") (polygons, lines, etc) can have any number of attributes. In POPs, position (`P`) is standard, and built-in optional attributes are [normals](https://docs.derivative.ca/Normals "Normals") (`N`), texture coordinates (`Tex`), color (`Color`), etc.
_For attributes of SOPs see[SOP Attribute](https://docs.derivative.ca/SOP_Attribute "SOP Attribute") as this page is being re-focused on POPs (in-progress)._
A **point attribute** is a named set of numbers, one for each point of a POP. A **scalar point attribute** is a single number for each point. A **vector point attribute** is 2, 3 or 4 numbers per point, such as the `P` (position) attribute which is a float3 (3-number) vector attribute.
A **primitive attribute** is a named set of numbers, one for each primitive of a POP. A **scalar primitive attribute** is a single number for each primitive. A **vector primitive attribute** is 2, 3 or 4 numbers per primitive.
A **vertex attribute** is a named set of numbers, one for each vertex of each primitive of a POP. A **scalar vertex attribute** is a single number for each vertex. A **vector vertex attribute** is 2, 3 or 4 numbers per vertex.

###  Attribute Terminolgy
  * Built-in Attributes - Attributes that are strictly reserved, like `P`, `PointScale`, `N` and `Tex`.
  * Common Attributes - Attributes that are commonly used but not strictly controlled by TouchDesigner, like `PartMass` and `PartVel`.
  * Read-Only Attributes - attributes that are pre-computed by TouchDesigner (like normalized point number `_PointU`) that can be used in Math POP. Math Mix, Math Combine POPs and others.
  * Components of Attributes - For attributes that are vectors, a flaot3 has 3 "components".
  * Attribute Class - refers to Point, Vertex and Primitive classes.
  * Array Attribute - an attribute type that has per-point multiple float or float2 etc
  * Scalar Attribute vs Vector Attribute

##  Common Attributes
###  Normals (N)[")]
See [Normals](https://docs.derivative.ca/Normals "Normals"). A normal is a directional vector associated with a particular geometric entity, commonly perpendicular to it. The normal to a surface at a given point is a vector perpendicular to the surface at that point, and is computed as the cross product of the tangent vectors at that point.
###  Color (Color)[")]
Surface color and alpha specified by RGBA. Values range from 0 to 1. The alpha component `Color.a` controls the transparency of a given element, where 1 is fully opaque, and 0 is fully transparent.
###  Texture Coordinates (Tex)[")]
Items are located spatially by XYZ values. To differentiate texture coordinate space from XYZ space, the labels U and V and sometimes W are used instead of X and Y and Z. ​ In order to place texture maps (images) onto geometry, we must assign texture coordinates to the geometry. A texture map resides in its own (U, V) texture coordinate space. When assigned to the geometry, the (U, V) coordinates determine how to map the image onto the geometry, where U,V of 0,0 uses the bottom left of the texture image, and 1,1 use the top-right. ​ Most generator POPs like [Sphere POP](https://docs.derivative.ca/Sphere_POP "Sphere POP") and [Plane POP](https://docs.derivative.ca/Plane_POP "Plane POP") have texture coordinates already assigned to each point or vertex. ​ Texture coordinates can be visualized in the following manner: Texture maps have their own coordinate space. If the texture were a table cloth with a grid pattern, the color at location 3, 4 on the table cloth remains at location 3, 4 even when the cloth is wrapped around an irregularly shaped object. The color at location 3, 4 can be said to be in the table-cloth's coordinate space. ​
##  Order of Attribute Precedence
The order of precedence for attributes from highest to lowest is:
  1. Vertex Attributes
  2. Point Attributes
  3. Primitive Attributes

Attributes with a higher order of precedence override the same attributes with a lower order of precedence. (Only the [Bone Group SOP](https://docs.derivative.ca/Bone_Group_SOP "Bone Group SOP") has Detail attributes from skeletons imported externally.)
Point and vertex attributes are interpolated across primitives, allowing more local flexibility than primitive attributes (e.g. `Color`). Vertex attributes deal with the situation where shared points need different values for the attributes at the boundary of primitives, like the longitudinal seam of a polar texture map for example. Primitive colors typically take us less memory point colors, and point colors less than vertex colors.
##  Custom Attributes
Below are the Attributes which are currently reserved for TouchDesigner use.


##  Point Attributes
Point Attributes are Attributes on [Points](https://docs.derivative.ca/Point "Point") in a [POP](https://docs.derivative.ca/POP "POP").
Name  | Type  | Size  | Description  |  SOP to Create  |  SOP where Used  | Notes
---|---|---|---|---|---|---
`P` | float  | 3  | Point position  |  |  |
`Weight` | float  | 1  | Point weight  |  |  |
`N` | vector  | 3  | Surface Normal  |  |  [Normal POP](https://docs.derivative.ca/Normal_POP "Normal POP"), [Facet POP](https://docs.derivative.ca/Facet_POP "Facet POP") |
`Tex` | float  | 3  | Texture Coordinates  |  |  [Texture Map POP](https://docs.derivative.ca/Texture_Map_POP "Texture Map POP") |
`Color (Color.rgb and Color.a)` | float  | 4  | Surface color and alpha  |  |  |
`PartVel` | vector  | 3  | Particle Velocity  |  |  |
`PartMass` | float  | 1  | particle mass  |  |  [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP"), [Force Radial POP](https://docs.derivative.ca/Force_Radial_POP "Force Radial POP") |
`PartDrag` | float  | 1  | Drag  |  |  [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP"), [Force Radial POP](https://docs.derivative.ca/Force_Radial_POP "Force Radial POP") |
`PartLife` | float  | 1  | Life Expectancy  |  |  [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP") |
`PartAge` | float  | 1  | Age  |  |  [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP") |
`PartId` | float  | 1  | Particle Identifying Tag |  |  [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP") |
`PartInitP` | vector  | 3  | Rest Position  |  |  |
`PointScale` | float  | 1  | Scale of point for rendering  |  |  |
##  Vertex Attributes
A Triangle, Quadrelateral or Line Strip is made of a set of [Vertices](https://docs.derivative.ca/Vertex "Vertex"), and each Vertex refers to a [Point](https://docs.derivative.ca/Point "Point").
Name  | Type  | Size  | Description  |  SOP to Create  |  SOP where Used  | Notes
---|---|---|---|---|---|---
`N` | vector  | 3  | Surface normal  |  [Facet SOP](https://docs.derivative.ca/Facet_SOP "Facet SOP"), [Attribute Create SOP](https://docs.derivative.ca/Attribute_Create_SOP "Attribute Create SOP") |  |
`uv` | float  | 3  | Texture coordinates  |  [Texture SOP](https://docs.derivative.ca/Texture_SOP "Texture SOP") |  |
`Cd` | float  | 4  | Surface color and alpha  |  |  |
`creaseweight` | float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](https://docs.derivative.ca/Subdivide_SOP "Subdivide SOP").
`T` | float  | 4  | Tangents  |  [Attribute Create SOP](https://docs.derivative.ca/Attribute_Create_SOP "Attribute Create SOP") |  | two 2D vectors = 4 values
`pCapt` | float  | 2  | Capture data  |  |  | contains index and weight for a transform. See [Deforming Geometry (Skinning)](https://docs.derivative.ca/Deforming_Geometry_\(Skinning\) "Deforming Geometry \(Skinning\)")
##  Primitive Attributes
You can use the [Primitive SOP](https://docs.derivative.ca/Primitive_SOP "Primitive SOP") or the [SOP to DAT](https://docs.derivative.ca/SOP_to_DAT "SOP to DAT") and [DAT to SOP](https://docs.derivative.ca/DAT_to_SOP "DAT to SOP") pair to add or modify primitive attributes.
Name  | Type  | Size  | Description  |  SOP to Create  |  SOP where Used  | Notes
---|---|---|---|---|---|---
`N` | vector  | 3  | Surface normal  |  |  |
`Cd` | float  | 4  | Surface color and alpha  |  |  |
`creaseweight` | float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](https://docs.derivative.ca/Subdivide_SOP "Subdivide SOP").
`mat` | index  | 1  |  Material |  [Material SOP](https://docs.derivative.ca/Material_SOP "Material SOP") |  |
plus Force dir, fedge, fvortex, fspiral xxx


##  Data Types of Attributes
There are three different attribute data types. Each is handled slightly differently internally.
Vector Data  | This data type represents a 3D vector in space. When any transforms occur on the detail, this attribute will also be transformed. Examples of a vector attribute are normals (N) or velocity (PartVel).
---|---
Floating Point Data  | This data type represents an array of floating point values. The values are not transformed when the geometry gets transformed. Some examples of this type of attribute are diffuse colors (Cd), and texture co-ordinates (Tex).
Attributes are data associated with [POP](https://docs.derivative.ca/POP "POP") geometry. [Points](https://docs.derivative.ca/Point "Point"), [Vertex (Vertices)](https://docs.derivative.ca/Vertex "Vertex") and [Primitives](https://docs.derivative.ca/Primitive "Primitive") (polygons, lines, etc) can have any number of attributes.
POPs (**Point Operators**) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](https://docs.derivative.ca/Primitive "Primitive") is defined by a vertex list, which is list of point numbers.
A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.
A surface type in [SOPs](https://docs.derivative.ca/SOP "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](https://docs.derivative.ca/Point "Point") and Primitives are part of the [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), which is a part of a [SOP](https://docs.derivative.ca/SOP "SOP").
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
Each operator can have a set of text strings that are its "tags". You can set them and search for them within TouchDesigner.
MATs or Materials are an [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that applies a [Shader](https://docs.derivative.ca/Shader "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.
