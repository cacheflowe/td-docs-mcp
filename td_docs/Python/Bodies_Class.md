---
url: https://docs.derivative.ca/Bodies_Class
category: Python
title: Bodies_Class
---

# Bodies Class
The Bodies Class describes the set of all [Bodies](https://docs.derivative.ca/Body_Class "Body Class") in an [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP") (Actor COMPs are used by the [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP") and [Nvidia Flex Solver COMP](https://docs.derivative.ca/Nvidia_Flex_Solver_COMP "Nvidia Flex Solver COMP")). The Bodies object is accessed via its Actor COMP and is used much like a Python list.

```
bodies = op('bsolver1/actor1').bodies	# get the Bodies object
print(len(bodies))						# number of Bodies
print(bodies[0])						# first Body in the list
for b in bodies:
	print(b)							# print all Bodies

```

## Members
No operator specific members.

## Methods
No operator specific methods.
