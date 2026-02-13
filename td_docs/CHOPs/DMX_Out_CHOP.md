---
url: https://docs.derivative.ca/DMX_Out_CHOP
category: CHOPs
title: DMX_Out_CHOP
---

# DMX Out CHOP
## Summary

The DMX Out CHOP sends channels to [DMX](https://docs.derivative.ca/DMX "DMX"), [Art-Net](https://docs.derivative.ca/Art-Net "Art-Net"), [sACN](https://docs.derivative.ca/SACN "SACN"), [KiNET](https://www.colorkinetics.com/global/learn/optics-matter), or FTDI devices. Channel values for DMX are 0-255.
The first channel you send into the DMX Out will correspond to the first DMX address (DMX channel) As you add channels to the DMX Out, you will access the next DMX channels in order. For example, if you input 12 channels into the DMX out, you will be controlling DMX channels 1 thru 12.
The DMX in TouchDesigner was developed on the [ENTTEC](http://www.enttec.com) device, namely their [DMX USB Pro](http://www.enttec.com/?main_menu=Products&pn=70304) and DMX over Ethernet devices, but it should work for many devices and software that support DMX/Art-Net/sACN/KiNET.
A Routing Table can be provided in a DAT where addresses can be specified by adding rows for each channel and specifying net, subnet and universe.
**ENTTEC NOTE:** - Use ENTTEC's [NMU (Node Management Utility)](http://www.enttec.com/us/products/controls/dmx-over-ethernet/nmu/) to configure and inspect the ENTTEC devices found on your network.
**macOS NOTE:** - ENTTEC USB Pro may not connect automatically, to enable it enter the following command in the Terminal:
`sudo kextunload -b com.apple.driver.AppleUSBFTDI`
**Tip** : See the [OP Snippets](https://docs.derivative.ca/OP_Snippets "OP Snippets") for setup and usage examples.
**Tip** : Use [WireShark](https://www.wireshark.org/) to watch your DMX network traffic.

See also: [DMX Out POP](https://docs.derivative.ca/DMX_Out_POP "DMX Out POP"), [Art-Net](https://docs.derivative.ca/Art-Net "Art-Net"), [sACN](https://docs.derivative.ca/SACN "SACN"), [DMX In CHOP](https://docs.derivative.ca/DMX_In_CHOP "DMX In CHOP"), [DMX](https://docs.derivative.ca/DMX "DMX")
[dmxoutCHOP_Class](https://docs.derivative.ca/DmxoutCHOP_Class "DmxoutCHOP Class")

## Parameters - DMX Page
- Active `active` - Connects to the device while On.
- Interface `interface` - ⊞ - Select the type of interface to connect to the device with.
  * Enttec Generic Serial `serial` - Uses the operating system's serial calls to write data.
  * Enttec USB Pro `enttecusbpro` -
  * Enttec USB Pro Mk2 `enttecusbpromk2` -
  * Art-Net `artnet` - Sets the interface to [Art-Net](http://en.wikipedia.org/wiki/Art-Net) protocol.
  * sACN `sacn` - Sets the interface to [sACN](https://en.wikipedia.org/wiki/Architecture_for_Control_Networks) protocol.
  * KiNET `kinet` - Sets the interface to [KiNET](https://www.colorkinetics.com/global/learn/led-lighting-technology#KiNET) protocol.

- Format `format` - ⊞ - Select between sending Packet Per Sample or Packet Per Channel.
  * Packet Per Sample `packetpersample` - Each channel acts as a DMX channel, ie. 512 channels for 1 universe.
  * Packet Per Channel `packetperchan` - Each sample in a channel acts as a DMX channel. This allows for setting up a channel for each universe, ie. 1 channel with 512 samples for 1 universe. Add multiple channels for multiple universes.

- Rate `rate` - How often data is sent to the device (per second). ```
       **WARNING: DMX512 devices have a maximum refresh rate of 44Hz. It is recommended that Rate <= 44 for reliable performance.**

```

## Parameters - Serial Page
- Serial Port `serialport` - ⊞ - When the Interface parameter is set to Generic Serial this parameter lets you select which Serial (COM) port to use.
  * COM3 `com3` -

- DMXking Port `dmxkingport` - ⊞ - Select a DMXking port to send to.
  * Default `default` -

- Device `device` - ⊞ - Select a DMX device from the menu.
  * * `*` -

## Parameters - Network Page
- Net (0-127) `net` - When the Interface parameter is set to Art-Net, this sets the net address. A net is a groups of 16 consecutive subnets or 256 consecutive universes. The range for this parameter is 0-127. This is **not** a network IP address.
- Subnet (0-15) `subnet` - When the Interface parameter is set to Art-Net, this sets the subnet address. A subnet is a group of 16 consecutive universes. The range for this parameter is 0-15. This is **not** a network subnet mask.
- Universe `universe` - When the Interface parameter is set to Art-Net, this sets the universe address. A single DMX512 frame of 512 channels is referred to as a universe. The range for this parameter is 0-15.
- Multicast `multicast` - Enable multicast for sACN. Multicast automatically builds the IP based on Net, Subnet, and Universe of the device. This allows for sending to multiple devices at once by specifying multiple universes.
- Network Address `netaddress` - Specify the IP address to use. This address corresponds to the receiving device address. When the address is set to its default 255.255.255.255, the messages are instead broadcast to all devices on the network. The Art-Net Net, Subnet and Universe of the receiving devices must still match those specified in the DMX Out CHOP in all cases.
- Local Address `localaddress` - ⊞ - When the sending machine is equipped with multiple network adapters, this parameter can be used to choose which adapter to send the data from by specifying its IP address here.
  * 192.168.0.102 `192.168.0.102` -

- Local Port `localport` - In rare cases it can be necessary to supply a custom port from which the data should be sent. The default of `-1` means the O/S assigned port is being used.
- Use Custom Port `customport` - Enable the Network Port parameter to specify the port of the receiving hardware.
- Network Port `netport` - Let's you specify the port of the receiving hardware. By default and the spec of ArtNet this is set to 6454 and should only be changed in rare cases.
- Send ArtSync `sendartsync` - When enabled will send out ArtSync packets. ArtSync packets are used to synchronize multiple universes together. It will do this by waiting for all ArtDmx packets to finish sending, then follow up by sending an ArtSync packet.
- ArtSync Timeout `artsynctimeout` - Specify the time in milliseconds that ArtSync will wait for all ArtDmx packets to complete sending, before sending the ArtSync packet. If they have not all been sent when the timeout is reached, then ArtSync will terminate and the ArtSync packet will not be sent. Additionally, a new frame of ArtDmx packets will be sent and a new ArtSync will be initiated.
- CID `cid` - The unique ID of the sender.
- Source `source` - User assigned name of source (for informative purposes).
- Priority `priority` - The priority of the data being sent, if there are multiple sources.
- KiNET Version `kinetversion` - ⊞ - Set the version of the KiNET protocol to use.
  * DmxOut (v1) `v1` -
  * PortOut (v2) `v2` -

- Use Custom KiNET Port `customkinetport` - When enabled, can specify a custom port for the KiNET v2 interface. When disabled, the port will be the broadcast port: 255.
- KiNET Port `kinetport` - Specifies the port for KiNET v2 interface.
- Routing Table `routingtable` - Available when using Packet Per Channel Format for Art-Net or sACN. Use the docked Table DAT to route channels to the appropriate universes. Addresses can be specified by adding rows for each channel and specifying net, subnet, universe, and netaddress. The net, subnet, universe, and netaddress columns are optional and correspond to the DMX Out CHOP's Net, Subnet, Universe, and Network Address parameters respectively. If for example the `net` column is missing from the Routing Table, the `Net` parameter is used instead.
When removing the Routing Table from the parameter, the specified address will be used for the first channel while all other channels are assigned to consecutive addresses.
**Note:** For sACN the first available universe has the index 1 as universe 0 is reserved by the system for future use.

## Parameters - Common Page
- Time Slice `timeslice` - Turning this on forces the channels to be "[Time Sliced](https://docs.derivative.ca/Time_Slicing "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame.
- Scope `scope` - To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Sample Rate Match `srselect` - ⊞ - Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available.
  * Resample At First Input's Rate `first` - Use rate of first input to resample others.
  * Resample At Maximum Rate `max` - Resample to the highest sample rate.
  * Resample At Minimum Rate `min` - Resample to the lowest sample rate.
  * Error If Rates Differ `err` - Doesn't accept conflicting sample rates.

- Export Method `exportmethod` - ⊞ - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](https://docs.derivative.ca/Export "Export") article for more information.
  * DAT Table by Index `datindex` - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name `datname` - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter `autoname` - The channel is the full destination of where to export to, such has `geo1/transform1:tx`.

- Export Root `autoexportroot` - This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to.
- Export Table `exporttable` - The DAT used to hold the export information when using the DAT Table Export Methods (See above).
- Rename from `commonrenamefrom` - The channel pattern to rename. See [Pattern Matching](https://docs.derivative.ca/Pattern_Matching "Pattern Matching").
- Rename to `commonrenameto` - The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](https://docs.derivative.ca/Pattern_Replacement "Pattern Replacement").
**Example:**     Channel Names: `c[1-10:2] ambient`     Rename From: `c* ambient`     Rename To: `b[1-5] amb`
This example fetches channels `c1 c3 c5 c7 c9` and `ambient`.
They are then renamed to to `b1 b2 b3 b4 b5` and `amb`.
See the [Rename CHOP](https://docs.derivative.ca/Rename_CHOP "Rename CHOP") for a further description of rename patterns.

## Operator Inputs
  * Input 0:  -

## Info CHOP Channels
Extra Information for the DMX Out CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
## Common CHOP Info Channels
  * start - Start of the CHOP interval in samples.

  * length - Number of samples in the CHOP.

  * sample_rate - The samplerate of the channels in frames per second.

  * num_channels - Number of channels in the CHOP.

  * time_slice - 1 if CHOP is Time Slice enabled, 0 otherwise.

  * export_sernum - A count of how often the export connections have been updated.

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
