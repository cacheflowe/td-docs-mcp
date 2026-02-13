---
url: https://docs.derivative.ca/Position_Class
category: Python
title: Position_Class
---

# Position Class
The position class holds a single 3 component position. A position is a single point in space, and it's important to use a position or [vector](https://docs.derivative.ca/Vector_Class "Vector Class") as appropriate for the data that is being calculated, since matrix operations on them will end in different results. When being multiplied by a [Matrix](https://docs.derivative.ca/Matrix_Class "Matrix Class"), this class will implicitly have a 4th component (W component) of 1. If the Matrix is a projection matrix that will cause the W component to become something other than 1, all 4 components will be divided by W to make the position homogeneous again. A new position can be created without any arguments, with 3 arguments for the x,y,z values, or with a single argument which is a variable that has 3 entries such as a list of length 3, or another position or vector.
**Note:** tdu.___ and TDU.___ can be used interchangeably. In general, TDU.___ is used to represent a class, while tdu.___ is used for the instantiator function.
Examples of creating a position:

```
p = tdu.Position() # starts as (0, 0, 0)
p2 = tdu.Position(1, 5, 0)
values = [0, 1, 0]
p3 = tdu.Position(values)

```

## Instantiators
`TDU.Position(*args)`→ `TDU.Position`:
Create a new position object. The following argument forms are valid instantiators:
  * `tdu.Position()` - (0, 0, 0)
  * `tdu.Position(vector : TDU.Vector)` - copy the vector values
  * `tdu.Position(position: TDU.Position)` - copy the position
  * `tdu.Position(x : float, y : float,  z : float)` - (x, y, z)
  * `tdu.Position(f : float)` - (f, f, f)
  * `tdu.Position(pos : list)` - 3 item list to fill position

## Members
`x` → `float` :
Gets or sets the X component of the position.

`y` → `float` :
Gets or sets the Y component of the position.

`z` → `float` :
Gets or sets the Z component of the position.
## Methods
`translate(x, y, z)`→ `None`:
Translates the position by the specified values.
  * x, y, z - The values to translate by.

```
p.translate(5, 2, 0)

```

`scale(x, y, z)`→ `None`:
Scales each component of the position by the specified values.
  * x, y, z - The values to scale each component of the position by.

```
p.scale(1, 2, 1)

```

`copy()`→ `TDU.Position`:
Returns a new position that is a copy of the position.

```
newV = v.copy()

```

###  Special Functions
`TDU.Position[i]`→ `float`:
Gets or sets the component of the position specified by i, where i can be 0, 1, or 2.

```
y = p[1]
p[1] = y + 2.0

```

`TDU.Position * float`→ `TDU.Position`:
Scales the position by the give float scalar and returns a new Position as the result.

```
p = p * 0.1
p = 0.1 * p

```

`TDU.Position + float`→ `TDU.Position`:
Adds the given scalar to all 3 components of the position and returns a new position as the result.

```
p = p + 1.2
p = 1.2 + p

```

`TDU.Position - float`→ `TDU.Position`:
Subtracts the given scalar from all 3 components of the position and returns a new position as the result.

```
p = p - 1.2
p = 1.2 - p

```

`TDU.Vector + TDU.Position`→ `TDU.Position`:
Adds the vector to the position. ie. it displaces the given position by the vector. Returns a new position as the result.

```
p2 = v + p1
p2 = p1 + v

```

`TDU.Position - TDU.Vector`→ `TDU.Position`:
Subtracts the vector from the position. Notice that the reverse is not a legal operation: subtracting a position from a vector does not have any meaning. Returns a new position with the results.

```
p2 = p1 - v

```

`TDU.Position - TDU.Position`→ `TDU.Vector`:
Subtracts the two positions to create a vector that is pointing from the 2nd one to the 1st one, with length equal to the distance between the positions.

```
v = p1 - p2

```

`TDU.Position += float`→ `None`:
Adds the given scalar to all 3 components of the position, the position will contain the result of the operation.

```
p += 0.1

```

`TDU.Position += TDU.Vector`→ `None`:
Displaces the position by the given vector, the position will contain the result of the operation.

```
p += v

```

`TDU.Position -= float`→ `None`:
Subtracts the given scalar from all 3 components of the position, the position will contain the result of the operation.

```
p -= 0.4

```

`TDU.Position -= TDU.Vector`→ `None`:
Displaces the position by the given vector, the position will contain the result of the operation.

```
p -= v

```

`TDU.Matrix * TDU.Position`→ `TDU.Position`:
Multiplies the Position by the matrix and returns the a new position as the result.

```
p2 = m * p1

```

`TDU.Position / float`→ `TDU.Position`:
Divides each component of the position by the scalar and returns the a new position as the result.

```
p2 = p1 / 2.0

```

`TDU.Position *= TDU.Matrix`→ `None`:
Multiplies the position by the matrix, the position will contain the result. The is position multiplied on the right of the matrix. It is the equivalent of doing Position = Matrix * Position.

```
p *= m

```

`TDU.Position *= float`→ `None`:
Scales all 3 components of the position by the given scalar. The position will contain the result.

```
p *= 1.3

```

`TDU.Position *= TDU.Position`→ `None`:
Component-wise multiplies the 3 components of the first position by the 3 components of the 2nd position.

```
p1 *= p2

```

`abs(TDU.Position)`→ `TDU.Position`:
Returns a new position with all 3 components being the absolute value of the given position's components.

```
p2 = abs(p1)

```

`-TDU.Position`→ `TDU.Position`:
Returns a new position with all 3 component's being negated.

```
p2 = -p1

```
