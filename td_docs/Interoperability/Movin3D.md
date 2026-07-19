---
url: https://docs.derivative.ca/Movin3D
category: Interoperability
title: Movin3D
---

# Movin3D

[MOVIN](https://movin3d.com/) is a 3D motion AI company that develops real-time, markerless motion capture solutions. Their flagship product, **MOVIN TRACIN** , is a portable LiDAR-based device that captures full-body motion data without markers, suits, or a dedicated studio. Powered by on-device AI that fuses LiDAR point clouds and vision data, MOVIN TRACIN delivers production-ready motion capture at a fraction of the cost of traditional optical systems.

MOVIN TRACIN streams motion data to TouchDesigner in real time via OSC using **MOVIN Studio** , the companion desktop application (Windows). This enables TouchDesigner users to drive real-time visuals, lighting, and sound using live human motion — ideal for live performances, interactive installations, and immersive experiences.

MOVIN TRACIN works in any lighting condition including complete darkness, and is resistant to electromagnetic interference from LED walls, audio gear, and broadcast equipment.

For full product details, see [MOVIN TRACIN](https://movin3d.com/tracin) and [movin3d.com](https://movin3d.com/).

##  Motion Capture Streaming (OSC In CHOP)[")]

MOVIN Studio streams skeleton joint rotations over OSC, which TouchDesigner receives natively via the [OSC In CHOP](OSC_In_CHOP.md "OSC In CHOP"). The channel names encode the path and parameter for each joint, so a [Null CHOP](../CHOPs/Null_CHOP.md "Null CHOP") with the Export Method set to _Channel Name is Path:Parameter_ can drive a character rig directly.

###  Setup

**1. Add an OSC In CHOP**

In your TouchDesigner project, add an [OSC In CHOP](OSC_In_CHOP.md "OSC In CHOP") from the CHOP tab. Set the **Network Port** to `11237` (the default port used by MOVIN Studio for TouchDesigner streaming).

**2. Add a Null CHOP**

Add a [Null CHOP](../CHOPs/Null_CHOP.md "Null CHOP") and connect the OSC In CHOP to it. In the Null CHOP's **Common** tab, set the **Export Method** to `Channel Name is Path:Parameter`.

**3. Import the same character in both MOVIN Studio and TouchDesigner**

Import an FBX character file into your TouchDesigner project. Then import the _same_ FBX file into MOVIN Studio. For details on importing characters into MOVIN Studio, see [Import Custom Character](https://help.movin3d.com/movin-studio-usage-guide/import-custom-character) in the MOVIN documentation.

**Important:** The **Node Name** set in TouchDesigner must match the **Character Name** configured in MOVIN Studio. If the names do not match, live streaming will not work correctly.

**4. Configure and start streaming in MOVIN Studio**

In MOVIN Studio, open the Streaming tab and select **TouchDesigner** as the streaming platform. Verify that the port number matches the one configured in the OSC In CHOP (`11237` by default). Set the **Host** to `127.0.0.1` if TouchDesigner is running on the same machine, or to the IP address of the TouchDesigner machine if streaming over a network. Click **Start Streaming**.

**5. Enable Export on the Null CHOP**

Back in TouchDesigner, enable the Export flag by clicking the green circular icon at the bottom-right of the Null CHOP. You should see gray dotted lines connecting the Null CHOP to the character's joints, indicating that motion data is being applied in real time.

###  OSC Channel Format

MOVIN Studio sends one OSC message per joint per frame. The channel names follow the pattern:
```
/<CharacterName>/<JointName>:<Parameter>
```

For example, if the character is named `myCharacter` and the joint is `Hips`, the channels will include rotation values such as:
```
/myCharacter/Hips:rx
/myCharacter/Hips:ry
/myCharacter/Hips:rz
```

The Null CHOP's `Channel Name is Path:Parameter` export method uses this naming convention to automatically map incoming channels to the corresponding joint transform parameters on the character hierarchy in TouchDesigner.

##  Point Cloud Streaming (OSC In DAT + Python)[")]

In addition to skeleton data, MOVIN TRACIN can stream raw LiDAR point cloud data to TouchDesigner. Because the point cloud data is more complex (arrays of XYZ positions and optional intensity values), this workflow uses an [OSC In DAT](../DATs/OSC_In_DAT.md "OSC In DAT") with a Python callback to parse the incoming data into geometry that can be rendered.

###  Setup

**1. Add an OSC In DAT**

Add an [OSC In DAT](../DATs/OSC_In_DAT.md "OSC In DAT") and set its **Network Port** to the port configured for point cloud output in MOVIN Studio (check the MOVIN Studio streaming settings for the correct port — this is separate from the mocap skeleton port).

**2. Create a callback DAT**

Create a [Text DAT](../Glossary/Text_DAT.md "Text DAT") and reference it as the **Callbacks DAT** on the OSC In DAT. The callback script parses incoming point cloud messages and writes them into a format that can be consumed by geometry operators.

Below is an example callback that receives point cloud data and stores it for use with a [Script SOP](../SOPs/Script_SOP.md "Script SOP") or [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP"):
```
# Example OSC In DAT callback for MOVIN point cloud data
# Assign this Text DAT as the Callbacks DAT on your OSC In DAT

def onReceiveOSC(dat, rowIndex, message, bytes, timeStamp, address, args, peer):
    """
    Called for each incoming OSC message.

    The point cloud data arrives as OSC messages containing
    arrays of float values representing XYZ positions.
    Parse these and store them for use in a Script SOP or
    other geometry pipeline.
    """

    # Filter for point cloud address pattern
    if '/pointcloud' in address:
        # args contains the point cloud data as a flat list of floats
        # organized as [x0, y0, z0, x1, y1, z1, ...]
        points = []
        for i in range(0, len(args) - 2, 3):
            x = args[i]
            y = args[i + 1]
            z = args[i + 2]
            points.append((x, y, z))

        # Store points for access by Script SOP or other operators
        op('pointcloud_storage').store('points', points)
        op('pointcloud_storage').store('num_points', len(points))

    return
```

**3. Visualize with a Script SOP**

Use a [Script SOP](../SOPs/Script_SOP.md "Script SOP") (or [Script POP](https://docs.derivative.ca/Script_POP "Script POP")) to read the stored points and create geometry:
```
# Example Script SOP for visualizing MOVIN point cloud
# Place this in the Script SOP's callbacks

def onCook(scriptSOP):
    scriptSOP.clear()

    points = op('pointcloud_storage').fetch('points', [])

    for pt in points:
        p = scriptSOP.appendPoint()
        p.x = pt[0]
        p.y = pt[1]
        p.z = pt[2]

    return
```

Alternatively, the point cloud can be fed into a [Geometry COMP](../Glossary/Geometry_COMP.md "Geometry COMP") and rendered using the [Render TOP](../TOPs/Render_TOP.md "Render TOP") with a point sprite material for real-time visualization.

**Note:** For a complete working example of both mocap and point cloud streaming together, download the sample project linked in the [Sample Project](#Sample_Project) section below.

##  Sample Project

MOVIN provides a TouchDesigner sample project that demonstrates how to receive both mocap skeleton data and point cloud data together:
  * **Download:** [MOVIN TouchDesigner Sample Project (Google Drive)](https://drive.google.com/drive/folders/1JBOIXo8Ze7letvP2k-SvP6FXJTOHffRE)
  * **MOVIN Downloads Page:** [movin3d.com/downloads](https://www.movin3d.com/downloads#movin-studio)

The sample project includes all the operators and callbacks pre-configured, and is the fastest way to get started.

A step-by-step streaming guide is also available in the MOVIN documentation: [Streaming Mocap Data into TouchDesigner](https://help.movin3d.com/movin-studio-usage-guide/live-streaming/streaming-mocap-data-into-touchdesigner).

##  Troubleshooting

  * **No data arriving in the OSC In CHOP** — Verify that the port number in the OSC In CHOP matches the port configured in MOVIN Studio. Check that Windows Firewall is not blocking the connection. If streaming across machines, ensure both are on the same network and the Host IP in MOVIN Studio is set to the TouchDesigner machine's IP address.
  * **Character does not move** — Make sure the Export flag (green circle) is enabled on the Null CHOP. Confirm that the character's Node Name in TouchDesigner exactly matches the Character Name in MOVIN Studio.
  * **Skeleton appears distorted or broken** — Ensure the same FBX character file is loaded in both MOVIN Studio and TouchDesigner. Different files or mismatched bone hierarchies will cause retargeting errors.
  * **Point cloud data not appearing** — Verify that the OSC In DAT is set to the correct port for point cloud streaming (separate from the mocap port). Check that the callback DAT is properly referenced and that the address pattern in the callback matches what MOVIN Studio is sending.

##  External Links

  * [MOVIN Website](https://movin3d.com/)
  * [MOVIN TRACIN Product Page](https://movin3d.com/tracin)
  * [MOVIN Documentation](https://help.movin3d.com/)
  * [TouchDesigner Streaming Guide](https://help.movin3d.com/movin-studio-usage-guide/live-streaming/streaming-mocap-data-into-touchdesigner)
  * [TouchDesigner Sample Project](https://drive.google.com/drive/folders/1JBOIXo8Ze7letvP2k-SvP6FXJTOHffRE)
  * [MOVIN GitHub](https://github.com/MOVIN3D)

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](../Glossary/Script.md "Script") or [GLSL](../Glossary/GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](../Glossary/Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](../Glossary/CHOP_Viewer.md "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](../Glossary/Parameter.md "Parameter").

The location of an operator within the TouchDesigner environment, for example, `/geo1/circle1`, a node called `circle1` in a component called `geo1`. The path `/` is called [Root](../Glossary/Root.md "Root"). This path is displayed at the top of every [Pane](../Glossary/Pane.md "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or `http:` address, see [Folder](../Glossary/Folder.md "Folder").

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](../Glossary/Network_Path.md "Network Path"), which determine the output of the operator.

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](../Glossary/Script.md "Script") or [GLSL](../Glossary/GLSL.md "GLSL") Shader, but can be any multi-line text. [Tables](../Glossary/Table_DAT.md "Table DAT") are rows and columns of cells, each containing a text string.

A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](../General/Python.md "Python") and the original [Tscript](../Glossary/Tscript.md "Tscript"). Scripts and single-line commands can also be run in the [Textport](../Glossary/Textport.md "Textport").

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](../Glossary/Text_DAT.md "Text DAT") and referenced by a [GLSL Material](../MATs/GLSL_MAT.md "GLSL MAT") or a [GLSL TOP](../TOPs/GLSL_TOP.md "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.
