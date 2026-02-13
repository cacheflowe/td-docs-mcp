---
url: https://docs.derivative.ca/MQTT_Client_DAT
category: DATs
title: MQTT_Client_DAT
---

# MQTT Client DAT
## Summary

The MQTT Client DAT receives and sends data from/to [MQTT](https://docs.derivative.ca/MQTT "MQTT") devices via MQTT servers (broker). TouchDesigner can act as a client and another computer needs to act as a MQTT Server. Once a client establishes a connection with a server, it can do two things:
  1. Send a message to the server to express interest in any data that has a specific "topic" string. This is called "subscribing". Then the MQTT Client DAT will receive all messages that the server gets with that topic.
  2. Inform the server that it will send messages to the server with a certain topic string, and then send messages with that topic. The messages then get forward to any client that has expressed interest in that topic.

See also [MQTT](https://docs.derivative.ca/MQTT "MQTT"), [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT").
[mqttclientDAT_Class](https://docs.derivative.ca/MqttclientDAT_Class "MqttclientDAT Class")

## Parameters - Connect Page
- Active `active` - Enable the connection.
- Network Address `netaddress` - The address of the broker to connect to. The address should take the form `<protocol>://<host>:<port>`. Accepted protocol URIs can include `tcp`, `ssl`, `ws`, and `wss`.
- Specify ID `specifyid` - Allows naming the client with parameter `User Client ID`, otherwise automatically and uniquely generated for each connection.
- User Client ID `usercid` - Client name when `Specify ID` enabled.
- Keep Alive Interval `keepalive` - Specifies in seconds, the maximum time to expect without communication. If no data is sent during this time, a lightweight ping message is sent to the server instead. Can be set to 0 to avoid pings.
- Max in Flight `maxinflight` - Controls how many messages can be in-flight simultaneously.
- Clean Session `cleansession` - If `Specify ID` is selected, the server will preserve any state information associated with the connection of that ID, such as subscriptions, delivery attempts, etc.
- Verify Certificate `verifycert` - Enables TLS (transport layer security) certificate verification against the server (ie. broker).
- Username `username` - Specify the username for authentication if the server requires it. MQTT servers that support the MQTT v3.1 protocol provide authentication and authorization via username and password.
- Password `password` - Specify the password for authentication if the server requires it. MQTT servers that support the MQTT v3.1 protocol provide authentication and authorization via username and password.
- Reconnect `reconnect` - Will attempt to reconnect to the MQTT broker.

## Parameters - Received Data Page
- Callbacks DAT `callbacks` - The Callbacks DAT contains functions that are called when connections are made, lost or published data arrives. See [mqttclientDAT_Class](https://docs.derivative.ca/MqttclientDAT_Class "MqttclientDAT Class") for usage.
- Execute from `executeloc` - ⊞ - Determines the location the script is run from.
  * Current Node `current` - The script is executed from the current node location (for example, where 'cc' points to).
  * Callbacks DAT `callbacks` - The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
  * Specified Operator `op` - The script is executed from the operator specified in the From Operator parameter below.

- From Operator `fromop` - The operator whose state change will trigger the DAT to execute its script when Execute From is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute From parameter is set to Specified Operator.
- Clamp Output `clamp` - The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited.
- Maximum Lines `maxlines` - Limits the number of messages, older messages are removed from the list first.
- Clear Output `clear` - Deletes all lines except the heading. To clear with a python script `op(_"opname"_).par.clear.pulse()`
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
Extra Information for the MQTT Client DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific MQTT Client DAT Info Channels
  * connected -

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
