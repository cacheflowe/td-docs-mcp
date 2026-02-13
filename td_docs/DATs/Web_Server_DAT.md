---
url: https://docs.derivative.ca/Web_Server_DAT
category: DATs
title: Web_Server_DAT
---

# Web Server DAT
## Summary

The Web Server DAT allows you to connect to TouchDesigner as a web client, through a web browser for example. The Web Server DAT supports HTTP, WebSockets, as well as the sending/receiving of binary data, such as images (uploading/downloading). How client requests are handled is left up to the user via callbacks.
The Web Server DAT can be secure, and also supports basic authentication via the authenticateBasic in the [webserverDAT_Class](https://docs.derivative.ca/WebserverDAT_Class "WebserverDAT Class"). Currently only Basic authentication (ie. encoded username and password) is supported via a python method. Authentication will be in the HTTP request dictionary under the key 'Authorization'.
Ultimately, security is the complete responsibility of the user. It is up to the user to ensure that HTTP requests are properly authenticated, and any data storing usernames/passwords are encrypted or saved privately.
HTTPS is supported via the Secure (TLS) parameter.
The Web Server DAT is built with [POCO](https://github.com/pocoproject/poco) v1.13.3.
See also: [Web Client DAT](https://docs.derivative.ca/Web_Client_DAT "Web Client DAT")
[webserverDAT_Class](https://docs.derivative.ca/WebserverDAT_Class "WebserverDAT Class")

## Parameters - Web Server Page
- Active `active` - Starts and Stops the webserver.
- Restart `restart` - When the server is active, pulsing will restart it.
- Port `port` - The web server's connection port. Eg. If the port number is 9980, the web server can be connected to locally (via a web browser) at the address "localhost:9980".
- Secure (TLS) `secure` - When enabled, the web server will use transport layer security (TLS) to create secure connections with clients. As a result, the web server will run through HTTPS instead of HTTP.
- Private Key File Path `privatekey` - The path to the private key file of the server's TLS certificate.
- Certificate File Path `certificate` - The path to the certificate file of the server's TLS certificate.
- Certificate Password `password` - The password for the certificate specified above. The password is only visually hidden and can still be accessed via python. In order to protect it and encrypt it when the project is saved, the Web Server DAT should be put in a private component.
- Callbacks DAT `callbacks` - A reference to a DAT with python callbacks. The Web Server DAT relies heavily on the Callbacks DAT, and in fact most functionality passes through the callbacks.
`onHTTPRequest` - Triggered when the web server receives an HTTP request. The request is a dictionary of HTTP headers. Similarly, response is a dictionary of response data such as status and reason. Additional key/value pairs can be added to the response dictionary that will be added as headers in the HTTP response. The response server must be returned from the callback. This response will be sent back to the client.
`onWebSocketOpen` - Triggered when a WebSocket connection is opened with a client. The client address is passed to the callback.
`onWebSocketClose` - Triggered when a WebSocket connection is closed. The client address is passed to the callback.
`onWebSocketReceiveText` - Triggered when the server's WebSocket connection receives text data from a client. The client that sent the text data is passed through to the callback.
`onWebSocketReceiveBinary` - Triggered when the server's WebSocket connection receives binary data from a client. The client that sent the binary data is passed through to the callback.
`onServerStart` - Triggered when the server starts.
`onServerStop` - Triggered when the server stops.

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
Extra Information for the Web Server DAT can be accessed via an [Info CHOP](https://docs.derivative.ca/Info_CHOP "Info CHOP").
###
Specific Web Server DAT Info Channels
  * server_running -

  * websocket_connections -

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
