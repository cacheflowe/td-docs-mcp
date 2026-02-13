---
url: https://docs.derivative.ca/Runs_Class
category: Python
title: Runs_Class
---

# Runs Class
The Runs class describes the set of all delayed [run objects](https://docs.derivative.ca/Run_Class "Run Class"). It can be accessed with the runs object, found in the automatically imported [td module](https://docs.derivative.ca/Td_Module "Td Module"). See [Run Command Examples](https://docs.derivative.ca/Run_Command_Examples "Run Command Examples") for more info.

```
print(len(runs))	# number of active run objects
print(runs[0])		# first run object
for r in runs:
	r.kill()		# kill all run objects

```

## Members
No operator specific members.

## Methods
No operator specific methods.
