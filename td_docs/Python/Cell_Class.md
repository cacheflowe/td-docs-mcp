---
url: https://docs.derivative.ca/Cell_Class
category: Python
title: Cell_Class
---

# Cell Class
The Cell Class describes the contents of a single cell from a [DAT](https://docs.derivative.ca/DAT "DAT") operator table. The [DAT Class](https://docs.derivative.ca/DAT_Class "DAT Class") offers many ways of accessing its individual cells. [DAT](https://docs.derivative.ca/DAT "DAT") cells are always internally stored as strings, but may be accessed as numeric values.
**IMPORTANT** : `op('table1')[1,2]` is this python cell object which usually gets converted for you to the string in the cell. More safely use `op('table1')[1,2].val` which always gives you the string.

## Members
`valid` → `bool` **(Read Only)** :
True if the referenced cell currently exists, False if it has been deleted.

`row` → `int` **(Read Only)** :
The numeric row of the cell.

`col` → `int` **(Read Only)** :
The numeric column of the cell.

`owner` → `OP` **(Read Only)** :
The [OP](https://docs.derivative.ca/OP_Class "OP Class") to which this object belongs.

`val` → `str` :
Get or set the cell contents, which are always stored as a string value.
## Methods
`run(*args, endFrame=False, fromOP=None, asParameter=False, group=None, delayFrames=0, delayMilliSeconds=0, wallTime=False, delayRef=None)`→ `td.Run`:
[Run](https://docs.derivative.ca/Run_Class "Run Class") the contents of the cell as a script, returning a Run object which can be used to optionally modify its execution.
  * endFrame - (Keyword, Optional) If set to True, the execution will be delayed until the end of the current frame.
  * fromOP - (Keyword, Optional) Specifies an optional [operator](https://docs.derivative.ca/OP_Class "OP Class") from which the execution will be run relative to.
  * asParameter - (Keyword, Optional) When fromOP used, run relative to a parameter of fromOP.
  * group - (Keyword, Optional) Can be used to specify a group label string. This label can then be used with the [td.runs](https://docs.derivative.ca/Runs_Class "Runs Class") object to modify its execution.
  * delayFrames - (Keyword, Optional) Can be used to delay the execution a specific amount of frames.
  * delayMilliSeconds - (Keyword, Optional) Can be used to delay the execution a specific amount of milliseconds. This value is rounded to the nearest frame.
  * wallTime - (Keyword, Optional) Setting this to True results in the delay options being based on actual elapsed time instead of elapsed frames.
  * delayRef - (Keyword, Optional) Specifies an optional [operator](https://docs.derivative.ca/OP_Class "OP Class") from which the delay time is derived. If none is provided, will use the cell owner.
  * arg - (Optional) Arguments that will be made available to the script in a local tuple named args.

`offset(r, c)`→ `Cell | None`:
The cell offset to this cell by the specified amount, or None.
  * r - The number of rows from the cell. Positive values count down, while negative values count up.
  * c - The number of columns from the cell. Positive values count right, while negative values count left.

```
c = op('table1')['March', 'Sales']
d = c.offset(-1, 2)  # one row up, two columns right of cell C

```

###  Casting to a Value
The Cell Class implements all necessary methods to be treated as a number or a string, which in this case gets or sets its value. Therefore, an explicit call to get or set val is unnecessary when used in a parameter, or in an expression. For example, the following are equivalent in a numeric parameter:

```
(float)n[1,2]
n[1,2].val
n[1,2]

```

Or equivalently, for a string parameter:

```
(str)n[1,2]
n[1,2].val
n[1,2]

```

Similarly, expressions on Cells will autocast themselves automatically:

```
n[1,2].val + 1 # string plus 1, error
n[1,2] + 1 # autocasted value plus 1

```

In the second case, the contents of the Cell are used to determine if numeric or string operations should be used. For example, if cell n[1,2] contains "3" then:

```
n[1,2].val + n[1,2].val # will return "33" since .val is a string.

```

However,

```
n[1,2] + n[1,2] # will return 6 since the contents "3" are numeric.

```

If n[1,2] contained a non-numeric value such as "a" then

```
n[1,2] + n[1,2] # will return "aa"

```

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
