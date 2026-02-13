---
url: https://docs.derivative.ca/DMX_Out_POP
category: POPs
title: DMX_Out_POP
---

# DMX Out POP
## Summary

The DMX Out POP can send to DMX, Art-Net, sACN, [KiNET](https://www.colorkinetics.com/global/learn/optics-matter), or FTDI devices.
The DMX Out POP merges the DMX universes from each of its [DMX Fixture POP](https://docs.derivative.ca/DMX_Fixture_POP "DMX Fixture POP") inputs, and sends them to the device. It can merge any number of DMX Fixture POPs but conflicts may arise if multiple DMX Fixture POPs write to the same channel value of a DMX universe. A warning will be output in that case, and for debugging such conflicts the [DMX Map DAT](https://docs.derivative.ca/DMX_Map_DAT "DMX Map DAT") is a useful tool.
**Note:** every input must be a DMX Fixture POP, whether they are wired or by parameter OP reference.
The DMX in TouchDesigner was developed on the [ENTTEC](http://www.enttec.com) device, namely their [DMX USB Pro](http://www.enttec.com/?main_menu=Products&pn=70304) and DMX over Ethernet devices, but it should work for many devices and software that support DMX/Art-Net/sACN/KiNET.
A Routing Table can be provided in a DAT where network addresses can be specified by adding rows for each DMX512 universe and then specifying the net, subnet and universe values.
**Tip** : You can use a single DMX Out POP to gather and serve any number of DMX Fixture POPs in your project because you can specify recursively from root `/*` the path of all DMX Fixture POPs to Search for in the DMX Fixture POPs parameter. You can use a [Folder DAT](https://docs.derivative.ca/Folder_DAT "Folder DAT") to find all the DMX Fixture POPs in your project.
**ENTTEC NOTE:** - Use ENTTEC's [NMU (Node Management Utility)](http://www.enttec.com/us/products/controls/dmx-over-ethernet/nmu/) to configure and inspect the ENTTEC devices found on your network.
**macOS NOTE:** - ENTTEC USB Pro may not connect automatically, to enable it enter the following command in the Terminal:
`sudo kextunload -b com.apple.driver.AppleUSBFTDI`
**Tip** : Use [WireShark](https://www.wireshark.org/) to watch your DMX network traffic. When sending to a large number of universes (eg. for volumetric lighting) it is advantageous to use unicast (see: DMXFixtureNetAddress attribute for the [DMX Fixture POP](https://docs.derivative.ca/DMX_Fixture_POP "DMX Fixture POP")) rather than broadcast as it will be more efficient and can avoid overwhelming the network.
See also: [Art-Net](https://docs.derivative.ca/Art-Net "Art-Net"), [sACN](https://docs.derivative.ca/SACN "SACN"), [DMX In CHOP](https://docs.derivative.ca/DMX_In_CHOP "DMX In CHOP"), [DMX Out CHOP](https://docs.derivative.ca/DMX_Out_CHOP "DMX Out CHOP"), [DMX](https://docs.derivative.ca/DMX "DMX")
[dmxoutPOP_Class](https://docs.derivative.ca/DmxoutPOP_Class "DmxoutPOP Class")

## Parameters - DMX Page
- Active `active` - When enabled, will be actively sending to the device.
- Interface `interface` - ⊞ - Select the type of interface to connect to the device with.
  * Generic Serial `serial` - Uses the operating system's serial calls to write data.
  * Enttec USB Pro `enttecusbpro` -
  * Enttec USB Pro Mk2 `enttecusbpromk2` -
  * Art-Net `artnet` - Sets the interface to [Art-Net](http://en.wikipedia.org/wiki/Art-Net) protocol.
  * sACN `sacn` - Sets the interface to [sACN](https://en.wikipedia.org/wiki/Architecture_for_Control_Networks) protocol.
  * KiNET `kinet` - Sets the interface to [KiNET](https://www.colorkinetics.com/global/learn/led-lighting-technology#KiNET) protocol.

- Rate `rate` - How often data is sent to the device (per second). **WARNING: DMX512 devices have a maximum refresh rate of 44Hz. It is recommended that Rate <= 44 for reliable performance.**

## Parameters - Fixtures Page
- Fixture `fixture` - Start of Sequential Parameter Blocks for DMX Fixture POP inputs, either wired or referenced.
- Active `fixture0active` - When active, this Fixture is merged and sent.
- DMX Fixture POPs `fixture0pop` - A reference to one or more DMX Fixture POPs. The parameter is disabled if there is a corresponding wired input.

## Parameters - Serial Page
- Serial Port `serialport` - ⊞ - When the Interface parameter is set to Generic Serial this parameter lets you select which Serial (COM) port to use.
  * COM3 `com3` -

- DMXking Port `dmxkingport` - ⊞ - Select a DMXking port to send to.
  * Default `default` -

- Device `device` - ⊞ - Select a DMX device from the menu.
  * * `*` -

## Parameters - Network Page
- Multicast `multicast` - Enable multicast for sACN. Multicast automatically builds the IP based on Net, Subnet, and Universe of the device. This allows for sending to multiple devices at once by specifying multiple universes.
- Network Address `netaddress` - Specify the IP address to use. This address corresponds to the receiving device address. When the address is set to its default 255.255.255.255, the messages are instead broadcast to all devices on the network. The Net, Subnet and Universe of the receiving devices must still match those specified in the DMX Out POP in all cases. If a netaddress is specified in the Routing Table for a given net/subnet/universe then that will be used instead.
- Local Address `localaddress` - ⊞ - When the sending machine is equipped with multiple network adapters, this parameter can be used to choose which adapter to send the data from by specifying its IP address here.
  * 192.168.178.150 `192.168.178.150` -
  * 10.2.0.2 `10.2.0.2` -

- Local Port `localport` - In rare cases it can be necessary to supply a custom port from which the data should be sent. The default of `-1` means the O/S assigned port is being used.
- Use Custom Port `customport` - Enable the Network Port parameter to specify the port of the receiving hardware. When disabled, default port is 6454 for Art-Net, 5568 for sACN, and 6038 for KiNET.
- Network Port `netport` - Specify the port of the receiving hardware.
- Priority `priority` - The data priority, if there are multiple sources. Used with sACN and KiNET protocols.
- Send ArtSync `sendartsync` - When enabled will send out ArtSync packets. ArtSync packets are used to synchronize multiple universes together. It will do this by waiting for all ArtDmx packets to finish sending, then follow up by sending an ArtSync packet.
- ArtSync Timeout `artsynctimeout` - Specify the time in milliseconds that ArtSync will wait for all ArtDmx packets to complete sending, before sending the ArtSync packet. If they have not all been sent when the timeout is reached, then ArtSync will terminate and the ArtSync packet will not be sent. Additionally, a new frame of ArtDmx packets will be sent and a new ArtSync will be initiated.
- CID `cid` - The unique ID of the sender.
- Source `source` - User assigned name of source (for informative purposes).
- KiNET Version `kinetversion` - ⊞ - Select the version of the KiNET protocol to use.
  * DmxOut (v1) `v1` -
  * PortOut (v2) `v2` -

- Use Custom KiNET Port `customkinetport` - When enabled, can specify a custom port for the KiNET v2 interface. When disabled, the port will be the broadcast port: 255.
- KiNET Port `kinetport` - Specifies the port for KiNET v2 interface.
- Routing Table `routingtable` - Use a Table DAT to specify netaddress, source, cid, priority, and kinetport values for specific universes. The net, subnet, universe columns must be filled in with valid values. Note: the [DMX Fixture POP](https://docs.derivative.ca/DMX_Fixture_POP "DMX Fixture POP") can override the netaddress value with its own Routing Table.

## Parameters - Multipliers Page
- Use Multipliers `usemultipliers` - Enable the use of multipliers, which apply a post-operation multiply [0-1] on specific named channels (ie. the name set using the Name parameter on a DMX Fixture POP).
- Multiplier `multiplier` - Start of Sequential Parameter Blocks for a channel multipplier. If there are duplicate channel names the multipliers will be combined for that channel.
- DMX Channels `multiplier0dmxchannels` - Select the DMX Channel names (derived from the Name parameters on the input DMX Fixture POPs). The accompanying menu has a list of all available channel names. One Multiplier sequence block can reference multiple channel names in a space delimited format: eg. "Dimmer RGB", where Dimmer and RGB are channel names. "*" can be used to apply the multiplier to every single channel.
- Multiplier Value `multiplier0value` - The multiplier value from [0-1] to apply to any channel that matches the associated channel names specified in DMX Channels.

## Parameters - Common Page
- Bypass `bypass` - Pass through the first input to the output unchanged.
- Free Extra GPU Memory `freeextragpumem` - Free memory that has accumulated when output memory has grown and shrunk.
- Delete Input Attributes `delinputattrs` - Only output which attributes you specify in this POP - helps isolate attributes into a separate branch.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the DMX Out POP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common POP Info Channels
###
## Common Operator Info Channels
  * total_cooks - Number of times the operator has cooked since the process started.

  * cook_time - Duration of the last cook in milliseconds.

  * cook_frame - Frame number when this operator was last cooked relative to the component timeline.

  * cook_abs_frame - Frame number when this operator was last cooked relative to the absolute time.

  * cook_start_time - Time in milliseconds at which the operator started cooking in the frame it was cooked.

  * cook_end_time - Time in milliseconds at which the operator finished cooking in the frame it was cooked.

  * cooked_this_frame - 1 if operator was cooked this frame.

  * warnings - Number of warnings in this operator if any.

  * errors - Number of errors in this operator if any.
