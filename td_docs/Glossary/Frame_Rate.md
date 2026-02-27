---
url: https://docs.derivative.ca/Frame_Rate
category: Glossary
title: Frame_Rate
---

# Frame Rate
The frame rate is the Frames-per-Second (FPS) that TouchDesigner's [Timeline](https://docs.derivative.ca/Timeline "Timeline") runs at.
The global frame rate of a project is set with the `project.cookRate` Member of the [Project Class](https://docs.derivative.ca/Project_Class "Project Class").
All non-audio [CHOPs](https://docs.derivative.ca/CHOP "CHOP") have their sample rate set by default to this rate.
Every component can have its own frame rate and start-end range. See the [Time COMP](https://docs.derivative.ca/Time_COMP "Time COMP").
Frame rate is stored in the Timeline's [Time COMP](https://docs.derivative.ca/Time_COMP "Time COMP") in the parameter called **Rate**. It can be set through the Timeline's UI, directly via the component's Rate parameter or via the `rate` Member of the [timeCOMP Class](https://docs.derivative.ca/TimeCOMP_Class "TimeCOMP Class").
Note that a movie file read by the [Movie File In TOP](https://docs.derivative.ca/Movie_File_In_TOP "Movie File In TOP") may have its own "frame rate" or "frames per second", but in TouchDesigner we call it the movie's "images per second" or "sample rate" to avoid confusion.
See [Optimize](https://docs.derivative.ca/Optimize "Optimize").
The [Frames](https://docs.derivative.ca/Frame "Frame")-per-Second that TouchDesigner's [Timeline](https://docs.derivative.ca/Timeline "Timeline") runs at. Set with `project.cookRate`.
The panel at the bottom of TouchDesigner, it controls the current global looping [Time](https://docs.derivative.ca/Time_COMP "Time COMP") your TouchDesigner project, or of just one component.
