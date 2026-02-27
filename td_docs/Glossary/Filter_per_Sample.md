---
url: https://docs.derivative.ca/Filter_per_Sample
category: Glossary
title: Filter_per_Sample
---

# Filter per Sample
CHOPs that (temporally) filter over time, like the [Lag CHOP](https://docs.derivative.ca/Lag_CHOP "Lag CHOP") and [Filter CHOP](https://docs.derivative.ca/Filter_CHOP "Filter CHOP") can also treat each sample as its own filter. Turn on their Filter per Sample parameter and each sample will behave like separate filter.
For example, if you have 20 channels that are 100 samples long that are all set to 0, feeding into a Filter CHOP with Filter per Sample turned on, and then you set only one sample of the input to 1, that sample of the output will ramp up to 1 over one second, but all other samples will remain 0. Each sample is a separate filter.
Other CHOPs with this feature are [Hold CHOP](https://docs.derivative.ca/Hold_CHOP "Hold CHOP"), [Slope CHOP](https://docs.derivative.ca/Slope_CHOP "Slope CHOP"), [Speed CHOP](https://docs.derivative.ca/Speed_CHOP "Speed CHOP") and [Spring CHOP](https://docs.derivative.ca/Spring_CHOP "Spring CHOP").
A powerful feature of CHOPs that filter over time, like the [Lag CHOP](https://docs.derivative.ca/Lag_CHOP "Lag CHOP") and [Filter CHOP](https://docs.derivative.ca/Filter_CHOP "Filter CHOP") where each sample acts as its own filter.
An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
