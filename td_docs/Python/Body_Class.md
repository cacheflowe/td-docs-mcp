---
url: https://docs.derivative.ca/Body_Class
category: Python
title: Body_Class
---

# Body Class
The Body Class describes the contents of a single body within an [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP"). The [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP") has a list of all its bodies.

## Members
`index` → `int` **(Read Only)** :
The index of this Body in its [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP") (owner).

`owner` → `OP` **(Read Only)** :
The [Actor COMP](https://docs.derivative.ca/Actor_COMP "Actor COMP") to which this body belongs.

`rotate` → `tdu.Vector` :
Get or set the body's rotation in world space.

`translate` → `tdu.Position` :
Get or set the body's translation in world space.

`angularVelocity` → `tdu.Vector` :
Get or set the body's angular velocity.

`linearVelocity` → `tdu.Vector` :
Get or set the body's linear velocity.
## Methods
`applyImpulseForce(force, relPos=None)`→ `None`:
Applies impulse force to a body in a Bullet simulation.
  * force - The impulse force to apply to the body.
  * relPos (Keyword, Optional) - If specified, applies the force at the relative position, otherwise applied at (0,0,0).

`applyTorque(torque)`→ `None`:
Applies torque to a body in a Bullet simulation. The torque will only be applied for a single frame.
  * torque - The torque to apply to the body this frame.

`applyImpulseTorque(torque)`→ `None`:
Applies impulse torque to a body in a Bullet simulation.
  * torque - The impulse torque to apply to the body.

`applyForce(force, relPos=None)`→ `None`:
Applies force to a body in a Bullet simulation. The force will only be applied for a single frame.
  * force - The force to apply to the body this frame.
  * relPos (Keyword, Optional) - If specified, applies the force at the relative position, otherwise applied at (0,0,0).
