---
url: https://docs.derivative.ca/ParGroup
category: Glossary
title: ParGroup
---

# ParGroup

A ParGroup or Parameter Group is a group of related parameters that you can set and get as a whole instead of its individual parameters, for example, ParGroup `t` is `tx ty tz`.

##  ParGroup

A [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") is a group of related parameters. It is often more natural to work with the [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") as a whole instead of its individual [parameters](../SOPs/Par_Class.md "Par Class").

Often all parameters sharing the same line on a [parameter dialog](Parameter_Dialog.md "Parameter Dialog") belong to the same [ParGroup](../Python/ParGroup_Class.md "ParGroup Class"). For example, in the [Transform TOP](../TOPs/Transform_TOP.md "Transform TOP"), _Translate_ is a type of [ParGroup](../Python/ParGroup_Class.md "ParGroup Class"), with two primary [Par](../SOPs/Par_Class.md "Par Class") objects: _tx_ , _ty_ and a unit [Par](../SOPs/Par_Class.md "Par Class").

ParGroups with only single elements are also possible. For example, the _Uniform Scale_ parameter of the [ Geometry Object](Geometry_COMP.md "Geometry COMP") belongs to a [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") with only one parameter. Note that ParGroups with multiple elements only contain numeric elements. Strings only exist in ParGroups of size 1.

See also [ParGroup Execute DAT](../DATs/ParGroup_Execute_DAT.md "ParGroup Execute DAT")

###  Basic Usage

The following example assumes _n_ is a [Transform TOP](../TOPs/Transform_TOP.md "Transform TOP") with its translate set to _1, 2_ Like _n.par_ , _n.parGroup_ can be used to access individual [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") objects:
```
t = n.parGroup.t     # set t to the Translate ParGroup
t = n.parGroup["t"]  # for convenience, name mapping access also works. Exact names only, no wildcards.
```

From here, most of the members and methods available to [Par](../SOPs/Par_Class.md "Par Class") objects are also available to [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") objects. Instead of returning one value however, they return a tuple of values where applicable.
```
t.expr   # returns (None, None) if the translate parameter has no expressions set
```

###  Evaluation

```
t.eval()   # returns (1, 2)
```

Note that if the [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") contains only a single element, such as the _Uniform Scale_ parameters, its _eval()_ method still returns a tuple and not a single value:
```
n.parGroup.scale.eval()  # returns (1.0,)
```

###  Size, Mapping and Iteration

```
len(t)   # returns 2, as this ParGroup contains 2 primary parameters.  The unit parameter is ''not'' included here.

t[1].name   # returns 'ty', since t[1] return Par object ty.

[i.name for i in t] # returns [‘tx’, ‘ty’] #primary parameters only

[i.name for i in t.pars()] # returns [‘tx’, ‘ty’, 'unit'] #all parameters
```

The pars method is identical to OP.pars, and returns **all** parameters in this ParGroup, primary or otherwise.

###  Assignment

ParGroups can be assigned a single value (a scalar) or a tuple of the same size. Note in the following examples, both tuples () and lists [] are interchangeable. In some cases though, using list syntax is less ambiguous: _[3] vs (3,),_ since _(3)_ is not a tuple.
```
n.parGroup.t = (4, 5)    #assign tx=4, ty=5
n.parGroup.t = [4,5]    # any iterable object of size 2 will do

n.parGroup.t = 5             #assign 5 to tx, ty
n.parGroup.t = n.parGroup.p   #assign pivot values to translate parameter.

n.parGroup.t = (1,2,3)  # error, cannot assign 3 elements to 2.
```

Note that the above also works when assigning directly to the Parameter val members:
```
n.parGroup.t.val = (1,2)
```

###  Arithmetic

ParGroups can be used in some arithmetic expressions directly, as operations are applied pairwise:
```
n.parGroup.t + 1  # returns (2.0, 3.0)
n.parGroup.t + (1,2)  #returns (2.0, 4.0)
```

To ensure forward compatibility though, it is best to create [ParGroup](../Python/Vector_Class.md "Vector Class") objects where applicable:
```
tdu.Vector(n.parGroup.t) + (1,2)   #returns a Vector with values 2.0  4.0
```

###  Casting

Casting a [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") to a bool will always raise an exception, as the [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") will always be a non-empty tuple, thus normally returning _True_. This could lead to confusion where bool(n.parGroup.button) always returns _True_ , leading one to assume the button value itself is true.

Casting a [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") to a float or int however, will only succeed if that [ParGroup](../Python/ParGroup_Class.md "ParGroup Class") contains exactly 1 element, as in the case of a _Uniform Scale_ for example:
```
5 + float(n.parGroup.scale)
```

This also means _op('geo1').parGroup.scale_ for example, can be used in a single parameter expression expecting a numeric avlue.

Furthermore, the global functions _any()_ and _all()_ work as expected, given that ParGroups behave like tuples:
```
	any(n.parTuple.t)	# true if any of tx,ty,tz non-zero
	all(n.parTuple.t)	# true if all of tx,ty,tz non-zero
```

A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.

A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup `t` is `tx ty tz`.

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").
