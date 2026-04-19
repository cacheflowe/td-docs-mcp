---
url: https://docs.derivative.ca/Array_Attribute
category: Glossary
title: Array_Attribute
---

# Array Attribute

An **Array Attribute** is an [Attribute](https://docs.derivative.ca/Attribute "Attribute") with multiple **elements** of a specific Attribute Data Type, for example an attribute made of 12 intergers. This enables POPs to hold more complex data.

The possible **Attribute Data Types** include single-value float (32-bit), integer, unsigned integer (uint), double(-precision float), or 2- 3- or 4-component vectors like float2, float3, float4, int2, mat33 and mat44 matrices, and others.

**How to create array attributes** -
  * In an [Attribute POP](https://docs.derivative.ca/Attribute_POP "Attribute POP"), on the Create page, under New Attribute, give it a name (`MonthTempC`), a Type (float), a Size (1, a single number and not a vector)), turn on the Array toggle and specify the number of elements (12). That shows up in the popup help and the node viewer as `MonthTempC[12]` - 12 floating point numbers, with a default value of 0.
  * DAT to POP will create an array of the column heading is a nane in the form `MyArrayAttribute[3]` and will collect similarly-named columns into one array attribute.

**How to initialize values in Array Attributes** - Alternately you can create one to four elements at a time in each Combine block in Math Mix, where Operation is A, A is any number and the output is `MonthlyTempC[0]`, then `MonthlyTempC[1]`, etc. (You can do 4 values for A per block.)

How to do math on Array Attributes - Aside from operating on array attributes in GLSL POPs, the Math Mix and Combine POPs surrently operate on one element per block (not looped)

A fufure build will offer more powerful creation and manipulation of Array Attributes.

An Array Attribute is an [Attribute](https://docs.derivative.ca/Attribute "Attribute") with multiple **elements** of a specific **Attribute Data Type** , for example an attribute made of 12 intergers.

Attributes make up the numeric data blocks of [POPs](https://docs.derivative.ca/POP "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.

POPs (Point Operators) is a new [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that works with 3D geometry or any general numeric data, runs on GPU-accelerated graphics cards or chips, is rendered as images or passed to devices like DMX lighting, LED arrays, lasers or other external systems.
