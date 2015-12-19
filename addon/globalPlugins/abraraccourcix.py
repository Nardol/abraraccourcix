# -*- coding: utf-8 -*-
# Abraraccourcix Global Plugin for NVDA
# Copyright (C) 2015 Patrick ZAJDA <patrick@zajda.fr>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: pause

import globalPluginHandler, addonHandler
import ui
import wx
from keyboardHandler import KeyboardInputGesture

# We initialize translation support
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# We initialize the scripts category shown on input gestures dialog
	scriptCategory = u"Abraraccourcix"

	def script_pauseFermer(self, gesture):
		KeyboardInputGesture.fromName("alt+f4").send()
		# Translators: confirmation message when Alt+F4 has been performed
		wx.CallLater(100,ui.message, _("Window closed"))
	# Translators: message presented when user performes input help for the pose key script
	script_pauseFermer.__doc__ = _(u"Close the focused window")

	__gestures={
		"kb:pause": "pauseFermer",
	}
