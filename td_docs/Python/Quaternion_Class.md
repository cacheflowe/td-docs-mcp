---
url: https://docs.derivative.ca/Quaternion_Class
category: Python
title: Quaternion_Class
---

# Quaternion Class
Holds a Quaternion object which can be used to manipulate rotations in various ways.
**Note:** tdu.___ and TDU.___ can be used interchangeably. In general, TDU.___ is used to represent a class, while tdu.___ is used for the instantiator function.
Quaternions can be constructed using a few different ways to describe the initial rotation:

```
# From Euler Angles, rx, ry, rz in degrees
q = tdu.Quaternion(30, 5, -5)
q = tdu.Quaternion([30, 5, -5])
# From an angle and a rotation axis
q = tdu.Quaternion(30, tdu.Vector(0, 1, 0))
# From two vectors, rotate from the first vector to the
second vector
q = tdu.Quaternion(tdu.Vector(1, 0, 0), tdu.Vector(0, 1, 0))
# From a set of 4 quaternion values
q = tdu.Quaternion(x, y, z, w)
q = tdu.Quaternion([x, y, z, w])
# From a Matrix
q = tdu.Quaternion(tdu.Matrix())
# From a quaternion
q = tdu.Quaternion(tdu.Quaternion())

```

Quaternions can be used like simple Python lists:

```
print(q[1])		# same as q.y
q[2] = 0		# same as q.z

```

See also [Transform CHOP](https://docs.derivative.ca/Transform_CHOP "Transform CHOP") which accepts, manipulates and outputs quaternions as sets of CHOP channels.

## Instantiators
`TDU.Quaternion(*args)`→ `TDU.Quaternion`:
The following argument forms are valid instantiators:
  * `tdu.Quaternion()` - (0, 0, 0, 1)
  * `tdu.Quaternion(quaternion : TDU.Quaternion)` - copy the quaternion in the argument
  * `tdu.Quaternion(rx : float, ry : float, rz : float)` - from Euler angles in degrees
  * `tdu.Quaternion(rot : float, axis: TDU.Vector[](https://docs.derivative.ca/Vector_Class "Vector Class"))` - from a rotation angle and a rotational axis
  * `tdu.Quaternion(v1 : TDU.Vector[](https://docs.derivative.ca/Vector_Class "Vector Class"), v2: TDU.Vector[](https://docs.derivative.ca/Vector_Class "Vector Class"))` - rotate from v1 to v2
  * `tdu.Quaternion(x : float, y : float, z : float, w : float)` - from quaternion values
  * `tdu.Quaternion(xyzw : list)` - from quaternion values in a list
  * `tdu.Quaternion(matrix : TDU.Matrix)` - from a matrix

## Members
`x` → `float` :
Get or set the x component of the quaternion.

`y` → `float` :
Get or set the y component of the quaternion.

`z` → `float` :
Get or set the z component of the quaternion.

`w` → `float` :
Get or set the w component of the quaternion.
## Methods
`lerp(q2, factor)`→ `TDU.Quaternion`:
Returns the linear interpolation of the quaternion with another quaternion and an interpolation factor.
The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc. The interpolation factor must be between 0 and 1.

```
q3 = q.lerp(q2, factor)

```

`length()`→ `float`:
Returns the length of the quaternion.

```
l = q.length()

```

`cross(q2)`→ `TDU.Vector`:
Returns the cross product of the quaternion and argument.
The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc.

```
l = q.cross(q2)

```

`rotate(vec)`→ `TDU.Vector`:
Rotates a vector using the current quaternion. Returns a new vector.

```
v2 = q.rotate(v1)

```

`slerp(q2, factor)`→ `TDU.Quaternion`:
Returns the spherical interpolation of the quaternion with another quaternion and an interpolation factor.
The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc.

```
q3 = q.slerp(q2, factor)

```

`eulerAngles(order='xyz')`→ `tuple`:
Returns euler angles in degrees as a tuple (i.e. pitch as x, yaw as y, roll as z) from current quaternion and a rotation order. The 'order' argument can be set to any valid rotation order which by default is set to 'xyz'.

```
r = q.eulerAngles(order='xyz')

```

`fromEuler(order='xyz')`→ `tuple`:
Returns and set the current quaternion from euler angles in degrees as a 3 inputs argument (i.e. pitch as x, yaw as y, roll as z). The 'order' argument can be set to any valid rotation order which by default is set to 'xyz'.

```
r = q.fromEuler(order='xyz')

```

`axis()`→ `TDU.Vector`:
Returns the rotation axis vector of the quaternion.

```
v = q.axis()

```

`dot(q2)`→ `float`:
Returns the dot product of the quaternion and the argument.
The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc.

```
l = q.dot(q2)

```

`exp()`→ `TDU.Quaternion`:
Returns the exponential of the quaternion as a new quaternion.

```
q2 = q.exp()

```

`copy()`→ `TDU.Quaternion`:
Creates a copy of the quaternion with separate values.

`log()`→ `TDU.Quaternion`:
Returns the natural logarithm of the current quaternion as a new quaternion.

```
l = q.log()

```

`inverse()`→ `None`:
Invert the quaternion in place.

```
q.inverse()

```

`angle()`→ `float`:
Returns the rotation angle (in degrees) of the quaternion.

```
a = q.angle()

```

###  Special Functions
`Quaternion *= Quaternion`→ `TDU.Quaternion`:
Applies the rotation of one quaternion to another quaternion.

```
# apply rotation of q2 to q1
q1 *= q2

```

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
