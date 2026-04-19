---
url: https://docs.derivative.ca/Alembic
category: Interoperability
title: Alembic
---

# Alembic

"Alembic is an open computer graphics interchange framework. Alembic distills complex, animated scenes into a non-procedural, application-independent set of baked geometric results. This 'distillation' of scenes into baked geometry is exactly analogous to the distillation of lighting and rendering scenes into rendered image data.

Alembic is focused on efficiently storing the computed results of complex procedural geometric constructions. It is very specifically NOT concerned with storing the complex dependency graph of procedural tools used to create the computed results. For example, Alembic will efficiently store the animated vertex positions and animated transforms that result from an arbitrarily complex animation and simulation process which could involve enveloping, corrective shapes, volume-preserving simulations, cloth and flesh simulations, and so on. Alembic will not attempt to store a representation of the network of computations (rigs, basically) which are required to produce the final, animated vertex positions and animated transforms." [[1]](https://docs.derivative.ca/Alembic#cite_note-1)

The conversion between the Alembic geometries scopes to the TouchDesigner attributes types are shown in the table below:
---
**Alembic Scope** |  **TouchDesigner Attribute**
Varying, Vertex |  Point
Facevarying |  Vertex
Uniform, Constant |  Primitive

##  Alembic Importing

Alembic files can be brought into TouchDesigner through the [Alembic In POP](https://docs.derivative.ca/Alembic_In_POP "Alembic In POP") and [Alembic SOP](https://docs.derivative.ca/Alembic_SOP "Alembic SOP")). The supported Alembic primitives are polymesh, curves, and points for geometry. As well, Alembic transformations are supported.

Polymesh primitives are imported as triangles or quads for faces of 3 or 4 vertices respectively, and as a close lined strip for faces with greater than 4 vertices.

An Alembic archive may contain one or more object paths for one or multiple geometries. It is possible to view these objects all at once or select them separately using the 'Object Path' parameter menu. If separate selected objects contain duplicate attributes (ie. sharing a name) but associated with a different attribute class (eg. vertex vs. point), then the duplicate attribute will be converted to a vertex attribute.

Each object in an Alembic file schema may possess standard or custom attributes. The standard attributes are normal (`N`), velocity (`V`), and texture coordinates (`Tex`). Multiple custom attributes may live in an Alembic schema with more flexible names and types. Most Alembic attributes are supported but not all convert one-to-one into a POP format:
  * 16-bit int attributes (eg. Int16, V2s, P3s, etc.) are converted to 32-bit int.
  * 64-bit attributes (eg. Uint64, Int64, V2d, etc.) are converted to double, which is the only 64-bit attribute that POPs currently support.
  * Attributes with > 4 components (eg. Box3f, M33f, M44f etc.) are packed as an array of vec4's. If there is an array of these attributes then they will be packed together back-to-back. Eg. M44f has 16 components and will be imported as float4[4], and M44f[2] will be imported as float4[8] with M44f[0] first followed by M44f[1].

List of **unsupported** attributes:
  * String/WString
  * 8-bit and 16-bit float color
  * Bool
  * UChar/Char

##  Alembic Exporting

Alembic files can be exported using the , and output to Alembic files through the [Alembic Out POP](https://docs.derivative.ca/Alembic_Out_POP "Alembic Out POP").

Currently only single-object Alembic files are supported. When the exported POP only contains Point primitives it will be exported as a single Points Alembic object. All of other face primitives (triangles and quads) will be exported into a PolyMesh object. File Out POP does not support exporting line strips or curves yet.

###  Attributes

The File Out POP supports writing multiple different attribute types. Of these there are two types, built-in and custom.

Built-in attributes include `Color`, `N`, and Texture Coordinates (by default `Tex`, however can be specified with the Tex Coord Attribute parameter). These attributes will be automatically written if they exist.

Custom attributes can be specified on the Inputs page of the [Alembic Out POP](https://docs.derivative.ca/Alembic_Out_POP "Alembic Out POP") and support the following types
  * `int`, `uint`, `float`, `double`
  * `int2`, `float2`, `double2`
  * `int3`, `float3`, `double3`
  * Array attributes of the previous types such as `float3[15]`

Additionally attributes with two or more components can be written as a Point or Vector attribute.

For POPs with only point primitives only point attributes can be written. For POPs with face primitives, point, vertex, and primtive attributes can be exported.

For animated point clouds, two additional Attributes can be specified, the Ids Attribute and the Velocity Attribute. For POPs created with the [Particle POP](https://docs.derivative.ca/Particle_POP "Particle POP") these would be `PartId` and `PartVel` respectively.
  1. [↑](#cite_ref-1) Alembic Introduction [[[1]](https://www.alembic.io/)]

A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

Attributes make up the numeric data blocks of [POPs](https://docs.derivative.ca/POP "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](https://docs.derivative.ca/Primitive "Primitive") is defined by a vertex list, which is list of point numbers.

A surface type in [POPs](https://docs.derivative.ca/POP "POP") and [SOPs](https://docs.derivative.ca/SOP "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](https://docs.derivative.ca/Point "Point") and Primitives are part of the [Geometry Detail](https://docs.derivative.ca/Geometry_Detail "Geometry Detail"), which is a part of a [SOP](https://docs.derivative.ca/SOP "SOP").

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](https://docs.derivative.ca/Root "Root"). This path is displayed at the top of every [Pane](https://docs.derivative.ca/Pane "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](https://docs.derivative.ca/Folder "Folder").

POPs (Point Operators) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
