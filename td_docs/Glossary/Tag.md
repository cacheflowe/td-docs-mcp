---
url: https://docs.derivative.ca/Tag
category: Glossary
title: Tag
---

# Tag

Each operator can have a set of text strings that are its "tags". For example, tags can be used to categorize and gather components of a certain user-defined classification, such as 'color filter' or 'audio effect'.

You can put tags on operators in the UI at the top of the Parameter dialog, and via python using, for example `node.tags = ['tag 1', 'tag 2']`

You can search for operators with specific tags using `OP.findChildren()` method and the [OP Find DAT](../DATs/OP_Find_DAT.md "OP Find DAT").

See [OP_Class](../Python/OP_Class.md "OP Class")

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](Node.md "Node").
