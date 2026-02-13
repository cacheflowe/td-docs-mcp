---
url: https://docs.derivative.ca/AbsTime_Class
category: Python
title: AbsTime_Class
---

# absTime Class

This class contains information on the "[absolute time](https://docs.derivative.ca/Absolute_Time "Absolute Time")", the time TouchDesigner has been running since the process started. It can be accessed with the abstime object, found in the automatically imported [td module](https://docs.derivative.ca/Td_Module "Td Module"). It is paused only with the power on/off button at the top of the UI, or with the power() method in the [td module](https://docs.derivative.ca/Td_Module "Td Module") or pausing the root timeline. Absolute time is the same for all nodes. See [absolute time](http://en.wikipedia.org/wiki/Absolute_time_and_space).

## Members
`frame` → `float` **(Read Only)** :
Absolute total number of frames played since the application started. Paused only with the power On/Off or with power() or pausing the main timeline.

```
absTime.frame
tdu.rand(absTime.frame + .1) # a unique random number that is consistent across all nodes, changing every frame

```

`seconds` → `float` **(Read Only)** :
Absolute total seconds played since the application started. Paused only with the power On/Off or with power() or pausing the main timeline.

`step` → `float` **(Read Only)** :
Number of absolute frames elapsed between start of previous and current frame. When this value is greater than 1, the system is dropping frames.

`stepSeconds` → `float` **(Read Only)** :
Absolute time elapsed between start of previous and current frame.
## Methods
No operator specific methods.

Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off or the root timeline is paused.
