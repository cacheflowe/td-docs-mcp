---
url: https://docs.derivative.ca/Learning_About_POPs
category: Glossary
title: Learning_About_POPs
---

# Learning About POPs

The [OP Snippets](../Learn/OP_Snippets.md "OP Snippets") for POPs have examples for "**POP CONCEPTS** ", plus snippets for every POP.

For more live examples, download the [POPs Examples Package](https://www.dropbox.com/scl/fo/dvvqnl61dgmicxoebl4sy/AFuNixO4WWcAbyM5KkUi9F4?rlkey=f152v4uuzou81c7477w1yf6im&st=zzro8oie&dl=0) and start with `Overview.toe` or Darien Brito's POP Guide.

▸What are Point Operators

POPs (**Point Operators**) is a new [Operator Family](Operator_Family.md "Operator Family") of TouchDesigner for creating and modifying 3D geometry data that runs on accelerated GPU graphics cards or chips.

The "P" in "POPs" refers to “points” but co-incidentally it envelops other P’s - primitives, polygons, particle systems, point clouds and any form of data points for data visualizations.

The data for POPs all starts as  _points with attributes_ , and from points we can work with particle systems, point clouds, polygons, lines, spline curves, and any 3D geometrical shape and form of data points.

POPs are rendered by the [Render TOP](../TOPs/Render_TOP.md "Render TOP") or can be passed to devices like DMX lighting systems, LED arrays, lasers or other external systems.

Most simply, a POP is made of a points list, a vertex list, and a primitive list.

### Points

Every POP contains a list of points which is made of a set of Point Attributes. The most common attribute is Position (`P`), the XYZ position in 3D space of the points. The POP may have other attributes like Color (`Color`) (always with a red, green, blue and alpha component) and Normal (`N`) which is a direction vector (with 3 components). The points can also have extra user-defined attributes, or attributes that are automatically-generated from certain POP operators.

Points are part of the building blocks of polygons, lines, line strips, spline curves, point clouds, particle systems, any 3D geometrical shape and any form of data points.

### Primitives

Every POP contains a set of “primitives”, also with a set of Primitive Attributes. The types of primitives are:
  * **Point** (1 point)
  * **Line** (2-points)
  * **Line Strip** (1 or more points)
  * **Triangle** (3 points)
  * **Quad** (4 points)

Primitives can have attributes, for example `Color` which is applied to the entire primitive.

### Vertices

Each primitive has a list of vertices. A vertex is an index into the points list. So a quad primitive is 4 vertices which is a set of 4 indices of points in the point list. If a quad primitive has vertices with index 6, 7, 8, 9 then it refers to the 7th 8th 9th and 10th points, Vertices can also have attributes.

### POP History

_POPs are a replacement and re-think of TouchDesigner's historically first operator family,**SOPs** (1989), with many new features and benefits. Like SOPs, POPs are a procedural family of operators that create and affect points, and primitives like triangles, quads and lines. POPs implements point clouds and particles, and it imports FBX, obj , Alembic files and more._

See the section at the end of this page titled "**SOPs vs POPs** " for a deeper comparison of two two.

### POPs are rendered with Geometry Components

POPs are placed in Geometry COMPs to get rendered with the [Render TOP](../TOPs/Render_TOP.md "Render TOP"). Materials (MATs) are applied to the Geometry COMPs (as with SOPs) and use POP attributes. The Geometry COMPs are passed to a Render TOP.

3D operators running on the GPU gives us:
- Speed due to high GPU parallelism. - Less memory: POPs are highly memory-optimized as only the attributes that change get created in any POP.

### POPs implements many features of CHOPs

it is not necessary to convert POPs to CHOPs (which causes GPU to CPU to GPU copies) to do math/logic/mixing operations on 3D data and attributes. By keeping the data and the process on the GPU is it faster and uses less memory.

### Generator and Filter Operators

Like the other TouchDesigner families of operators, POPs include "generator" operators that create new shapes or import them from files or other systems, plus "filter" operators that modify the data coming from other POPs and may generate complex shapes and data from simpler inputs.

**original intro video:** <https://forum.derivative.ca/t/intro-to-pops-video-from-iihq/519824>

▸Some POP Features and Concepts
  * **Creating New Attributes** - Some POPs allow for easy creation of new attributes simply by naming a new attribute in the Output Scope parameter. TouchDesigner will auto-choose a size and type of attribute. (in [Math POP](../POPs/Math_POP.md "Math POP"), [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP"), [Limit POP](../POPs/Limit_POP.md "Limit POP") and numerous others)
  * **Math with no Coding** - Several POPs like [Transform POP](../POPs/Transform_POP.md "Transform POP"), [Math POP](../POPs/Math_POP.md "Math POP"), [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") and [Normalize POP](../POPs/Normalize_POP.md "Normalize POP") give fundamental manipulation capabilities without a need for coding. Generally POPs eliminate a lot of the need for coding.

Setting Attribute type and Size - Where you see >>> it lets you specify attribute type and size.
  * **Attributes Feeding Rendering** - POPs is better-tied to rendering as attributes are more extensive and controllable. Like glowing lines are a combination of geo and shading. In some cases hidden POPs generate the polys to render glow or lines.
  * **Compute Shaders** is the programming language within POPs. You can write custom GPU shaders with the GLSL POP, the GLSL Advanced POP, which have numerous helper functions and pre-built examples. [You can also write custom C++ POP operators](../POPs/CPlusPlus_POP.md "CPlusPlus POP") which lets you set up code on the CPU side.
  * **Multi- Component Attributes** - An attribute can be one number per point, but also can have 2, 3 or 4 components, such as float4 `Color`: it has multiple "components" `Color(0)`, `Color(1)`, `Color(2)` and `Color(3)`. On top of that, "arrays" are for example multiple float3 in one attribute, which you can create in an [Attribute POP](../POPs/Attribute_POP.md "Attribute POP").
  * **Attribute Component Swizzling** - `Color(0)`, `Color(1)`, `Color(2)` and `Color(3)` cam be written as `Color.rgba`. `P(1)` can be written as `P.y`.
  * **Single- Component menus** - where a single component of an attribute needs to be specified, (like for an index) there is single-component menu that is used in many POPa, which lets you choose one from all the POP's attributes' components.
  * **Multi-columns of Parameters** (the Parameter Size parameter): Most POPs give one set of parameters that apply to all components of a vector. You will see “Parameter Size” on some POPs that give you 1, 2, 3, or 4 sets of parameters, which then give you one parameter set for each component. For example, on a ReRange POP this enables you to apply a different re-range for each of the X Y ad Z components of a position (which in CHOPs required three CHOPs).
  * **Memory Reduction via References** - Each POP only allocates memory for attributes that it is modifying or creating anew. If it is not modifying Position, for example, it will use the Position from a POP that is flowing into the POP. This saves a lot of memory. Tip: At the bottom left corner of the POPs viewers it shows which attributes it has created/modified in that POP, The rest of the attributes are being passed through untouched from POPs upstream (called “POP attribute references”).

Also, the middle-click info popup on a node shows the attribute names, and if they are followed by an `(r)` it is a reference to memory in another node.

**Line Strips** are **primitives** (like triangles, quads etc) made of multi-points, and can be created via most generator POPs, the [Line POP](../POPs/Line_POP.md "Line POP") or the [Primitive POP](../POPs/Primitive_POP.md "Primitive POP").
  *     * Line Strips can also be created from any point list that has a `LineBreak` attribute, which in the [Line Break POP](../POPs/Line_Break_POP.md "Line Break POP") takes the point list in its order, and splits it into line strip primitives based on `0` or `1` in the `LineBreak` attribute, or integers in a `LineStripIndex` attribute.
  * **High Precision** - User-defined attributes can be single or double precision floats, also 32-bit or 64-bit integers.
  * **GLSL POPs** - Some POPs let you code in GLSL-style compute shaders.
  * **Weights** - Several POPs generate 0-1 value weights per-point, and others use those weights to blend between two states, like the Transform POP which can partially transform each point.
  * **Dimensions** - [Dimension](Dimension.md "Dimension") - a higher-order organization of the list of points in a POP.
  * **Parameters driven per-point by Attributes** - [Transform POP](../POPs/Transform_POP.md "Transform POP") and [Noise POP](../POPs/Noise_POP.md "Noise POP") have some pars driven by their [Map page](Mapping_POP_Attributes_to_Parameters.md "Mapping POP Attributes to Parameters").
  * **Multi-POP Inputs with Sequential Blocks** - The POPs that allow unlimited inputs, like Merge, Switch, Math Mix, Blend, Attribute Combine etc. share a new flexible way of specifying inputs. You can (1) wire them in one-by one as before, or you can (2) specify multi-inputs like "`box*`" using pattern matching in a parameter. And you can (3) add a sequential block per input, where each block has a POP path parameter. The latter is most flexible as each sequential block can have extra parameters, like for the [Attribute Combine POP](../POPs/Attribute_Combine_POP.md "Attribute Combine POP"), which attributes you want to extract from each input, or for the Merge POP, which groups you want to merge in for each input. For each wired-input, it auto-creates a sequential block. (You can use pattern matching in each sequential block). You can mix wired and unwired inputs if needed.
  * **Sorting** with the [Sort POP](../POPs/Sort_POP.md "Sort POP") is implemented with modern fast sorting algorithms. Sort can be based on any attribute component.
  * **Over-Allocation Caveat of GPUs** : If a POP's number of points, primitives or vertices cannot be determined at the start of cooking, it needs to allocate a max number of thee entities and not use some memory. So they have to sometimes over-allocate. Some POPs have parameters that let you set the max amount of things you expect in the POP.
  * **Class Conversions** - To transfer from the "class" Point Attributes to/from Vertex Attributes to/from Primitive Attributes, use the [Attribute Convert POP](../POPs/Attribute_Convert_POP.md "Attribute Convert POP"). Use the [Convert POP](../POPs/Convert_POP.md "Convert POP") to convert between primitive types.
  * **GPU -resident computing** - You can keep your computing on the GPU and not break the parallelism caused by sending/receiving form the CPU. Since TOPs are GPU-based too, interactions between them are also optimized. POPs are all GPU except when CPU absolutely needed (like loading files).
  * **Line Material** is implemented with an POP underneath and does a conversion into a set of triangles. More aspects of lines are controllable per-point using attributes. More Line MAT features are controlled using POP attributes via the Line MAT’s Attributes page.

▸Primitives

Primitive Types

Primitive types in POPs are:
  * **Point** primitive - has one index into the point list
  * **Line** primitive - a set of two points in the point list
  * **Line Strip** primitive - a set of any number of points in the point list
  * **Triangle** primitive - a set of three points
  * **Quad** - primitive - a set of four points

**Tip** : The [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") shows it all, using its Extract menu set to Primitives, Points, or Vertices

### Line Strips Open or Closed

Line strips can be open or closed. In POPs a line strip is closed if its last vertex’s point index is the same number as the first vertex’s point index.

Points without Primitives (and why points alone don’t render)

You can have a set of points without any primitives. (you can get this with any Generator POP, or with the [Primitive POP](../POPs/Primitive_POP.md "Primitive POP"))

Render Instancing only looks at the point list. [Copy SOP](../SOPs/Copy_SOP.md "Copy SOP") templates don’t care. Many POPs don't care - they go through the points in the point list and mod something and that's it.

But you can’t render (in the [Render TOP](../TOPs/Render_TOP.md "Render TOP") points themselves unless they have a point primitive.

The generators (Circle, Torus, Tube, Point Generator, Box, Rectangle and Sphere) (when Connectivity is set to None, where applicable) can all create points with a corresponding primitive.

The [Primitive POP](../POPs/Primitive_POP.md "Primitive POP") (like the [Add SOP](../SOPs/Add_SOP.md "Add SOP")), can strip off primitives and leave you with no primitives, unless you create them in the Primitives tab.

Order of primitives in POPs - Primitives are re-grouped with this specific order: all Triangles first, then Quads, Line Strips, Lines and Points.

▸Attributes

Standard Reserved Attributes

These are fixed-purpose built-in attributes: Every point has a position, that is called the `P` attribute (actually you can have a POP without a `P` attribute). `P` has 3 components including `P(0)`, `P(1)` and `P(2)` for the X, Y and Z dimensions. `P` is a “float3” attribute type (a “vector attribute”).

(note that any attribute that is a single float, like `PointScale`, is called a scalar attribute.)

Each point can have other optional attributes that are added using various POPs. `N` is for normals and is a 3-float vector attribute (float3). `Color` is the point color and always has 4 components , for red, green, blue and alpha. Often you will see `Color(0) Color(1) Color(2)` for changing the RGB only (or `Color.rgb` in its swizzled form). `Tex` is the texture coordinates for point and is always a 3-float vector attribute, which includes the 3rd dimension of a 3D texture.

You can create and modify color and texture attributes in many general places in POPs, like in [Normalize POP](../POPs/Normalize_POP.md "Normalize POP"), [Math POP](../POPs/Math_POP.md "Math POP"), [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP"), [Pattern POP](../POPs/Pattern_POP.md "Pattern POP"), [Noise POP](../POPs/Noise_POP.md "Noise POP"), [Random POP](../POPs/Random_POP.md "Random POP"), [Projection POP](../POPs/Projection_POP.md "Projection POP"), Lookup*, [Line POP](../POPs/Line_POP.md "Line POP") and more.

### Common Attributes

There are other attribute names that are commonly used in TouchDesigner that you should use as a habit unless there is a reason not to do so. These include `Tan` (tangent), `Pointscale`, `LineWidth`, `Dir`, `Dist`, `Vel`, `Disp, Speed`, `Accel`, `Weight`, `Curv` (curvature), `Index` (general index) `Nebr` (neighbor indexes), `PartForce` (particles)

[Particle POP](../POPs/Particle_POP.md "Particle POP") attributes have a `Part` prefix. [Ray POP](../POPs/Ray_POP.md "Ray POP") attributes have a `Ray` prefix.

Attributes with 1 component - like `Weight` or `PointScale` are called “scalar attributes”.

### Point Attributes, Vertex Attributes or Primitive Attributes

Points have attributes, but primitives and vertices can also have attributes.

**Why would you put attributes on vertices instead of points**? Most often point attributes are desirable and adequate. If `Weight` depends only on a position `P`, a point attribute is fine. But if a point is shared by two or more vertices of two or more primitives, you may want to put a different color or texture coordinate for each vertex.

### Where to create Attributes

You can create attributes with the [Attribute POP](../POPs/Attribute_POP.md "Attribute POP"), but you can create attributes on the fly with most POPs by specifying a new name where you would give the output attribute name. Example: Math POP.

### Attribute Data Types

Attributes can be any name and any size if they are floats. An Attribute can be
  * float (32-bit)
  * double (64-bit double-precision floats)
  * integer (32-bit)
  * uint (unsigned 32 bit integers)

POPs that have counters like Ray, Line Metrics or Neighbor POP create unsigned integer attributes.

Attribute sizes can be:
  * scalar attribute 1-component
  * vector attribute with 2+ component (for example, float2, float3 or float4)
  * matrix attribute - 2x2 up-to 4x4 matrices

### Array Attributes

Separately you can have [Array Attributes](Array_Attribute.md "Array Attribute"), like an array of 5 float elements, for example, represented as `MyArray[0]` to `MyArray[4]`. Or an array of 5 float4, like `ColorScheme[5]` where a component of that may be `ColorScheme[5](2)`.

### Attribute Names

Attribute names can contain only alphabetic characters A-Z lower and upper case. Attribute names will always start with a letter. Standard and Common attributes defined by Derivative are named with the first letter capitalized like `Weight`. User-defined attributes can start with lower or upper case, but to avoid future conflicts and be more recognized as user-defined, it’s recommended you start them with lower case.

### List of Attributes

You can get a list of all point attributes: in python `op('pop1').pointAttributes()` with pattern matching in the (). Or you can look at the middle-click Info popup. Also in each POP node viewer at the bottom left it shows which attributes are added or changed (see below). Check the section Python Members and Functions.
![image.png](attachment:aaa05af9-0d7f-43c5-9714-786150826ad4:fbd1ebff-b43f-4565-8b9e-d4d55c92425f.png)

### POPs without a P Attribute

It is possible to create and manipulate a POP without the `P` attribute - a point can represent any data and not necessarily something with a position. Or on a POP chain, the `P` doesn’t matter. A point without a `P` attribute is given a `P` value of (0, 0, 0) when, for instance you want to display a `P`-less point in 3D. You can strip a `P` off using an [Attribute Combine POP](../POPs/Attribute_Combine_POP.md "Attribute Combine POP"), for example.

▸Creating new Custom Attributes
  * An [Attribute POP](../POPs/Attribute_POP.md "Attribute POP") can be used to create any new attributes on points, vertices or primitives, and initialize it with constant values.
  * But many POPs like Math POP or Limit POP take one attribute in, and you can create any new attribute in which to put the results. By default, the output attribute is the same type as the selected input attribute. But where you Output to an attribute you can specify a new attribute name and type.
  * If the Output Attribute name is in _italics_ , it means it will auto-fill the attribute of that name.
  * POPs like the [Field POP](../POPs/Field_POP.md "Field POP") or [Line Metrics POP](../POPs/Line_Metrics_POP.md "Line Metrics POP") generate new attributes with suggested default names.
  * There are numerous specialized POPs that give more complex settings, like Noise and Pattern.
  * Parameter set for specifying a new output attribute - Click the >>> icon.
    * Five parameters help you to: (1) put values on same attribute input, (2) another attribute that exists in the POP already, (3) a new attribute (both reserved-name attributes or entirely new attributes).
  * Multi-component parameters - A float3 attribute said to have three “components” and is a vector attribute. The POP parameters, depending on their settings, and cause 1, 2, 3 or 4 components of an incoming attribute to be passed to the output stage. If it's 1 component, it gets passed to all components of the output attribute. Otherwise the number of components (2, 3 or 4) of an output must match the number of components of the input.
  * If the output is a new attribute, and all components don't get filled then it uses the default values.
  * Custom attributes can be 64-bit floats or 32-bit integers, integers and unsigned integers, and can be manipulated as such. (built-ins are 32-bit)
  * auto-name creation - In POPs like Math, Math Mix and Math Combine, you may see an output attribute name in italics, which means that is the name of the attribute it will create or modify by default, so you don’t have to type the name yourself.
  * Output Attributes are standardized - output attribute block, the menu of attribute choices or attribute component choice,. must start with an alphabetic character.
  * standard error/warning checking - On some POPs when combining inputs, there is an Error/Warning menu that lets you choose what to do.

▸Selecting Components of Attributes and Swizzling

For an attribute made of 2 or more numbers, like Position (`P`) or `Color`, each number is called a “component” of the attribute. (yes, components are other thing in TouchDesigner too, we’re referring to “components of attributes” here.)

When selecting which attributes to operate on, or which attributes to output, you can select some of the components of an attribute. Whereas the attribute `Color` is the same as `Color(0) Color(1) Color(2) and Color(3)` together, you can select `Color(0) Color(2)` to get and use the red and blue components only.

If an input attribute scope is `P(1) P(0)`, it is not the same as `P(0) P(1)`. Since `P(0)` and `P(1)` are the X and Y values and the position, `P(1) P(0)` gives two values, the Y value followed by the X. If you then output the results (say in a Math CHOP) to `P(0) P(1)`, then you have swapped the X and Y components. This is a powerful mechanism to mix and re-order components of Attributes.

Matching input components to output components, and Parameter Size 1 to 4: See in `Overview.toe` `/components_of_attributes`.

### Swizzling and Components of Attributes

When you need to specify one or more components of an attribute, there are several more compact alternatives. Attributes can now use swizzling forms -
  * `P.xy` is equivalent to `P(0) P(1)` and `P.z` is `P(2)`
  * `Color.rgb`is equivalent to `Color(0) Color(1) Color(2)` and `Color.a` is alpha `Color(3)`.
  * `MyAttr.i0123` is the general indexing form of any attribute (”`.i`” meaning index) `MyAttr(0) MyAttr(1) MyAttr(2)` `MyAttr(3)`.
  * and for any attribute you can comma-separate numbers in `()`:

`MyAttr(0, 1, 2)` or `MyAttr(0,1,2)`is equivalent to `MyAttr(0) MyAttr(1) MyAttr(2)`

You can also reorder, for example `x` and `y`, using `P.yxz` or `P(1,0,2)`

(pro tip: Attributes that are float4 like “homogenous” positions can refer to the 4th component as .w. These are used with 4x4 matrix multiplications.)

(See in POPExamples in `Overview.toe` the component `/swizzling`)

▸Reserved and Common Attribute Names

The standard reserved-name attributes:
  * `P` position (3-float)
  * `N` normal (3-float)
  * `T` tangent (4-float, last on is polarity)
  * `Color` ((diffuse) color and alpha (was `Cd` in SOPs)
  * `PointScale` (float)
  * `Tex` (3-float) (was `uv` in SOPs)
  * `PartForce`, `PartMass` etc - particle attributes from the Particle POP
  * `SegMethod TanIn TanOut` etc attributes from the Line POP that define spline curve properties
  * Nebr*` - attributes generated by the Neighbor POP
  * new: `Weight` (from Field POP, used in Transform POP and elsewhere)
  * `LineWidth` (line width for rendering Line MAT)
  * `LineBreak` (a break in a line strip (int) used in Line Break POP)
    * `LineStripIndex`
  * `BonePaths`, `BoneBindPoses` (for skeletons)

Names generated / used in some POPs
  * `Dir` Direction (3-float) (found in [Line Metrics POP](../POPs/Line_Metrics_POP.md "Line Metrics POP")). also `Dist` `Dir` `Disp` `Tan`
  * upcoming: `Vel` Velocity (3-float) (future Slope POP, see [Cache Blend POP](../POPs/Cache_Blend_POP.md "Cache Blend POP"))
  * upcoming: `Accel` (acceleration)

Other Considerations
  * other colors, like base col* or vs reflected color, or specular... ?
  * future: something for `Angular` speed? etc
  * `Up` = tbd
  * attributes for metaballs (future)
  * attributes for SDFs (future)

▸Groups

Groups (of Points, Vertices or Primitives) are represented internally with a bit flag, where 32 groups per POP are possible in a 32-bit GPU word. Groups are created with the Group POP. The Group POP can also convert a group to an attribute which is less limited but takes more memory.

Numerous operators are able to affect points, vertices or primitives that are in a specified group and not affect other points, vertices or primitives. For example the Transform POP for affecting certain points, or the Merge POP for extracting parts of other OPs into its output, uses groups.

Other POPs may create groups automatically. ([Extrude POP](https://docs.derivative.ca/Extrude_POP "Extrude POP"), [Copy POP](../POPs/Copy_POP.md "Copy POP"))

See also [Dimension](Dimension.md "Dimension") - it is a form of grouping on structured point lists, without the need to manually create groups. (see [Copy POP](../POPs/Copy_POP.md "Copy POP"))

▸Some POP Common Features

Each POP may have some combination of these features:

### Input Selection

For multiple inputs
  * for each input, one sequential block is created
  * inputs can be references to other POPs also
  * you can do pattern-matching to do multi-POPs in one block
  * for each input you can select which attributes or groups that you want to work on (like Attribute Combine, Math Mix, Merge POPs)

### Scope

  * choose which type (”class”) of attribute: operates on Point, Vertex or Group attributes (menu)
  * Scope or Group to determine effect or not
  * Affect based on an Attribute component value
  * may use weight to determine degree of effect (any component of an attribute as weight)

### Selecting Attributes

  * Select any attribute from the input POP that you want to use, commonly through the Input Attribute Scope.
  * Select any components of an attribute. `P(0) P(1)` gives only X and Y
  * re-order components - `P(2) P(0) P(1)` in the input will give Z Y X to the next stage.
  * Select any attribute as Reference (like in Noise)

### Operation

  * (modify an array of 1 to 4 components)
  * For multi-component attributes (float2, float3, etc), one set of parameters can be used for all the components, or you can get one set of parameters for each component. (using the Parameter Size par)

### Some Math

  * Basic Arithmetic and simple functions like in Math, [ReRange POP](../POPs/ReRange_POP.md "ReRange POP"), [Limit POP](../POPs/Limit_POP.md "Limit POP")
  * there is no Function POP - see the menus in Math POP or Math Mix POP for more complete math functions.
  * generative functions like in [Pattern POP](../POPs/Pattern_POP.md "Pattern POP").
  * 1, 2 or 3 attribute components are used as lookup indexes in the Lookup Texture POP, Lookup Channel POP and Lookup Attribute POP.
  * Some POPs generate normalized attributes: [Normalize POP](../POPs/Normalize_POP.md "Normalize POP") (like a bounding box), [Texture Map POP](../POPs/Texture_Map_POP.md "Texture Map POP"), [Projection POP](../POPs/Projection_POP.md "Projection POP")

### Topology

Some operations alter topology or generate new topology.

See [POP Topology](POP_Topology.md "POP Topology"). This will help keep things running smoothly by reducing unnecessary memory allocations whenever possible. The page explains a few ways to limit those allocations.

### Post-Process

  * Re-range values
  * Collapse down to subset of points/primitives
  * Quantize menu to logic on-off, integer Floor, Round or Ceiling
  * generate a Group
  * create a new attribute

### Output Attribute

  * Direct the output to any existing or new Attribute (a built-in or custom attribute)
  * The components of an attribute can be re-ordered on output, and be routed to any other existing or new attribute. (specify `P(1) P(0) P(2)` to swap X and Y on input or output (or swizzling notation `P.yxz`), for example.)
  * standard parameter set for specifying the output attribute format via >>> in the parameter dialog.

### Connectivity

In POPs where a grid (rows and columns and sometimes slices) of points is created, you usually can choose how they are connected - like rows of line strips, triangles, quads, or none.

▸Particles

See [Particle POP](../POPs/Particle_POP.md "Particle POP") to get a current description of the Particle POP.

The following is other general information about points as particles.

What is a particle? - A Particle is simply a single POP point - the minimum is a P attribute for its position. But they can be extended with attributes…. velocity, direction, speed, age, mass, force, even with a full 3x3 or 4x4 transform per-point.

The Particle POP adds these attributes optionally and you can use them in your particle feedback loop.

Note that a point is not rendered as a dot. You need to create a Point primitive in order for points to be visible. Most generators will do that when Connectivity is set to Point Primitives.

A time-history of a point can be created with the [Trail POP](../POPs/Trail_POP.md "Trail POP") which creates a line strip for each point, using an `id` attribute for the particles. (see `Overview.toe` example for `/Trail`) So a particle can be visualized as a multi-point line strip.

Alternately you can render geometry per-point without creating new data via instancing in a [Geometry COMP](Geometry_COMP.md "Geometry COMP") (this is the classic SOPs method).

Another way to represent a particle is with any geometry as it would be created with a Copy POP. This create new geometry in a POP that can be further manipulated/animated before rendering.

However with the Copy GLSL POP, you can, at every point, run a compute shader code to warp a geometry based on the point’s attributes, so you can generate, for example, birds on the fly, so to speak. (Examples are in the Examples/ folder.)

Further rendering of stuff at each point is the domain of special rendering shaders rendering on surfaces instanced at each point, like point sprites or the Line MAT.

Particle motion is done through “integrating” over time (integration here means a force is converted to speed, speed is converted to position one frame later). So aside from the Particle POP, a [Feedback POP](../POPs/Feedback_POP.md "Feedback POP") can be used to accomplish this involving a loop that involves multiple POPs. The example from Roy & Tim Gerritsen and Peter Sistrom component are illustrations of that.

Alternately you can do all the simulation within one GLSL operator. There is currently not much example code in POPs to help with this.

Forces - can be represented as a POP with parameters specifying the force by creating or adding to a float3 `PartForce` attribute of a POP, or by using a Force POP which adds to this attribute. Ultimately the force has to be added to the particles and converted to new velocity and positions. (Clarify:) Alternately a set of points of primitives, each which defines force properties via its attributes. It’s up to the force integrator (the [Particle POP](../POPs/Particle_POP.md "Particle POP")) to interpret that and convert the forces and velocities to next position. Regular POPs and operators with custom parameters can be used to build these.

To be clarified:

Particle Generator / Emitters - where and what attribute do you launch with. birth/death

Collisions -

▸Point Clouds

Point clouds in POPs have the same functionality as they do in TOPs (if you are familiar with that workflow).

Any POP with connectivity (triangle, quad, line, linestrip) removed can be considered a point cloud.

There are two forms of point clouds:
  * a set of points with no primitives.
  * a set of points, with a set of “Point Primitives” where each point primitive is the index number of a point in the point list. Only these can be rendered directly in the renderer.

You can read in files containing point clouds using the [Point File In POP](../POPs/Point_File_In_POP.md "Point File In POP"), or the [File In POP](../POPs/File_In_POP.md "File In POP"). You can generate them with a [Point Generator POP](../POPs/Point_Generator_POP.md "Point Generator POP").

How to write out point cloud files: [File Out POP](../POPs/File_Out_POP.md "File Out POP")

Why point clouds in POPs is better than doing point clouds in TOPs:
  * No need to think of matching XYZ position values to RGB color channels.
  * No dividing into groups of 4.
  * No need for Active channel as in the square textures.
  * unlimited attributes per-point.
  * Easier to collapse into subsets (via groups in POPs, or via Delete POP)
  * POP-created groups: special group names reserved (start with _ ?)
  * SOPs and point clouds are no longer separated - all integrated in POPs.
  * Being simply points, it is the same stuff as particles.

There is an example of GaussianSplats in the Examples/GaussianSpats folder.

▸Lines and Curves

There is no curve primitive, but linestrips can contain curve attributes and/or be linear- or spline-subdivided, smoothed and resampled with the [Line POP](../POPs/Line_POP.md "Line POP"), [Line Divide POP](../POPs/Line_Divide_POP.md "Line Divide POP"), [Line Smooth POP](../POPs/Line_Smooth_POP.md "Line Smooth POP") and [Line Resample POP](../POPs/Line_Resample_POP.md "Line Resample POP") (these subdivide any Line Strip).

The Line POP divides the curve directly in the Line POP, or it outputs control points with extra attributes that define the curve shape: Weight, Tension, Interpolation Type, Bezier tangents In and Out, tangent continuity (3 cases). These attributes, no matter where they are generated, can be used by the [Line Divide POP](../POPs/Line_Divide_POP.md "Line Divide POP"). Some 3D curves can be read into POPs in the [Alembic In POP](../POPs/Alembic_In_POP.md "Alembic In POP") and others.

The [Line Smooth POP](../POPs/Line_Smooth_POP.md "Line Smooth POP") can also add points and smooth lines.

▸Read-Only Built-In Attributes

Read-Only Built-In Attributes are convenient internally-generated attributes that can be used where specifying an attribute in a POP parameter. They include numbers like a point’s integer index number, or the point index normalized between 0 and 1, which is otherwise hard to get (you could get it with a [Pattern POP](../POPs/Pattern_POP.md "Pattern POP") and [Normalize POP](../POPs/Normalize_POP.md "Normalize POP")).

Where to find the read-only attributes: They appear on a secondary menu to the attribute name menu you see in Math, Math Mix and the Lookup POPs, for example. Roll over the > at the bottom of the attribute menu to choose a built-in.

They also inclode basic constants like `pi` (3.14158).

They are used most commonly in Math and Math Mix POPs, the [Lookup Channel POP](../POPs/Lookup_Channel_POP.md "Lookup Channel POP"), [Lookup Texture POP](../POPs/Lookup_Texture_POP.md "Lookup Texture POP"), [Lookup Attribute POP](../POPs/Lookup_Attribute_POP.md "Lookup Attribute POP"), and in [Delete POP](../POPs/Delete_POP.md "Delete POP"), [Group POP](../POPs/Group_POP.md "Group POP") and others.

All read-only built-in attribute names start with `_`. They are all reserved names. Some built-ins are generated per-point, per-primitive or per-vertex, depending on what class of attribute (point, vertex, primitive) you are modifying.

Built-in read-only attributes behave like normal attributes, but they are not output or passed to the next POP.

### List of Built-in Read-Only Attributes

a partial list:
  * `_PointI` - the integer point index
  * `_PointU` (point index normalized 0 to 1) (first point is 0, last point is 1)
  * `_PointCy` (point index normalized cyclical going from 0 to (N-1)/N ) (so when `_PointCy` is 1, it is the first point of the point list.
  * `_PrimI` - the primitive index
  * `_PrimU` (primitive index normalized 0 to 1)
  * `_PrimCy` (primitive index normalized cyclic…)
  * `_VertI` - the current vertex number, when working on vertices.
  * `_VertU` - (vertex index normalized 0 to 1)
  * `_VertCy` - (vertex index normalized cyclic…)
  * `_DimI[]` - every point has a position in its multi-dimensional array - the col/row/slice/etc that a point is in. `_DimI[1]` would be the row number of a point in a 3D grid, for example.
  * `_StepSeconds` - the step in seconds since the last time the network was cooked (the “[Time Slice](https://docs.derivative.ca/index.php?title=Time_Slice&action=edit&redlink=1 "Time Slice \(page does not exist\)")”)
  * `_StepFrames` - the step in frames
  * `_MaxInt` and `_MaxUInt` and `_NoNeighbor` these are special numbers that can be used in expressions to compare with attribute values.
  * `_ArrayI`, `_ArrayU`, `_ArrayCy` - for iterating through every element in an [Array Attribute](Array_Attribute.md "Array Attribute").

**xxx ![image.png](attachment:afbcefc1-a066-4e95-9acf-a20db04c2b2b:image.png)**

▸"index" vs "id"

index

In POPs, "index" is invariant, and is not an attribute. You see index in [POP to DAT](../DATs/POP_to_DAT.md "POP to DAT") point lists, primitive lists, and the vertex list for each primitives. For the lists, Index starts at 0 and increases in steps of 1.

You cannot write to “index”. “Index” also appears in the built-in attributes as `_PointI`, `_PointU` and `_PointCy`. The same goes for vertex index of a primitive, and primitive index of a POP, they are invariant and not attributes.

Index is also referenced/used in all the Lookup POPs in the same way via built-in attributes.

Like line numbers in a text file, they identify where the information is relative to the start.

### id

“id”, such as `PartId` for particles, is commonly used for a unique number on an entity that stays with that entity for its lifetime, but can be found in any order, and there may not exist an id of a certain value, i.e. id==7 may not exist in a list of points. The [Particle POP](../POPs/Particle_POP.md "Particle POP") generates its own id’s on points. Use id in an attribute name when building your own similar systems.

▸Texture Mapping

The common attribute that we use for texture coordinates in POPs is `Tex` (formerly `uvw`), which is always a float3 vector attribute type, where the 3rd value is used for 3D textures where applicable, and unused (set to 0) otherwise. But you can use any attribute name when you assign it to a material (via the >>> icon in parameters). Some materials use several sets of texture coordinates, you can call them anything, like `TexA`, `TexB`, etc ...

The `Tex` attribute can be created on all the generator POPs, and created/adjusted with the [Texture Map POP](../POPs/Texture_Map_POP.md "Texture Map POP"), but also in many other POPs that give greater control, like [Normalize POP](../POPs/Normalize_POP.md "Normalize POP"), Math, Math Mix, Projection, Noise, Pattern, Transform, Lookup* and more.

Texture coordinates are created on points or on vertices of primitives, so you have to keep an eye on where they are. They are put on vertices when there is texture wrapping like on a sphere or a torus, but on points in other cases (like grids).

▸Dimension

Dimension is a powerful concept in POPs that provides some organization of the points its point list. See the wiki page for [Dimension](Dimension.md "Dimension") for details. Summary:

A POP’s point list may have an implied structure within it. For example, a [Grid POP](../POPs/Grid_POP.md "Grid POP") is a list of points implicitly arranged in columns and rows that may not be known if they are connected as a set of triangles, quads or point primitives. A Grid POP has two dimensions by default (the rows and columns), and three if you increase the number of slices. When you pass a POP to another POP, you may want to preserve what is known about its structure.

Dimension is the metadata that describes the structure of a point list in a POP, and is passed from POP to POP.

▸Python Members and Functions

These functions will give you values on the CPU. If you need them on the GPU, look at the [Analyze POP](../POPs/Analyze_POP.md "Analyze POP").

To avoid stalls, use the `delayed=True` directives below, though data will be a frame behind.
  * `OP.bounds(delayed=False, selected=False, recurse=True)`
  * `OP.numPoints(delayed=False) # size of point list`
  * `OP.numVerts(delayed=False)`
  * `OP.numPrims(delayed=False)`
  * `OP.points(attributeName, startIndex=0 (optional), count=0 (optional), delayed=False)`
  * `OP.verts(attributeName, startIndex=0 (optional), count=0 (optional), delayed=False)`
  * `OP.prims(attributeName, startIndex=0 (optional), count=0 (optional), delayed=False)`
  * `OP.pointAttributes`
    * `len(OP.pointAttributes) # get the number of attributes`
    * `[x for x in OP.pointAttributes] # a way to get it in a list`
    * `[*OP.pointAttributes] # another way to get it in a list`
  * `list = [x for x in OP.pointAttributes]  ;  list[1].name, list[1].size, list[1].type # attribute definition print( l[2].name )`
  * also `isArray`, `arraySize` and `numMatCols` members
  * `OP.vertAttributes`
  * `OP.primAttributes`

lists of attributes that were changed or created in the operator:
  * `OP.pointAttributesChanged[]`
  * * `OP.vertAttributesChanged[]`
  * `OP.primAttributesChanged[]`

That is, it will not include any attribute in the output that has not changed in any way. Attributes that were deleted are not included.

how POPs are structured as grids:
  * `OP.dimension` an array of integers describing number of columns, rows, …

Printing info about attributes:
```
for attribute in op('somepop').pointAttributes:
    print(attribute.name, attribute.size, attribute.type)`
```
More: [POP Class](../Python/POP_Class.md "POP Class")

▸Custom GLSL Shaders

Although we often say POPs let you avoid having to writing GLSL code, it is equally true that POPs make it easier you for you to write GLSL code. See [Write GLSL POPs](https://docs.derivative.ca/Write_GLSL_POPs "Write GLSL POPs").

▸Driving parameters per-point using Attributes via Map page

On some parameters of some POPs, you can have a different parameter value for each point of the POP. Some POPs let you map one of its attributes to a parameter using a [Map page on the parameter dialog](Mapping_POP_Attributes_to_Parameters.md "Mapping POP Attributes to Parameters").

For example, on the [Transform POP](../POPs/Transform_POP.md "Transform POP")'s Map page, you can choose an attribute or a component of an attribute, and map the values of that attribute to a translate parameter, giving a different translate value for each point.

The attribute value can alternately be added to the value in the parameter, or multiplied by the value in the parameter.

A Map page can also tie a CHOP channel to a parameter to give a separate parameter value per point.

▸The `.pop` File Format Native to POPs

The `.pop` [File Type](../Interoperability/File_Types.md "File Types") ix a native POP file format that is an exact lossless representation of a POP's output. A `.pop` file preserves all primitive types, attributes, groups and [Dimension](Dimension.md "Dimension").

It is created with the [File Out POP](../POPs/File_Out_POP.md "File Out POP") or by right-clicking a POP node and selecting Save Geometry. It is read into TouchDesigner with a [File In POP](../POPs/File_In_POP.md "File In POP").

See [pop_File_Format](https://docs.derivative.ca/Pop_File_Format "Pop File Format") for more info.

▸Point Count and Topology Info on CPU/GPU, Memory Management

For certain POPs operations:
  * The number of resulting points is only known on the GPU. The resulting POP will have “Point Count Info on GPU” instead of “Point Count Info on CPU” in the info popup (examples: Facet POP: Cusp and Consolidate operation…)
  * The number of resulting vertices and primitives (Topology Info) is only known on the GPU. The resulting POP will have “Topology Info on GPU” instead of “Topology Info on CPU” in the info popup (example Convert POP: open or close line strips)
  * Both the point count and the topology info are only known on the GPU. In that case the resulting POPs will have “Point Count Info on GPU” and “Topology Info on GPU” in the info popup (example Delete POP)

For the points and/or topology of these POPs , the memory allocated is the maximum memory the POP could use.

Downloading the actual point count and topology info (number of primitives and vertices) for these POPs from the GPU causes a stall.

For the downstream POPs compute shaders, the point count info and the topology info are passed through buffers to avoid the stall and unnecessary work: this is called indirect dispatch of compute shaders - this is a bit more expansive than a regular compute shader dispatch though.

The middle click info popup does the download and show what is used versus what is allocated.

Some OPs ([POP to DAT](../DATs/POP_to_DAT.md "POP to DAT"), copy topology back to CPU on GPU POP) as well as the python functions allow a “next frame” asynchronous download that prevents the stall but introduces a 1 frame latency. Copy topology back to CPU turns the POP back into a regular POP, only allocating necessary memory again downstream.

The [Topology POP](../POPs/Topology_POP.md "Topology POP") allows you to manually allocate memory for POPs with info on the GPU , so some unused memory can be reclaimed without a stall.

The [Feedback POP](../POPs/Feedback_POP.md "Feedback POP") has a toggle to limit the memory allocated to a multiple of the input memory to prevent the memory used from blowing up when geometry is created inside the feedback loop. (superseded by [Topology POP](../POPs/Topology_POP.md "Topology POP") features)

For integrated GPUs, CPU and GPU share memory so the download of information from the GPU doesn’t cause a stall (still to be done automatically)

See also [POP Topology](POP_Topology.md "POP Topology").

▸Advanced Features and Topics

Instancing vs Copying

Instance where possible, but if you want to do anything with data after a copy, like deform it, use [Copy POP](../POPs/Copy_POP.md "Copy POP"). For small data sets it doesn’t matter much.

## Fetching info about POP Array and Matrix attributes

attributes members:
  * `isArray`

_True if the attribute is an an array._
  * `arraySize`

_The size of the array if for array attributes, 0 otherwise._
  * `numMatCols`

_The number of columns for matrix attributes, 0 otherwise._
  * `numMatRows`

_The number of rows for matrix attributes, 0 otherwise._

Sample formatting when printing attributes:
  * P: 3 <class 'float'>
  * B: 3x2[2] <class 'float'>
  * Test: 1[3] <class 'int'>
  * N: 3 <class 'float'>
  * A: 4x4 <class 'float'>

Downloading array and matrix attributes (with `POP.pointAttributes['Test'].vals()` or `POP.points('Test')` for POP `POP` and attribute `Test`)

Arrays are lists, matrices are tuples of tuples, we might offer numpy arrays in the future see toe for examples

[PythonMatrixArrayAttribs.3.toe](attachment:f32d0d0c-c5e9-4250-8349-89675f0c733d:PythonMatrixArrayAttribs.3.toe)

### Indirect and Direct POP Info

"Copy Topology Info Back to CPU" toggle on some POPs:

For a number of POPs/operation, including the [Proximity POP](../POPs/Proximity_POP.md "Proximity POP"), the number of resulting points/prims/verts is only known on the GPU.

If that's the case the result is what we call "indirect POP" because the POPs after do indirect dispatches of compute shaders, getting topology from GPU buffers.

That also means that for these POPs, GPU memory is allocated for the max number of points/prims/verts that can result.

and the POPs after use this max number to do their memory allocation.

Since knowing the actual number of points/prims/verts means downloading the data from the GPU which causes a stall.

So that's what this toggle does, it downloads the topology info and turns the POP back into a "direct POP".

It should be in a separate POP and we may do this in the future.

▸POPs vs SOPs

This is of interest if you use SOPs already. See the table below for the POPs to use in place of some SOPs.
  * POPs run on the GPU as highly-parallelized compute shaders. SOPs run on the CPU.
  * POPs give better, more modern workflow than SOPs: It combines key features of SOPs, CHOPs and TOPs.
  * All point cloud-relevant TOPs are implemented in POPs and more, without the limitation of mapping to 4-channel image formats.
    * You can retrieve point clouds from TOPs ([TOP to POP](../POPs/TOP_to_POP.md "TOP to POP")), [Point File In POP](../POPs/Point_File_In_POP.md "Point File In POP"), and there are native point cloud generators in POPs.
  * TOP-resident `particlesGPU` is re-implemented in POPs. Particle systems are enabled with the [Feedback POP](../POPs/Feedback_POP.md "Feedback POP") and general data manipulation.
  * POPs has more powerful creation and manipulation of attributes, and controlling of the data types of attributes including signed /unsigned integers, and double precision.
  * “attribute arrays” are new - they can be, for example, an array of 12 float3 vectors.
  * doing lots of raw math in POPs with [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") is possible versus the simplistic/slow Point SOP.
  * SOPs can have closed polygons with unlimited number of sides and get rendered as filled polygon surfaces. POPs only have triangles and quads to represent surfaces. POP Line Strips can be closed but they do not render as closed surfaces.
  * Open polygons in SOPs is like “line strips” in POPs, but line strips can be closed, however that doesn’t mean line strips form a surface. A closed line strip is a looping line in 3d space.
  * POPs do not follow SOPs directly. For example, the [Normal POP](../POPs/Normal_POP.md "Normal POP") creates surface normals and tangents whereas SOPs do it in a Facet SOP.
  * You can render SOPs and POPs in the same [Render TOP](../TOPs/Render_TOP.md "Render TOP").
  * You can right-click on a POP and select a [Geometry COMP](Geometry_COMP.md "Geometry COMP") to create a POP-in-a-Geo.
  * Geometry Instancing is done in the same way as SOPs/CHOPs/DATs, where POP attributes can be used on the Instancing pages.
  * POPs implement features of spline curves (but as spline-divided Line Strips): Bezier, BSpline, and Cardinal splines in for example a [Line Divide POP](../POPs/Line_Divide_POP.md "Line Divide POP").

POPs presently do not implement the following:
  * booleans on surfaces
  * NURBS
  * primitive type "Mesh". Meshes in SOPs are point arrangements where rows/columns are defined. Replacing this in POPs is the more powerful concept of point arrangement called [Dimensions](Dimension.md "Dimension").

The POPs to use in place of some SOPs  SOP | function |  POP
---|---|---
Add SOP | for creating points only |  [Point POP](../POPs/Point_POP.md "Point POP")
Facet SOP | for creating normals |  [Normal POP](../POPs/Normal_POP.md "Normal POP")
Point SOP | simple math on points |  [Math POP](../POPs/Math_POP.md "Math POP"), [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP")
Limit SOP | channel to points |  [CHOP to POP](../POPs/CHOP_to_POP.md "CHOP to POP")
Limit SOP | creating geometry | mostly [Copy POP](../POPs/Copy_POP.md "Copy POP")
Texture SOP | coordinates for textures |  [Normalize POP](../POPs/Normalize_POP.md "Normalize POP"), [Texture Map POP](../POPs/Texture_Map_POP.md "Texture Map POP"), [Projection POP](../POPs/Projection_POP.md "Projection POP"), [Line Metrics POP](../POPs/Line_Metrics_POP.md "Line Metrics POP")
Trace SOP | outline from image |  [Trace POP](https://docs.derivative.ca/Trace_POP "Trace POP")
Vertex SOP | vertex attributes |  [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP"), [Attribute POP](../POPs/Attribute_POP.md "Attribute POP"), several others
Attribute Create SOP | create normals and tangents |  [Normal POP](../POPs/Normal_POP.md "Normal POP")
Attribute SOP | delete and rename attributes |  [Attribute POP](../POPs/Attribute_POP.md "Attribute POP")
| create new attribute | many: [Attribute POP](../POPs/Attribute_POP.md "Attribute POP"), [Math POP](../POPs/Math_POP.md "Math POP"), [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP"), [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP"), [Limit POP](../POPs/Limit_POP.md "Limit POP"), [ReRange POP](../POPs/ReRange_POP.md "ReRange POP")
| attribute math like Math CHOP |  [Math POP](../POPs/Math_POP.md "Math POP"), [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP")
| rerange like Math CHOP |  [ReRange POP](../POPs/ReRange_POP.md "ReRange POP"), [Math POP](../POPs/Math_POP.md "Math POP"), [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP")
| functions like Function CHOP |  [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP"), [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP")
Deform SOP | bone-driven deformation |  [Skin Deform POP](../POPs/Skin_Deform_POP.md "Skin Deform POP")
▸New Structural Technologies in POPs

This is a compilation of things you will see in POPs that may not (yet) appear in other parts of TouchDesigner. In order of increasing esotericism…..
1. management of POP inputs on multi-input POPs using sequential parameter blocks which you see in Math Mix POP and Blend POP among others.
  *     * one block per input.
    * each input has its own set of parameters in a sequential block.
    * each input can be a wire or a reference via a parameter.
2. “Resizable parameters” - Parameter Size letting you use separate parameters on each component of an attribute. Setting to to 3 gives 3 columns of parameters for X Y and Z.
3. You can turn on options to change what pars are in sequential parameter blocks. Line POP and Create POP have this.
4. sequential parameter blocks whose parameters are user-defined (not custom pars), found in Point POP, Line POP, Primitive POP, Curve POP.
5. Map page - parameters driven by attributes - parameter can have different values per-point based on an attribute of that POP.
6. and parameter hints (when Math Mix output attribute is blank, and also mapping hints)
7. instancing (of fields or forces etc) via the Specification parameter (reference to a POP whose point list represents one instance per point) (Field POP, Force POP)
8. disabling of inactive parameters of a multi-value parameter set.
9. Sequential blocks are now more structured and flexible.
10. Users can now make their own custom sequential blocks in the Component Editor.
11. Auto-renaming of operator names to represent their new type.
12. Parameter panels without labels. Page menus all on one line. Geo viewer titles.
13. parameter suffixes now universally 0-based.
14. Multi-column pop-up menus. double-pop-down menus (for attributes).
15. Collapsing sequential blocks into single-line summary (Math Mix and Math Combine POP's Combine page)

POPs (Point Operators) is a new [Operator Family](Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

TOuch Environment file, the file type used by TouchDesigner to save your entire project.

POPs (Point Operators) is a new [Operator Family](Operator_Family.md "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

Each POP and SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](Primitive.md "Primitive") is defined by a vertex list, which is list of point numbers.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

shared points, normals on shared points, unique points, recalculate.

A surface type in [POPs](../POPs/POP.md "POP") and [SOPs](../SOPs/SOP.md "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](Point.md "Point") and Primitives are part of the [Geometry Detail](Geometry_Detail.md "Geometry Detail"), which is a part of a [SOP](../SOPs/SOP.md "SOP").

A primitive in POPs that has 1 or more connected points.

A sequence of vertices form a [Polygon](Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](Point_List.md "Point List"), and each [Point](Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

An [Operator Family](Operator_Family.md "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

Operators that do not need any inputs connected are called Generators in TouchDesigner, like a Pattern CHOP. See [Filter](Filter.md "Filter").

A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

Rendering is the creation of a 3D image with the Render TOP. Rendering is also used more generally to include the compositing (with TOPs) to generate an output image.

An [Operator Family](Operator_Family.md "Operator Family") that contains its own [Network](Network.md "Network"). There are sixteen 3D [Object Component](Object_Component.md "Object Component") and ten 2D [Panel Component](Panel_Component.md "Panel Component") types. See also [Network Path](Network_Path.md "Network Path").

In a parameter dialog, Setting Parameter Size to 3 gives 3 columns of parameters to control X Y and Z separately for example.

A sequence of vertices form a [Polygon](Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](Point_List.md "Point List"), and each [Point](Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

MATs or Materials are an [Operator Family](Operator_Family.md "Operator Family") that applies a [Shader](Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

MATs or Materials are an [Operator Family](Operator_Family.md "Operator Family") that applies a [Shader](Shader.md "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](../POPs/Group_POP.md "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

A [Link](Link.md "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](Operator_Family.md "Operator Family").

The grey dashed lines between nodes is a Reference (or [Link](Link.md "Link")). A Reference is (1) a [Parameter Reference](Parameter_Reference.md "Parameter Reference"), a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](https://docs.derivative.ca/index.php?title=Node_Reference&action=edit&redlink=1 "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.

A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](Export.md "Export"), node [Paths](Network_Path.md "Network Path") in parameters, and [expressions](Expression.md "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](Wire.md "Wire") that connects nodes in the same [Operator Family](Operator_Family.md "Operator Family").

POP Topology is the relationship between geometric entities making up POPs, and refers to the POP's [Primitives](Primitive.md "Primitive"), the [Vertx / Vertices](Vertex.md "Vertex") of each Primitive, and the [Points](Point.md "Point") list that the Vertices refer to.

Dimension is metadata of a POP that describes the structure of the point list, which may be arranged as rows and columns of points (which is two dimensions of size _nrows_ and _ncolumns_).

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").

The 3D data held in POPs and passed for rendering by the [Geometry COMP](Geometry_COMP.md "Geometry COMP").

(1) A [Geometry Component](Geometry_COMP.md "Geometry COMP") can instance and render its SOP geometry many times: once for each sample in a CHOP, row of a DAT table, pixel in a TOP, or point of a SOP, (2) An instance is an OP that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Switch OPs and in some cases Select OPs.

A [Operator Family](Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
