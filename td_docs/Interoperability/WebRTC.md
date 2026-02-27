---
url: https://docs.derivative.ca/WebRTC
category: Interoperability
title: WebRTC
---

# WebRTC

###
What is WebRTC

[WebRTC](https://webrtc.org) (Web Real-Time communication) is an open standard for peer-to-peer communication on the web. It supports sending of low-latency video, audio, and generic data between peers. WebRTC is supported by all modern browsers and thus provides a mechanism to stream video/audio/data from TouchDesigner to web browsers.
Further reading: [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API).
###
WebRTC in TouchDesigner

WebRTC in TouchDesigner is supported through the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT"). A WebRTC DAT represents a peer on one end of any number of WebRTC peer-to-peer connections. The approach to the WebRTC DAT is python focused, following the callback-focused nature of the [WebRTC JavaScript library](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection). Method/callback names are kept as close as possible to their JavaScript counterparts.
WebRTC video and audio input/output is done via the [Video Stream In TOP](https://docs.derivative.ca/Video_Stream_In_TOP "Video Stream In TOP"), [Video Stream Out TOP](https://docs.derivative.ca/Video_Stream_Out_TOP "Video Stream Out TOP"), [Audio Stream In CHOP](https://docs.derivative.ca/Audio_Stream_In_CHOP "Audio Stream In CHOP"), and [Audio Stream Out CHOP](https://docs.derivative.ca/Audio_Stream_Out_CHOP "Audio Stream Out CHOP") with reference to a [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT").
See [WebrtcDAT_Class](https://docs.derivative.ca/WebrtcDAT_Class "WebrtcDAT Class").
For users that wish to test, review, or demo the technology, TouchDesigner 2022.21000+ includes [Palette:signalingServer](https://docs.derivative.ca/Palette:signalingServer "Palette:signalingServer"), [Palette:signalingClient](https://docs.derivative.ca/Palette:signalingClient "Palette:signalingClient") and [Palette:webRTC](https://docs.derivative.ca/Palette:webRTC "Palette:webRTC") COMPs in the WebRTC folder of the [Palette](https://docs.derivative.ca/Palette "Palette").
To get it up and running quickly, start two TouchDesigner processes. In one process, add a signalingServer, a signalingClient and webRTC COMP. In the other process, add a signalingClient and a webRTC COMP. Visit the respective help articles linked to figure out which parameters to fill or tweak to your needs.
Advanced users are encouraged to visit the extension pages of the signalingServer, signalingClient and webRTC COMPs.
The palette contains the [Palette:webRTCPanel](https://docs.derivative.ca/Palette:webRTCPanel "Palette:webRTCPanel") and the [Palette:webRTCPanelRcv](https://docs.derivative.ca/Palette:webRTCPanelRcv "Palette:webRTCPanelRcv"). These components allow to quickly share a remote panel over a WebRTC session. Details on how to get a quick setup going are available on the [Palette:webRTCPanel](https://docs.derivative.ca/Palette:webRTCPanel "Palette:webRTCPanel") page.
There is also a web based version of the webRTCPanelRcv component available [in the following repository](https://github.com/TouchDesigner/WebRTC-Remote-Panel-Web-Demo) as well as an online demo following [this link](https://touchdesigner.github.io/WebRTC-Remote-Panel-Web-Demo/).
An article introducing users to the technology as well as a quick setup guide is available at [the following link](https://derivative.ca/community-post/experience-webrtc-and-webrtc-remote-panel-new-webrtc-remote-panel-web-demo/67004).
###
Signaling

In order to establish a peer-to-peer connection over WebRTC, a negotiation process must be completed through a mutually-agreed upon signaling server. A WebRTC connection cannot be established without a signaling server.
The signaling server must relay messages (ie. offers, answers, candidates) between connecting peers so they can complete the negotiation process. The protocol and design of the signaling server is undefined by WebRTC and is left completely open.
For example, TouchDesigner's sample signaling server ([Palette:signalingServer](https://docs.derivative.ca/Palette:signalingServer "Palette:signalingServer")) uses WebSockets. Connection to that signaling server can be done using a [Palette:signalingClient](https://docs.derivative.ca/Palette:signalingClient "Palette:signalingClient") in conjunction with [Palette:webRTC](https://docs.derivative.ca/Palette:webRTC "Palette:webRTC") COMP.
Further reading:
<https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Connectivity>
<https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Signaling_and_video_calling>
###
SDP

SDP (Session Description Protocol) is the protocol used in WebRTC to describe one end of a peer-to-peer connection. It contains a variety of information about what a peer can support over a connection including: audio info, video info, data channel info, codecs, source address, candidates, and more.
SDPs are exchanged through a signaling server.
In TouchDesigner the local SDP will be passed through the [onOffer](https://docs.derivative.ca/WebrtcDAT_Class#Callbacks) and [onAnswer](https://docs.derivative.ca/WebrtcDAT_Class#Callbacks) callbacks after [createOffer](https://docs.derivative.ca/WebrtcDAT_Class#createOffer) and [createAnswer](https://docs.derivative.ca/WebrtcDAT_Class#createAnswer) are called respectively. It must be set locally on the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT") using [setLocalDescription](https://docs.derivative.ca/WebrtcDAT_Class#setLocalDescription), then passed to the signaling server. Once the corresponding remote SDP is received, it should be set with [setRemoteDescription](https://docs.derivative.ca/WebrtcDAT_Class#setRemoteDescription).
Further reading: [Anatomy of a WebRTC SDP](https://webrtchacks.com/sdp-anatomy/).
###
ICE

ICE (Interactive Connectivity Establishment) is the protocol used to connect two peers over a network. An important part of the network connection process are [ICE candidates](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Connectivity#ice_candidates), which are essentially connection points at which a remote peer can reach the local peer. They are typically associated with a media stream, either audio or video.
The ICE candidate gathering process is typically executed after an offer or answer is created. Candidates will be passed through to the onIceCandidate callback on the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT") where they should then be sent to the signaling server. Remote ICE candidates can be added using the [addIceCandidate](https://docs.derivative.ca/WebrtcDAT_Class#addIceCandidate) method as they are received from the signaling server.
ICE candidates can either be locally generated, STUN (Session Traversal Utilities for NAT), or TURN (Traversal Using Relay NAT).
**STUN** : [STUN servers](https://www.3cx.com/pbx/what-is-a-stun-server/) will generate ICE candidates for a peer. There are many free public STUN servers available, and by default the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT") uses stun:stun.l.google.com:19302. In some set-ups NAT traversal may not be possible using the candidates generated by a STUN server (eg. because of firewall), and the connection will fail. In these cases a TURN server will be required.
**TURN** : [TURN servers](https://webrtc.org/getting-started/turn-server) act as a relay between peers, which is useful in the event that the peers cannot connect directly using STUN (eg. because NAT traversal fails or due to network ambiguity perhaps). It is unlikely that there are any free TURN servers available because they must also relay media traffic between peers. Custom TURN server URLs can be specified on the ICE page of the [WebRTC DAT](https://docs.derivative.ca/WebRTC_DAT "WebRTC DAT").
Sample for testing of ICE candidate gathering on your machine: <https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/>
###
Versions
