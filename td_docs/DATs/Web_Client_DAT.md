---
url: https://docs.derivative.ca/Web_Client_DAT
category: DATs
title: Web_Client_DAT
---

# Web Client DAT
## Summary

The Web Client DAT allows you to send HTTP requests to web servers from TouchDesigner. It supports GET, POST, PUT, DELETE, HEAD, OPTIONS and PATCH http methods.
The Web Client DAT supports various authentication types such as: basic, oauth1, oauth2.
The Web Client DAT allows for streaming from web servers.
The Web Client DAT sends HTTP requests to web servers and then outputs the response in the DAT. With streaming enabled it can stream data from a web server.
When streaming is enabled, Clamp Output as Rows should be enabled. This turns the output of the DAT into a FIFO table instead of raw text. Only the last N lines will be displayed, where N is the value of the Maximum Lines parameter. This will prevent the text in the DAT from getting too larger and will keep cook-times down as a result.
The Web Client DAT supports sending of GET, POST, PUT, DELETE, HEAD, OPTIONS, and PATCH request methods. The Web Client DAT also supports 4 authentication methods: Basic, Digest, OAuth1, and OAuth2.
The first input is the extra headers to send in the request. It should be a table with 2 columns, structured as name/value pairs. For example:
Content-Type  | application/json
---|---
Connection  | Close
The second input is the data/parameters to send in the request. This can be a table with two columns, structured as name/value pairs. It can also just be text, in which case it will be sent as is. If the request method doesn't have a request body (eg. GET, OPTIONS) then it will append the input to the URL as query parameters if a table, otherwise it will be sent as the request data.
name  | joe
---|---
month  | May
The Web Client DAT is the successor to the [Web DAT](https://docs.derivative.ca/Web_DAT "Web DAT").
See also: [Web Server DAT](https://docs.derivative.ca/Web_Server_DAT "Web Server DAT"), [SocketIO DAT](https://docs.derivative.ca/SocketIO_DAT "SocketIO DAT"), [XML DAT](https://docs.derivative.ca/XML_DAT "XML DAT"), [TCP/IP DAT](https://docs.derivative.ca/TCP/IP_DAT "TCP/IP DAT"), [WebSocket DAT](https://docs.derivative.ca/WebSocket_DAT "WebSocket DAT"), [Web DAT](https://docs.derivative.ca/Web_DAT "Web DAT").
[webclientDAT_Class](https://docs.derivative.ca/WebclientDAT_Class "WebclientDAT Class")

## Parameters - Web Client Page
- Active `active` - Toggles the operator on/off.
- Request Method `reqmethod` - ⊞ - Selects the [HTTP request method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).
  * GET `get` - The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
  * POST `post` - The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.
  * PUT `put` - The PUT method replaces all current representations of the target resource with the request payload.
  * DELETE `delete` - The DELETE method deletes the specified resource.
  * HEAD `head` - The HEAD method asks for a response identical to that of a GET request, but without the response body.
  * OPTIONS `options` - The OPTIONS method is used to describe the communication options for the target resource.
  * PATCH `patch` - The PATCH method is used to apply partial modifications to a resource.

- URL `url` - The URL of the server to send the HTTP request. Generally, if sending an HTTP request to a secure server, then the URL should begin with "https://".
- Upload File `uploadfile` - The contents of the upload file will be sent to the server (chunked, if necessary).
- Request `request` - Sends the request
- Stop `stop` - Stops the stream of data from the server.
- Stream `stream` - Enables streaming. This is only necessary to enable if the server support streaming.
- Verify Certificate (SSL) `verifycert` - Enables TLS (transport layer security) certificate verification.
- Timeout `timeout` - Timeout time in milliseconds of the request if no response is received from the web server.
- Include Header in Output `includeheader` - Includes the header in the output of the response.

## Parameters - Authentication Page
- Authentication Type `authtype` - ⊞ - The type of authentication.
  * None `none` - No authentication
  * Basic `basic` - Basic authentication is base-64 encoded username and password.
  * Digest `digest` - Digest authentication is base-64 encoded username and password that's encrypted with a hashing function. Digest is a more secure version of Basic authentication.
  * OAuth1 `ouath1` - Version 1 of OAuth. OAuth1 requires App Key, App Secret, User OAuth Token, and User OAuth Secret. These can be found via the account on the web server that request is being sent to. For example, in the case of the Twitter API the values of these 4 parameters can be found under the account profile.
  * OAuth2 `ouath2` - Version 2 of OAuth. OAuth2 first requires an HTTP request be sent to the web server to acquire the Client ID and token. It can be acquired using a browser.

- Username `username` - Username used in Basic/Digest authentication.
- Password `pw` - Password used in Basic/Digest authentication.
