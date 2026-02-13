---
url: https://docs.derivative.ca/Timecode_Class
category: TOPs
title: Timecode_Class
---

# Timecode Class
The Timecode class holds a timecode value. See also [Timecode](https://docs.derivative.ca/Timecode "Timecode") and [Timecode CHOP](https://docs.derivative.ca/Timecode_CHOP "Timecode CHOP").
  * `str` (Optional) - Initializes the Timecode object from a Timecode formatted String: ie. `hh:mm:ss:ff` or `hh:mm:ss.ff`
  * `fps` - (Keyword, Optional) Initialize the Timecode object with the specified fps. If not specified it will be initialized with the rate of the local time.
  * `hour` - (Keyword, Optional) Specify the hour. Should be left blank if a String arg is provided. 0 by default.
  * `minute` - (Keyword, Optional) Specify the minute. Should be left blank if a String arg is provided. 0 by default.
  * `second` - (Keyword, Optional) Specify the second. Should be left blank if a String arg is provided. 0 by default.
  * `frame` - (Keyword, Optional) Specify the frame. Should be left blank if a String arg is provided. 0 by default.
  * `negative` - (Keyword, Optional) Specify whether the Timecode is negative. Should be left blank if a String arg is provided. False by default.
  * `smpte` - (Keyword, Optional) Specify whether the Timecode is SMPTE standard. True by default. If the the `smpte` flag is OFF, you can break the standard and have time greater than 24 hours, negative time, and any number of frames per second above SMPTE's 60 limit.
  * `length` - (Keyword, Optional) Specify a custom length for the timecode. Used in conjunction with countdown. Must be greater than 0.
  * `cycle` - (Keyword, Optional) Specify if the timecode cycles back to the first value upon reaching the custom length. True if it cycles, False if it holds the last value (ie. length). Only used if a custom length is set.
  * `autoDropFrame` - (Keyword, Optional) When enabled, will automatically calculate drop-frames for fractional rates (eg. 29.97). True by default.

```
t = tdu.Timecode() # 00:00:00:00 with fps=me.time.rate
t2 = tdu.Timecode('01:11:11:15', fps=30) # 01:11:11:15 with fps=30
t3 = tdu.Timecode(frame=185, fps=30) # 00:00:06:05 with fps=30
t4 = tdu.Timecode(hour=1, minute=2, second=3, frame=4, negative=True, fps=30) # -01:02:03:04 with fps=30

```



## Members
`countdown` → `tdu.Timecode` **(Read Only)** :
Return a Timecode Object of the difference between the length and the current time. If a custom length is not specified then it will use a default: 23:59:59:ff for SMPTE and 99:59:59:ff.

`dropFrame` → `bool` **(Read Only)** :
True if the Timecode is drop-frame, False otherwise.

`fps` → `float` :
Get or set the framerate (in frames per second) of the Timecode.

`frame` → `int` **(Read Only)** :
The Timecode frame: 0 to fps-1

`hour` → `int` **(Read Only)** :
The Timecode hour: 0 to 99 if non-SMPTE, 0 to 23 otherwise.

`minute` → `int` **(Read Only)** :
The Timecode minute: 0 to 59.

`second` → `int` **(Read Only)** :
The Timecode second: 0 to 59.

`negative` → `bool` :
True if the Timecode is negative, and False otherwise. Always False if the Timecode is following SMPTE standard.

`smpte` → `bool` :
True if the Timecode is SMPTE standard, and False otherwise. SMPTE Timecodes cannot be negative and cannot exceed 24 hours.

`text` → `str` **(Read Only)** :
Get the text format of the Timecode.

`totalFrames` → `int` **(Read Only)** :
The total number of Timecode frames, which is calculated from the hour, minute, second, frame values. Whether or not the Timecode is drop frame will also affect the value.

`totalSeconds` → `float` **(Read Only)** :
The total number of Timecode seconds, which is calculated from the hour, minute, second, frame values. Whether or not the Timecode is drop frame will also affect the value.

`cycle` → `bool` :
Get or set whether the timecode cycles. True if the Timecode cycles when the timecode value reaches the custom length (ie. specified with setLength()). If False then the timecode value will hold the last value (ie. length).
## Methods
`setComponents(hour, minute, second, frame, negative=False, fps=None)`→ `None`:
Set the Timecode from individual time components.
  * hour - The new hour value.
  * minute - The new minute value.
  * second - The new second value.
  * frame - The new frame value.
  * negative (Keyword, Optional) - Whether the new Timecode is negative. False by default.
  * fps (Keyword, Optional) - The Timecode's FPS. If not specified then the FPS will not change.
  * autoDropFrame - (Keyword, Optional) When enabled, will automatically calculate drop-frames for fractional rates (eg. 29.97). True by default.

```
n.setComponents(12, 22, 33, 45, negative=True, fps=60) -> new Timecode will be -12:22:33:45.

```

`setString(timecodeStr, fps=None)`→ `None`:
Set the Timecode from a string formated as [-]hh:mm:ss:ff.
  * timecodeStr - The string in the format: [-]hh:mm:ss:ff.
  * fps (Keyword, Optional) - The Timecode's FPS. If not specified then the FPS will not change.

```
n.setString('01:01:00:00', fps=60)

```

`setTotalFrames(totalFrames, fps=None)`→ `None`:
Set the Timecode to a single integer value representing the new total frames.
  * totalFrames - The new total frame value.
  * fps (Keyword, Optional) - The Timecode's FPS. If not specified then the FPS will not change.

```
n.setTotalFrames(120, fps=60) # new Timecode will be 00:00:02:00

```

`setLength(length)`→ `None`:
Set Timecode to a custom length. Useful in conjunction with countdown.
  * length - The new length, either a total frame value or a Timecode Object. Must be above 0.

```
n.setLength(600) # sets the length to 10 seconds for a Timecode with 60 FPS.

```

The [Frames](https://docs.derivative.ca/Frame "Frame")-per-Second that TouchDesigner's [Timeline](https://docs.derivative.ca/Timeline "Timeline") runs at. Set with `project.cookRate`.
The sub-[Family](https://docs.derivative.ca/Operator_Family "Operator Family") of [Component](https://docs.derivative.ca/Component "Component") types that are used to define and render 3D scenes. A [Geometry Component](https://docs.derivative.ca/Geometry_COMP "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](https://docs.derivative.ca/Camera_COMP "Camera COMP") and [Light COMP](https://docs.derivative.ca/Light_COMP "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.
