---
url: https://docs.derivative.ca/Serial_CHOP
category: CHOPs
title: Serial_CHOP
---

# Serial CHOP
## Summary

The Serial CHOP is used for serial communication through an external port, using the RS-232 protocol. These ports are usually a 9 pin connector, or a USB port on new machines. (Using a USB port requires a USB-to-serial adaptor and driver.) All of a computer's available serial ports can be found in the Device Manager under the Windows operating system. Their names begin with 'COM'. Example: COM1, COM2, COM3, etc.
This CHOP monitors changes in its input channels, and sends the corresponding script through the serial connection. Any ASCII numeric digits '0'..'9' that are received, are stored and reflected in the output channel named 'return'.
When you need to receive more complex data, other than simple ASCII numbers use the [Serial DAT](https://docs.derivative.ca/Serial_DAT "Serial DAT").
See also [Serial DAT](https://docs.derivative.ca/Serial_DAT "Serial DAT"), [serialDAT_Class](https://docs.derivative.ca/SerialDAT_Class "SerialDAT Class"), [Arduino](https://docs.derivative.ca/Arduino "Arduino").
[serialCHOP_Class](https://docs.derivative.ca/SerialCHOP_Class "SerialCHOP Class")

## Parameters - Port Page
- Active `active` - This check box enables the serial connection.
- State `state` - ⊞ - The type of input transition to monitor.
  * Off to On `offtoon` -
  * While On `on` -
  * On to Off `ontooff` -
  * While Off `off` -
  * Value Change `valuechange` -

- Port `port` - ⊞ - Selects the COM port that the serial connection will use.
  * COM3 `com3` -

- Baud Rate `baudrate` - The maximum number of bits of information, including "control" bits, that are transmitted per second. Check your input device's default baud rate and set accordingly.
- Baud Rate Menu `baudmenu` - ⊞ - Use this menu to select from some commonly used baud rates.
  * 1200 `1200` -
  * 2400 `2400` -
  * 9600 `9600` -
  * 19200 `19200` -
  * 38400 `38400` -
  * 57600 `57600` -
  * 115200 `115200` -
  * 230400 `230400` -
  * 460800 `460800` -
  * 921600 `921600` -
  * 1382400 `1382400` -

- Data Bits `databits` - ⊞ - This parameter sets the number of data bits sent in each. Data bits are transmitted "backwards". Backwards refers to the order of transmission, which is from least significant bit (LSB) to most significant bit (MSB). To interpret the data bits, you must read from right to left.
  * 6 `6` -
  * 7 `7` -
  * 8 `8` -
  * 9 `9` -

- Parity `parity` - ⊞ - This parameter can be set to none, even, or odd. The optional parity bit follows the data bits and is included as a simple means of error checking. Parity bits work by specifying ahead of time whether the parity of the transmission is to be even or odd. If the parity is set to be odd, the transmitter will then set the parity bit in such a way as to make an odd number of 1's among the data bits and the parity bit.
  * Even `even` -
  * Odd `odd` -
  * None `none` -

- Stop Bits `stopbits` - ⊞ - The last part of transmission packet consists of 1 or 2 Stop bits. The connection will now wait for the next Start bit.
  * 1 `1` -
  * 2 `2` -

## Parameters - Scripts Page
- Script `script` - Sequence of scripts corresponding to input channels. These strings are sent out the serial port when the corresponding channel change is detected. For example, Script 2 is sent to the serial port when the third input channel goes from off to on. These scripts will also convert escape sequences like <CR> and \n for carriage returns and \r for line feed.
- Callback `script0callback` - Enter the script for Script 0 here.

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
Extra Information for the Serial CHOP can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
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
