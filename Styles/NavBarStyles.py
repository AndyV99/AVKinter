#!/usr/bin/env python
""" Provides Styling for AVKBNavBars

"""

from .Styles import defaults

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
                      pbackButtonStyle=defaults['NAVBAR']['backButtonStyle'],
                      pnextButtonStyle=defaults['NAVBAR']['nextButtonStyle'],
                      ptitleLabelStyle=defaults['NAVBAR']['titleLabelStyle']):
	"""
	Defines a new AVKNavBar Style
	:param pname: Name of new style
	:param pbackgroundColor: Color of background
	:param pbackButtonStyle: Style of the back button
	:param pnextButtonStyle: Style of the next button
	:param ptitleLabelStyle: Style of the title label
	:return: None
	"""
	AVKNavBarStyles[pname] = {
		'backgroundColor': pbackgroundColor,
		'backButtonStyle': pbackButtonStyle,
		'nextButtonStyle': pnextButtonStyle,
		'ptitleLabelStyle': ptitleLabelStyle
	}
