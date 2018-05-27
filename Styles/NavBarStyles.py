#!/usr/bin/env python
""" Provides Styling for AVKBNavBars

"""

from Styles import defaults

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

AVKNavBarStyles = {
	'DEFAULT': defaults['NAVBAR']
}

def newAVKNavBarStyle(pname,
                      pbackgroundColor=defaults['NAVBAR']['backgroundColor'],
                      pbackButtonStyle=defaults['BUTTON'],
                      pnextButtonStyle=defaults['BUTTON'],
                      ptitleLabelStyle=defaults['LABEL']):
	AVKNavBarStyles[pname] = {
		'backgroundColor': pbackgroundColor,
		'backButtonStyle': pbackButtonStyle,
		'nextButtonStyle': pnextButtonStyle,
		'ptitleLabelStyle': ptitleLabelStyle
	}
