---
url: https://docs.derivative.ca/Introduction_to_Python_Tutorial
category: Learn
title: Introduction_to_Python_Tutorial
---

# Introduction to Python Tutorial
This tutorial is a general introduction to using [Python in TouchDesigner](https://docs.derivative.ca/Python "Python"). It doesn't require previous knowledge of Python, but it also doesn't go into "how to program". Resources for learning Python in general are [here](https://docs.derivative.ca/Category:Python#Learning_Python "Category:Python"). Experienced programmers will also be able to glean the basics of working in TouchDesigner quickly from the information here.

#  Python in Parameter Expressions
One of the easiest and most common places to use Python is in [parameter expressions](https://docs.derivative.ca/Parameter_Expression "Parameter Expression"). Parameter expressions allow you to write a one line Python program to set the value of a parameter. If the value of the expression changes, the parameter's value will update automatically.
This section will teach you all the basics of writing parameter expressions. For an extensive list of example TouchDesigner Python expressions, see the Expressions sections in [Python Tips](https://docs.derivative.ca/Python_Tips "Python Tips").
##  Writing a Simple Python Expression
To start with, create a [Text TOP](https://docs.derivative.ca/Text_TOP "Text TOP") using the [OP Create Dialog](https://docs.derivative.ca/OP_Create_Dialog "OP Create Dialog") by selecting _Text_ from the TOP family. If the [Parameter Dialog](https://docs.derivative.ca/Parameter_Dialog "Parameter Dialog") is not open, press p keyboard shortcut to open it.
To enter an expression into the 'Text' parameter, expand the parameter by clicking on its name, then press the blue square. It is now in expression mode. In the entry area, type
```
'Hello World!'

```

and press <Enter> key. You should see this:
[![Python HelloWorld.png](https://docs.derivative.ca/images/d/d5/Python_HelloWorld.png)](https://docs.derivative.ca/File:Python_HelloWorld.png)
The quotes are important to let Python know that "Hello World!" is a string (a series of letters) and not a command. Let's try a command now. Replace your expression with
```
absTime.frame

```

You can see the current frame changing now in both the parameter and the TOP display. Breaking down your short expression, there are two parts: `absTime` is TouchDesigner's [absolute time](https://docs.derivative.ca/AbsTime_Class "AbsTime Class") object, the `.` tells Python you want information inside it (called a member), and `frame` is the specific thing you want from `absTime`.
This simple process will let you create powerful interactions in TouchDesigner. In general, you just have to write short expressions in Python code explaining the piece of data you want. Part of the power of TouchDesigner is that (in most cases) this information will automatically be updated in your parameter if it changes.
##  Accessing Operators in Expressions: `me`, `op`, and `parent`
While `absTime` is a standalone object in TouchDesigner, most of the time you will be getting information from operators in your network. To use information from the operator that the expression is located on, you use the `me` object. In your Text DAT's 'Text' parameter expression, write `me.name`. Change the name of the operator by clicking on it and you will see the change reflected in the viewer.
For the next example, put down a [Rectangle TOP](https://docs.derivative.ca/Rectangle_TOP "Rectangle TOP") next to your Text TOP. The `op` command (op stands for "operator") lets you navigate to other operators and get information about them. In the Text TOP's 'Text' parameter, enter `op('rectangle1').type`. You should now have this:
[![Python Rectangle.png](https://docs.derivative.ca/images/2/27/Python_Rectangle.png)](https://docs.derivative.ca/File:Python_Rectangle.png)
As you probably figured out, the text now displays the operator type of _rectangle1_. Let's break down that expression a little more. The parentheses after `op` indicate that it is a "function". A function is a command that (usually) requires extra information, called arguments. The extra information in this case is `'rectangle1'`, which indicates which operator you want. After that, there is the familiar dot notation explaining that you want the `type` of the operator you named. The `'rectangle1'` is a Touchdesigner [path](https://docs.derivative.ca/Network_Path "Network Path") and you will use these all the time. You're probably familiar with this sort of notation from file browsers. In the examples below, you'll notice that paths that begin with `/` are "absolute" paths, starting from the project's top network level (also known as [root](https://docs.derivative.ca/Root "Root")), while ones that don't start with `/` are "relative" paths, meaning the path starts from the operator where the expression is located.
Path Expression | Result
---|---
`op('rectangle1')` | operator named _rectangle1_ next to me
`op('comp/rectangle1')` | operator named _rectangle1_ inside an operator named _comp_ next to me
`op('/project1')` | operator named _project1_ at the top network level
`op('/project1/rectangle1')` | operator named _rectangle1_ inside the operator named _project1_ , which is at the top network level
`op('..')` | the operator I am inside, a.k.a. my "parent"
`op('.')` | the operator containing the expression, same as `me`
`op('./rectangle1')` | an operator named _rectangle1_ inside me
Another common way of accessing operators is using `parent`. The `parent()` function returns the component one level up in the network hierarchy. You can give it a number as well, so `parent(2)` return the component two levels up in the network hierarchy.
###  Operator Shortcuts Using `parent` and `op`
The `parent` object can also be used to search upward in the hierarchy for a named **Parent Shortcut**. For example, in the 'Text' parameter of the Text TOP, enter this expression:
```
parent.Project

```

This returns the operator _/project1_ because in the tutorial file, the _project1_ component has the Parent Shortcut `Project`. You can see this by opening _/project1's_ parameter box and looking at the 'Parent Shortcut' parameter on the 'Common' page. Using this `parent.<shortcut>` syntax will search upward until an operator with that Parent Shortcut is found.
Similarly, the `op` object can be used to search anywhere in your TouchDesigner file for a component with a [Global OP Shortcut](https://docs.derivative.ca/Global_OP_Shortcut "Global OP Shortcut"). As an example, open _/project1's_ parameters again and type `MyGlobal` into the 'Global OP Shortcut' parameter on the 'Common' page. You can now get that operator by entering `op.MyGlobal` into the Text TOP's 'Text' parameter expression.
A couple important notes here. **Global OP Shortcuts must be unique.** You can only ever have one of a given name in your file. They are best used only for the most important and unique components in your file. **Parent Shortcuts don't have to be unique and the first one found searching upward will be returned.** These shortcuts are used often; it is highly recommended to give your custom components a Parent Shortcut at their top level.
You can also combine the various ways of looking for operators. For example `parent.Project.op('text1')` will return the operator _text1_ inside _/project1_.
##  Accessing Parameters in Expressions: `par`
Parameters on operators can be accessed by using the [par](https://docs.derivative.ca/Par_Class "Par Class") object. To start, expand the 'Size' parameter on _rectangle1_. You'll notice that there are two separate values, 'sizex' and 'sizey', which are the actual parameter names. Put 'sizey' into [expression mode](https://docs.derivative.ca/Parameter_Mode "Parameter Mode") and enter
```
me.par.sizex

```

When you change 'sizex', 'sizey' now stays in sync, keeping the rectangle in a square shape. Now, in the 'Text' parameter of your Text TOP, enter this expression:
```
op('rectangle1').par.sizex

```

Now changing 'sizex' keeps the displayed text in sync as well. To review, the general process here is to use `me` or `op` to reach the operator you want, then access the parameter you want via the `par` object. [![Python Pars.png](https://docs.derivative.ca/images/e/e9/Python_Pars.png)](https://docs.derivative.ca/File:Python_Pars.png)
##  Accessing CHOP channels
Another common use of parameter expressions is to access [CHOP](https://docs.derivative.ca/CHOP "CHOP") channel data. For this example, put down a [Beat CHOP](https://docs.derivative.ca/Beat_CHOP "Beat CHOP"). Rather than typing the expression this time, we are going to use drag/drop to create it. Follow these steps:
  1. Press the _+_ button on the bottom right of the Beat CHOP to make its viewer active.
  2. Select _rectangle1_ to see its parameter dialog.
  3. Drag the 'ramp' channel and drop it into the left (_x_) entry box in the 'Size' parameter.
  4. Select **CHOP Reference** from the popup menu.

You will now have the following expression in 'sizex':
```
op('beat2')['ramp']

```

In Python, the `[]` square bracket notation is a way to specify elements in a collection. In this case, because CHOPs can have multiple channels, you specify which channel you want by putting its name in the square brackets. While you will usually want to use the name, you also have the option of picking a channel by number. Change the 'sizex' expression to op('beat2')[0] and you will see the same results. Note that in Python, the first element of a sequential list is always zero, not one.
##  More Complex Expressions, Errors, and `eval`
You may have noticed that your Text TOP shows an unreadable jumble of numbers now, because the CHOP sends data that changes quickly and has many digits. To fix this, we will use Python's `round` function which takes two arguments: the number to round and the number of decimal places to show. Enter the following into the 'Text' parameter of the Text TOP:
```
round(op('rectangle1').par.sizex,1)

```

The parameter turns red and a red X marker is placed on the operator. This is what an error looks like. Don't worry, errors are an unavoidable part of scripting. Before we fix it, it's worth looking at a couple different ways to view the error message. One is to hover over the parameter or expression. Another is to click on the red X marker on the node. This specific error is _td.Par doesn't define __round__ method_. The problem is that technically `op('rectangle1').par.sizex` returns a parameter object and not an actual number, which is what the `round` function wants. Often using a parameter object will work, but occasionally you will run into this problem and need to convert from a parameter to a value. To do this, use the `eval` function. Change your expression to this:
```
round(op('rectangle1').par.sizex.eval(),1)

```

[![Python Eval.png](https://docs.derivative.ca/images/5/59/Python_Eval.png)](https://docs.derivative.ca/File:Python_Eval.png)
For an extensive list of example TouchDesigner Python expressions, see the Expressions sections in [Python Tips](https://docs.derivative.ca/Python_Tips "Python Tips").
#  Python in the Textport
When working with Python in TouchDesigner it is very helpful to have a [Textport](https://docs.derivative.ca/Textport "Textport") open. For quick tasks, you can open a floating textport by pressing **alt-t** , but for more extended Python work like this tutorial, opening a textport pane is recommended. To do this:
  1. Click the downward facing arrow on the far right above the TouchDesigner network view and choose 'Split left/right'.
  2. Click the downward facing triangle on the far left above your new pane and choose 'Textport and DATs'.

[![Python textport.png](https://docs.derivative.ca/images/5/5e/Python_textport.png)](https://docs.derivative.ca/File:Python_textport.png)
The textport performs these useful functions when working with Python:
  * Displays output from `print` and `debug` statements in Python code.
  * Displays all error messages from Python code.
  * Lets you test simple Python.

As a simple test, type `print('Hello World!')` into the textport and press <Enter>.
##  Working With TouchDesigner Objects in the Textport
Accessing TouchDesigner objects from the textport is quite similar to in parameter expressions. Most commonly, you will start with an operator, which means you will need its path. There's a great trick for this:
  1. Enter `r = op('` into the textport. Do not press <Enter>.
  2. Drag and drop your _rectangle1_ operator into the textport. The path is automatically appended to your command.
  3. Finish the line by typing `')` and pressing <Enter>.

You have now assigned your rectangle operator to the variable `r`. Type `r` and press <Enter> and you will see information about the operator. Here's a few more things to try while you're at it:
Textport Command  | Result
---|---
`r.name` | the operator name
`r.par.fillcolorr` | the value of the fill color parameter's red attribute
`r.par.fillcolorr = 0` | set the value of fill color red to 0
`dir(r)` | a list of the data and functions available in the operator
`help(r.resetViewer)` | show help for the operator's `resetViewer` method
You can use this technique to examine TouchDesigner objects, to test simple Python code, and to perform simple, one time Python tasks.
#  Python in DATs
Any Python code more extensive than expressions goes in [DAT|DATs]. There are four main places where you will find/create such code:
  1. **Callbacks (callback DATs and execute DATs)** - react to various TouchDesigner events
  2. **Script Operators** - actually a subset of callback DATs, this code creates the content in these special operators
  3. **Extensions** - create a Python interface for custom components
  4. **Standalone modules** - generalized, reusable Python code

Before we dive into working with Python in DATs, you may want to set up an external editor if you haven't already. DATs and the textport can be used for editing, but external editors provide more extensive tools including syntax highlighting, code folding, etc. To set this up, see [Editing DAT Text in an External Editor](https://docs.derivative.ca/DAT#Editing_DAT_Text_in_an_External_Editor "DAT").
The sections below will build on the simple examples described above in [Python in Parameter Expressions](#Python_in_Parameter_Expressions).
##  Callbacks
Callbacks let you use Python to react to many different kinds of changes in TouchDesigner. Some operators will have callback DATs attached to them when you create them, such as [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP"), while other callback DATs stand alone as their own operator types, such as [Parameter Execute DAT](https://docs.derivative.ca/Parameter_Execute_DAT "Parameter Execute DAT").
For this example, put down a Parameter Execute DAT next to the operators you created in the [Python in Parameter Expressions](#Python_in_Parameter_Expressions) section. To set it up to watch the 'Text' parameter on the Text TOP, do the following:
  1. Drag the Text TOP into _parexec1_ DAT's 'OP' parameter. It should now contain the name of the Text TOP. We changed that name above, so yours might be different.
  2. To pick which specific parameter to watch, type `text` in _parexec1_ DAT's 'Parameters' parameter.

Now that we've set up the parameters, we can write some Python. Right-click on _parexec1_ and select 'Edit Contents...'. We want to run code when the parameter value changes, so first let's make sure we're getting messages properly. Change the `onValueChange` callback to look like this:
```
def onValueChange(par, prev):
	debug(par)

```

If you look back at the textport, you'll see a debug statement showing up every tenth of a second, when the number in the parameter. Just to show something interesting you might do with this, now change the `onValueChange` callback (including the import line above) to:
```
import random

def onValueChange(par, prev):
	op('rectangle1').par.fillcolorr = random.random()
	op('rectangle1').par.fillcolorg = random.random()
	op('rectangle1').par.fillcolorb = random.random()

```

You will now see the rectangle's square changing to a random color every time the Text TOP's 'Text' parameter changes. This effect would be impossible to achieve with just parameter expressions.
For those unfamiliar with Python, the `**import**`statement is how you reference external Python code, called**modules**. Once you import the module `random`, you can use the function in it that happens also to be called `random`. To see a list of modules available with TouchDesigner, go [here](https://docs.derivative.ca/Python_Classes_and_Modules#Standard_Python_Modules "Python Classes and Modules").
###  `print` vs. `debug`
An important thing to note in the above section is the `debug` command. It is a TouchDesigner utility that works much like a Python `print` statement but automatically adds exactly where in your network the `debug` command came from. In TouchDesigner, you will often find yourself needing to send information to the textport in order to fix problems in your scripts. You should always use the `debug` statement to do this instead of `print`.
###  Execute DATs
Execute DATs are DAT operators that provide callbacks for events in TouchDesigner. For example, the example above uses a Parameter Execute DAT to react to parameter value changes. Here are the execute DATs and what they react to:
  * **[CHOP Execute](https://docs.derivative.ca/CHOP_Execute_DAT "CHOP Execute DAT")** - changes in CHOP channels
  * **[DAT Execute](https://docs.derivative.ca/DAT_Execute_DAT "DAT Execute DAT")** - changes in a DAT table.
  * **[OP Execute](https://docs.derivative.ca/OP_Execute_DAT "OP Execute DAT")** - general operator changes, such as name, children, wiring, etc.
  * **[Panel Execute](https://docs.derivative.ca/Panel_Execute_DAT "Panel Execute DAT")** - interactions with a [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") (UI).
  * **[Parameter Execute](https://docs.derivative.ca/Parameter_Execute_DAT "Parameter Execute DAT")** - changes to parameter values and settings
  * **[Execute](https://docs.derivative.ca/Execute_DAT "Execute DAT")** - system events, such as startup, file save, operator creation, etc.

See [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") for examples of all these.
##  Script OPs
Script OPs are operators that provide callbacks that actually create the data of the operator itself. When you place one of these operators, there will be a callback DAT attached to it automatically. In the DAT, you can edit the `onCook` callback to define the operator's behavior when it cooks. Here is a list of the script OPs:
  * **[Script CHOP](https://docs.derivative.ca/Script_CHOP "Script CHOP")** - use Python to create a CHOP and its channels.
  * **[Script DAT](https://docs.derivative.ca/Script_DAT "Script DAT")** - use Python to create a DAT table.
  * **[Script SOP](https://docs.derivative.ca/Script_SOP "Script SOP")** - use Python to create a SOP using points, curves, meshes etc.
  * **[Script TOP](https://docs.derivative.ca/Script_TOP "Script TOP")** - use Python to create a TOP image.

See [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") for examples of all these.
##  Extensions
[Extensions](https://docs.derivative.ca/Extensions "Extensions") are Python classes that allow you to build data and functionality into your custom [components](https://docs.derivative.ca/Component "Component"). There is a lot to extensions and we will only brush the surface in the tutorial below. For a more in-depth look at Extensions, look [here](https://docs.derivative.ca/Extensions "Extensions"). This simple technique for adding Python attributes and functions is incredibly powerful for giving custom components extended Python functionality.
###  Creating An Extension
To create a default extension, follow these steps:
  1. Create a new [Container COMP](https://docs.derivative.ca/Container_COMP "Container COMP")
  2. Use the [RMB Menu](https://docs.derivative.ca/RMB_Menu "RMB Menu") on the new component to select 'Customize Component...'
  3. Open the 'Extension Code' section
  4. Enter the name `TutorialExt` and press 'Add'
  5. Press 'Edit' to see the contents

There's a lot going on in there that we aren't going to get into here, but to get an idea of what extensions are for, just note these lines of code:
```
		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

```

###  Accessing An Extension From Inside a Component
To see the extension in action, go inside the container COMP. The first thing you'll notice is that there is a DAT in there called _TutorialExt_. This is where the actual extension text is located, and you can edit it through the Component Editor, as shown above, or directly by changing the DAT here.
For this example, create a [Text TOP](https://docs.derivative.ca/Text_TOP "Text TOP") here in the container. Change the Text TOP's 'Text' parameter to expression mode (click the blue square) and enter the following expression:
```
ext.TutorialExt.a

```

This uses the `ext` object to search upward for `TutorialExt` and return it's `a` attribute. **Extensions can be accessed from anywhere inside their component using the `ext` object.** You can change this expression to `ext.TutorialExt.B` to see that value as well. You can use both extension attributes and extension functions in this way.
###  Accessing An Extension From Outside a Component
Promoted members of Extensions can also be accessed from outside their components. **Extension members are "promoted" when they start with a capital letter.** This applies to both attributes and functions.
To see this in action, navigate upward out of the component by pressing u keyboard shortcut. Create another Text TOP here, and again enter an expression into its 'Text' parameter. This time, the expression is: `op('container1').B`. As you can see, the extension attribute acts as a member of the container COMP itself. If you try the expression `op('container1').a` you'll get an error. This is because only capitalized attributes and functions of an extension are promoted to this level.
##  DATs as Modules
All DATs with Python code in them can be used as modules. Importing these modules is a little different than in most Python however, because they exist in TouchDesigner networks instead of in files. For the following examples, work inside `/project1`.
Place a Text DAT and rename it to _utils_. Enter the following function:
```
def my_adder(x,y):
	return 10*x+y

```

Add another text DAT and rename it to _test_. In this DAT enter the following:
```
import utils
a = utils.my_adder(1,3)
print(a)

```

Open a textport, then run the _test_ module by right-clicking on its node and selecting 'Run Script'. **Note: if your node viewer is active on _test_ you will have to right-click on its name bar.**
You will see the resulting `13` in the textport. The `my_utils` DAT has been treated as a module, using the import statement.
###  Component Modules
To create **Component Modules** that are accessible anywhere inside a component, you must place them in a specific child of that component, namely `local/modules`. You can create this path if it doesn't already exist by creating a [Base COMP](https://docs.derivative.ca/Base_COMP "Base COMP") called _local_ with another Base COMP called _modules_ inside it.
###  The `import` statement in TouchDesigner
TouchDesigner uses a special version of the `import` statement which looks for modules in the following order:
  1. The current component
  2. The current component's Component Modules
  3. The Component Modules of each parent until it reaches the root component
  4. The component modules of /sys component (internal TouchDesigner modules)
  5. The regular Python disk search

**Note: When you attempt to import an external module, it will first look for DATs of that name in the same folder , so be sure to avoid name conflicts keeping the above search order in mind.**
###  Module On Demand, the `mod` object
The import statement, though useful contains two disadvantages:
  * Module names must be single words, so relative DAT paths cannot be used.
  * They are unsuitable for use in a parameter expression.

To avoid this, use the [ Module On Demand](https://docs.derivative.ca/MOD_Class "MOD Class") or `mod` object.
In the DAT _test_ , replace the contents with the following code:
```
a = mod.utils.my_adder(1,3)
print(a)

```

Notice how no import statement is needed, making this evaluation suitable for one-line parameter expressions.
String paths, including relative paths can also be used in the `mod` object. Simply pass in the string as a parameter to the mod object:
```
a = mod('utils').my_adder(1,3)
print(a)

```

Both absolute and relative paths may be used:
```
a = mod('/project1/utils').my_adder(1,3)
print(a)

```

All of the above will result in the same output.
**Note:`mod` uses the same search order described above for `import`.**
###  The `module` member
You can also access a DAT as a module via its `module` member. Using this method, the _test_ script would be:
```
a = op('/project1/utils').module.my_adder(1,3)
print(a)

```

This method of access is useful if you know exactly where your module is located and want to avoid any of TouchDesigner's automated searching.
###  Automatic Recompilation of Modules
If you access a TouchDesigner object such as a CHOP channel or parameter in the root code of a module, as opposed to accessing it in a function or class, the module will recompile automatically whenever that TD object changes. This can cause slowdowns and unexpected results, so it is a best practice to keep such references in functions. Furthermore, there are some edge cases where the module will _not_ recompile automatically causing further confusion. The following illustrates the best practice:
```
# Don't do it like this. The module will recompile every time value0 changes
value = op('constant1').par.value0

# Do it like this:
def value0():
	return op('constant1').par.value0

```

A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](https://docs.derivative.ca/DAT "DAT") and in scripts.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.
Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off or the root timeline is paused.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](https://docs.derivative.ca/Script "Script") or [GLSL](https://docs.derivative.ca/GLSL "GLSL") Shader, but can be any multi-line text. [Tables](https://docs.derivative.ca/Table_DAT "Table DAT") are rows and columns of cells, each containing a text string.
The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](https://docs.derivative.ca/Root "Root"). This path is displayed at the top of every [Pane](https://docs.derivative.ca/Pane "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](https://docs.derivative.ca/Folder "Folder").
A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax `parent.Name`, for example `parent.Effect.width` to obtain panel width.
A name for a component that is accessible from any node in a project, which can be declared in a component's Global Operator Shortcut parameter.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
A [Link](https://docs.derivative.ca/Link "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").
The grey dashed lines between nodes is a Reference (or [Link](https://docs.derivative.ca/Link "Link")). A Reference is (1) a [Parameter Reference](https://docs.derivative.ca/Parameter_Reference "Parameter Reference"), a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](https://docs.derivative.ca/index.php?title=Node_Reference&action=edit&redlink=1 "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.
A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](https://docs.derivative.ca/Export "Export"), node [Paths](https://docs.derivative.ca/Network_Path "Network Path") in parameters, and [expressions](https://docs.derivative.ca/Expression "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](https://docs.derivative.ca/Wire "Wire") that connects nodes in the same [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family").
The dialog box in which commands and scripts can typed in manually. Output to the textport includes script errors and messages from `print()` and `debug()` calls in python code. You can also edit DATs in the textport.
A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](https://docs.derivative.ca/Python "Python") and the original [Tscript](https://docs.derivative.ca/Tscript "Tscript"). Scripts and single-line commands can also be run in the [Textport](https://docs.derivative.ca/Textport "Textport").
Any component can be extended with its own Python classes which contain python functions and data.
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
