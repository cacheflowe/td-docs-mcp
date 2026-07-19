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
[](MediaWiki_Common.js.md#L-1)/* Any JavaScript here will be loaded for all users on every page load. */
[](MediaWiki_Common.js.md#L-2)
[](MediaWiki_Common.js.md#L-3)function findGetParameter(parameterName) {
[](MediaWiki_Common.js.md#L-4)    var result = null,
[](MediaWiki_Common.js.md#L-5)        tmp = [];
[](MediaWiki_Common.js.md#L-6)    location.search
[](MediaWiki_Common.js.md#L-7)        .substr(1)
[](MediaWiki_Common.js.md#L-8)        .split("&")
[](MediaWiki_Common.js.md#L-9)        .forEach(function (item) {
[](MediaWiki_Common.js.md#L-10)          tmp = item.split("=");
[](MediaWiki_Common.js.md#L-11)          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
[](MediaWiki_Common.js.md#L-12)        });
[](MediaWiki_Common.js.md#L-13)    return result;
[](MediaWiki_Common.js.md#L-14)}
[](MediaWiki_Common.js.md#L-15)
[](MediaWiki_Common.js.md#L-16)/* load TOC collapsed */
[](MediaWiki_Common.js.md#L-17)window.addEventListener('DOMContentLoaded', function() { try {
[](MediaWiki_Common.js.md#L-18)  if (document.getElementById('toc').getElementsByTagName('ul')[0].style.display != 'none') { toggleToc(); }
[](MediaWiki_Common.js.md#L-19)} catch (exception) {} }, false);
[](MediaWiki_Common.js.md#L-20)
[](MediaWiki_Common.js.md#L-21)/* custom toolbars */
[](MediaWiki_Common.js.md#L-22)var customizeToolbar = function () {
[](MediaWiki_Common.js.md#L-24)		'section': 'main',
[](MediaWiki_Common.js.md#L-25)		'group': 'format',
[](MediaWiki_Common.js.md#L-26)		'tools': {
[](MediaWiki_Common.js.md#L-27)			"TDpythonbutton": {
[](MediaWiki_Common.js.md#L-28)				label: 'Python code',
[](MediaWiki_Common.js.md#L-29)				type: 'button',
[](MediaWiki_Common.js.md#L-30)				icon: 'https://docs.derivative.ca/images/b/bf/Pythonbutton.png',
[](MediaWiki_Common.js.md#L-31)				action: {
[](MediaWiki_Common.js.md#L-32)					type: 'encapsulate',
[](MediaWiki_Common.js.md#L-33)					options: {
[](MediaWiki_Common.js.md#L-34)						pre: "<syntaxhighlight lang=python>",
[](MediaWiki_Common.js.md#L-35)						post: "</syntaxhighlight>"
[](MediaWiki_Common.js.md#L-36)	  				}
[](MediaWiki_Common.js.md#L-37)	           }
[](MediaWiki_Common.js.md#L-38)			},
[](MediaWiki_Common.js.md#L-39)			"TDcodebutton": {
[](MediaWiki_Common.js.md#L-40)			label: 'Source code',
[](MediaWiki_Common.js.md#L-41)			type: 'button',
[](MediaWiki_Common.js.md#L-42)			icon: 'https://docs.derivative.ca/images/0/05/Codebutton.png',
[](MediaWiki_Common.js.md#L-43)				action: {
[](MediaWiki_Common.js.md#L-44)					type: 'encapsulate',
[](MediaWiki_Common.js.md#L-45)					options: {
[](MediaWiki_Common.js.md#L-46)						pre: "<code>",
[](MediaWiki_Common.js.md#L-47)						post: "</code>"
[](MediaWiki_Common.js.md#L-48)	  				}
[](MediaWiki_Common.js.md#L-49)	            }
[](MediaWiki_Common.js.md#L-50)			},
[](MediaWiki_Common.js.md#L-51)			"TDyoutubebutton": {
[](MediaWiki_Common.js.md#L-52)			label: 'Embed YouTube video',
[](MediaWiki_Common.js.md#L-53)			type: 'button',
[](MediaWiki_Common.js.md#L-54)			icon: 'https://docs.derivative.ca/images/a/af/Youtube.png',
[](MediaWiki_Common.js.md#L-55)			action: {
[](MediaWiki_Common.js.md#L-56)				type: 'encapsulate',
[](MediaWiki_Common.js.md#L-57)				options: {
[](MediaWiki_Common.js.md#L-58)					pre: "{{#widget:YouTube|id=|width=|height=}}",
[](MediaWiki_Common.js.md#L-59)					post: ""
[](MediaWiki_Common.js.md#L-60)				}
[](MediaWiki_Common.js.md#L-61)			}
[](MediaWiki_Common.js.md#L-62)			}
[](MediaWiki_Common.js.md#L-63)		}
[](MediaWiki_Common.js.md#L-64)	} );
[](MediaWiki_Common.js.md#L-66)		'sections': {
[](MediaWiki_Common.js.md#L-67)			'templates': {
[](MediaWiki_Common.js.md#L-68)				'type': 'booklet', // Can also be 'booklet'
[](MediaWiki_Common.js.md#L-69)				'label': 'Templates',
[](MediaWiki_Common.js.md#L-70)				'pages':{
[](MediaWiki_Common.js.md#L-71)					'section-glossary': {
[](MediaWiki_Common.js.md#L-72)						'label': 'Glossary',
[](MediaWiki_Common.js.md#L-73)						'layout': 'characters',
[](MediaWiki_Common.js.md#L-74)						'characters':[
[](#L-75)							{
[](MediaWiki_Common.js.md#L-76)								'action': {
[](MediaWiki_Common.js.md#L-77)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-78)									'options': {
[](MediaWiki_Common.js.md#L-79)										'pre': '{{',
[](MediaWiki_Common.js.md#L-80)										'peri':'Glossary|Title=|Short=|Long=',
[](MediaWiki_Common.js.md#L-81)										'post':'}}'
[](MediaWiki_Common.js.md#L-82)									}
[](MediaWiki_Common.js.md#L-83)								},
[](MediaWiki_Common.js.md#L-84)								'label': 'Glossary Template'
[](MediaWiki_Common.js.md#L-85)							},
[](MediaWiki_Common.js.md#L-86)							{
[](MediaWiki_Common.js.md#L-87)								'action': {
[](MediaWiki_Common.js.md#L-88)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-89)									'options': {
[](MediaWiki_Common.js.md#L-90)										'pre': '[[',
[](#L-91)										'peri':'Category: Touch Glossary',
[](MediaWiki_Common.js.md#L-92)										'post':']]'
[](MediaWiki_Common.js.md#L-93)									}
[](MediaWiki_Common.js.md#L-94)								},
[](MediaWiki_Common.js.md#L-95)								'label': 'Glossary Category'
[](MediaWiki_Common.js.md#L-96)							}
[](MediaWiki_Common.js.md#L-97)						]
[](MediaWiki_Common.js.md#L-98)					},
[](MediaWiki_Common.js.md#L-99)					'section-operators': {
[](MediaWiki_Common.js.md#L-100)						'label': 'Operator Pages',
[](MediaWiki_Common.js.md#L-101)						'layout': 'characters',
[](MediaWiki_Common.js.md#L-102)						'characters':[
[](#L-103)							{
[](MediaWiki_Common.js.md#L-104)								'action': {
[](MediaWiki_Common.js.md#L-105)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-106)									'options': {
[](MediaWiki_Common.js.md#L-107)										'pre': '{{Summary',
[](MediaWiki_Common.js.md#L-108)										'peri':'|opFamily=|opLabel=|opType=|opClass=|opFilter=|opLicense=|opCategory=|os=|hardware=|short=|long=',
[](MediaWiki_Common.js.md#L-109)										'post':'}}'
[](MediaWiki_Common.js.md#L-110)									}
[](MediaWiki_Common.js.md#L-111)								},
[](MediaWiki_Common.js.md#L-112)								'label': 'Operator Summary'
[](MediaWiki_Common.js.md#L-113)							},
[](MediaWiki_Common.js.md#L-114)							{
[](MediaWiki_Common.js.md#L-115)								'action': {
[](MediaWiki_Common.js.md#L-116)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-117)									'options': {
[](MediaWiki_Common.js.md#L-118)										'pre': '{{ParameterPage',
[](MediaWiki_Common.js.md#L-119)										'peri':'|opFamily=|pageName=|pageSummary=|items=',
[](MediaWiki_Common.js.md#L-120)										'post':'}}'
[](MediaWiki_Common.js.md#L-121)									}
[](MediaWiki_Common.js.md#L-122)								},
[](MediaWiki_Common.js.md#L-123)								'label': 'Parameter Page'
[](MediaWiki_Common.js.md#L-124)							},
[](MediaWiki_Common.js.md#L-125)							{
[](MediaWiki_Common.js.md#L-126)								'action': {
[](MediaWiki_Common.js.md#L-127)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-128)									'options': {
[](MediaWiki_Common.js.md#L-129)										'pre': '{{ParameterSubPage',
[](MediaWiki_Common.js.md#L-130)										'peri':'|opFamily=|pageName=|pageSummary=|items=',
[](MediaWiki_Common.js.md#L-131)										'post':'}}'
[](MediaWiki_Common.js.md#L-132)									}
[](MediaWiki_Common.js.md#L-133)								},
[](MediaWiki_Common.js.md#L-134)								'label': 'Parameter Sub Page'
[](MediaWiki_Common.js.md#L-135)							},
[](MediaWiki_Common.js.md#L-136)							{
[](MediaWiki_Common.js.md#L-137)								'action': {
[](MediaWiki_Common.js.md#L-138)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-139)									'options': {
[](MediaWiki_Common.js.md#L-140)										'pre': '{{OPSection',
[](MediaWiki_Common.js.md#L-141)										'peri':'|opFamily=|sectionName=|sectionSummary=|items=',
[](MediaWiki_Common.js.md#L-142)										'post':'}}'
[](MediaWiki_Common.js.md#L-143)									}
[](MediaWiki_Common.js.md#L-144)								},
[](MediaWiki_Common.js.md#L-145)								'label': 'Operator Section'
[](MediaWiki_Common.js.md#L-146)							},
[](MediaWiki_Common.js.md#L-147)							{
[](MediaWiki_Common.js.md#L-148)								'action': {
[](MediaWiki_Common.js.md#L-149)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-150)									'options': {
[](MediaWiki_Common.js.md#L-151)										'pre': '{{OPSubSection',
[](MediaWiki_Common.js.md#L-152)										'peri':'|opFamily=|sectionName=|sectionSummary=',
[](MediaWiki_Common.js.md#L-153)										'post':'}}'
[](MediaWiki_Common.js.md#L-154)									}
[](MediaWiki_Common.js.md#L-155)								},
[](MediaWiki_Common.js.md#L-156)								'label': 'Operator Sub Section'
[](MediaWiki_Common.js.md#L-157)							},
[](MediaWiki_Common.js.md#L-158)							{
[](MediaWiki_Common.js.md#L-159)								'action': {
[](MediaWiki_Common.js.md#L-160)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-161)									'options': {
[](MediaWiki_Common.js.md#L-162)										'pre': '{{InfoCHOPChannels',
[](MediaWiki_Common.js.md#L-163)										'peri':'|opFamily=|opLabel=|infoChannels=',
[](MediaWiki_Common.js.md#L-164)										'post':'}}'
[](MediaWiki_Common.js.md#L-165)									}
[](MediaWiki_Common.js.md#L-166)								},
[](MediaWiki_Common.js.md#L-167)								'label': 'Operator Info CHOP Section'
[](MediaWiki_Common.js.md#L-168)							},
[](MediaWiki_Common.js.md#L-169)							{
[](MediaWiki_Common.js.md#L-170)								'action': {
[](MediaWiki_Common.js.md#L-171)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-172)									'options': {
[](MediaWiki_Common.js.md#L-173)										'pre': '{{InfoChannel',
[](MediaWiki_Common.js.md#L-174)										'peri':'|chanName=|chanSummary=',
[](MediaWiki_Common.js.md#L-175)										'post':'}}'
[](MediaWiki_Common.js.md#L-176)									}
[](MediaWiki_Common.js.md#L-177)								},
[](MediaWiki_Common.js.md#L-178)								'label': 'Info CHOP Channel'
[](MediaWiki_Common.js.md#L-179)							}
[](MediaWiki_Common.js.md#L-180)						]
[](MediaWiki_Common.js.md#L-181)					},
[](MediaWiki_Common.js.md#L-182)					'section-oppars': {
[](MediaWiki_Common.js.md#L-183)						'label': 'Operator Parameters',
[](MediaWiki_Common.js.md#L-184)						'layout': 'characters',
[](MediaWiki_Common.js.md#L-185)						'characters':[
[](#L-186)							{
[](MediaWiki_Common.js.md#L-187)								'action': {
[](MediaWiki_Common.js.md#L-188)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-189)									'options': {
[](MediaWiki_Common.js.md#L-190)										'pre': '{{Parameter',
[](MediaWiki_Common.js.md#L-191)										'peri':'|opFamily=|opType=|parName=|parLabel=|parDefault=|parType=|parReadOnly=|parOrder=|parSummary=|parItems=',
[](MediaWiki_Common.js.md#L-192)										'post':'}}'
[](MediaWiki_Common.js.md#L-193)									}
[](MediaWiki_Common.js.md#L-194)								},
[](MediaWiki_Common.js.md#L-195)								'label': 'Parameter'
[](MediaWiki_Common.js.md#L-196)							},
[](MediaWiki_Common.js.md#L-197)							{
[](MediaWiki_Common.js.md#L-198)								'action': {
[](MediaWiki_Common.js.md#L-199)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-200)									'options': {
[](MediaWiki_Common.js.md#L-201)										'pre': '{{ParameterItem',
[](MediaWiki_Common.js.md#L-202)										'peri':'|opFamily=|parName=|itemName=|itemLabel=|itemDefault=|itemSummary=',
[](MediaWiki_Common.js.md#L-203)										'post':'}}'
[](MediaWiki_Common.js.md#L-204)									}
[](MediaWiki_Common.js.md#L-205)								},
[](MediaWiki_Common.js.md#L-206)								'label': 'Parameter Item'
[](MediaWiki_Common.js.md#L-207)							}
[](MediaWiki_Common.js.md#L-208)						]
[](MediaWiki_Common.js.md#L-209)					},
[](MediaWiki_Common.js.md#L-210)					'section-class': {
[](MediaWiki_Common.js.md#L-211)						'label': 'Python Classes',
[](MediaWiki_Common.js.md#L-212)						'layout': 'characters',
[](MediaWiki_Common.js.md#L-213)						'characters':[
[](#L-214)							{
[](MediaWiki_Common.js.md#L-215)								'action': {
[](MediaWiki_Common.js.md#L-216)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-217)									'options': {
[](MediaWiki_Common.js.md#L-218)										'pre': '{{',
[](MediaWiki_Common.js.md#L-219)										'peri':'OPClassSummary|OPfamily=|OPtype=|OPlabel=',
[](MediaWiki_Common.js.md#L-220)										'post':'}}'
[](MediaWiki_Common.js.md#L-221)									}
[](MediaWiki_Common.js.md#L-222)								},
[](MediaWiki_Common.js.md#L-223)								'label': 'OPClassSummary'
[](MediaWiki_Common.js.md#L-224)							},
[](MediaWiki_Common.js.md#L-225)							{
[](MediaWiki_Common.js.md#L-226)								'action': {
[](MediaWiki_Common.js.md#L-227)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-228)									'options': {
[](MediaWiki_Common.js.md#L-229)										'pre': '{{',
[](MediaWiki_Common.js.md#L-230)										'peri':'TDClassSummary|label=|summary=',
[](MediaWiki_Common.js.md#L-231)										'post':'}}'
[](MediaWiki_Common.js.md#L-232)									}
[](MediaWiki_Common.js.md#L-233)								},
[](MediaWiki_Common.js.md#L-234)								'label': 'TDClassSummary'
[](MediaWiki_Common.js.md#L-235)							},
[](MediaWiki_Common.js.md#L-236)							{
[](MediaWiki_Common.js.md#L-237)								'action': {
[](MediaWiki_Common.js.md#L-238)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-239)									'options': {
[](MediaWiki_Common.js.md#L-240)										'pre': '{{',
[](MediaWiki_Common.js.md#L-241)										'peri':'ClassMemberSection|Sectionsummary=|items=|empty=',
[](MediaWiki_Common.js.md#L-242)										'post':'}}'
[](MediaWiki_Common.js.md#L-243)									}
[](MediaWiki_Common.js.md#L-244)								},
[](MediaWiki_Common.js.md#L-245)								'label': 'ClassMemberSection'
[](MediaWiki_Common.js.md#L-246)							},
[](MediaWiki_Common.js.md#L-247)							{
[](MediaWiki_Common.js.md#L-248)								'action': {
[](MediaWiki_Common.js.md#L-249)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-250)									'options': {
[](MediaWiki_Common.js.md#L-251)										'pre': '{{',
[](MediaWiki_Common.js.md#L-252)										'peri':'ClassMember|class=|name=|type=|set=|text=|deprecated=',
[](MediaWiki_Common.js.md#L-253)										'post':'}}'
[](MediaWiki_Common.js.md#L-254)									}
[](MediaWiki_Common.js.md#L-255)								},
[](MediaWiki_Common.js.md#L-256)								'label': 'ClassMember'
[](MediaWiki_Common.js.md#L-257)							},
[](MediaWiki_Common.js.md#L-258)							{
[](MediaWiki_Common.js.md#L-259)								'action': {
[](MediaWiki_Common.js.md#L-260)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-261)									'options': {
[](MediaWiki_Common.js.md#L-262)										'pre': '{{',
[](MediaWiki_Common.js.md#L-263)										'peri':'ClassMethodSection|SectionSummary=|items=|empty=',
[](MediaWiki_Common.js.md#L-264)										'post':'}}'
[](MediaWiki_Common.js.md#L-265)									}
[](MediaWiki_Common.js.md#L-266)								},
[](MediaWiki_Common.js.md#L-267)								'label': 'ClassMethodSection'
[](MediaWiki_Common.js.md#L-268)							},
[](MediaWiki_Common.js.md#L-269)							{
[](MediaWiki_Common.js.md#L-270)								'action': {
[](MediaWiki_Common.js.md#L-271)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-272)									'options': {
[](MediaWiki_Common.js.md#L-273)										'pre': '{{',
[](MediaWiki_Common.js.md#L-274)										'peri':'ClassMethod|class=|name=|call=|returns=|text=|deprecated=',
[](MediaWiki_Common.js.md#L-275)										'post':'}}'
[](MediaWiki_Common.js.md#L-276)									}
[](MediaWiki_Common.js.md#L-277)								},
[](MediaWiki_Common.js.md#L-278)								'label': 'ClassMethod'
[](MediaWiki_Common.js.md#L-279)							},
[](MediaWiki_Common.js.md#L-280)							{
[](MediaWiki_Common.js.md#L-281)								'action': {
[](MediaWiki_Common.js.md#L-282)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-283)									'options': {
[](MediaWiki_Common.js.md#L-284)										'pre': '{{SubSection|title=|text=}}'
[](MediaWiki_Common.js.md#L-285)									}
[](MediaWiki_Common.js.md#L-286)								},
[](MediaWiki_Common.js.md#L-287)								'label': 'Class SubSection'
[](MediaWiki_Common.js.md#L-288)							},
[](MediaWiki_Common.js.md#L-289)						]
[](MediaWiki_Common.js.md#L-290)					},
[](MediaWiki_Common.js.md#L-291)					'section-page': {
[](MediaWiki_Common.js.md#L-292)						'label': 'General Page Elements',
[](MediaWiki_Common.js.md#L-293)						'layout': 'characters',
[](MediaWiki_Common.js.md#L-294)						'characters':[
[](#L-295)							{
[](MediaWiki_Common.js.md#L-296)								'action': {
[](MediaWiki_Common.js.md#L-297)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-298)									'options': {
[](MediaWiki_Common.js.md#L-299)										'pre': '{{History}}'
[](MediaWiki_Common.js.md#L-300)									}
[](MediaWiki_Common.js.md#L-301)								},
[](MediaWiki_Common.js.md#L-302)								'label': 'Tag History'
[](MediaWiki_Common.js.md#L-303)							},
[](MediaWiki_Common.js.md#L-304)							{
[](MediaWiki_Common.js.md#L-305)								'action': {
[](MediaWiki_Common.js.md#L-306)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-307)									'options': {
[](MediaWiki_Common.js.md#L-308)										'pre': '{{SOPNavBox|opFamily=SOP}}'
[](MediaWiki_Common.js.md#L-309)									}
[](MediaWiki_Common.js.md#L-310)								},
[](MediaWiki_Common.js.md#L-311)								'label': 'Category Navigation Box'
[](MediaWiki_Common.js.md#L-312)							},
[](MediaWiki_Common.js.md#L-313)							{
[](MediaWiki_Common.js.md#L-314)								'action': {
[](MediaWiki_Common.js.md#L-315)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-316)									'options': {
[](MediaWiki_Common.js.md#L-317)										'pre': '{{#invoke:Category|list|COMPs}}'
[](MediaWiki_Common.js.md#L-318)									}
[](MediaWiki_Common.js.md#L-319)								},
[](MediaWiki_Common.js.md#L-320)								'label': 'Category List'
[](MediaWiki_Common.js.md#L-321)							},
[](MediaWiki_Common.js.md#L-322)							{
[](MediaWiki_Common.js.md#L-323)								'action': {
[](MediaWiki_Common.js.md#L-324)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-325)									'options': {
[](MediaWiki_Common.js.md#L-326)										'pre': '{{lowercase}}'
[](MediaWiki_Common.js.md#L-327)									}
[](MediaWiki_Common.js.md#L-328)								},
[](MediaWiki_Common.js.md#L-329)								'label': 'Force pagetitle to lowercase'
[](MediaWiki_Common.js.md#L-330)							},
[](MediaWiki_Common.js.md#L-331)							{
[](MediaWiki_Common.js.md#L-332)								'action': {
[](MediaWiki_Common.js.md#L-333)									'type': 'encapsulate',
[](MediaWiki_Common.js.md#L-334)									'options': {
[](MediaWiki_Common.js.md#L-335)										'pre': '#REDIRECT [[:{{FULLPAGENAME}}]]'
[](MediaWiki_Common.js.md#L-336)									}
[](MediaWiki_Common.js.md#L-337)								},
[](MediaWiki_Common.js.md#L-338)								'label': 'Redirect to Experimental'
[](MediaWiki_Common.js.md#L-339)							}
[](MediaWiki_Common.js.md#L-340)						]
[](MediaWiki_Common.js.md#L-341)					},
[](MediaWiki_Common.js.md#L-342)				}
[](MediaWiki_Common.js.md#L-343)			}
[](MediaWiki_Common.js.md#L-344)		}
[](MediaWiki_Common.js.md#L-345)	} );
[](MediaWiki_Common.js.md#L-346)};
[](MediaWiki_Common.js.md#L-347)
[](MediaWiki_Common.js.md#L-348)
[](MediaWiki_Common.js.md#L-349)/* Check if view is in edit mode and that the required modules are available. Then, customize the toolbar … */
[](MediaWiki_Common.js.md#L-350)if ( [ 'edit', 'submit' ].indexOf( mw.config.get( 'wgAction' ) ) !== -1 ) {
[](MediaWiki_Common.js.md#L-351)	mw.loader.using( 'user.options' ).then( function () {
[](MediaWiki_Common.js.md#L-352)		// This can be the string "0" if the user disabled the preference ([[phab:T54542#555387]])
[](MediaWiki_Common.js.md#L-353)		if ( mw.user.options.get( 'usebetatoolbar' ) == 1 ) {
[](MediaWiki_Common.js.md#L-354)			$.when(
[](MediaWiki_Common.js.md#L-356)			).then( customizeToolbar );
[](MediaWiki_Common.js.md#L-357)		}
[](MediaWiki_Common.js.md#L-358)	} );
[](MediaWiki_Common.js.md#L-359)}
[](MediaWiki_Common.js.md#L-360)
[](MediaWiki_Common.js.md#L-361)// Redirect anonymous users to login form.
[](MediaWiki_Common.js.md#L-362)/*
[](MediaWiki_Common.js.md#L-363)jQuery(document).ready(function() {
[](MediaWiki_Common.js.md#L-364)  if (jQuery('#pt-anon_oauth_login').length) {
[](MediaWiki_Common.js.md#L-365)   var titleUrl = findGetParameter('title');
[](MediaWiki_Common.js.md#L-366)   if (titleUrl) {
[](MediaWiki_Common.js.md#L-367)     var returnUrl = '/index.php?title=Special:OAuth2Client/redirect&returnto=' + titleUrl;
[](MediaWiki_Common.js.md#L-368)   }
[](MediaWiki_Common.js.md#L-369)   else {
[](MediaWiki_Common.js.md#L-370)     var returnUrl = '/index.php?title=Special:OAuth2Client/redirect&returnto=Main+Page';
[](MediaWiki_Common.js.md#L-371)   }
[](MediaWiki_Common.js.md#L-372)   window.location.href = returnUrl;
[](MediaWiki_Common.js.md#L-373)  }
[](MediaWiki_Common.js.md#L-374)});
[](MediaWiki_Common.js.md#L-375)*/
```

An [Operator Family](../Glossary/Operator_Family.md "Operator Family") which operate on [Channels](../Glossary/Channel.md "Channel") (a sequence of numbers ([Samples](../Glossary/Sample.md "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

A [CHOP](../Glossary/CHOP.md "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](../Glossary/Sample.md "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](../Glossary/Export.md "Export") to [Parameters](../Glossary/Parameter.md "Parameter").

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](../Glossary/Network_Path.md "Network Path"), which determine the output of the operator.

Each operator can have a set of text strings that are its "tags". You can set them and search for them within TouchDesigner.

A [Operator Family](../Glossary/Operator_Family.md "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.
