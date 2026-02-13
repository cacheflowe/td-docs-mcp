---
url: https://docs.derivative.ca/MediaWiki:Common.js
category: COMPs
title: MediaWiki:Common.js
---

# MediaWiki:common.js
**Note:** After publishing, you may have to bypass your browser's cache to see the changes.
  * **Firefox / Safari:** Hold _Shift_ while clicking _Reload_ , or press either _Ctrl-F5_ or _Ctrl-R_ (_⌘-R_ on a Mac)
  * **Google Chrome:** Press _Ctrl-Shift-R_ (_⌘-Shift-R_ on a Mac)
  * **Internet Explorer / Edge:** Hold _Ctrl_ while clicking _Refresh_ , or press _Ctrl-F5_
  * **Opera:** Press _Ctrl-F5_.

```
[](https://docs.derivative.ca/MediaWiki:Common.js#L-1)/* Any JavaScript here will be loaded for all users on every page load. */
[](https://docs.derivative.ca/MediaWiki:Common.js#L-2)
[](https://docs.derivative.ca/MediaWiki:Common.js#L-3)function findGetParameter(parameterName) {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-4)    var result = null,
[](https://docs.derivative.ca/MediaWiki:Common.js#L-5)        tmp = [];
[](https://docs.derivative.ca/MediaWiki:Common.js#L-6)    location.search
[](https://docs.derivative.ca/MediaWiki:Common.js#L-7)        .substr(1)
[](https://docs.derivative.ca/MediaWiki:Common.js#L-8)        .split("&")
[](https://docs.derivative.ca/MediaWiki:Common.js#L-9)        .forEach(function (item) {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-10)          tmp = item.split("=");
[](https://docs.derivative.ca/MediaWiki:Common.js#L-11)          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
[](https://docs.derivative.ca/MediaWiki:Common.js#L-12)        });
[](https://docs.derivative.ca/MediaWiki:Common.js#L-13)    return result;
[](https://docs.derivative.ca/MediaWiki:Common.js#L-14)}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-15)
[](https://docs.derivative.ca/MediaWiki:Common.js#L-16)/* load TOC collapsed */
[](https://docs.derivative.ca/MediaWiki:Common.js#L-17)window.addEventListener('DOMContentLoaded', function() { try {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-18)  if (document.getElementById('toc').getElementsByTagName('ul')[0].style.display != 'none') { toggleToc(); }
[](https://docs.derivative.ca/MediaWiki:Common.js#L-19)} catch (exception) {} }, false);
[](https://docs.derivative.ca/MediaWiki:Common.js#L-20)
[](https://docs.derivative.ca/MediaWiki:Common.js#L-21)/* custom toolbars */
[](https://docs.derivative.ca/MediaWiki:Common.js#L-22)var customizeToolbar = function () {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-24)		'section': 'main',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-25)		'group': 'format',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-26)		'tools': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-27)			"TDpythonbutton": {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-28)				label: 'Python code',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-29)				type: 'button',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-30)				icon: 'https://docs.derivative.ca/images/b/bf/Pythonbutton.png',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-31)				action: {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-32)					type: 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-33)					options: {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-34)						pre: "<syntaxhighlight lang=python>",
[](https://docs.derivative.ca/MediaWiki:Common.js#L-35)						post: "</syntaxhighlight>"
[](https://docs.derivative.ca/MediaWiki:Common.js#L-36)	  				}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-37)	           }
[](https://docs.derivative.ca/MediaWiki:Common.js#L-38)			},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-39)			"TDcodebutton": {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-40)			label: 'Source code',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-41)			type: 'button',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-42)			icon: 'https://docs.derivative.ca/images/0/05/Codebutton.png',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-43)				action: {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-44)					type: 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-45)					options: {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-46)						pre: "<code>",
[](https://docs.derivative.ca/MediaWiki:Common.js#L-47)						post: "</code>"
[](https://docs.derivative.ca/MediaWiki:Common.js#L-48)	  				}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-49)	            }
[](https://docs.derivative.ca/MediaWiki:Common.js#L-50)			},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-51)			"TDyoutubebutton": {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-52)			label: 'Embed YouTube video',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-53)			type: 'button',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-54)			icon: 'https://docs.derivative.ca/images/a/af/Youtube.png',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-55)			action: {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-56)				type: 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-57)				options: {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-58)					pre: "{{#widget:YouTube|id=|width=|height=}}",
[](https://docs.derivative.ca/MediaWiki:Common.js#L-59)					post: ""
[](https://docs.derivative.ca/MediaWiki:Common.js#L-60)				}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-61)			}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-62)			}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-63)		}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-64)	} );
[](https://docs.derivative.ca/MediaWiki:Common.js#L-66)		'sections': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-67)			'templates': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-68)				'type': 'booklet', // Can also be 'booklet'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-69)				'label': 'Templates',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-70)				'pages':{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-71)					'section-glossary': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-72)						'label': 'Glossary',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-73)						'layout': 'characters',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-74)						'characters':[
[](#L-75)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-76)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-77)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-78)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-79)										'pre': '{{',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-80)										'peri':'Glossary|Title=|Short=|Long=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-81)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-82)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-83)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-84)								'label': 'Glossary Template'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-85)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-86)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-87)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-88)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-89)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-90)										'pre': '[[',
[](#L-91)										'peri':'Category: Touch Glossary',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-92)										'post':']]'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-93)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-94)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-95)								'label': 'Glossary Category'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-96)							}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-97)						]
[](https://docs.derivative.ca/MediaWiki:Common.js#L-98)					},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-99)					'section-operators': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-100)						'label': 'Operator Pages',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-101)						'layout': 'characters',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-102)						'characters':[
[](#L-103)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-104)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-105)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-106)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-107)										'pre': '{{Summary',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-108)										'peri':'|opFamily=|opLabel=|opType=|opClass=|opFilter=|opLicense=|opCategory=|os=|hardware=|short=|long=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-109)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-110)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-111)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-112)								'label': 'Operator Summary'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-113)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-114)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-115)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-116)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-117)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-118)										'pre': '{{ParameterPage',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-119)										'peri':'|opFamily=|pageName=|pageSummary=|items=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-120)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-121)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-122)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-123)								'label': 'Parameter Page'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-124)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-125)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-126)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-127)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-128)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-129)										'pre': '{{ParameterSubPage',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-130)										'peri':'|opFamily=|pageName=|pageSummary=|items=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-131)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-132)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-133)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-134)								'label': 'Parameter Sub Page'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-135)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-136)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-137)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-138)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-139)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-140)										'pre': '{{OPSection',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-141)										'peri':'|opFamily=|sectionName=|sectionSummary=|items=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-142)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-143)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-144)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-145)								'label': 'Operator Section'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-146)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-147)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-148)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-149)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-150)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-151)										'pre': '{{OPSubSection',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-152)										'peri':'|opFamily=|sectionName=|sectionSummary=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-153)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-154)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-155)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-156)								'label': 'Operator Sub Section'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-157)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-158)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-159)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-160)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-161)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-162)										'pre': '{{InfoCHOPChannels',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-163)										'peri':'|opFamily=|opLabel=|infoChannels=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-164)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-165)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-166)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-167)								'label': 'Operator Info CHOP Section'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-168)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-169)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-170)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-171)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-172)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-173)										'pre': '{{InfoChannel',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-174)										'peri':'|chanName=|chanSummary=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-175)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-176)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-177)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-178)								'label': 'Info CHOP Channel'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-179)							}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-180)						]
[](https://docs.derivative.ca/MediaWiki:Common.js#L-181)					},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-182)					'section-oppars': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-183)						'label': 'Operator Parameters',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-184)						'layout': 'characters',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-185)						'characters':[
[](#L-186)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-187)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-188)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-189)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-190)										'pre': '{{Parameter',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-191)										'peri':'|opFamily=|opType=|parName=|parLabel=|parDefault=|parType=|parReadOnly=|parOrder=|parSummary=|parItems=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-192)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-193)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-194)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-195)								'label': 'Parameter'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-196)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-197)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-198)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-199)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-200)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-201)										'pre': '{{ParameterItem',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-202)										'peri':'|opFamily=|parName=|itemName=|itemLabel=|itemDefault=|itemSummary=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-203)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-204)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-205)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-206)								'label': 'Parameter Item'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-207)							}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-208)						]
[](https://docs.derivative.ca/MediaWiki:Common.js#L-209)					},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-210)					'section-class': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-211)						'label': 'Python Classes',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-212)						'layout': 'characters',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-213)						'characters':[
[](#L-214)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-215)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-216)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-217)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-218)										'pre': '{{',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-219)										'peri':'OPClassSummary|OPfamily=|OPtype=|OPlabel=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-220)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-221)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-222)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-223)								'label': 'OPClassSummary'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-224)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-225)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-226)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-227)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-228)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-229)										'pre': '{{',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-230)										'peri':'TDClassSummary|label=|summary=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-231)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-232)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-233)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-234)								'label': 'TDClassSummary'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-235)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-236)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-237)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-238)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-239)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-240)										'pre': '{{',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-241)										'peri':'ClassMemberSection|Sectionsummary=|items=|empty=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-242)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-243)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-244)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-245)								'label': 'ClassMemberSection'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-246)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-247)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-248)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-249)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-250)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-251)										'pre': '{{',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-252)										'peri':'ClassMember|class=|name=|type=|set=|text=|deprecated=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-253)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-254)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-255)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-256)								'label': 'ClassMember'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-257)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-258)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-259)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-260)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-261)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-262)										'pre': '{{',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-263)										'peri':'ClassMethodSection|SectionSummary=|items=|empty=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-264)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-265)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-266)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-267)								'label': 'ClassMethodSection'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-268)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-269)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-270)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-271)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-272)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-273)										'pre': '{{',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-274)										'peri':'ClassMethod|class=|name=|call=|returns=|text=|deprecated=',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-275)										'post':'}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-276)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-277)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-278)								'label': 'ClassMethod'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-279)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-280)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-281)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-282)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-283)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-284)										'pre': '{{SubSection|title=|text=}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-285)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-286)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-287)								'label': 'Class SubSection'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-288)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-289)						]
[](https://docs.derivative.ca/MediaWiki:Common.js#L-290)					},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-291)					'section-page': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-292)						'label': 'General Page Elements',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-293)						'layout': 'characters',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-294)						'characters':[
[](#L-295)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-296)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-297)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-298)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-299)										'pre': '{{History}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-300)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-301)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-302)								'label': 'Tag History'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-303)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-304)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-305)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-306)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-307)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-308)										'pre': '{{SOPNavBox|opFamily=SOP}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-309)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-310)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-311)								'label': 'Category Navigation Box'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-312)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-313)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-314)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-315)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-316)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-317)										'pre': '{{#invoke:Category|list|COMPs}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-318)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-319)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-320)								'label': 'Category List'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-321)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-322)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-323)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-324)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-325)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-326)										'pre': '{{lowercase}}'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-327)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-328)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-329)								'label': 'Force pagetitle to lowercase'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-330)							},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-331)							{
[](https://docs.derivative.ca/MediaWiki:Common.js#L-332)								'action': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-333)									'type': 'encapsulate',
[](https://docs.derivative.ca/MediaWiki:Common.js#L-334)									'options': {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-335)										'pre': '#REDIRECT [[:Experimental:{{FULLPAGENAME}}]]'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-336)									}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-337)								},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-338)								'label': 'Redirect to Experimental'
[](https://docs.derivative.ca/MediaWiki:Common.js#L-339)							}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-340)						]
[](https://docs.derivative.ca/MediaWiki:Common.js#L-341)					},
[](https://docs.derivative.ca/MediaWiki:Common.js#L-342)				}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-343)			}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-344)		}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-345)	} );
[](https://docs.derivative.ca/MediaWiki:Common.js#L-346)};
[](https://docs.derivative.ca/MediaWiki:Common.js#L-347)
[](https://docs.derivative.ca/MediaWiki:Common.js#L-348)
[](https://docs.derivative.ca/MediaWiki:Common.js#L-349)/* Check if view is in edit mode and that the required modules are available. Then, customize the toolbar … */
[](https://docs.derivative.ca/MediaWiki:Common.js#L-350)if ( [ 'edit', 'submit' ].indexOf( mw.config.get( 'wgAction' ) ) !== -1 ) {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-351)	mw.loader.using( 'user.options' ).then( function () {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-352)		// This can be the string "0" if the user disabled the preference ([[phab:T54542#555387]])
[](https://docs.derivative.ca/MediaWiki:Common.js#L-353)		if ( mw.user.options.get( 'usebetatoolbar' ) == 1 ) {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-354)			$.when(
[](https://docs.derivative.ca/MediaWiki:Common.js#L-356)			).then( customizeToolbar );
[](https://docs.derivative.ca/MediaWiki:Common.js#L-357)		}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-358)	} );
[](https://docs.derivative.ca/MediaWiki:Common.js#L-359)}
[](https://docs.derivative.ca/MediaWiki:Common.js#L-360)
[](https://docs.derivative.ca/MediaWiki:Common.js#L-361)// Redirect anonymous users to login form.
[](https://docs.derivative.ca/MediaWiki:Common.js#L-362)/*
[](https://docs.derivative.ca/MediaWiki:Common.js#L-363)jQuery(document).ready(function() {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-364)  if (jQuery('#pt-anon_oauth_login').length) {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-365)   var titleUrl = findGetParameter('title');
[](https://docs.derivative.ca/MediaWiki:Common.js#L-366)   if (titleUrl) {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-367)     var returnUrl = '/index.php?title=Special:OAuth2Client/redirect&returnto=' + titleUrl;
[](https://docs.derivative.ca/MediaWiki:Common.js#L-368)   }
[](https://docs.derivative.ca/MediaWiki:Common.js#L-369)   else {
[](https://docs.derivative.ca/MediaWiki:Common.js#L-370)     var returnUrl = '/index.php?title=Special:OAuth2Client/redirect&returnto=Main+Page';
[](https://docs.derivative.ca/MediaWiki:Common.js#L-371)   }
[](https://docs.derivative.ca/MediaWiki:Common.js#L-372)   window.location.href = returnUrl;
[](https://docs.derivative.ca/MediaWiki:Common.js#L-373)  }
[](https://docs.derivative.ca/MediaWiki:Common.js#L-374)});
[](https://docs.derivative.ca/MediaWiki:Common.js#L-375)*/

```

An [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") which operate on [Channels](https://docs.derivative.ca/Channel "Channel") (a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.
A [CHOP](https://docs.derivative.ca/CHOP "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](https://docs.derivative.ca/Sample "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](https://docs.derivative.ca/Export "Export") to [Parameters](https://docs.derivative.ca/Parameter "Parameter").
Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](https://docs.derivative.ca/Network_Path "Network Path"), which determine the output of the operator.
Each operator can have a set of text strings that are its "tags". You can set them and search for them within TouchDesigner.
A [Operator Family](https://docs.derivative.ca/Operator_Family "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
