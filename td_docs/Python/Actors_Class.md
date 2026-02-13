---
url: https://docs.derivative.ca/Actors_Class
category: Python
title: Actors_Class
---

# Actors Class
The Actors Class describes the set of all [Actor COMPs](https://docs.derivative.ca/Actor_COMP "Actor COMP") used by the [Bullet Solver COMP](https://docs.derivative.ca/Bullet_Solver_COMP "Bullet Solver COMP") and [Nvidia Flex Solver COMP](https://docs.derivative.ca/Nvidia_Flex_Solver_COMP "Nvidia Flex Solver COMP"). It can be accessed with a Bullet Solver COMP. It can be accessed much like a Python list.

```
actors = op('bsolver1').actors	# get the Actors object
print(len(actors))				# number of Actors
print(actors[0])				# first Actor component in the list
for a in actors:
	print(a)					# print all Actors

```

## Members
No operator specific members.

## Methods
No operator specific methods.
