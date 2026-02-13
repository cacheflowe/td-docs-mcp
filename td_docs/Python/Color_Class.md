---
url: https://docs.derivative.ca/Color_Class
category: Python
title: Color_Class
---

# Color Class
The color class holds a single 4 component color (R, G, B, A).
**Note:** tdu.___ and TDU.___ can be used interchangeably. In general, TDU.___ is used to represent a class, while tdu.___ is used for the instantiator function.

```
v = tdu.Color() # starts as (0, 0, 0, 1)
v2 = tdu.Color(0, 0, 1, 1)
values = [0, 1, 0, 1]
v3 = tdu.Color(values)
green = v3[1] # access individual elements by index. Same as v3.g

```

## Instantiators
`TDU.Color(*args)`→ `TDU.Color`:
The following argument forms are valid instantiators:
  * `tdu.Color()` - black with full opacity (0, 0, 0, 1)
  * `tdu.Color(color : TDU.Color)` - copy the color in the argument
  * `tdu.Color(rgba: list)` - list of 4 values as a color (r, g, b, a)
  * `tdu.Color(f: float)` - (f, f, f, 1)
  * `tdu.Color(r : float, g : float, b : float, a: float)` - separate arguments as color elements

## Members
`r` → `float` :
Gets or sets the red component of the color.

`g` → `float` :
Gets or sets the green component of the color.

`b` → `float` :
Gets or sets the blue component of the color.

`a` → `float` :
Gets or sets the alpha component of the color.
## Methods
`[index]`→ `float`:
Sample values may be accessed from a Color using the [] subscript operator.

`copy()`→ `TDU.Color`:
Returns a new color that is a copy of the color.
