---
url: https://docs.derivative.ca/ArcBall_Class
category: Python
title: ArcBall_Class
---

# ArcBall Class
Encapsulates many aspects of 3D viewer interaction. Rotation via arcball, translation and scale.

```
a = TDU.ArcBall(forCamera=False)

```

## Instantiators
`TDU.ArcBall(forCamera=False)`→ `TDU.ArcBall`:
Create a new ArcBall object
  * `forCamera` - If True, matrices used are from the camera perspective (the world matrices are inverted before being returned or used)

## Members
No operator specific members.

## Methods
`beginPan(u, v)`→ `None`:
Begin a pan at at the given u and v.

```
m.beginPan(.1, .2)

```

`beginRotate(u, v)`→ `None`:
Begin an arcball rotation at the given u and v.

```
m.beginRotate(.1, .2)

```

`beginDolly(u, v)`→ `None`:
Begin a dolly at at the given u and v.

```
m.beginDolly(.1, .2)

```

`pan(u, v)`→ `None`:
Pan the view by the given x and y.

```
m.pan(.1, .2)

```

`panTo(u, v, scale=1.0)`→ `None`:
Pan from the u,v given in the last call to beginPan() to the given u and v, applying a scale as well to the pan amount.
  * scale - (Keyword, Optional) Scale the operation by this amount.

```
m.panTo(.1, .2)

```

`rotateTo(u, v, scale=1.0)`→ `None`:
Rotates the arcball to the given u and v position.
  * scale - (Keyword, Optional) Scale the operation by this amount.

```
m.rotateTo(.1, .2)

```

`dolly(z)`→ `None`:
Dolly the view by the given z value.

```
m.dolly(.3)

```

`dollyTo(u, v, scale=1.0)`→ `None`:
Dolly from the u,v given in the last call to beginDolly() to the given u and v, applying a scale as well to the dolly amount.(Keyword, Optional)
  * scale - Scale the operation by this amount.

```
m.dollyTo(.1, .2)

```

`transform()`→ `TDU.Matrix`:
Gets the current transform [matrix](https://docs.derivative.ca/Matrix_Class "Matrix Class") for the arcball.

```
m.transform()

```

`setTransform(matrix:TDU.Matrix[](https://docs.derivative.ca/Matrix_Class "Matrix Class"))`→ `None`:
Sets the current transform matrix for the arcball. Scales in the given matrix will be ignored.

```
m.setTransform(m)

```

`identity()`→ `None`:
Resets all values of the ArcBall to the default state.

```
m.identity()

```
