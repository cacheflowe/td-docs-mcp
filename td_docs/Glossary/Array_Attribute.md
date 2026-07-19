---
url: https://docs.derivative.ca/Array_Attribute
category: Glossary
title: Array_Attribute
---

# Array Attribute

An **Array Attribute** is an [Attribute](Attribute.md "Attribute") with multiple **elements** of a chosen Attribute Data Type. For example an array attribute can be made of 12 integer elements for each point. This enables POPs to hold more complex data and crunch calculations on the GPU with minimal overhead.

Like any attribute, each array attribute has a **Data Type** which can be a (32-bit) float, integer, unsigned integer (uint), double(-precision float), matrix or quaternion, and can be 1- 2- 3- or 4-component "vectors" like float2, float3, float4. For example, one array attribute can be 12 float4 vectors: float4[12].

**How to create array attributes** -
  * [Attribute POP](../POPs/Attribute_POP.md "Attribute POP") - On the Create page under New Attribute, give it a name (examplez: `MonthlyTempC`), a Type (float), a Size (1 - each array element will be a single float). Turn on the Array toggle and specify the number of elements (e.g. 12). That shows up in the popup help and the node viewer as `MonthlyTempC[12]` - 12 floating point numbers, with a default value of 0.
  * [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP") - On its New page, create array attributes with constant values in the same way.
  * [DAT to POP](../POPs/DAT_to_POP.md "DAT to POP") - With data coming from DATs, it can create an array attribute based on the names in the column headings, like `MyArray[0] MyArray[1] MyArray[2]` for an array of floats, and will collect similarly-named columns into one array attribute.
  * [CHOP to POP](../POPs/CHOP_to_POP.md "CHOP to POP") - It can create array attributes based on the naming of CHOP channels. For example channel names `Abc_0_` and `Abc_1_` create an array attribute named `Abc` with 2 float elements. Set the Convert with Channels Selection to Autoconvert Precise Names.
  * [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") and [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP") on the Combine page can create array attributes from other array attributes.
  * GLSL POPs ([GLSL POP](../POPs/GLSL_POP.md "GLSL POP"), [GLSL Advanced POP](../POPs/GLSL_Advanced_POP.md "GLSL Advanced POP"), [GLSL Copy POP](../POPs/GLSL_Copy_POP.md "GLSL Copy POP")) can create new array attributes similar to the [Attribute POP](../POPs/Attribute_POP.md "Attribute POP").

**How to set values in Array Attributes** -
  * Fill in values from the [Lookup Channel POP](../POPs/Lookup_Channel_POP.md "Lookup Channel POP"), or the [Random POP](../POPs/Random_POP.md "Random POP").
  * Manually create one to four elements at a time in each Combine block in Math Mix, where Operation is A, A is any number and the output is `MonthlyTempC[0]`, then `MonthlyTempC[1]`, etc. (You can do 4 values for A per block.)
  * The built-in attributes `_ArrayI` and `_ArrayU` in Math Mix and Math Combine POPs give ascending values in the elements of array attributes.
  * Set values with custom code in GLSL POPs ([GLSL POP](../POPs/GLSL_POP.md "GLSL POP"), [GLSL Advanced POP](../POPs/GLSL_Advanced_POP.md "GLSL Advanced POP"), [GLSL Copy POP](../POPs/GLSL_Copy_POP.md "GLSL Copy POP"))

**How to do math on Array Attributes** - The Math Mix and Math Combine POPs on their Combine page apply automatic "array looping" wherever array attributes are specified in the A, B or C fields. The required `[:]` signifies the operation is executed on every array element, loosely following the pythong syntax. If an array attribute has N elements, the sequential blocks will repeat itself N times. It applies the same parameters to each loop, using the Nth element of any array specified, putting the result into the the Nth element of an existing or new N-size array in the block's output attribute. Having the operation executed on a certain range with `[x:y]` (for range x to y) is currently not supported.

For example, to convert monthly temperatures from Centigrade to Farenheit, in a sequential block, make the math Operation be A * B + C, put `MonthTempC[:]` in A, put `1.8` in B, `32` in C, and for output, put a new name `MonthTempF[:]`. This will convert, for each element of `MonthTempC`, Centigrade to Farenheit temperature (degrees * 1.8 + 32) and the result put in a new array attribute with 12 elements called `MonthTempF`.

If each point of a POP represents a city, and `MonthTempC` contains average temperature for each of 12 months, it is doing temperature conversions for all cities for all months in one sequential block.

**POPs supporting array attributes** - The POPs that can operate on array attributes are listed below.
  * [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP") and [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") - On the Combine page it iterates over array elements.
  * [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP") - On the New Attributes page array attributes can be created. On the Pre and Post pages the math can be applied to array attributes.
  * [Lookup Channel POP](../POPs/Lookup_Channel_POP.md "Lookup Channel POP"), [Lookup Texture POP](../POPs/Lookup_Texture_POP.md "Lookup Texture POP"), [Lookup Attribute POP](../POPs/Lookup_Attribute_POP.md "Lookup Attribute POP") - support for iterations over array elements.
  * [Math POP](../POPs/Math_POP.md "Math POP"), [ReRange POP](../POPs/ReRange_POP.md "ReRange POP"), [Limit POP](../POPs/Limit_POP.md "Limit POP"), [Quantize POP](../POPs/Quantize_POP.md "Quantize POP") [Normalize POP](../POPs/Normalize_POP.md "Normalize POP") - support for iterations over array elements.
  * [Noise POP](../POPs/Noise_POP.md "Noise POP") - iterates over array elements, when combining with array input attribute, or when using an array attribute for the Noise Lookup Attribute - it uses the same seed for each array element.
  * [Random POP](../POPs/Random_POP.md "Random POP") - iterates over array elements only when combining with array input attribute. It also doesn’t allow to output to a new array attribute if there’s no input attribute array. It uses a different seed for each array element.

**Combining the elements of an array down to one element** (a non-array) - The Operation menu on the [Math Combine POP](../POPs/Math_Combine_POP.md "Math Combine POP") and [Math Mix POP](../POPs/Math_Mix_POP.md "Math Mix POP") contains functions to combine array elements of each point. The functions are `arrayavg()`, `arrayadd()`, `arraymult()`, `arraymin()`, `arraymax()` and `arraylength()`, combining the elements of an array down to one.

If you don't want to combine all the elements, just the first N elements, a second integer attribute can be used to specify a number-of-elements per-point with the following syntax `[:_ArraySizeAttrName_]`. For example, when working with array attributes coming from the[Neighbor POP](../POPs/Neighbor_POP.md "Neighbor POP"), you would use `[:NumNebr]`.

**Built-In Read-Only Attributes for Arrays** - There are built-in read-only attributes useful with arrays in the POP attribute name menus. They are: `_ArrayI` (the index of the element in the array), `_ArrayU` (normalized between 0 and 1, and `_ArrayCy` (normalized 0 to almost 1, making it cyclic).

Notation - float4 array attribute, int3 array attribute. data type / array / attribute

An Array Attribute is an [Attribute](Attribute.md "Attribute") with multiple **elements** of a chosen **Attribute Data Type** , for example an attribute made of 12 integers.

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

An [Operator Family](Operator_Family.md "Operator Family") which operate on [Channels](Channel.md "Channel") (a sequence of numbers ([Samples](Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
