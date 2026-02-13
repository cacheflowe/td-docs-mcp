---
url: https://docs.derivative.ca/Font_SOP
category: SOPs
title: Font_SOP
---

# Font SOP
## Summary

**Note** : Font SOP deprecated build 2019.14650, use [Text SOP](https://docs.derivative.ca/Text_SOP "Text SOP").
The Font SOP allows you to create text in your model from Adobe Type 1 Postscript Fonts.
To install fonts, copy the font files to the `$TFS/touch/fonts` directory of your installation path. They will be ready to be used in the Font SOP after restarting TouchDesigner.
[fontSOP_Class](https://docs.derivative.ca/FontSOP_Class "FontSOP Class")

## Parameters - Page
- Primitive Type `type` - ⊞ - Select from the following types. For information on the different types, see the Geometry Types section. Bzier Curves and Polygons provide the most efficient use of memory, because they use polygons for letters containing straight segments, and Bzier curves for all others.
**Note:** Due to an Open GL bug, holes in Bzier fonts may shade incorrectly.
  * Bezier Curves and Polygons `bezierpoly` -
  * Beziers Only `bezier` -
  * Polygons Only `poly` -

- Font `file` - Choose the font to create the text. By clicking on the + button a File Dialog will appear, and clicking menu drop down brings up a menu of the most used fonts.
- Text `text` - Enter the text you want to generate here.
Your text can contain the following special characters:
  * ` \ ` - Take the next character literally (so you can use the / and ` characters in your text);
  * ` `string` ` - Evaluate the string contained by the backquotes (above the T key) as an expression;
  * ` \n ` - Start a new line;
  * ` \xxx ` - Specify a character by it's ascii code (e.g. \007).

**For Example:** If you put something like `\\$F3` in the text string, you should see all the possible characters of a font as you play the animation (set the last frame to 256).
**Entering Expressions as Text** - You can also use expressions for the text.
**For Example:**`me.time.frame` - will display the current frame.
`op('null1')['chan1']` - will display the current value of channel chan1 in CHOP `null1`.
`'hello world'[int(me.time.frame)%11]` - causes the eleven letters of the text to appear in succession during the first eleven frames.
**Other Methods of Entering Text -** You can use the `\xxx` decimal notation to specify characters. The available characters will depend on the font type used.
**For Example:** \065 - will display '`a`'.
You can also use the [Par Class](https://docs.derivative.ca/Par_Class "Par Class") to set text in the Font SOP. This can be done from the textport, a [Logic CHOP](https://docs.derivative.ca/Logic_CHOP "Logic CHOP") or [Expression CHOP](https://docs.derivative.ca/Expression_CHOP "Expression CHOP"), or any script. (See [Scripting](https://docs.derivative.ca/Introduction_to_Python_Tutorial "Introduction to Python Tutorial") articles)
**For Example:**`op('font1').par.text = 'hello world'` - will display the words: hello world
- Center Text Horizontally `hcenter` - This check box allows you to center the text horizontally about X = 0.
- Center Text Vertically `vcenter` - This check box allows you to center the text vertically about Y = 0.
- Translate `t` - ⊞ - Translates the geometry in x, y and z.
  * X `tx` -
  * Y `ty` -
  * Z `tz` -

- Scale `s` - ⊞ - Scales the text in the X and Y axis.
  * X `sx` -
  * Y `sy` -

- Kerning `kern` - ⊞ - Letter spacing in the X direction. Line spacing in the Y direction if there are multiple lines. If you need manual character-by-character, you can do it in Model mode.
  * X `kernx` -
  * Y `kerny` -

- Italic Angle `italic` - Doesn't actually give an italic version of the font, but rather obliques the text by shearing it the specified number of degrees. A negative number makes the text slant to the left.
- Level of Detail `lod` - Adobe fonts are defined by Bzier curves. If polygons only is selected, the Font SOP converts these to polygons. This value adjusts the number of points in the polygons that it gets converted to.
- Hole Faces `hole` - Generates holes in polygons and Bzier faces.
- Texture Coordinates `texture` - ⊞ - This adds uv coordinates to the geometry created by the Font SOP.
  * Off `off` - No uv coordinates added.
  * Orthographic `ortho` - Orthographic uv coordinates added.
