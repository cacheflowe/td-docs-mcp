---
url: https://docs.derivative.ca/SysInfo_Class
category: Python
title: SysInfo_Class
---

# SysInfo Class
The SysInfo class describes current system information. **Note:** It can be accessed with the `sysinfo` object, found in the automatically imported [td module](https://docs.derivative.ca/Td_Module "Td Module").

```
# return the amount of available ram
sysinfo.ram

```

## Members
`numCPUs` → `int` **(Read Only)** :
The number of CPUs/cores on the system.

`ram` → `float` **(Read Only)** :
Amount of available RAM memory.

`numMonitors` → `int` **(Read Only)** :
The number of monitors.

`xres` → `int` **(Read Only)** :
The system's current monitor resolution width.

`yres` → `int` **(Read Only)** :
The system's current monitor resolution height.

`tfs` → `str` **(Read Only)** :
The path to the TFS directory.

`MIDIInputs` → `list[str]` **(Read Only)** :
A list of all MIDI Input device names.

`MIDIOutputs` → `list[str]` **(Read Only)** :
A list of all MIDI Output device names.

`GPUName` → `str` **(Read Only)** :
The name of the selected GPU.

`GPUID` → `str` **(Read Only)** :
The UUID of the selected GPU.

`GPUPlatformID` → `str` **(Read Only)** :
The OS identifier of the selected GPU.
## Methods
No operator specific methods.

The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.
