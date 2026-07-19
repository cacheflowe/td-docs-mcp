---
url: https://docs.derivative.ca/TouchDesigner_Python_Classes
category: General
title: TouchDesigner_Python_Classes
---

# Python Classes and Modules

(Redirected from [TouchDesigner Python Classes](https://docs.derivative.ca/index.php?title=TouchDesigner_Python_Classes&redirect=no "TouchDesigner Python Classes"))

The following list of important Python classes and modules is roughly grouped together by subject.

[Python Reference](https://docs.derivative.ca/Category:Python_Reference "Category:Python Reference") has an alphabetical list of all TouchDesigner Python pages on this wiki.

###  Operator Related Classes

The following classes are Python interfaces for operators and objects that operators use. Individual operator classes (e.g. [TextTOP Class](../TOPs/Text_TOP_Class.md "TextTOP Class") and [RampTOP Class](../TOPs/Ramp_TOP_Class.md "RampTOP Class")) are not listed but do exist in the [`td` module](https://docs.derivative.ca/Td_Module "Td Module"), and links to each can be found [here](https://docs.derivative.ca/Category:Python_Reference "Category:Python Reference") or by clicking on the Python Help button in their [parameter dialog](../Glossary/Parameter_Dialog.md "Parameter Dialog"). These classes are found in the [td module](https://docs.derivative.ca/Td_Module "Td Module") so do not need to be imported.
  * **[OP Class](../Python/OP_Class.md "OP Class")** - a TouchDesigner [operator](Operator.md "Operator").
    * **[Connector Class](../Python/Connector_Class.md "Connector Class")** - a wire connector for an OP. Lists of these can be found in `OP.inputConnectors` and `OP.outputConnectors`. Components also have `COMP.inputCOMPConnectors` and `COMP.outputCOMPConnectors`.
    * **[Page Class](../Python/Page_Class.md "Page Class")** - a parameter page. Lists of these can be found in `OP.pages` and, on components and script operators, `OP.customPages`.
    * **[ParCollection Class](../Python/ParCollection_Class.md "ParCollection Class")** (`OP.par`) - holds all the parameters for an OP.
      * **[Par Class](../SOPs/Par_Class.md "Par Class")** - an individual [parameter](../Glossary/Parameter.md "Parameter").
    * **[ParGroupCollection Class](../Python/ParGroupCollection_Class.md "ParGroupCollection Class")** (`OP.par`) - holds all the parameter groups for an OP.
      * **[ParGroup Class](../Python/ParGroup_Class.md "ParGroup Class")** - an individual parameter group.
        * **[ParGroupPulse Class](../Python/ParGroupPulse_Class.md "ParGroupPulse Class")** - an individual parameter group with a pulse par.
        * **[ParGroupUnit Class](../Python/ParGroupUnit_Class.md "ParGroupUnit Class")** - an individual parameter group with a unit par.
    * **[SequenceCollection Class](../Python/SequenceCollection_Class.md "SequenceCollection Class")** (`OP.seq`) - holds all the sequences for an OP.
      * **[Sequence Class](../Python/Sequence_Class.md "Sequence Class")** - describes and controls a set of sequential parameters. Sequential parameters will have a reference to one of these objects in their `sequence` member.
        * **[SequenceBlock Class](../Python/SequenceBlock_Class.md "SequenceBlock Class")** - used to access the parGroups of a specific block (set of parGroups) in a sequence.
    * **[CHOP Class](../Python/CHOP_Class.md "CHOP Class")** - subclass of OPs defining [CHOP](../Glossary/CHOP.md "CHOP") operators.
      * **[Channel Class](../Python/Channel_Class.md "Channel Class")** - a [channel](../Glossary/Channel.md "Channel") object. Accessed through a CHOP index or other CHOP members such as `chan`, `chans` etc.
      * **[Segment Class](../Python/Segment_Class.md "Segment Class")** - describes a single segment from a [Timer CHOP](../CHOPs/Timer_CHOP.md "Timer CHOP").
    * **[COMP Class](../Python/COMP_Class.md "COMP Class")** - a subclass of OPs defining [component](../Glossary/Component.md "Component") operators.
      * **[ObjectCOMP Class](../Python/ObjectCOMP_Class.md "ObjectCOMP Class")** - a subclass of COMPs defining [Objects](../Glossary/Object.md "Object"), used to create and render 3D scenes.
      * **[PanelCOMP Class](../Python/PanelCOMP_Class.md "PanelCOMP Class")** - a subclass of COMPS defining [Panel Components](../Glossary/Panel_Component.md "Panel Component"), used to create 2D UI elements.
        * **[Panel Class](../Python/Panel_Class.md "Panel Class")** - a member of panelCOMPs containing all associated [panel values](../Glossary/Panel_Value.md "Panel Value"). Accessed through `panelCOMP.panel`.
          * **[PanelValue Class](../Python/PanelValue_Class.md "PanelValue Class")** - individual [panel values](../Glossary/Panel_Value.md "Panel Value"). Accessed through the `panel` member of panelCOMPS and also in callbacks in the [Panel Execute DAT](../Glossary/Panel_Execute_DAT.md "Panel Execute DAT").
        * **[ListAttributes Class](../Python/ListAttributes_Class.md "ListAttributes Class")** - a collection of [list attributes](../Python/ListAttribute_Class.md "ListAttribute Class") used in a [ListCOMP](../Python/ListCOMP_Class.md "ListCOMP Class").
          * **[ListAttribute Class](../Python/ListAttribute_Class.md "ListAttribute Class")** - contains attributes defining a cell in a [ListCOMP](../Python/ListCOMP_Class.md "ListCOMP Class").
        * **[Actors Class](../Python/Actors_Class.md "Actors Class")** - describes the set of all Actor COMPs used by the Bullet Solver COMP and Nvidia Flex Solver COMP. used in a [BulletsolverCOMP](../Python/BulletsolverCOMP_Class.md "BulletsolverCOMP Class") or [flexsolverCOMP](../Python/FlexsolverCOMP_Class.md "FlexsolverCOMP Class").
        * **[Bodies Class](../Python/Bodies_Class.md "Bodies Class")** - a collection of [bodies](../Python/Body_Class.md "Body Class") used in an [ActorCOMP](../Python/ActorCOMP_Class.md "ActorCOMP Class").
          * **[Body Class](../Python/Body_Class.md "Body Class")** - a single body (physics object) used in an [ActorCOMP](../Python/ActorCOMP_Class.md "ActorCOMP Class").
      * **[VFS Class](../Python/VFS_Class.md "VFS Class")** - a COMP's Virtual File System
        * **[VFSFile Class](../Python/VFSFile_Class.md "VFSFile Class")** - a virtual file contained within a Virtual File System.
    * **[DAT Class](../Python/DAT_Class.md "DAT Class")** - a subclass of OPs defining [DAT](../Glossary/DAT.md "DAT") operators.
      * **[Cell Class](../Python/Cell_Class.md "Cell Class")** - defines an individual cell of a [DAT](../Glossary/DAT.md "DAT") table.
      * **[Peer Class](../Python/Peer_Class.md "Peer Class")** - describes the network connection originating a message in the callback functions found in [oscinDAT](../DATs/OSC_In_DAT.md "OSC In DAT"), [tcpipDAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT"), [udpinDAT](../Interoperability/UDP_In_DAT.md "UDP In DAT"), [udtinDAT](../DATs/UDT_In_DAT.md "UDT In DAT").
    * **[MAT Class](../Python/MAT_Class.md "MAT Class")** - a subclass of OPs defining [MAT](../MATs/MAT.md "MAT") operators.
    * **[POP Class](../Python/POP_Class.md "POP Class")** - a subclass of OPs defining [POP](../POPs/POP.md "POP") operators.
      * **[Bounds Class](../Python/Bounds_Class.md "Bounds Class")** - contains bounds data (min, max, center, size)
      * **[Attributes Class](../Python/Attributes_Class.md "Attributes Class")** - a collection of POP [attributes](../Glossary/Attribute.md "Attribute")
        * **[Attribute Class](../Python/Attribute_Class.md "Attribute Class")** - information about an entity such as its color, velocity, normal, and so on.
    * **[SOP Class](../SOPs/SOP_Class.md "SOP Class")** - a subclass of OPs defining [SOP](../SOPs/SOP.md "SOP") operators.
      * **[Attributes Class](../Python/Attributes_Class.md "Attributes Class")** - a collection of SOP [attributes](../Glossary/Attribute.md "Attribute")
        * **[Attribute Class](../Python/Attribute_Class.md "Attribute Class")** - information about an entity such as its color, velocity, normal, and so on.
          * **[AttributeData Class](../Python/AttributeData_Class.md "AttributeData Class")** - contains specific geometric Attribute values, associated with a Prim Class, Point Class, or Vertex Class.
      * **[Group Class](../Python/Group_Class.md "Group Class")** - describes groups lists of Prim Class or Point Class.
      * **[Points Class](../Python/Points_Class.md "Points Class")** - a collection of [points](../SOPs/Point_Class.md "Point Class").
        * **[Point Class](../SOPs/Point_Class.md "Point Class")** - a single geometry [point](../Glossary/Point.md "Point").
          * **[InputPoint Class](../Python/InputPoint_Class.md "InputPoint Class")** - a special point object used in [Point SOP](../SOPs/Point_SOP.md "Point SOP") parameters.
      * **[Prims Class](../SOPs/Prims_Class.md "Prims Class")** - a collection of [primitives](../Python/Prim_Class.md "Prim Class").
        * **[Prim Class](../Python/Prim_Class.md "Prim Class")** - a single geometry [primitive](../Glossary/Primitive.md "Primitive").
          * **[Poly Class](../Python/Poly_Class.md "Poly Class")** - a subclass of Prim defining a geometry [polygon](../Glossary/Polygon.md "Polygon").
          * **[Mesh Class](../Python/Mesh_Class.md "Mesh Class")** - a subclass of Prim defining a geometry [mesh](https://docs.derivative.ca/Mesh "Mesh").
          * **[Bezier Class](../Python/Bezier_Class.md "Bezier Class")** - a subclass of Prim defining a set of Bezier curves.
          * **[Vertex Class](../Python/Vertex_Class.md "Vertex Class")** - a member of Prim defining a single geometry [vertex](../Glossary/Vertex.md "Vertex").
    * **[TOP Class](../TOPs/TOP_Class.md "TOP Class")** - a subclass of OPs defining [TOP](../TOPs/TOP.md "TOP") operators.
      * **[CUDAMemory Class](../Python/CUDAMemory_Class.md "CUDAMemory Class")** - holds a reference to CUDA memory.
        * **[CUDAMemoryShape Class](../Python/CUDAMemoryShape_Class.md "CUDAMemoryShape Class")** - describes the shape of a CUDA memory segment.
      * **[TextLine Class](../Python/TextLine_Class.md "TextLine Class")** - a line of text in the [Text TOP](../TOPs/Text_TOP.md "Text TOP") or [Text SOP](../SOPs/Text_SOP.md "Text SOP"), after it has been formatted. Contains various members about the line such as it's text, position etc.

###  Helper Classes

The following helper objects are part of the [td module](https://docs.derivative.ca/Td_Module "Td Module") and can thus be accessed anywhere, including expressions, without imports (e.g. `absTime.frame`).
  * **[AbsTime Class](../Python/AbsTime_Class.md "AbsTime Class")** (`absTime`) - information about [absolute time](../Glossary/Absolute_Time.md "Absolute Time")
  * **[App Class](../Python/App_Class.md "App Class")** (`app`) - information about the TouchDesigner app, including version, installation folders, etc.
  * **[Project Class](../Python/Project_Class.md "Project Class")** (`project`) - information about the current TouchDesigner session
  * **[TDU Class](../Python/TDU_Class.md "TDU Class")** (`tdu`) - generic utilities for TouchDesigner not relating directly to TD objects.
    * **[ArcBall Class](../Python/ArcBall_Class.md "ArcBall Class")** (`tdu.ArcBall`) - encapsulates many aspects of 3D viewer interaction.
    * **[Camera Class](../Python/Camera_Class.md "Camera Class")** (`tdu.Camera`) - maintains a 3D position and orientation for a camera and provides multiple methods for manipulating the camera's position and direction.
    * **[Color Class](../Python/Color_Class.md "Color Class")** (`tdu.Color`) - holds a 4 component color
    * **[Dependency Class](../Python/Dependency_Class.md "Dependency Class")** (`tdu.Dependency`) - used to create [Dependable](../Glossary/Dependency.md "Dependency") Python data.
    * **[Matrix Class](../Python/Matrix_Class.md "Matrix Class")** (`tdu.Matrix`) - holds a single 4x4 matrix for use in transformations. See [ObjectCOMP Class](../Python/ObjectCOMP_Class.md "ObjectCOMP Class") for transforms of 3D objects.
    * **[Position Class](../Python/Position_Class.md "Position Class")** (`tdu.Position`) - holds a 3 component position
    * **[Quaternion Class](../Python/Quaternion_Class.md "Quaternion Class")** (`tdu.Quaternion`) - holds a quaternion object for 3D rotations
    * **[Timecode Class](../TOPs/Timecode_Class.md "Timecode Class")** (`tdu.Timecode`) - holds a timecode value
    * **[Vector Class](../Python/Vector_Class.md "Vector Class")** (`tdu.Vector`) - holds a 3 component vector
  * **[Licenses Class](../Python/Licenses_Class.md "Licenses Class")** (`licenses`) - information about installed [license](../Python/License_Class.md "License Class") objects
    * **[DongleList Class](../Python/DongleList_Class.md "DongleList Class")** (`licenses.dongles`) - list of attached dongles
      * **[Dongle Class](../Python/Dongle_Class.md "Dongle Class")** - an individual dongle connected to the system
    * **[License Class](../Python/License_Class.md "License Class")** - a single instance of an installed license
      *         * **[ProductEntry Class](../Python/ProductEntry_Class.md "ProductEntry Class")** - a dongle entry for a single dongle connected to the system
  * **[MOD Class](../Python/MOD_Class.md "MOD Class")** (`mod`) - access to modules located in TouchDesigner DATs
  * **[Monitors Class](../Python/Monitors_Class.md "Monitors Class")** (`monitors`) - access to information about all connected display devices
    * **[Monitor Class](../Python/Monitor_Class.md "Monitor Class")** - an individual display device
  * **[Runs Class](../Python/Runs_Class.md "Runs Class")** (`runs`) - information about all delayed [run objects](../Python/Run_Class.md "Run Class")
    * **[Run Class](../Python/Run_Class.md "Run Class")** - an individual delayed run object
  * **[SysInfo Class](../Python/SysInfo_Class.md "SysInfo Class")** (`sysInfo`) - current system/hardware information
  * **[UI Class](../Python/UI_Class.md "UI Class")** (`ui`) - information about application ui elements
    * **[Colors Class](../Python/Colors_Class.md "Colors Class")** (`ui.colors`) - application colors
    * **[Options Class](../Python/Options_Class.md "Options Class")** (`ui.options`) - configurable ui options
    * **[Panes Class](../Python/Panes_Class.md "Panes Class")** (`ui.panes`) - collection of all panes open in the editor
      * **[Pane Class](../Python/Pane_Class.md "Pane Class")** - an individual pane object
        * **[NetworkEditor Class](../Python/NetworkEditor_Class.md "NetworkEditor Class")** - subclass of Pane that displays a network editor
    * **[Preferences Class](../Python/Preferences_Class.md "Preferences Class")** (`ui.preferences`) - collection of TouchDesigner preferences
    * **[Undo Class](../Python/Undo_Class.md "Undo Class")** (`ui.undo`) - tools for interacting with the undo system, including creating script-based undo steps

###  Standard Python Modules

The [`td` module](https://docs.derivative.ca/Td_Module "Td Module") also automatically imports a number of helpful standard modules, allowing them to be accessed in expressions through their namespace (e.g. `math.cos(math.pi)`):
  * [`collections`](https://docs.python.org/3.7/library/collections.html) - container datatypes
  * [`enum`](https://docs.python.org/3.7/library/enum.html) - support for enumerations
  * [`inspect`](https://docs.python.org/3.7/library/inspect.html) - inspect live objects
  * [`math`](https://docs.python.org/3.7/library/math.html) - mathematical functions
  * [`re`](https://docs.python.org/3.7/library/re.html) - regular expression operations
  * [`sys`](https://docs.python.org/3.7/library/sys.html) - OS specific data and functions
  * [`traceback`](https://docs.python.org/3.7/library/traceback.html) - stack utilities
  * [`warnings`](https://docs.python.org/3.7/library/warnings.html) - warning control

###  TouchDesigner Utility Modules and Python Utilities

The following contain extended Python utilities for use with TouchDesigner.
  * **[TDFunctions](https://docs.derivative.ca/TDFunctions "TDFunctions")** - A variety of utilities for advanced Python coding in TouchDesigner.
  * **[TDJSON](https://docs.derivative.ca/TDJSON "TDJSON")** - JSON utilities specific to TouchDesigner.
  * **[TDStoreTools](https://docs.derivative.ca/TDStoreTools "TDStoreTools")** - utilities for use with TouchDesigner's [Storage](../Glossary/Storage.md "Storage") and [Dependency](../Glossary/Dependency.md "Dependency") system.
  * **[TDResources](https://docs.derivative.ca/TDResources "TDResources")** (`op.TDResources...`) - not a module, but does contain system resources that can be accessed via Python. It includes system [pop-up menu](https://docs.derivative.ca/TDResources#Pop-Up_Menu "TDResources"), [button pop-up menu](https://docs.derivative.ca/TDResources#Button_Pop-Up_Menu "TDResources"), [pop-up dialog](https://docs.derivative.ca/TDResources#Pop-Up_Dialog "TDResources"), and [mouse](https://docs.derivative.ca/TDResources#Mouse "TDResources") resources.

###  3rd Party Packages

**The following 3rd party packages are automatically installed with TouchDesigner.** They are not in the [td module](https://docs.derivative.ca/Td_Module "Td Module"), so must be imported explicitly to be used in scripts. The name in parentheses is the actual package name used (e.g. to use OpenCV, write this at top of script: `import cv2`). For information on adding or installing other Python modules, see [Importing Modules](../Learn/Introduction_to_Python_Tutorial.md#Importing_Modules).
  * **[attrs](https://www.attrs.org)** (`attr`) - Classes without boilerplate.
  * **[box](https://pypi.org/project/python-box/)** (`box`) - Advanced Python dictionaries with dot notation access.
  * **[Certifi](https://pypi.org/project/certifi/)** (`certifi`) - Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
  * **[Chardet](https://pypi.org/project/chardet/)** (`chardet`) - The Universal Character Encoding Detector.
  * **[charset-normalizer](https://pypi.org/project/charset-normalizer/)** (`charset_normalizer`) - A library that helps you read text from an unknown charset encoding.
  * **[decorator](https://github.com/micheles/decorator)** (`decorator`) - Define signature-preserving function decorators and decorator factories.
  * **[defusedxml](https://pypi.org/project/defusedxml/)** (`defusedxml`) - XML bomb protection for Python stdlib modules.
  * **[depthai](https://pypi.org/project/depthai/)** (`depthai`) - Python bindings for C++ [depthai-core library](https://docs.luxonis.com/projects/api/en/latest/).
  * **[idna](https://pypi.org/project/idna/)** (`idna`) - Support for the Internationalised Domain Names in Applications (IDNA) protocol.
  * **[jsonpath](https://pypi.org/project/jsonpath-ng/)** (`jsonpath_ng`) - JSONPath tools for accessing and altering JSON structures.
  * **[jsonschema](https://pypi.org/project/jsonschema/)** (`jsonschema`) - jsonschema is an implementation of the [JSON Schema](https://json-schema.org/) specification for Python.
  * **[jsonschema-specifications](https://github.com/python-jsonschema/jsonschema-specifications)** (`jsonschema_specifications`) - The JSON Schema meta-schemas and vocabularies, exposed as a Registry.
  * **[MWParserFromHell](https://mwparserfromhell.readthedocs.io/en/latest/)** (`mwparserfromhell`) - An easy-to-use and outrageously powerful parser for MediaWiki wikicode.
  * **[NumPy](http://www.numpy.org)** (`numpy`) - Fundamental package for scientific computing with Python.
  * **[OAuthlib](https://pypi.org/project/oauthlib/)** (`oauthlib`) - Library to build OAuth and OpenID Connect servers.
  * **[opencv-python](https://pypi.org/project/opencv-python/)** (`cv2`) - Pre-built CPU-only OpenCV packages for Python (computer vision).
  * **[packaging](https://pypi.org/project/packaging/)** (`packaging`) - Package tools including version handling, specifiers, markers, requirements, tags, utilities. Used for version string comparison.
  * **[pip](https://pypi.org/project/pip/)** (`pip`) - pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.
  * **[ply](https://www.dabeaz.com/ply/)** (`ply`) - Parsing tools for lex and yacc.
  * **[pygdtf](https://pypi.org/project/pygdtf/)** (`pygdtf`) - General Device Type Format (GDTF) library for Python.
  * **[pymvr](https://pypi.org/project/pymvr/)** (`pymvr`) - My Virtual Rig (MVR) library for Python.
  * **[Pygments](https://pypi.org/project/Pygments/)** (`pygments`) - A syntax highlighting package written in Python.
  * **[pyparsing](https://pypi.org/project/pyparsing/)** (`pyparsing`) - A library of classes that client code uses to construct parsing grammar directly in Python code.
  * **[pyrankvote](https://pypi.org/project/pyrankvote/)** (`pyrankvote`) - PyRankVote is a python library for different ranked-choice voting systems (sometimes called preferential voting systems) created by Jon Tingvold in June 2019.
  * **[pyrfc6266](https://pypi.org/project/pyrfc6266/)** (`pyrfc6266`) - RFC6266 implementation in Python.
  * **[pyrsistent](https://pypi.org/project/pyrsistent/)** (`pyrsistent`) - Pyrsistent is a number of persistent collections (by some referred to as functional data structures). Persistent in the sense that they are immutable.
  * **[PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)** (`yaml`) - YAML parser and emitter.
  * **[referencing](https://pypi.org/project/referencing/)** (`referencing`) - JSON Referencing + Python.
  * **[Requests](http://docs.python-requests.org/en/master/)** (`requests`) - The only Non-GMO HTTP library for Python, safe for human consumption
  * **[Requests OAuthlib](https://requests-oauthlib.readthedocs.io/en/latest/index.html)** (`requests_oauthlib`) - Easy-to-use Python interface for building OAuth1 and OAuth2 clients
  * **[rpds](https://pypi.org/project/rpds-py/)** (`rpds`) - Python bindings to Rust's persistent data structures (rpds).
  * **[six](https://pypi.org/project/six/)** (`six`) - Python 2 and 3 compatibility utilities.
  * **[smartypants](https://pypi.org/project/smartypants/)** (`smartypants`) - a Python fork of [SmartyPants](http://daringfireball.net/projects/smartypants/).
  * **[tabulate](https://pypi.org/project/tabulate/)** (`tabulate`) - Pretty-print tabular data in Python.
  * **[tzdata](https://pypi.org/project/tzdata/)** (`tzdata`) - Provider of IANA time zone data.
  * **[urllib3](https://urllib3.readthedocs.io/en/latest/)** (`urllib3`) - HTTP client.
  * **[whats-that-code](https://pypi.org/project/whats-that-code/)** (`whats_that_code`) - programming language detection library.

###  Installing Custom Packages and Modules

You can also install your own Python packages that are not included with TouchDesigner. For instructions, go [here](https://docs.derivative.ca/Category:Python#Installing_Custom_Python_Packages "Category:Python").

Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](../Glossary/Node.md "Node").

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that contains its own [Network](../Glossary/Network.md "Network"). There are sixteen 3D [Object Component](../Glossary/Object_Component.md "Object Component") and ten 2D [Panel Component](../Glossary/Panel_Component.md "Panel Component") types. See also [Network Path](../Glossary/Network_Path.md "Network Path").

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

Lets you embed files inside a `.tox[](../Glossary/.tox.md ".tox")` or `.toe[](../Glossary/.toe.md ".toe")` file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a `vfs:` syntax.

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

Attributes make up the numeric data blocks of [POPs](../POPs/POP.md "POP"). Each POPs has three blocks of data: a Point List which includes the `P` point Position attribute, a Primitive List and a Vertex List, and each are made of any number of attributes.

A sequence of vertices form a [Polygon](../Glossary/Polygon.md "Polygon") in a [SOP](../SOPs/SOP.md "SOP"). Each vertex is an integer index into the [Point List](../Glossary/Point_List.md "Point List"), and each [Point](../Glossary/Point.md "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off or the root timeline is paused.

applies to python objects, parameters, nodes.

is the [Procedural](../Glossary/Procedural.md "Procedural") mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](../Glossary/Cook.md "Cook").

TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The [Network Path](../Glossary/Network_Path.md "Network Path") or Path for root is simply `/`. A typical path is `/project1/moviein1`.
