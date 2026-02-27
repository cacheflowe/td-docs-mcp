---
url: https://docs.derivative.ca/Dimension
category: Glossary
title: Dimension
---

# Dimension
A POP’s point list may have an implied structure within it. For example, a [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP") or [Plane POP](https://docs.derivative.ca/Plane_POP "Plane POP") is a list of points implicitly arranged in columns and rows, thus having two dimensions. This information is passed to downstream POPs. The rows and columns are considered "dimensions". A Grid POP has two dimensions by default, and three dimensions if you increase its number of slices (default 1). When you pass a POP to another POP, you may want to preserve and use what is known about its structure.
**Dimension** is the metadata that describes the structure of the point list, and is passed from POP to POP.
Points are organized generally as N-dimensions, where each dimension has some number of elements. Dimensions compound: You get three dimensions by copying a circle (a [Circle POP](https://docs.derivative.ca/Circle_POP "Circle POP") has a dimension of 1) onto each point of a 2-dimensional grid.
When converting a [POP to TOP](https://docs.derivative.ca/POP_to_TOP "POP to TOP"), you may want to create the corresponding width and height (and depth) of pixels in the TOP. The dimension is used for this. When converting a [TOP to POP](https://docs.derivative.ca/TOP_to_POP "TOP to POP"), you will want to preserve its width and height resolutions, again generating the correct dimensions.
Middle-click on a POP to see its popup info: You will see numbers for Dimension, for example, on a [Torus POP](https://docs.derivative.ca/Torus_POP "Torus POP") :
```
Dimension 20 40

```

indicating a 20 x 40 point arrangement. If you multiply the dimension numbers you will always get the total number of points in the POP. In this example, in memory, the first 20 numbers are the first row, etc.
```
Dimension 20 40 12

```

indicates a 20 x 40 x 12 point arrangement (12 sets of 40 sets of 20 points)
Some generator POPs are multi-dimensional (Torus (2 dimensions), Tube (2 dimensions), Grid (2 or 3), in some cases Sphere is 2 dimensions….).
Some POPs always preserve the dimensions (like [Math POP](https://docs.derivative.ca/Math_POP "Math POP") which only changes point values). Some POPs increase the number of dimensions ([Copy POP](https://docs.derivative.ca/Copy_POP "Copy POP"), [Trail POP](https://docs.derivative.ca/Trail_POP "Trail POP") and sometimes [Merge POP](https://docs.derivative.ca/Merge_POP "Merge POP"))
Some POPs destroy multi-dimensions ([Delete POP](https://docs.derivative.ca/Delete_POP "Delete POP")). A Grid POP is no longer 2-dimensions if you, for example, delete one point. It becomes 1-dimension whose size simply is the total number of points.
All POPs have at least 1 dimension with the number of dimension elements being the number of points, like the Circle POP.
If a POP has N dimensiona nad any of the dimensions is 0, then the POP will have 0 points.
NOTE: This replaces the concept of meshes in SOPs.
###  Built-In Attributes for Dimension
You can use the dimensions when working with attributes like in [Math Mix POP](https://docs.derivative.ca/Math_Mix_POP "Math Mix POP") or [Lookup Channel POP](https://docs.derivative.ca/Lookup_Channel_POP "Lookup Channel POP"), accessible on any attribute parameter menu: at the bottom of the attribute menu press the > submenu.
`_NumDim` is the number of dimensions of the input.
`_DimSize[0]` would be the number of columns in a grid or torus or tube. `_DimSize[1]` is the number of rows. etc,
`_DimI[0]` is the column number of a point, `_Dim[1]` is the row number.
`_DimU[0]` is the point’s column represented as a normalized number between 0 and 1. `_DimU[0]` is 1 for the last point in a grid column. These numbers are useful for all the Lookup* CHOPs.
pro tip: `_DimCy[0]` is similar to `_DimU[0]` but is cyclic: The last column has `_DimU[0] == 1`, but the last column has `DimCy[0] == ( 1 - 1/numcols )`, so with 10 columns, the last column has `DimCy[0]  == .9`,. Therefore if you give a Lookup POP an index value of `1` and it’s cyclic, it’s referring to the first point.
Note: although built-in attributes for dimension are most convenient, you can also **extract the dimensions of any POP into a point attribute using the** [Analyze POP](https://docs.derivative.ca/Analyze_POP "Analyze POP").
###  Python for Dimension
In python, `POP.dimension` is the list of sizes of each dimension, for example `[10, 20, 8]`. It is the map of points arranged in memory.
`len(POP.dimension)` is the number of dimensions, `3` in this case. Always the number of points in a POP is the product of all the dimensions.
NOTE: The term “array” is not used with dimension. An attribute is an array if it is more than one float3 for instance.
For the [Grid POP](https://docs.derivative.ca/Grid_POP "Grid POP"), in python, `POP.dimension[0]` is the number of columns, `POP.dimension[1]` is number of rows, `POP.dimension[2]` is number of slices if there is more than 1 slice.
And if you copy this 3D grid to points of a circle, `POP.dimension[4]` is the number of circle points you stamped to.
`POP.numPoints = POP.dimension[0] * POP.dimension[1] * POP.dimension[2] * POP.dimension[3]`
Attributes vs Python  | Attribute | Python
---|---|---
number of points | `_NumPoints` |  `POP.numPoints()`
dimension info object | - |  `POP.dimension`
number of dimensions | `_NumDim` |  `len(POP.dimension)`
elements in first dimension | `_DimSize[0]` |  `POP.dimension[0]`
index of point in first dimension | `_DimI[0]` | -
index of point in second dimension | `_DimI[1]` | -
normalized index of point in first dimension | `_DimU[0]` | -
cyclic normalized index of point in first dimension |  `_DimCy[0`] | -
attribute value | _attributeName_ |  `POP.points(_attributeName_)`
POPs (**Point Operators**) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](https://docs.derivative.ca/Render_TOP "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
Dimension is metadata of a POP that describes the structure of the point list, which may be made of rows and columns of points (which is two dimensions of size nrows and ncolumns).
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
Attributes are data associated with [POP](https://docs.derivative.ca/POP "POP") geometry. [Points](https://docs.derivative.ca/Point "Point"), [Vertex (Vertices)](https://docs.derivative.ca/Vertex "Vertex") and [Primitives](https://docs.derivative.ca/Primitive "Primitive") (polygons, lines, etc) can have any number of attributes.
