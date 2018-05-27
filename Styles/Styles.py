#!/usr/bin/env python
""" Provides Styling for AVK Widgets

"""

from tkinter import font
from tkinter import GROOVE

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

defaults = {
	"BUTTON": {
		'font': ("Arial", 11, font.NORMAL),
		'fontColor': '#FFFFFF',
		'backgroundColor': '#000000',
		'activeFontColor': '#AFAFAF',
		'activeBackgroundColor': '#FF0000',
		'relief': GROOVE
	},
	"LABEL": {
		'font': ("Arial", 11, font.NORMAL),
		'fontColor': '#FFFFFF',
		'backgroundColor': '#000000'
	},
	"NAVBAR": {
		'backgroundColor': '#000000',
		'backButtonStyle': "DEFAULT",
		'nextButtonStyle': "DEFAULT",
		'titleLabelStyle': "DEFAULT"
	}
}



