# -*- coding: utf-8 -*-
# Abraraccourcix Global Plugin for NVDA
# Copyright (C) 2015 Patrick ZAJDA <patrick@zajda.fr>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: pause

import globalPluginHandler, addonHandler
import api
import ui
import wx
from keyboardHandler import KeyboardInputGesture

# We initialize translation support
addonHandler.initTranslation()

def getWindowTitleAndAppModule():
	""" Return the current window title and the corresponding appModule """
	obj=api.getForegroundObject()
	title=obj.name
	if not isinstance(title,basestring) or not title or title.isspace():
		title=obj.appModule.appName  if obj.appModule else "No title"
	return title, obj.appModule if obj.appModule else "No appModule"

def checkNewWindow(title, appModule):
		newTitle, newAppModule = getWindowTitleAndAppModule()
		if newTitle == title and newAppModule == appModule:
			# Translators: message announced if the window was probably not closed
			ui.message(_(u"Window probably not closed"))
		else :
			# Translators: confirmation message when Alt+F4 has been performed
			ui.message(_("Window closed"))

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# We initialize the scripts category shown on input gestures dialog
	scriptCategory = u"Abraraccourcix"

	def script_pauseFermer(self, gesture):
		title,appModule = getWindowTitleAndAppModule()
		KeyboardInputGesture.fromName("alt+f4").send()
		wx.CallLater(100, checkNewWindow, title, appModule)
	# Translators: message presented when user performes input help for the pose key script
	script_pauseFermer.__doc__ = _(u"Close the focused window")

	__gestures={
		"kb:pause": "pauseFermer",
	}
