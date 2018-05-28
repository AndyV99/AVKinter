#!/usr/bin/env python
""" Provides Styling for AVKButtons

"""

from .Styles import defaults

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

AVKButtonStyles = {
	'DEFAULT': defaults['BUTTON']
}

def newAVKButtonStyle(pname,
                      pfont=defaults['BUTTON']['font'],
                      pfontColor=defaults['BUTTON']['fontColor'],
                      pbackgroundColor=defaults['BUTTON']['backgroundColor'],
                      pactiveFontColor=defaults['BUTTON']['activeFontColor'],
                      pactiveBackgroundColor=defaults['BUTTON']['activeBackgroundColor'],
                      prelief=defaults['BUTTON']['relief']):
	"""
	Defines a new AVKButton style
	:param pname: Name of new style
	:param pfont: Font definition as tuple
	:param pfontColor: Color of font as hex string
	:param pbackgroundColor: Color of background as hex string
	:param pactiveFontColor: Color of font when button clicked
	:param pactiveBackgroundColor: Color of background when button clicked
	:param prelief: Relief of button defined in tkinter
	:return: None
	"""
	AVKButtonStyles[pname] = {
		'font': pfont,
		'fontColor': pfontColor,
		'backgroundColor': pbackgroundColor,
		'activeFontColor': pactiveFontColor,
		'activeBackgroundColor': pactiveBackgroundColor,
		'relief': prelief
	}
