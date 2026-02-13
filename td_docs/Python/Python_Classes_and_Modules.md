---
url: https://docs.derivative.ca/Python_Classes_and_Modules
category: Python
title: Python_Classes_and_Modules
---

# Python Classes and Modules

The following list of important Python classes and modules is roughly grouped together by subject.
[Python Reference](https://docs.derivative.ca/Category:Python_Reference "Category:Python Reference") has an alphabetical list of all TouchDesigner Python pages on this wiki.
###  Operator Related Classes
The following classes are Python interfaces for operators and objects that operators use. Individual operator classes (e.g. [TextTOP Class](https://docs.derivative.ca/TextTOP_Class "TextTOP Class") and [RampTOP Class](https://docs.derivative.ca/RampTOP_Class "RampTOP Class")) are not listed but do exist in the [`td` module](https://docs.derivative.ca/Td_Module "Td Module"), and links to each can be found [here](https://docs.derivative.ca/Category:Python_Reference "Category:Python Reference") or by clicking on the Python Help button in their [parameter dialog](https://docs.derivative.ca/Parameter_Dialog "Parameter Dialog"). These classes are found in the [td module](https://docs.derivative.ca/Td_Module "Td Module") so do not need to be imported.
  * **[OP Class](https://docs.derivative.ca/OP_Class "OP Class")** - a TouchDesigner [operator](https://docs.derivative.ca/Operator "Operator").
    * **[Connector Class](https://docs.derivative.ca/Connector_Class "Connector Class")** - a wire connector for an OP. Lists of these can be found in `OP.inputConnectors` and `OP.outputConnectors`. Components also have `COMP.inputCOMPConnectors` and `COMP.outputCOMPConnectors`.
    * **[Page Class](https://docs.derivative.ca/Page_Class "Page Class")** - a parameter page. Lists of these can be found in `OP.pages` and, on components and script operators, `OP.customPages`.
    * **[ParCollection Class](https://docs.derivative.ca/ParCollection_Class "ParCollection Class")** (`OP.par`) - holds all the parameters for an OP.
      * **[Par Class](https://docs.derivative.ca/Par_Class "Par Class")** - an individual [parameter](https://docs.derivative.ca/Parameter "Parameter").
    * **[ParGroupCollection Class](https://docs.derivative.ca/ParGroupCollection_Class "ParGroupCollection Class")** (`OP.par`) - holds all the parameter groups for an OP.
      * **[ParGroup Class](https://docs.derivative.ca/ParGroup_Class "ParGroup Class")** - an individual parameter group.
        * **[ParGroupPulse Class](https://docs.derivative.ca/ParGroupPulse_Class "ParGroupPulse Class")** - an individual parameter group with a pulse par.
        * **[ParGroupUnit Class](https://docs.derivative.ca/ParGroupUnit_Class "ParGroupUnit Class")** - an individual parameter group with a unit par.
    * **[SequenceCollection Class](https://docs.derivative.ca/SequenceCollection_Class "SequenceCollection Class")** (`OP.seq`) - holds all the sequences for an OP.
      * **[Sequence Class](https://docs.derivative.ca/Sequence_Class "Sequence Class")** - describes and controls a set of sequential parameters. Sequential parameters will have a reference to one of these objects in their `sequence` member.
        * **[SequenceBlock Class](https://docs.derivative.ca/SequenceBlock_Class "SequenceBlock Class")** - used to access the parGroups of a specific block (set of parGroups) in a sequence.
    * **[CHOP Class](https://docs.derivative.ca/CHOP_Class "CHOP Class")** - subclass of OPs defining [CHOP](https://docs.derivative.ca/CHOP "CHOP") operators.
      * **[Channel Class](https://docs.derivative.ca/Channel_Class "Channel Class")** - a [channel](https://docs.derivative.ca/Channel "Channel") object. Accessed through a CHOP index or other CHOP members such as `chan`, `chans` etc.
      * **[Segment Class](https://docs.derivative.ca/Segment_Class "Segment Class")** - describes a single segment from a [Timer CHOP](https://docs.derivative.ca/Timer_CHOP "Timer CHOP").
    * **[COMP Class](https://docs.derivative.ca/COMP_Class "COMP Class")** - a subclass of OPs defining [component](https://docs.derivative.ca/Component "Component") operators.
      * **[ObjectCOMP Class](https://docs.derivative.ca/ObjectCOMP_Class "ObjectCOMP Class")** - a subclass of COMPs defining [Objects](https://docs.derivative.ca/Object "Object"), used to create and render 3D scenes.
      * **[PanelCOMP Class](https://docs.derivative.ca/PanelCOMP_Class "PanelCOMP Class")** - a subclass of COMPS defining [Panel Components](https://docs.derivative.ca/Panel_Component "Panel Component"), used to create 2D UI elements.
        * **[Panel Class](https://docs.derivative.ca/Panel_Class "Panel Class")** - a member of panelCOMPs containing all associated [panel values](https://docs.derivative.ca/Panel_Value "Panel Value"). Accessed through `panelCOMP.panel`.
          * **[PanelValue Class](https://docs.derivative.ca/PanelValue_Class "PanelValue Class")** - individual [panel values](https://docs.derivative.ca/Panel_Value "Panel Value"). Accessed through the `panel` member of panelCOMPS and also in callbacks in the [Panel Execute DAT](https://docs.derivative.ca/Panel_Execute_DAT "Panel Execute DAT").
        * **[ListAttributes Class](https://docs.derivative.ca/ListAttributes_Class "ListAttributes Class")** - a collection of [list attributes](https://docs.derivative.ca/ListAttribute_Class "ListAttribute Class") used in a [ListCOMP](https://docs.derivative.ca/ListCOMP_Class "ListCOMP Class").
          * **[ListAttribute Class](https://docs.derivative.ca/ListAttribute_Class "ListAttribute Class")** - contains attributes defining a cell in a [ListCOMP](https://docs.derivative.ca/ListCOMP_Class "ListCOMP Class").
        * **[Actors Class](https://docs.derivative.ca/Actors_Class "Actors Class")** - describes the set of all Actor COMPs used by the Bullet Solver COMP and Nvidia Flex Solver COMP. used in a [BulletsolverCOMP](https://docs.derivative.ca/BulletsolverCOMP_Class "BulletsolverCOMP Class") or [flexsolverCOMP](https://docs.derivative.ca/FlexsolverCOMP_Class "FlexsolverCOMP Class").
        * **[Bodies Class](https://docs.derivative.ca/Bodies_Class "Bodies Class")** - a collection of [bodies](https://docs.derivative.ca/Body_Class "Body Class") used in an [ActorCOMP](https://docs.derivative.ca/ActorCOMP_Class "ActorCOMP Class").
          * **[Body Class](https://docs.derivative.ca/Body_Class "Body Class")** - a single body (physics object) used in an [ActorCOMP](https://docs.derivative.ca/ActorCOMP_Class "ActorCOMP Class").
      * **[VFS Class](https://docs.derivative.ca/VFS_Class "VFS Class")** - a COMP's Virtual File System
        * **[VFSFile Class](https://docs.derivative.ca/VFSFile_Class "VFSFile Class")** - a virtual file contained within a Virtual File System.
    * **[DAT Class](https://docs.derivative.ca/DAT_Class "DAT Class")** - a subclass of OPs defining [DAT](https://docs.derivative.ca/DAT "DAT") operators.
      * **[Cell Class](https://docs.derivative.ca/Cell_Class "Cell Class")** - defines an individual cell of a [DAT](https://docs.derivative.ca/DAT "DAT") table.
      * **[Peer Class](https://docs.derivative.ca/Peer_Class "Peer Class")** - describes the network connection originating a message in the callback functions found in [oscinDAT](https://docs.derivative.ca/OSC_In_DAT "OSC In DAT"), [tcpipDAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT"), [udpinDAT](https://docs.derivative.ca/UDP_In_DAT "UDP In DAT"), [udtinDAT](https://docs.derivative.ca/UDT_In_DAT "UDT In DAT").
    * **[MAT Class](https://docs.derivative.ca/MAT_Class "MAT Class")** - a subclass of OPs defining [MAT](https://docs.derivative.ca/MAT "MAT") operators.
    * **[SOP Class](https://docs.derivative.ca/SOP_Class "SOP Class")** - a subclass of OPs defining [SOP](https://docs.derivative.ca/SOP "SOP") operators.
      * **[Attributes Class](https://docs.derivative.ca/Attributes_Class "Attributes Class")** - a collection of SOP [attributes](https://docs.derivative.ca/Attribute "Attribute")
        * **[Attribute Class](https://docs.derivative.ca/Attribute_Class "Attribute Class")** - information about an entity such as its color, velocity, normal, and so on.
          * **[AttributeData Class](https://docs.derivative.ca/AttributeData_Class "AttributeData Class")** - contains specific geometric Attribute values, associated with a Prim Class, Point Class, or Vertex Class.
      * **[Group Class](https://docs.derivative.ca/Group_Class "Group Class")** - describes groups lists of Prim Class or Point Class.
      * **[Points Class](https://docs.derivative.ca/Points_Class "Points Class")** - a collection of [points](https://docs.derivative.ca/Point_Class "Point Class").
        * **[Point Class](https://docs.derivative.ca/Point_Class "Point Class")** - a single geometry [point](https://docs.derivative.ca/Point "Point").
          * **[InputPoint Class](https://docs.derivative.ca/InputPoint_Class "InputPoint Class")** - a special point object used in [Point SOP](https://docs.derivative.ca/Point_SOP "Point SOP") parameters.
      * **[Prims Class](https://docs.derivative.ca/Prims_Class "Prims Class")** - a collection of [primitives](https://docs.derivative.ca/Prim_Class "Prim Class").
        * **[Prim Class](https://docs.derivative.ca/Prim_Class "Prim Class")** - a single geometry [primitive](https://docs.derivative.ca/Primitive "Primitive").
          * **[Poly Class](https://docs.derivative.ca/Poly_Class "Poly Class")** - a subclass of Prim defining a geometry [polygon](https://docs.derivative.ca/Polygon "Polygon").
          * **[Mesh Class](https://docs.derivative.ca/Mesh_Class "Mesh Class")** - a subclass of Prim defining a geometry [mesh](https://docs.derivative.ca/Mesh "Mesh").
          * **[Bezier Class](https://docs.derivative.ca/Bezier_Class "Bezier Class")** - a subclass of Prim defining a set of Bezier curves.
          * **[Vertex Class](https://docs.derivative.ca/Vertex_Class "Vertex Class")** - a member of Prim defining a single geometry [vertex](https://docs.derivative.ca/Vertex "Vertex").
    * **[TOP Class](https://docs.derivative.ca/TOP_Class "TOP Class")** - a subclass of OPs defining [TOP](https://docs.derivative.ca/TOP "TOP") operators.
      * **[CUDAMemory Class](https://docs.derivative.ca/CUDAMemory_Class "CUDAMemory Class")** - holds a reference to CUDA memory.
        * **[CUDAMemoryShape Class](https://docs.derivative.ca/CUDAMemoryShape_Class "CUDAMemoryShape Class")** - describes the shape of a CUDA memory segment.
      * **[TextLine Class](https://docs.derivative.ca/TextLine_Class "TextLine Class")** - a line of text in the [Text TOP](https://docs.derivative.ca/Text_TOP "Text TOP") or [Text SOP](https://docs.derivative.ca/Text_SOP "Text SOP"), after it has been formatted. Contains various members about the line such as it's text, position etc.

###  Helper Classes
The following helper objects are part of the [td module](https://docs.derivative.ca/Td_Module "Td Module") and can thus be accessed anywhere, including expressions, without imports (e.g. `absTime.frame`).
  * **[AbsTime Class](https://docs.derivative.ca/AbsTime_Class "AbsTime Class")** (`absTime`) - information about [absolute time](https://docs.derivative.ca/Absolute_Time "Absolute Time")
  * **[App Class](https://docs.derivative.ca/App_Class "App Class")** (`app`) - information about the TouchDesigner app, including version, installation folders, etc.
  * **[Project Class](https://docs.derivative.ca/Project_Class "Project Class")** (`project`) - information about the current TouchDesigner session
  * **[TDU Class](https://docs.derivative.ca/TDU_Class "TDU Class")** (`tdu`) - generic utilities for TouchDesigner not relating directly to TD objects.
    * **[ArcBall Class](https://docs.derivative.ca/ArcBall_Class "ArcBall Class")** (`tdu.ArcBall`) - encapsulates many aspects of 3D viewer interaction.
    * **[Camera Class](https://docs.derivative.ca/Camera_Class "Camera Class")** (`tdu.Camera`) - maintains a 3D position and orientation for a camera and provides multiple methods for manipulating the camera's position and direction.
    * **[Color Class](https://docs.derivative.ca/Color_Class "Color Class")** (`tdu.Color`) - holds a 4 component color
    * **[Dependency Class](https://docs.derivative.ca/Dependency_Class "Dependency Class")** (`tdu.Dependency`) - used to create [Dependable](https://docs.derivative.ca/Dependency "Dependency") Python data.
    * **[Matrix Class](https://docs.derivative.ca/Matrix_Class "Matrix Class")** (`tdu.Matrix`) - holds a single 4x4 matrix for use in transformations. See [ObjectCOMP Class](https://docs.derivative.ca/ObjectCOMP_Class "ObjectCOMP Class") for transforms of 3D objects.
    * **[Position Class](https://docs.derivative.ca/Position_Class "Position Class")** (`tdu.Position`) - holds a 3 component position
    * **[Quaternion Class](https://docs.derivative.ca/Quaternion_Class "Quaternion Class")** (`tdu.Quaternion`) - holds a quaternion object for 3D rotations
    * **[Timecode Class](https://docs.derivative.ca/Timecode_Class "Timecode Class")** (`tdu.Timecode`) - holds a timecode value
    * **[Vector Class](https://docs.derivative.ca/Vector_Class "Vector Class")** (`tdu.Vector`) - holds a 3 component vector

  * **[Licenses Class](https://docs.derivative.ca/Licenses_Class "Licenses Class")** (`licenses`) - information about installed [license](https://docs.derivative.ca/License_Class "License Class") objects
    * **[DongleList Class](https://docs.derivative.ca/DongleList_Class "DongleList Class")** (`licenses.dongles`) - list of attached dongles
      * **[Dongle Class](https://docs.derivative.ca/Dongle_Class "Dongle Class")** - an individual dongle connected to the system
    * **[License Class](https://docs.derivative.ca/License_Class "License Class")** - a single instance of an installed license
      *         * **[ProductEntry Class](https://docs.derivative.ca/ProductEntry_Class "ProductEntry Class")** - a dongle entry for a single dongle connected to the system
  * **[MOD Class](https://docs.derivative.ca/MOD_Class "MOD Class")** (`mod`) - access to modules located in TouchDesigner DATs
  * **[Monitors Class](https://docs.derivative.ca/Monitors_Class "Monitors Class")** (`monitors`) - access to information about all connected display devices
    * **[Monitor Class](https://docs.derivative.ca/Monitor_Class "Monitor Class")** - an individual display device
  * **[Runs Class](https://docs.derivative.ca/Runs_Class "Runs Class")** (`runs`) - information about all delayed [run objects](https://docs.derivative.ca/Run_Class "Run Class")
    * **[Run Class](https://docs.derivative.ca/Run_Class "Run Class")** - an individual delayed run object
  * **[SysInfo Class](https://docs.derivative.ca/SysInfo_Class "SysInfo Class")** (`sysInfo`) - current system/hardware information
  * **[UI Class](https://docs.derivative.ca/UI_Class "UI Class")** (`ui`) - information about application ui elements
    * **[Colors Class](https://docs.derivative.ca/Colors_Class "Colors Class")** (`ui.colors`) - application colors
    * **[Options Class](https://docs.derivative.ca/Options_Class "Options Class")** (`ui.options`) - configurable ui options
    * **[Panes Class](https://docs.derivative.ca/Panes_Class "Panes Class")** (`ui.panes`) - collection of all panes open in the editor
      * **[Pane Class](https://docs.derivative.ca/Pane_Class "Pane Class")** - an individual pane object
        * **[NetworkEditor Class](https://docs.derivative.ca/NetworkEditor_Class "NetworkEditor Class")** - subclass of Pane that displays a network editor
    * **[Preferences Class](https://docs.derivative.ca/Preferences_Class "Preferences Class")** (`ui.preferences`) - collection of TouchDesigner preferences
    * **[Undo Class](https://docs.derivative.ca/Undo_Class "Undo Class")** (`ui.undo`) - tools for interacting with the undo system, including creating script-based undo steps

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
  * **[TDStoreTools](https://docs.derivative.ca/TDStoreTools "TDStoreTools")** - utilities for use with TouchDesigner's [Storage](https://docs.derivative.ca/Storage "Storage") and [Dependency](https://docs.derivative.ca/Dependency "Dependency") system.
  * **[TDResources](https://docs.derivative.ca/TDResources "TDResources")** (`op.TDResources...`) - not a module, but does contain system resources that can be accessed via Python. It includes system [pop-up menu](https://docs.derivative.ca/TDResources#Pop-Up_Menu "TDResources"), [button pop-up menu](https://docs.derivative.ca/TDResources#Button_Pop-Up_Menu "TDResources"), [pop-up dialog](https://docs.derivative.ca/TDResources#Pop-Up_Dialog "TDResources"), and [mouse](https://docs.derivative.ca/TDResources#Mouse "TDResources") resources.

###  3rd Party Packages
**The following 3rd party packages are automatically installed with TouchDesigner.** They are not in the [td module](https://docs.derivative.ca/Td_Module "Td Module"), so must be imported explicitly to be used in scripts. The name in parentheses is the actual package name used (e.g. to use OpenCV, write this at top of script: `import cv2`). For information on adding or installing other Python modules, see [Importing Modules](https://docs.derivative.ca/Introduction_to_Python_Tutorial#Importing_Modules).
  * **[asn1crypto](https://pypi.org/project/asn1crypto/)** (`asn1crypto`) - Parsing and serializing ASN.1 structures.
  * **[attr](https://www.attr.org)** (`attr`) - Classes without boilerplate.
  * **[Certifi](https://pypi.org/project/certifi/)** (`certifi`) - Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
  * **[CFFI](https://cffi.readthedocs.io/en/latest/)** (`cffi`) - Interaction with C code.
  * **[Chardet](https://pypi.org/project/chardet/)** (`chardet`) - The Universal Character Encoding Detector.
  * **[charset-normalizer](https://pypi.org/project/charset-normalizer/)** (`charset_normalizer`) - A library that helps you read text from an unknown charset encoding.
  * **[Cryptography](https://cryptography.io/en/latest/)** (`cryptography`) - High level recipes and low level interfaces to common cryptographic algorithms.
  * **[decorator](https://github.com/micheles/decorator)** (`decorator`) - Define signature-preserving function decorators and decorator factories.
  * **[OAuthlib](https://pypi.org/project/oauthlib/)** (`oauthlib`) - Library to build OAuth and OpenID Connect servers.
  * **[opencv-python](https://pypi.org/project/opencv-python/)** (`cv2`) - Pre-built CPU-only OpenCV packages for Python.
  * **[depthai](https://pypi.org/project/depthai/)** (`depthai`) - Python bindings for C++ [depthai-core library](https://docs.luxonis.com/projects/api/en/latest/).
  * **[idna](https://pypi.org/project/idna/)** (`idna`) - Support for the Internationalised Domain Names in Applications (IDNA) protocol.
  * **[jsonpath](https://pypi.org/project/jsonpath-ng/)** (`jsonpath_ng`) - JSONPath tools for accessing and altering JSON structures.
  * **[jsonschema](https://pypi.org/project/jsonschema/)** (`jsonschema`) - jsonschema is an implementation of the [JSON Schema](https://json-schema.org/) specification for Python.
  * **[MWParserFromHell](https://mwparserfromhell.readthedocs.io/en/latest/)** (`mwparserfromhell`) - An easy-to-use and outrageously powerful parser for MediaWiki wikicode.
  * **[NumPy](http://www.numpy.org)** (`numpy`) - Fundamental package for scientific computing with Python.
  * **[OpenCV](https://opencv.org)** (`cv2`) - Open source computer vision.
  * **[packaging](https://pypi.org/project/packaging/)** (`packaging`) - Package tools including version handling, specifiers, markers, requirements, tags, utilities. Used for version string comparison.
  * **[pip](https://pypi.org/project/pip/)** (`pip`) - pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.
  * **[ply](https://www.dabeaz.com/ply/)** (`ply`) - Parsing tools for lex and yacc.
  * **[Pygments](https://pypi.org/project/Pygments/)** (`pygments`) - A syntax highlighting package written in Python.
  * **[pyparsing](https://pypi.org/project/pyparsing/)** (`pyparsing`) - A library of classes that client code uses to construct parsing grammar directly in Python code.
  * **[pyrankvote](https://pypi.org/project/pyrankvote/)** (`pyrankvote`) - PyRankVote is a python library for different ranked-choice voting systems (sometimes called preferential voting systems) created by Jon Tingvold in June 2019.
  * **[pyrsistent](https://pypi.org/project/pyrsistent/)** (`pyrsistent`) - Pyrsistent is a number of persistent collections (by some referred to as functional data structures). Persistent in the sense that they are immutable.
  * **[PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)** (`yaml`) - YAML parser and emitter.
  * **[Requests](http://docs.python-requests.org/en/master/)** (`requests`) - The only Non-GMO HTTP library for Python, safe for human consumption
  * **[Requests OAuthlib](https://requests-oauthlib.readthedocs.io/en/latest/index.html)** (`requests_oauthlib`) - Easy-to-use Python interface for building OAuth1 and OAuth2 clients
  * **[six](https://pypi.org/project/six/)** (`six`) - Python 2 and 3 compatibility utilities.
  * **[smartypants](https://pypi.org/project/smartypants/)** (`smartypants`) - a Python fork of [SmartyPants](http://daringfireball.net/projects/smartypants/).
  * **[tabulate](https://pypi.org/project/tabulate/)** (`tabulate`) - Pretty-print tabular data in Python.
  * **[urllib3](https://urllib3.readthedocs.io/en/latest/)** (`urllib3`) - HTTP client.
  * **[whats-that-code](https://pypi.org/project/whats-that-code/)** (`whats_that_code`) - programming language detection library.

###  Installing Custom Packages and Modules
You can also install your own Python packages that are not included with TouchDesigner. For instructions, go [here](https://docs.derivative.ca/Category:Python#Installing_Custom_Python_Packages "Category:Python").
Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](https://docs.derivative.ca/Node "Node").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that contains its own [Network](https://docs.derivative.ca/Network "Network"). There are sixteen 3D [Object Component](https://docs.derivative.ca/Object_Component "Object Component") and ten 2D [Panel Component](https://docs.derivative.ca/Panel_Component "Panel Component") types. See also [Network Path](https://docs.derivative.ca/Network_Path "Network Path").
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
Lets you embed files inside a `.tox[](https://docs.derivative.ca/.tox ".tox")` or `.toe[](https://docs.derivative.ca/.toe ".toe")` file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a `vfs:` syntax.
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
A sequence of vertices form a [Polygon](https://docs.derivative.ca/Polygon "Polygon") in a [SOP](https://docs.derivative.ca/SOP "SOP"). Each vertex is an integer index into the [Point List](https://docs.derivative.ca/Point_List "Point List"), and each [Point](https://docs.derivative.ca/Point "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.
Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off.
is the [Procedural](https://docs.derivative.ca/Procedural "Procedural") mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](https://docs.derivative.ca/Cook "Cook").
TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The [Network Path](https://docs.derivative.ca/Network_Path "Network Path") or Path for root is simply `/`. A typical path is `/project1/moviein1`.
