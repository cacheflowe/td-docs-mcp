---
url: https://docs.derivative.ca/Serial_DAT
category: DATs
title: Serial_DAT
---

# Serial DAT
## Summary

The Serial DAT is used for serial communication through an external port, using the RS-232 protocol. These ports are usually a 9 pin connector, or a USB port on new machines. (Using a USB port requires a USB-to-serial adapter and driver.) All of a computer's available serial ports can be found in the Device Manager in the Windows operating system under Computer –> Manage -> Devices -> Serial… -> COM ports. Their names begin with 'COM'. Example: COM1, COM2, COM3.
To send bytes out this connection, see the send methods in the [serialDAT_Class](https://docs.derivative.ca/SerialDAT_Class "SerialDAT Class"), or in Tscript the `send` Command.
See also [Arduino](https://docs.derivative.ca/Arduino "Arduino") and [Serial CHOP](https://docs.derivative.ca/Serial_CHOP "Serial CHOP").
[serialDAT_Class](https://docs.derivative.ca/SerialDAT_Class "SerialDAT Class")

## Parameters - Connect Page
- Active `active` - This check box enables the serial connection.
- Row/Callback Format `format` - ⊞ - Interpret the incoming data as binary or ASCII data. If the format is Per Byte, one row is appended for each binary byte received. If the format is Per Line, one row is appended for each null or newline delimited message received.
  * One Per Byte `perbyte` - (formerly called 'binary').
  * One Per Line `perline` - (formerly called 'Ascii') null/newln delimited.
  * One Per Message `permessage` - Full incoming msg.

- Port `port` - Selects the COM port that the serial connection will use. Default port names 1 through 8 are available in the popup menu, though any name can be manually entered in this field.
- Baud Rate `baudrate` - ⊞ - The maximum number of bits of information, including "control" bits, that are transmitted per second. Check your input device's default baud rate and set accordingly.
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

- DTR `dtr` - ⊞ - The DTR (data-terminal-ready) flow control. (Windows Only).
  * Disable `disable` - Disables the line when device is opened.
  * Enable `enable` - Enables the line when device is opened.
  * Handshake `handshake` - Enables handshaking with the device.

- RTS `rts` - ⊞ - The RTS (request-to-send) flow control. (Windows Only).
  * Disable `disable` - Disables the line when device is opened.
  * Enable `enable` - Enables the line when device is opened.
  * Handshake `handshake` - Enables RTS handshaking.
  * Toggle `toggle` - Line high only when bytes available.

## Parameters - Received Data Page
- Callbacks DAT `callbacks` - The Callbacks DAT will execute once for each message received.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location.
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the component specified in the Component parameter below.

- From Operator `fromop` - The path that the script will be executed from if the Execute From parameter is set to Specified Operator.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading. To clear with a script command, here is an example: `opparm -c /serial1 clear`
- Bytes Column `bytes` - Outputs the raw bytes of the message in a separate column.

## Parameters - Common Page
- Language `language` - ⊞ - Select how the DAT decides which script language to operate on.
  * Input `input` - The DAT uses the inputs script language.
  * Node `node` - The DAT uses it's own script language.

- Edit/View Extension `extension` - ⊞ - Select the file extension this DAT should expose to external editors.
  * dat `dat` - various common file extensions.
  * From Language `language` - pick extension from DATs script language.
  * Custom Extension `custom` - Specify a custom extension.

- Custom Extension `customext` - Specifiy the custom extension.
- Word Wrap `wordwrap` - ⊞ - Enable Word Wrap for Node Display.
  * Input `input` - The DAT uses the inputs setting.
  * On `on` - Turn on Word Wrap.
  * Off `off` - Turn off Word Wrap.

## Info CHOP Channels
Extra Information for the Serial DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Serial DAT Info Channels
  * bytes_read -

  * bytes_written -

  * bytes_write_queued -

  * bytes_write_rate -

  * messages_pending -

###
## Common DAT Info Channels
  * num_rows - Number of rows in this DAT.

  * num_cols - Number of columns in this DAT.

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
