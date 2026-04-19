---
url: https://docs.derivative.ca/Palette:webBrowser
category: Interoperability
title: Palette:webBrowser
---

# Palette:webBrowser

## Summary

The `webBrowser` component in the palette is an interactive interface to the [Web Render TOP](https://docs.derivative.ca/Web_Render_TOP "Web Render TOP"). It is currently available on Windows only, in the Commercial, Educational and Pro versions of TouchDesigner.

`webBrowser` and the [Web Render TOP](https://docs.derivative.ca/Web_Render_TOP "Web Render TOP") is the Chromium project underneath, with the CEF (Chromium Embedded Framework) wrapper providing the interface to the `webBrowser` and the [Web Render TOP](https://docs.derivative.ca/Web_Render_TOP "Web Render TOP").

NOTE: The `webBrowser` component and the Web Render TOP are provided as-is with no support of the features or performance of the underlying technologies. Numerous features or capabilities of the Chrome / Chromium are not functioning and it is up to you to determine if it is satisfactory for your needs, and you assume the risk of its use in production.

See also [Web Render TOP](https://docs.derivative.ca/Web_Render_TOP "Web Render TOP").

[Palette:webBrowser Ext](https://docs.derivative.ca/index.php?title=Palette:webBrowser_Ext&action=edit&redlink=1 "Palette:webBrowser Ext \(page does not exist\)")



General Usage

When you click on web pages in the panel, the new URL is placed in the Address parameter and the new page is displayed.

It has pulse parameters to do the common Reload, Back and Forward functions of a browser.

Three Search pages are built-in where you enter a string in the Search Term parameter, select the Search Page from the menu and press the Search pulse. The Search page is in an extendable table inside the webBrowser component.

You can set the panel resolution in the Layout page Width and Height parameters, and the page will re-render and adjust to the new size. Your mouse roller wheel will control the scrolling but CAVEAT: the scroll bar may not function with the mouse unless you drag off the scroll bar.

You can pass a JavaScript to the web page via the JavaScript and Send JavaScript parameters.

Status and Errors are reported in three read-only parameters.


## Parameters - Web Browser Page
- Help `Help` - Opens this page.
- Version `Version` -
- Address `Address` - Enter the url the Web Browser should render here. When navigating a website, the current url is shown here as well.
- Reload Current Page `Reload` - Reloads the page specified in the Address parameter by calling the JavaScript location.reload() function.
- Go Back `Goback` - Renders the previous visited page in the browser history by calling the JavaScript window.history.back() function.
- Go Forward `Goforward` - Renders the next visited page in the browser history by calling the JavaScript window.history.forward() function.
- Search Page `Searchpage` - ⊞ - Select from a list of predefined pages searchable with the Search Term parameter. The three predefined Pages: DuckDuckGo, TouchDesigner Wiki and TouchDesigner Forum are defined via a Table DAT inside the webBrowser component. To add or replace search pages, find the Table DAT called "pageSearch" and enter a name and label for how the search page would be displayed in this parameter, plus the url which allows to search.

For Example:

To add stackOverflow insert a new row into the table DAT called pageSearch with stack as the value for the name column, stackoverflow as the value for the label column and <https://stackoverflow.com/search?q=> as the value for the url column.
  * TouchDesigner Wiki `tdwiki` - Searches the TouchDesigner Documentation.

  * TouchDesigner Forum `tdforum` - Searches the TouchDesigner Forum.

  * DuckDuckGo `duckduck` - Searches DuckDuckGo.

- Search Term `Searchterm` - Search Term for Search Page.
- Search `Search` - Initiate Search on page specified in Search Page parameter.
- JavaScript `Javascript` - Specify JavaScript code to be executed on the currently loaded page. Have a look at the JavaScript HTML DOM Lessons for [JS HTML DOM](https://www.w3schools.com/js/js_htmldom.asp) to find some examples.
- Send JavaScript `Sendjavascript` - Send the JavaScript specified in the JavaScript parameter to the currently loaded website.
- HTTP Status `Httpstatus` -
- Error `Error` -
- Error Code `Errorcode` -


## Parameters - Settings Page
- Active `Active` - Enables/disables the [Web Render TOP](https://docs.derivative.ca/Web_Render_TOP "Web Render TOP").
- Update Only when Loaded `Updatewhenloaded` - Only shows the web page when it is full loaded.
- Transparent Background `Transparent` - Loads the webpage with a transparent background. This option will restart the browser process.
- Enable Audio `Audio` - Let the browser process play audio if the web page contains audio. This option will restart the browser process.
- Restart if Process Died `Autorestart` - Automatically restart the browser process if it died.
- Restart `Restart` - Restart the browser process.


## Operator Outputs

  * Output 0 - The webpage as a texture.
